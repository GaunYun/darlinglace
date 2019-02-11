
# -*- coding: iso-8859-1 -*-
# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from datetime import date, datetime, timedelta
from django.shortcuts import render
from django.http import HttpResponseRedirect
import phonenumbers
import paymill
import django
import hashlib
from paymill import PaymillContext
import json
from django.views.decorators.csrf import csrf_exempt
import socket
import mysql.connector
import datetime
from datetime import timedelta
from django.conf import settings

import string, threading
import random
import time
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
import pytz

import math
import requests



# encoding=utf8  
import sys

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


from django.conf import settings
from django.core.mail import send_mail
from django.core.wsgi import get_wsgi_application
from django.template.loader import get_template, render_to_string

import os, sys







ab_path = "/home/maxfischer2/mysite/Amoroso/"
sys.path.append(ab_path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()






def get_time_stamp_now():

    now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
    Y=now.year
    M=now.month
    D=now.day
    H=now.hour
    Mi=now.minute
    d1 = datetime.datetime.strptime(str(Y)+"-"+str(M)+"-"+str(D)+" "+str(H)+":"+str(Mi), "%Y-%m-%d %H:%M")



    
    return d1



def get_date_stamp_now():
    now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))


    Monat = ["Januar", "Februar", "Maerz", "April","Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
    d1=str(now.day)+". "+Monat[(now.month)-1]+" "+str(now.year)

    
    return d1








def define_bestelldetails(session_key,bestellnummer,gerichtname,bewertung,c,modelAB,sub_picture):
    bestelldetails = []
    style_names=[]
    class Bestelldetails(object):
        def __init__(self,style,anzahl,datum,freiemenge,datumweekday,status,bestellnummer,bewertung,bewertungstext,bewertungsdatum,picture_link_small,subtitle,preis,bhgroesse,slipgroesse,color,stylecode,passform,bewertungsheadline):
            self.style=style
            self.anzahl=anzahl
            self.datum=datum
            self.freiemenge=freiemenge
            self.datumweekday=datumweekday
            self.status=status
            self.bestellnummer=bestellnummer
            self.bewertung=bewertung
            self.bewertungstext=bewertungstext
            self.bewertungsdatum=bewertungsdatum
            self.picture_link_small=picture_link_small
            self.subtitle=subtitle
            self.preis=preis
            self.bhgroesse=bhgroesse
            self.slipgroesse=slipgroesse
            self.color=color
            self.stylecode=stylecode
            self.passform=passform
            self.bewertungsheadline=bewertungsheadline
            
            


    if bestellnummer=="":

        c.execute ("""select * from userdaten where gutscheincode=%s """,(session_key,))

        userdaten=c.fetchall()

        for row in userdaten:
            c.execute ("""select * from bestellt where gutscheincode=%s""",(row[11],))

            bestellt_daten=c.fetchall()

            for row_2 in bestellt_daten:
                c.execute ("""select * from cart_details where bestellnummer=%s and bestellt=%s""",(row_2[21],"ja",))

                session_table=c.fetchall()

                for row_3 in session_table:
                    c.execute   ("""select * from lingerieselection where name='%s'""" % (row_3[0],))
                    lingerieselection_name=c.fetchall()
                    for row_5 in lingerieselection_name:
                        if row_3[2]!="":
                            c.execute   ("""select * from %s where color='%s' and size='%s' and stylecode='%s'""" % ("stylecode", row_3[4],row_3[2],row_5[12],))

                            stylecode_daten=c.fetchall()
                        else:
                            c.execute   ("""select * from %s where color='%s' and size='%s'""" % ("stylecode", row_3[4],row_3[3],))

                            stylecode_daten=c.fetchall()                                        
                        

                        for row_6 in stylecode_daten:
                            freie_menge=min(int(row_6[4])-int(row_6[5]),10)
                            if row_2[23]=="VIP":                                                  
                                bestelldetails.append(Bestelldetails(row_3[0],row_3[1],row[18],freie_menge,row_3[4],row_3[6],row_2[21],row_3[16],row_3[18],row_3[19],get_pictures_from_consolidated_table(c,row_5[12],row_5[13],modelAB,sub_picture,row_5[2],"first","small"),row_5[9],row_5[4],row_3[2],row_3[3],row_6[2],row_5[12],row_3[20],row_3[17],))
                            else:
                                bestelldetails.append(Bestelldetails(row_3[0],row_3[1],row[18],freie_menge,row_3[4],row_3[6],row_2[21],row_3[16],row_3[18],row_3[19],get_pictures_from_consolidated_table(c,row_5[12],row_5[13],modelAB,sub_picture,row_5[2],"first","small"),row_5[9],row_5[3],row_3[2],row_3[3],row_6[2],row_5[12],row_3[20],row_3[17],))
                                     
    else:
        c.execute ("""select * from userdaten where gutscheincode=%s """,(session_key,))

        userdaten=c.fetchall()
        for row in userdaten:
            
            
            c.execute ("""select * from bestellt where gutscheincode=%s """,(row[11],))

            bestellt_daten=c.fetchall()

            for row_2 in bestellt_daten:
                c.execute ("""select * from cart_details where bestellnummer=%s and bestellt=%s""",(row_2[21],"ja",))
                session_table=c.fetchall()
                
                for row_3 in session_table:
                    if bestellnummer==row_2[21]:


                        c.execute ("""select * from lingerieselection """)

                        lingerieselection_daten=c.fetchall()
    
                        for row_5 in lingerieselection_daten:
                            if row_5[0]==row_3[0]:

                                

                                c.execute ("""select * from %s """% ("stylecode"))
                                stylecode_daten=c.fetchall()


                                for row_6 in stylecode_daten:
                                    if row_5[12]==row_6[1]:

                                        
                                        if (row_3[4]==row_6[2] and row_3[7]==row_6[1] and row_3[2]==row_6[3]) or (row_3[2]=="" and row_6[3]==row_3[3] and row_3[4]==row_6[2]):

                                            if row_2[23]=="VIP":                                                  
                                                bestelldetails.append(Bestelldetails(row_3[0],row_3[1],row[18],10,row_3[4],row_3[6],row_2[21],row_3[16],row_3[18],row_3[19],get_pictures_from_consolidated_table(c,row_6[1],row_3[4],modelAB,sub_picture,row_5[2],"first","small"),row_5[9],row_5[4],row_3[2],row_3[3],row_6[2],row_5[12],row_3[20],row_3[17],))

                                            else:
                                                bestelldetails.append(Bestelldetails(row_3[0],row_3[1],row[18],10,row_3[4],row_3[6],row_2[21],row_3[16],row_3[18],row_3[19],get_pictures_from_consolidated_table(c,row_6[1],row_3[4],modelAB,sub_picture,row_5[2],"first","small"),row_5[9],row_5[3],row_3[2],row_3[3],row_6[2],row_5[12],row_3[20],row_3[17],))





    json_string = json.dumps([Bestelldetails.__dict__ for Bestelldetails in bestelldetails])


    return json_string

def get_rabattname(gutscheincode,cart_gesamt,c):
    reload(sys)
    sys.setdefaultencoding("ISO-8859-1")
    
    c.execute ("""select * from gutscheine """)
    gutscheine=c.fetchall()
    return_string=""
    for row in gutscheine:
        if row[0]==gutscheincode:
            if row[4]==0:
                preis=str("%.2f" % round(row[5],2)).replace(".", ",")
                return_string= (""" Set für """+str(preis)+""" EUR""").decode('windows-1252')
            if row[4]==1:
                preis=str("%.2f" % round(row[6],2)).replace(".", ",")
                return_string= "Rabatt von "+str(preis)+""" EUR"""
            if row[4]==2:

                return_string= "Rabatt von "+str(int(row[7]*100))+"%"
            if row[4]==3:
                i=0
                zaehler=0
                preis=0
                while i<=cart_gesamt-1:
                    if i<=4:
                        if row[8+min(i,4)]!=0:
                            zaehler=zaehler+1
                            preis=preis+row[8+min(i,4)]
                    
                    i=i+1
                preis=str("%.2f" % round(preis,2)).replace(".", ",")
                if zaehler>1:
                    return_string= (str(zaehler)+""" Sets für """+str(preis)+""" EUR""").decode('windows-1252')
                else:
                    return_string= (str(zaehler)+""" Set für """+str(preis)+""" EUR""").decode('windows-1252')

    return return_string


def define_rebates(session_key,bestellnummer,string_list_cart,length_string_list,aenderung,c,conn,land,get_bestellewert,get_lieferkosten,get_rabatte):


    rebates = []
    class Rebates(object):
        def __init__(self,coupon,couponcode,braforfreevalue,braforfreecount,storecredit,credit,bestellung,gesamtpreis,aenderung,aenderung_rechnungsbetrag,lieferkosten,bestellnummer,rabattname):
            self.coupon=coupon
            self.couponcode=couponcode
            self.braforfreevalue=braforfreevalue
            self.braforfreecount=braforfreecount
            self.storecredit=storecredit
            self.credit=credit
            self.bestellung=bestellung
            self.gesamtpreis=gesamtpreis
            self.aenderung=aenderung
            self.aenderung_rechnungsbetrag=aenderung_rechnungsbetrag
            self.lieferkosten=lieferkosten
            self.bestellnummer=bestellnummer
            self.rabattname=rabattname


    
    delta=0
    aenderung_rechnungsbetrag=0
    zwischensumme=0


    c.execute ("""select * from userdaten where gutscheincode=%s """,(session_key,))

    userdaten=c.fetchall()

    for row in userdaten:

        gutscheincode=row[21]
        user=row[11]

        if bestellnummer!="":


            c.execute ("""select * from bestellt where gutscheincode=%s ORDER BY idforsorting DESC""",(row[11],))

            bestellt_data=c.fetchall()


            for row_2 in bestellt_data:
                if row_2[21]==bestellnummer or bestellnummer=="All":
                    coupon=float(row_2[17])
                    coupon_new=coupon
                    couponcode=row_2[18]
                    storecredit=float(row_2[28])
                    braforfreevalue=float(row_2[27])
                    braforfreecount=float(row_2[26])
                    credit=float(row_2[22])
                    versandkosten=float(row_2[16])
                    bestellnummer=row_2[21]





                    if string_list_cart!="":
                        bestellung=0
                        stylecodes_colorcodes=[]
                        c.execute ("""select * from cart_details where gutscheincode=%s and bestellt=%s and bestellnummer=%s""",(user,"ja",bestellnummer,))
                        for row_3 in c:
                            gesamtanzahl=gesamtanzahl+row_3[1]
                            stylecodes_colorcodes.append(row_3[7]+"_"+row_3[4])

                            j=0
                            while j<=length_string_list:
                                style=string_list_cart[j*7+0]
                                stylecode=string_list_cart[j*7+1]
                                colorcode=string_list_cart[j*7+2]
                                bh_groesse=string_list_cart[j*7+3]
                                slip_groesse=string_list_cart[j*7+4]
                                anzahl=int(string_list_cart[j*7+5])
                                preis=float(string_list_cart[j*7+6])
                                


                                if row_3[7]==stylecode and row_3[4]==colorcode and row_3[2]==bh_groesse and row_3[3]==slip_groesse:
                                    bestellung=bestellung+row_3[8]*anzahl

                                j=j+1
                        coupon_new=min(coupon,max(bestellung+versandkosten,0))
                        zwischensumme=bestellung-coupon_new+versandkosten

                        credit_new=min(credit,max(zwischensumme,0))
                        zwischensumme=bestellung-coupon_new-credit_new+versandkosten

                        braforfreevalue_new=0
                        braforfreecount_new=0
                        bestellung_alt=0

                        
                        c.execute ("""select * from cart_details where gutscheincode=%s and bestellt=%s and bestellnummer=%s ORDER BY preis DESC""" ,(user,"ja",bestellnummer,))
                        for row_3 in c:
                            
                            j=0
                            while j<=length_string_list:
                                style=string_list_cart[j*7+0]
                                stylecode=string_list_cart[j*7+1]
                                colorcode=string_list_cart[j*7+2]
                                bh_groesse=string_list_cart[j*7+3]
                                slip_groesse=string_list_cart[j*7+4]
                                anzahl=string_list_cart[j*7+5]
                                preis=string_list_cart[j*7+6]


                                if row_3[7]==stylecode and row_3[4]==colorcode and row_3[2]==bh_groesse and row_3[3]==slip_groesse:
                                    i=0
                                    while i<=int(anzahl)-1:

                                        if bestellung-coupon_new-credit_new-float(preis)-braforfreevalue_new>=0 and braforfreecount_new<braforfreecount:
                                            braforfreevalue_new=braforfreevalue_new+float(preis)
                                            braforfreecount_new=braforfreecount_new+1
                                        i=i+1
                                j=j+1


                            bestellung_alt=bestellung_alt+float(row_3[1])*row_3[8]

                            
                        
                        zwischensumme=bestellung-coupon_new-credit_new-braforfreevalue_new+versandkosten

                        storecredit_new=min(storecredit,max(zwischensumme,0))

                        if aenderung=="":


                            
                            c.execute("""update %s set rabatt=%%s, creditused=%%s,braforfreecount=%%s,braforfreevalue=%%s,storecredit=%%s where bestellnummer=%%s and gutscheincode=%%s and bestellt=%%s""" % ("bestellt"),(coupon_new,credit_new,braforfreecount_new,braforfreevalue_new,storecredit_new,bestellnummer,row[11],"ja",))                            
                            c.execute("""update userdaten set numberofbraforfree=%s, credit=%s,storecredit=%s where gutscheincode=%s""",(int(row[25])+braforfreecount-braforfreecount_new,int(row[10])+credit-credit_new,int(row[24])+storecredit-storecredit_new,session_key,))


                            conn.commit()
                        else:
                            delta=bestellung-bestellung_alt
                            aenderung_rechnungsbetrag=bestellung-bestellung_alt+(coupon-coupon_new)+(credit-credit_new)+(braforfreevalue-braforfreevalue_new)+(storecredit-storecredit_new)

                            if delta!=0:
                                bestellung=bestellung_alt







                        
                    else:


                        bestellung=0
        
                        coupon_new=coupon
                        credit_new=credit
                        braforfreevalue_new=braforfreevalue
                        braforfreecount_new=braforfreecount
                        storecredit_new=storecredit
                        gesamtanzahl=0

                        

                        c.execute ("""select * from cart_details where gutscheincode=%s and bestellt=%s and bestellnummer=%s""",(user,"ja",bestellnummer,))
                        for row_3 in c:
                            bestellung=bestellung+float(row_3[1])*row_3[8]


                        c.execute ("""select * from cart_details where gutscheincode=%s and bestellt=%s and bestellnummer=%s and productgroup=%s""",(user,"ja",bestellnummer,"lingerie",))
                        for row_3 in c:
                            gesamtanzahl=gesamtanzahl+row_3[1]

                            
                
                        c.execute ("""select * from cart_details where gutscheincode=%s and bestellt=%s and bestellnummer=%s ORDER BY preis DESC""" ,(user,"ja",bestellnummer,))
                        for row_3 in c:

                                        
                            i=0
                            while i<=int(row_3[1])-1:

                                if bestellung-coupon_new-credit_new-float(row_3[8])-braforfreevalue_new+versandkosten>=0 and braforfreecount_new<braforfreecount:
                                    braforfreevalue_new=braforfreevalue_new+float(row_3[8])
                                    braforfreecount_new=braforfreecount_new+1
                                i=i+1
                    zwischensumme=bestellung-coupon_new-credit_new-braforfreevalue_new-storecredit_new+delta+versandkosten
                    
                    rebates.append(Rebates(coupon_new,couponcode,braforfreevalue_new,braforfreecount_new,storecredit_new,credit_new,bestellung,zwischensumme,delta,aenderung_rechnungsbetrag,versandkosten,bestellnummer,get_rabattname(gutscheincode,gesamtanzahl,c),))
                           



        else:
            versandkosten=get_country_delivery_costs(land,c)
            credit=float(row[10])

            couponcode=row[21]
            coupon=float(-gutscheinwert_abrufen(couponcode,c,session_key,conn,"nein",user))
            gesamtanzahl=0



            braforfreecount=get_bra_for_free_in_VIP_model(c,row[11])
            storecredit=get_existing_store_credit(c,row[11])

            stylecodes_colorcodes=[]
            bestellung=0
            c.execute ("""select * from cart_details where gutscheincode=%s and bestellt=%s""",(user,"nein",))
            for row_3 in c:
                print row_3[0]
                print(row_3[1])
                print row_3[8]
                bestellung=bestellung+float(row_3[1])*row_3[8]



            c.execute ("""select * from cart_details where gutscheincode=%s and bestellt=%s and productgroup=%s""",(user,"nein","lingerie",))
            for row_3 in c:

                gesamtanzahl=gesamtanzahl+row_3[1]


                
            coupon_new=min(coupon,max(bestellung+versandkosten,0))
            zwischensumme=bestellung-coupon_new+versandkosten

            credit_new=min(credit,max(zwischensumme,0))
            zwischensumme=bestellung-coupon_new-credit_new+versandkosten                               
                    


            braforfreevalue_new=0
            braforfreecount_new=0

            c.execute ("""select * from cart_details where gutscheincode=%s and bestellt=%s ORDER BY preis DESC""",(user,"nein"))
            for row_3 in c:
                            
                i=0
                while i<=int(row_3[1])-1:

                    if bestellung-coupon_new-credit_new-float(row_3[8])-braforfreevalue_new>=0 and braforfreecount_new<braforfreecount:
                        braforfreevalue_new=braforfreevalue_new+float(row_3[8])
                        braforfreecount_new=braforfreecount_new+1
                    i=i+1

            
            zwischensumme=bestellung-coupon_new-credit_new-braforfreevalue_new+versandkosten                                    


            storecredit_new=min(storecredit,max(zwischensumme,0))
            
            
            
            zwischensumme=bestellung-coupon_new-credit_new-braforfreevalue_new-storecredit_new+versandkosten


            rebates.append(Rebates(coupon_new,couponcode,braforfreevalue_new,braforfreecount_new,storecredit_new,credit_new,bestellung,zwischensumme,delta,aenderung_rechnungsbetrag,versandkosten,bestellnummer,get_rabattname(gutscheincode,gesamtanzahl,c),))
    






            
    json_string = json.dumps([Rebates.__dict__ for Rebates in rebates])
    if bestellnummer=="":
        c.execute("""update userdaten set definerebates=%s,definerebatesbestellwert=%s,definerebateslieferkosten=%s,definerebatesrabatte=%s,gesamtanzahlbestellung=%s where gutscheincode=%s""",(json_string,zwischensumme,versandkosten,zwischensumme-bestellung-versandkosten,gesamtanzahl,user,))
        conn.commit()

            

    if get_bestellewert=="no" and get_rabatte=="no" and get_lieferkosten=="no":
        return json_string
    else:
        if get_bestellewert=="yes":
            return zwischensumme
        else:
            if get_lieferkosten=="yes":
                return versandkosten
            else:
                if get_rabatte=="yes":
                    return zwischensumme-bestellung-versandkosten



def get_pictures_from_consolidated_table(c,stylecode,colorcode,modelAB,sub_picture,pantytype,firstorall,bigorsmall):

    print(stylecode)
    print(colorcode)
    print(modelAB)
    print(sub_picture)
    print(pantytype)
    print(firstorall)
    print(bigorsmall)
    
    c.execute ("""select * from consolidated_picturelibrary where modelAB=%s and subpicture=%s and stylecode=%s and colorcode=%s and firtorall=%s and bigorsmall=%s """,(modelAB,sub_picture,stylecode,colorcode,firstorall,bigorsmall,))

    consolidated_picturelibrary=c.fetchall()
    picture=""
    for row in consolidated_picturelibrary:
        picture=row[6]
    print "get_pictures_from_consolidated_table"
    print picture
    return picture






def get_modelAB(user,c):
    c.execute ("""select * from userdaten where gutscheincode=%s """,(user,))
    for row in c:
        return row[47]
   


def get_subpicture(user,c):
    c.execute ("""select * from userdaten where gutscheincode=%s """,(user,))
    for row in c:
        return row[48]           
          


def define_bestellung(session_key,bestellnummer,c,transaction_id_ja_oder_nein):
    bestellung = []
    class Bestellung(object):
        def __init__(self,sessionidtablename,strasserechnung,hausnummerrechnung,stadtrechnung,plzrechnung,landrechnung,anrederechnung,vornamerechnung,nachnamerechnung,telefonnummerrechnung,zahlungsoption,namekarteninhaber,kartennummer,ablaufdatum,pruefnummer,bestellungspreis,lieferkosten,rabatt,rabattcode,datum,uhrzeit,bestellnummer,creditused,status,braforfreevalue,storecredit,braforfreecount,liefertermin,usercode,datasenttogoogleanalytics,unternehmensdetailsrechnung,strasselieferadresse,hausnummerlieferadresse,stadtlieferadresse,plzlieferadresse,landlieferadresse,anredelieferadresse,vornamelieferadresse,nachnamelieferadresse,telefonnummerlieferadresse,unternehmensdetailslieferadresse,transactionid):
            self.sessionidtablename=sessionidtablename
            self.strasserechnung=strasserechnung
            self.hausnummerrechnung=hausnummerrechnung
            self.stadtrechnung=stadtrechnung
            self.plzrechnung=plzrechnung
            self.landrechnung=landrechnung
            self.anrederechnung=anrederechnung
            self.vornamerechnung=vornamerechnung
            self.nachnamerechnung=nachnamerechnung
            self.telefonnummerrechnung=telefonnummerrechnung
            self.zahlungsoption=zahlungsoption
            self.namekarteninhaber=namekarteninhaber
            self.kartennummer=kartennummer
            self.ablaufdatum=ablaufdatum
            self.pruefnummer=pruefnummer
            self.bestellungspreis=bestellungspreis
            self.lieferkosten=lieferkosten
            self.rabatt=rabatt
            self.rabattcode=rabattcode
            self.datum=datum
            self.uhrzeit=uhrzeit
            self.bestellnummer=bestellnummer
            self.creditused=creditused
            self.status=status
            self.braforfreevalue=braforfreevalue
            self.storecredit=storecredit
            self.braforfreecount=braforfreecount
            self.liefertermin=liefertermin            
            self.usercode=usercode
            self.datasenttogoogleanalytics=datasenttogoogleanalytics
            self.unternehmensdetailsrechnung=unternehmensdetailsrechnung
            self.strasselieferadresse=strasselieferadresse
            self.hausnummerlieferadresse=hausnummerlieferadresse
            self.stadtlieferadresse=stadtlieferadresse
            self.plzlieferadresse=plzlieferadresse
            self.landlieferadresse=landlieferadresse
            self.anredelieferadresse=anredelieferadresse
            self.vornamelieferadresse=vornamelieferadresse
            self.nachnamelieferadresse=nachnamelieferadresse
            self.telefonnummerlieferadresse=telefonnummerlieferadresse
            self.unternehmensdetailslieferadresse=unternehmensdetailslieferadresse
            self.transactionid=transactionid

            


    c.execute ("""select * from userdaten """)

    userdaten=c.fetchall()
    

    for row in userdaten:
        if session_key!="all":
            if row[11]==session_key:
                c.execute ("""select * from bestellt where gutscheincode=%s ORDER BY idforsorting DESC""",(row[11],))
                for row_2 in c:

                    if row_2[21]==bestellnummer or bestellnummer=="all":
                        if row_2[10]=="2":
                            try:
                                kartennummer_kurz=row_2[12]
                                kartennummer_kurz=kartennummer_kurz[15:]
                            except:
                                kartennummer_kurz=""
                        else:
                            kartennummer_kurz=row_2[12]
                        if transaction_id_ja_oder_nein=="ja":
                            transaction_id=row_2[38]
                        else:
                            transaction_id=""
                        bestellung.append(Bestellung(row_2[0],row_2[1],row_2[2],row_2[3],row_2[4],row_2[5],row_2[6],row_2[7],row_2[8],row_2[9],row_2[10],row_2[11],kartennummer_kurz,row_2[13],row_2[14],row_2[15],row_2[16],row_2[17],row_2[18],row_2[19],row_2[20],row_2[21],row_2[22],row_2[24],row_2[27],row_2[28],row_2[26],row_2[29],row[11],row_2[39],row_2[40],row_2[41],row_2[42],row_2[43],row_2[44],row_2[45],row_2[46],row_2[47],row_2[48],row_2[49],row_2[50],transaction_id,))
        else:

            try:
                c.execute ("""select * from bestellt where gutscheincode=%s ORDER BY idforsorting DESC""",(row[11],))
                for row_2 in c:
                    if row_2[21]==bestellnummer or bestellnummer=="all":
                        if row_2[10]=="2":
                            try:
                                kartennummer_kurz=row_2[12]
                                kartennummer_kurz=kartennummer_kurz[15:]
                            except:
                                kartennummer_kurz=""
                        else:
                            kartennummer_kurz=row_2[12]
                        if transaction_id_ja_oder_nein=="ja":
                            transaction_id=row_2[38]
                        else:
                            transaction_id=""                            
                        bestellung.append(Bestellung(row_2[0],row_2[1],row_2[2],row_2[3],row_2[4],row_2[5],row_2[6],row_2[7],row_2[8],row_2[9],row_2[10],row_2[11],kartennummer_kurz,row_2[13],row_2[14],row_2[15],row_2[16],row_2[17],row_2[18],row_2[19],row_2[20],row_2[21],row_2[22],row_2[24],row_2[27],row_2[28],row_2[26],row_2[29],row[11],row_2[39],row_2[40],row_2[41],row_2[42],row_2[43],row_2[44],row_2[45],row_2[46],row_2[47],row_2[48],row_2[49],row_2[50],transaction_id,))

            except:
                print("error: no bestellt_table")


    json_string = json.dumps([Bestellung.__dict__ for Bestellung in bestellung])

    return json_string



def generate_link_email_marketing(link,userid,email_name):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                            password='okano1988',database='maxfischer2database')
    c = conn.cursor(buffered=True)




    print link
    print userid
    print email_name
    hashcode=hashlib.sha512(link+userid+email_name).hexdigest()
    print hashcode



    count_rows_email_marketing_links=c.execute ("""select * from email_marketing_links where hashcode=%s """,(hashcode,))
    c.execute(count_rows_email_marketing_links)
    zaehler_email_marketing_links=int(c.rowcount)
    if zaehler_email_marketing_links==0:
        c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s)""" % ("email_marketing_links"), (hashcode,link,userid,email_name,0,))
        conn.commit()

    return hashcode

    


    

def get_newsletterabbestellencode(user_id,c):
    newsletter_code=""
    c.execute ("""select * from userdaten where gutscheincode=%s """,(user_id,))
    for row in c:
        newsletter_code=row[64]

        
    return newsletter_code




conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                        password='okano1988',database='maxfischer2database')
c = conn.cursor(buffered=True)


print("do_something")
import sched, time
#s = sched.scheduler(time.time, time.sleep)
#def do_something(sc):
print("emails")
now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
date_now=day=str(now.year)+str(now.month-1)+str(now.day)


mail = smtplib.SMTP_SSL('smtp.strato.de:465')
mail.ehlo()
mail.login('kundensupport@darlinglace.com', 'Lingerie2017')

timer=0

s = sched.scheduler(time.time, time.sleep)
def do_something(sc): 
    
    global timer
#____________________________


    c.execute ("""select * from order_confirmation_emails """)
    order_confirmation_emails=c.fetchall()
    for row in order_confirmation_emails:
        if row[4]=="nein":
            bestellnummer=row[0]
            x=row[1]
            to=row[2]
            subject=row[3]
            empfaenger=to

            print("order_confirmation_email")
            # me == my email address
            # you == recipient's email address
            me = "Paula von Darling Lace <service@darlinglace.com>"
            you = to

            reload(sys)
            sys.setdefaultencoding("ISO-8859-1")

            
            # Create message container - the correct MIME type is multipart/alternative.
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = me
            msg['To'] = you

            von=me

            bestelldetails=define_bestelldetails(x,bestellnummer,"","",c,get_modelAB(x,c),get_subpicture(x,c))
            rebates=define_rebates(x,bestellnummer,"","","",c,conn,"","no","no","no")
            bestellung=define_bestellung(x,bestellnummer,c,"nein")
            print(bestellung)
            if bestellung!="[]" and rebates!="[]" and bestelldetails!="[]":

                bestelldetails=json.loads(bestelldetails)
                rebates=json.loads(rebates)
                bestellung=json.loads(bestellung)

                link_bestellungen='https://www.darlinglace.com/account_page/bestellungen_ansehen/'+bestellung[0]['bestellnummer']
                link_profil='https://www.darlinglace.com/account_page/'
                link_hilfe='https://www.darlinglace.com/help/'

                vorname=bestellung[0]['vornamelieferadresse']

                vorname_nachname=bestellung[0]['vornamelieferadresse']+""" """+bestellung[0]['nachnamelieferadresse']
                if bestellung[0]['unternehmensdetailslieferadresse']!="":
                    firmenname=bestellung[0]['unternehmensdetailslieferadresse']+"<br>"
                else:
                    firmenname=""

                strassenname_hausnummer=bestellung[0]['strasserechnung']+""" """+bestellung[0]['hausnummerrechnung']
                plz_stadt=bestellung[0]['plzlieferadresse']+""" """+bestellung[0]['stadtlieferadresse']
                
                bestellnummer=bestellung[0]['bestellnummer']
                lieferdatum=bestellung[0]['liefertermin']
                bestelldatum=bestellung[0]['datum']
                
                
                html_bestelldetails_email=""
                index=0
                for row_2 in bestelldetails:
                    print("123")

                    bild=json.loads(bestelldetails[index]['picture_link_small'])

                    bild=bild[0]["link"]
                    bild_alt=bestelldetails[index]['style']
                    style_name=bestelldetails[index]['style']
                    bhgroesse=bestelldetails[index]['bhgroesse']
                    slipgroesse=bestelldetails[index]['slipgroesse']
                    anzahl=bestelldetails[index]['anzahl']
                    preis=str('{0:.2f}'.format(int(bestelldetails[index]['anzahl'])*float(bestelldetails[index]['preis']))).replace(".", ",")
                    
 



                    html_bestelldetails_email=html_bestelldetails_email+"""<tr>
                        <td align="left">
                        <table cellpadding="0" cellspacing="0" border="0" align="center" wi=
                        dth="630" bgcolor="#ffffff">
                        <tbody>
                        <tr>
                        <td align="left" width="90" height="115"><img style="border: 1px so=
                        lid #eee;" width="90" height="115" src='https://www.darlinglace.com/"""+bild+"""' 
                        alt='"""+bild_alt+"""'></td>
                        <td align="left" width="30"></td>
                        <td align="left" width="400" valign="top"><font face="verdana" size="&#43;1">"""+style_name+"""</font><br>
                        <font face="verdana" size="-1" color="#787878">Slip: """+slipgroesse+"""<br>
                        BH: """+bhgroesse+"""<br>Anzahl: """+str(anzahl)+"""</font> </td>
                        <td align="right" width="110" valign="top"><font face="verdana" size="&#43;1">"""+preis+""" EUR</font></td>
                        </tr>
                        </tbody>
                        </table>
                        </td>
                        </tr>"""
                    index=index+1
                print(html_bestelldetails_email)          

                    

                zahlungsdetails_beschreibung="Bestellung:<br>"
                

                bestellung=str('{0:.2f}'.format(rebates[0]['bestellung'])).replace(".", ",")+" EUR"
                zahlungsdetails_werte=bestellung+"<br>"
                lieferkosten=str('{0:.2f}'.format(rebates[0]['lieferkosten'])).replace(".", ",")+" EUR"
                print lieferkosten
                if lieferkosten=="0,00 EUR":
                    lieferung_show="block"
                    zahlungsdetails_beschreibung=zahlungsdetails_beschreibung+"Lieferung:<br>"
                    lieferkosten="KOSTENLOS"
                    zahlungsdetails_werte=zahlungsdetails_werte+lieferkosten+"<br>"
                else:
                    lieferung_show="block"
                    zahlungsdetails_beschreibung=zahlungsdetails_beschreibung+"Lieferung:<br>"
                    zahlungsdetails_werte=zahlungsdetails_werte+lieferkosten+"<br>"
                    
                    
                VIP_sets_value=str('{0:.2f}'.format(rebates[0]['braforfreevalue'])).replace(".", ",")+" EUR"
                if VIP_sets_value=="0,00 EUR":
                    VIP_sets_show="none"
                else:
                    VIP_sets_show="block"
                    zahlungsdetails_werte=zahlungsdetails_werte+"-"+VIP_sets_value+"<br>"
                    zahlungsdetails_beschreibung=zahlungsdetails_beschreibung+"Sets umsonst (VIP):<br>"
                    
                VIP_guthaben_value=str('{0:.2f}'.format(rebates[0]['storecredit'])).replace(".", ",")+" EUR"
                if VIP_guthaben_value=="0,00 EUR":
                    VIP_guthaben_value_show="none"
                else:
                    VIP_guthaben_value_show="block"
                    zahlungsdetails_werte=zahlungsdetails_werte+"-"+VIP_guthaben_value+"<br>"
                    zahlungsdetails_beschreibung=zahlungsdetails_beschreibung+"VIP Guthaben:<br>"

                    
                rabatt=str('{0:.2f}'.format(rebates[0]['coupon'])).replace(".", ",")+" EUR"
                if rabatt=="0,00 EUR":
                    rabatt_show="none"
                else:
                    rabatt_show="block"
                    zahlungsdetails_werte=zahlungsdetails_werte+"-"+rabatt+"<br>"
                    zahlungsdetails_beschreibung=zahlungsdetails_beschreibung+"Rabatt:<br>"
                    
                freundschaftswerbung=str('{0:.2f}'.format(rebates[0]['credit'])).replace(".", ",")+" EUR"
                if freundschaftswerbung=="0,00 EUR":
                    freundschaftswerbung_show="none"
                else:
                    freundschaftswerbung_show="block"
                    zahlungsdetails_werte=zahlungsdetails_werte+"-"+freundschaftswerbung+"<br>"

                    zahlungsdetails_beschreibung=zahlungsdetails_beschreibung+"Freundschaftswerbung:<br>"
                    
                gesamt=str('{0:.2f}'.format(rebates[0]['gesamtpreis'])).replace(".", ",")+" EUR"
                




                
                darling_lace_logo=generate_link_email_marketing("https://www.darlinglace.com",row[1],"order_confirmation")
                header_mein_showroom=generate_link_email_marketing("https://www.darlinglace.com/Produktauswahl/Mein%20Showroom/",row[1],"order_confirmation")
                header_bh_sets=generate_link_email_marketing("https://www.darlinglace.com/Produktauswahl/BH%20Sets/",row[1],"order_confirmation")
                header_slip=generate_link_email_marketing("https://www.darlinglace.com/Produktauswahl/Slips/",row[1],"order_confirmation")
                instagram_link=generate_link_email_marketing("https://www.instagram.com/darling_lace/",row[1],"order_confirmation")
                facebook_link=generate_link_email_marketing("https://www.facebook.com/Darling-Lace-129368267722230/",row[1],"order_confirmation")
                kontaktiere_uns=generate_link_email_marketing("https://www.darlinglace.com/support/",row[1],"order_confirmation")
                VIP_club=generate_link_email_marketing("https://www.darlinglace.com/wie_funktioniert_VIP/",row[1],"order_confirmation")
                versand_retoure=generate_link_email_marketing("https://www.darlinglace.com/versand_rueckversand/",row[1],"order_confirmation")
                ueber_uns=generate_link_email_marketing("https://www.darlinglace.com/ueber_uns/",row[1],"order_confirmation")
                datenschutz=generate_link_email_marketing("https://www.darlinglace.com/datenschutz/",row[1],"order_confirmation")
                email_abbestellen=generate_link_email_marketing("https://www.darlinglace.com/newsletter_abmelden_page/?security_key="+get_newsletterabbestellencode(row[1],c),row[1],"order_confirmation")

            
                bestellung_bestellen_email=get_template('bestellung_bestellen_email_2.html')
                html=bestellung_bestellen_email.render({'campaign':'order_confirmation','email_abbestellen':email_abbestellen,'email_adresse':empfaenger,'datenschutz':datenschutz,'ueber_uns':ueber_uns,'versand_retoure':versand_retoure,'VIP_club':VIP_club,'kontaktiere_uns':kontaktiere_uns,'facebook_link':facebook_link,'instagram_link':instagram_link,'header_slip':header_slip,'header_bh_sets':header_bh_sets,'header_mein_showroom':header_mein_showroom,'darling_lace_logo':darling_lace_logo,'zahlungsdetails_werte':zahlungsdetails_werte,'zahlungsdetails_beschreibung':zahlungsdetails_beschreibung,'vorname':vorname,'bestelldatum':bestelldatum,'lieferung_show':lieferung_show,'VIP_sets_show':VIP_sets_show,'VIP_guthaben_value_show':VIP_guthaben_value_show,'rabatt_show':rabatt_show,'freundschaftswerbung_show':freundschaftswerbung_show,'bestelldetails':html_bestelldetails_email,'link_bestellungen':link_bestellungen,'link_profil':link_profil,'bestellnummer':bestellnummer,'lieferdatum':lieferdatum,'lieferdatum':lieferdatum,'vorname_nachname':vorname_nachname,'firmennname':firmenname,'strassenname_hausnummer':strassenname_hausnummer,'plz_stadt':plz_stadt,'bestellung':bestellung,'lieferkosten':lieferkosten,'VIP_sets_value':VIP_sets_value,'VIP_guthaben_value':VIP_guthaben_value,'rabatt':rabatt,'freundschaftswerbung':freundschaftswerbung,'gesamt':gesamt})



                text = strip_tags(html) 

                html=html.encode('utf8')


         

            #https://www.darlinglace.com/einladung/
                # Record the MIME types of both parts - text/plain and text/html.
            #    part2 = MIMEText(html.encode('utf-8'), 'plain', 'utf-8')
        #        part1 = ""
                part2 = MIMEText(html, 'html','utf-8')

                requests.post(
                    "https://api.mailgun.net/v3/darlinglace.de/messages",
                    auth=("api", "key-596fb4fd5ed94eed07b0321fc3a2d54d"),
                    data={"from": "Paula von Darling Lace <postmaster@darlinglace.de>",
                  "to": empfaenger,
                  "subject": subject,
                  "html": html})
                c.execute("""update order_confirmation_emails set emailsentout=%s where bestellnummer=%s""",("ja",bestellnummer,))

            else:
                print "bestellnummer macht probleme: "+bestellnummer

     
    conn.commit()



    #_________________________


    c.execute ("""select * from gutscheincodes_sent """)

    gutscheincodes_sent=c.fetchall()
    for row in gutscheincodes_sent:
        if row[4]=="no":
            code=row[0]
            empfaenger=row[3]
            betreff=row[8]
            message=row[7]
            von=row[9]
            reload(sys)
            sys.setdefaultencoding("ISO-8859-1")
            # me == my email address
            # you == recipient's email address
            me = "Paula von Darling Lace <service@darlinglace.com>"
            you = empfaenger

            # Create message container - the correct MIME type is multipart/alternative.
            msg = MIMEMultipart('alternative')
            msg['Subject'] = betreff
            msg['From'] = von
            msg['To'] = empfaenger












            
            darling_lace_logo=generate_link_email_marketing("https://www.darlinglace.com",code,"freunde_einladen")
            header_mein_showroom=generate_link_email_marketing("https://www.darlinglace.com/Produktauswahl/Mein%20Showroom/",code,"freunde_einladen")
            header_bh_sets=generate_link_email_marketing("https://www.darlinglace.com/Produktauswahl/BH%20Sets/",code,"freunde_einladen")
            header_slip=generate_link_email_marketing("https://www.darlinglace.com/Produktauswahl/Slips/",code,"freunde_einladen")
            instagram_link=generate_link_email_marketing("https://www.instagram.com/darling_lace/",code,"freunde_einladen")
            facebook_link=generate_link_email_marketing("https://www.facebook.com/Darling-Lace-129368267722230/",code,"freunde_einladen")
            kontaktiere_uns=generate_link_email_marketing("https://www.darlinglace.com/support/",code,"freunde_einladen")
            VIP_club=generate_link_email_marketing("https://www.darlinglace.com/wie_funktioniert_VIP/",code,"freunde_einladen")
            versand_retoure=generate_link_email_marketing("https://www.darlinglace.com/versand_rueckversand/",code,"freunde_einladen")
            ueber_uns=generate_link_email_marketing("https://www.darlinglace.com/ueber_uns/",code,"freunde_einladen")
            datenschutz=generate_link_email_marketing("https://www.darlinglace.com/datenschutz/",code,"freunde_einladen")
            einladung=generate_link_email_marketing("https://www.darlinglace.com/einladung?gutscheincode="+code,code,"freunde_einladen")
            email_abbestellen=generate_link_email_marketing("https://www.darlinglace.com/newsletter_abmelden_page/?security_key="+get_newsletterabbestellencode(code,c),code,"freunde_einladen")
            
            t=get_template('freunde_einladen_email.html')
            html=t.render({'campaign':'freunde_einladen','email_abbestellen':email_abbestellen,'von':von,'message':message,'einladung':einladung,'email_adresse':empfaenger,'datenschutz':datenschutz,'ueber_uns':ueber_uns,'versand_retoure':versand_retoure,'VIP_club':VIP_club,'kontaktiere_uns':kontaktiere_uns,'facebook_link':facebook_link,'instagram_link':instagram_link,'header_slip':header_slip,'header_bh_sets':header_bh_sets,'header_mein_showroom':header_mein_showroom,'darling_lace_logo':darling_lace_logo,'code':code})









            text = strip_tags(html) 

            html=html.encode('utf8')




        #https://www.darlinglace.com/einladung/
            # Record the MIME types of both parts - text/plain and text/html.
        #    part2 = MIMEText(html.encode('utf-8'), 'plain', 'utf-8')
            part1 = MIMEText(text.encode('utf-8'), 'plain')
            part2 = MIMEText(html, 'html','utf-8')




            requests.post(
                "https://api.mailgun.net/v3/darlinglace.de/messages",
                auth=("api", "key-596fb4fd5ed94eed07b0321fc3a2d54d"),
                data={"from": "Paula von Darling Lace <postmaster@darlinglace.de>",
              "to": empfaenger,
              "subject": betreff,
              "html": html})

            c.execute("""update gutscheincodes_sent set emailsent=%s,emailsentdate=%s,emailsenttime=%s where email=%s""",("yes",get_date_stamp_now(),get_time_stamp_now(),row[3]))

        



    conn.commit()



    #___________________________


    c.execute ("""select * from shipping_confirmation_emails """)

    shipping_confirmation_emails=c.fetchall()
    for row in shipping_confirmation_emails:
        if row[5]=="nein":
            bestellnummer=row[0]
            usercode=row[1]
            to=row[2]
            subject=row[3]
            tracking_number=row[4]
            x=row[1]
            empfaenger=row[2]

            # me == my email address
            # you == recipient's email address
            me = "Paula von Darling Lace <service@darlinglace.com>"
            you = to
            reload(sys)
            sys.setdefaultencoding("ISO-8859-1")

            # Create message container - the correct MIME type is multipart/alternative.
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = me
            msg['To'] = you

            von=me

            bestelldetails=define_bestelldetails(x,bestellnummer,"","",c,get_modelAB(x,c),get_subpicture(x,c))
            rebates=define_rebates(x,bestellnummer,"","","",c,conn,"","no","no","no")
            bestellung=define_bestellung(x,bestellnummer,c,"nein")
            print(bestellung)
            if bestellung!="[]" and rebates!="[]" and bestelldetails!="[]":

                bestelldetails=json.loads(bestelldetails)
                rebates=json.loads(rebates)
                bestellung=json.loads(bestellung)

                link_bestellungen='https://www.darlinglace.com/account_page/bestellungen_ansehen/'+bestellung[0]['bestellnummer']
                link_profil='https://www.darlinglace.com/account_page/'
                link_hilfe='https://www.darlinglace.com/help/'

                vorname=bestellung[0]['vornamelieferadresse']

                vorname_nachname=bestellung[0]['vornamelieferadresse']+""" """+bestellung[0]['nachnamelieferadresse']
                if bestellung[0]['unternehmensdetailslieferadresse']!="":
                    firmenname=bestellung[0]['unternehmensdetailslieferadresse']+"<br>"
                else:
                    firmenname=""

                strassenname_hausnummer=bestellung[0]['strasserechnung']+""" """+bestellung[0]['hausnummerrechnung']
                plz_stadt=bestellung[0]['plzlieferadresse']+""" """+bestellung[0]['stadtlieferadresse']
                
                bestellnummer=bestellung[0]['bestellnummer']
                lieferdatum=bestellung[0]['liefertermin']
                bestelldatum=bestellung[0]['datum']
                
                
                html_bestelldetails_email=""
                index=0
                for row_2 in bestelldetails:
                    print("123")

                    bild=json.loads(bestelldetails[index]['picture_link_small'])

                    bild=bild[0]["link"]
                    bild_alt=bestelldetails[index]['style']
                    style_name=bestelldetails[index]['style']
                    bhgroesse=bestelldetails[index]['bhgroesse']
                    slipgroesse=bestelldetails[index]['slipgroesse']
                    anzahl=bestelldetails[index]['anzahl']
                    preis=str('{0:.2f}'.format(int(bestelldetails[index]['anzahl'])*float(bestelldetails[index]['preis']))).replace(".", ",")
                    
 



                    html_bestelldetails_email=html_bestelldetails_email+"""<tr>
                        <td align="left">
                        <table cellpadding="0" cellspacing="0" border="0" align="center" wi=
                        dth="630" bgcolor="#ffffff">
                        <tbody>
                        <tr>
                        <td align="left" width="90" height="115"><img style="border: 1px so=
                        lid #eee;" width="90" height="115" src='https://www.darlinglace.com/"""+bild+"""' 
                        alt='"""+bild_alt+"""'></td>
                        <td align="left" width="30"></td>
                        <td align="left" width="400" valign="top"><font face="verdana" size="&#43;1">"""+style_name+"""</font><br>
                        <font face="verdana" size="-1" color="#787878">Slip: """+slipgroesse+"""<br>
                        BH: """+bhgroesse+"""<br>Anzahl: """+str(anzahl)+"""</font> </td>
                        <td align="right" width="110" valign="top"><font face="verdana" size="&#43;1">"""+preis+""" EUR</font></td>
                        </tr>
                        </tbody>
                        </table>
                        </td>
                        </tr>"""
                    index=index+1
                print(html_bestelldetails_email)          

                    

                zahlungsdetails_beschreibung="Bestellung:<br>"
                

                bestellung=str('{0:.2f}'.format(rebates[0]['bestellung'])).replace(".", ",")+" EUR"
                zahlungsdetails_werte=bestellung+"<br>"
                lieferkosten=str('{0:.2f}'.format(rebates[0]['lieferkosten'])).replace(".", ",")+" EUR"
                if lieferkosten=="0,00 EUR":
                    lieferung_show="block"
                    zahlungsdetails_beschreibung=zahlungsdetails_beschreibung+"Lieferung:<br>"
                    lieferkosten="KOSTENLOS"
                    zahlungsdetails_werte=zahlungsdetails_werte+lieferkosten+"<br>"
                else:
                    lieferung_show="block"
                    zahlungsdetails_beschreibung=zahlungsdetails_beschreibung+"Lieferung:<br>"
                    zahlungsdetails_werte=zahlungsdetails_werte+lieferkosten+"<br>"
                    
                    
                VIP_sets_value=str('{0:.2f}'.format(rebates[0]['braforfreevalue'])).replace(".", ",")+" EUR"
                if VIP_sets_value=="0,00 EUR":
                    VIP_sets_show="none"
                else:
                    VIP_sets_show="block"
                    zahlungsdetails_werte=zahlungsdetails_werte+"-"+VIP_sets_value+"<br>"
                    zahlungsdetails_beschreibung=zahlungsdetails_beschreibung+"Sets umsonst (VIP):<br>"
                    
                VIP_guthaben_value=str('{0:.2f}'.format(rebates[0]['storecredit'])).replace(".", ",")+" EUR"
                if VIP_guthaben_value=="0,00 EUR":
                    VIP_guthaben_value_show="none"
                else:
                    VIP_guthaben_value_show="block"
                    zahlungsdetails_werte=zahlungsdetails_werte+"-"+VIP_guthaben_value+"<br>"
                    zahlungsdetails_beschreibung=zahlungsdetails_beschreibung+"VIP Guthaben:<br>"

                    
                rabatt=str('{0:.2f}'.format(rebates[0]['coupon'])).replace(".", ",")+" EUR"
                if rabatt=="0,00 EUR":
                    rabatt_show="none"
                else:
                    rabatt_show="block"
                    zahlungsdetails_werte=zahlungsdetails_werte+"-"+rabatt+"<br>"
                    zahlungsdetails_beschreibung=zahlungsdetails_beschreibung+"Rabatt:<br>"
                    
                freundschaftswerbung=str('{0:.2f}'.format(rebates[0]['credit'])).replace(".", ",")+" EUR"
                if freundschaftswerbung=="0,00 EUR":
                    freundschaftswerbung_show="none"
                else:
                    freundschaftswerbung_show="block"
                    zahlungsdetails_werte=zahlungsdetails_werte+"-"+freundschaftswerbung+"<br>"

                    zahlungsdetails_beschreibung=zahlungsdetails_beschreibung+"Freundschaftswerbung:<br>"
                    
                gesamt=str('{0:.2f}'.format(rebates[0]['gesamtpreis'])).replace(".", ",")+" EUR"
                


                
                darling_lace_logo=generate_link_email_marketing("https://www.darlinglace.com",row[1],"shipping_confirmation")
                header_mein_showroom=generate_link_email_marketing("https://www.darlinglace.com/Produktauswahl/Mein%20Showroom/",row[1],"shipping_confirmation")
                header_bh_sets=generate_link_email_marketing("https://www.darlinglace.com/Produktauswahl/BH%20Sets/",row[1],"shipping_confirmation")
                header_slip=generate_link_email_marketing("https://www.darlinglace.com/Produktauswahl/Slips/",row[1],"shipping_confirmation")
                instagram_link=generate_link_email_marketing("https://www.instagram.com/darling_lace/",row[1],"shipping_confirmation")
                facebook_link=generate_link_email_marketing("https://www.facebook.com/Darling-Lace-129368267722230/",row[1],"shipping_confirmation")
                kontaktiere_uns=generate_link_email_marketing("https://www.darlinglace.com/support/",row[1],"shipping_confirmation")
                VIP_club=generate_link_email_marketing("https://www.darlinglace.com/wie_funktioniert_VIP/",row[1],"shipping_confirmation")
                versand_retoure=generate_link_email_marketing("https://www.darlinglace.com/versand_rueckversand/",row[1],"shipping_confirmation")
                ueber_uns=generate_link_email_marketing("https://www.darlinglace.com/ueber_uns/",row[1],"shipping_confirmation")
                datenschutz=generate_link_email_marketing("https://www.darlinglace.com/datenschutz/",row[1],"shipping_confirmation")
                datenschutz=generate_link_email_marketing("https://www.darlinglace.com/datenschutz/",row[1],"shipping_confirmation")
                link_tracking=generate_link_email_marketing('https://www.darlinglace.com/account_page/sendungsverfolgung_tracken/'+bestellnummer,row[1],"shipping_confirmation")
                email_abbestellen=generate_link_email_marketing("https://www.darlinglace.com/newsletter_abmelden_page/?security_key="+get_newsletterabbestellencode(row[1],c),row[1],"shipping_confirmation")



                bestellung_bestellen_email=get_template('bestellung_versenden_email.html')
                html=bestellung_bestellen_email.render({'campaign':'shipping_confirmation','email_abbestellen':email_abbestellen,'link_tracking':link_tracking,'email_adresse':empfaenger,'datenschutz':datenschutz,'ueber_uns':ueber_uns,'versand_retoure':versand_retoure,'VIP_club':VIP_club,'kontaktiere_uns':kontaktiere_uns,'facebook_link':facebook_link,'instagram_link':instagram_link,'header_slip':header_slip,'header_bh_sets':header_bh_sets,'header_mein_showroom':header_mein_showroom,'darling_lace_logo':darling_lace_logo,'zahlungsdetails_werte':zahlungsdetails_werte,'zahlungsdetails_beschreibung':zahlungsdetails_beschreibung,'vorname':vorname,'bestelldatum':bestelldatum,'lieferung_show':lieferung_show,'VIP_sets_show':VIP_sets_show,'VIP_guthaben_value_show':VIP_guthaben_value_show,'rabatt_show':rabatt_show,'freundschaftswerbung_show':freundschaftswerbung_show,'bestelldetails':html_bestelldetails_email,'link_bestellungen':link_bestellungen,'link_profil':link_profil,'bestellnummer':bestellnummer,'lieferdatum':lieferdatum,'lieferdatum':lieferdatum,'vorname_nachname':vorname_nachname,'firmennname':firmenname,'strassenname_hausnummer':strassenname_hausnummer,'plz_stadt':plz_stadt,'bestellung':bestellung,'lieferkosten':lieferkosten,'VIP_sets_value':VIP_sets_value,'VIP_guthaben_value':VIP_guthaben_value,'rabatt':rabatt,'freundschaftswerbung':freundschaftswerbung,'gesamt':gesamt})



                text = strip_tags(html) 

                html=html.encode('utf8')




            #https://www.darlinglace.com/einladung/
                # Record the MIME types of both parts - text/plain and text/html.
            #    part2 = MIMEText(html.encode('utf-8'), 'plain', 'utf-8')
         #       part1 = MIMEText(text, 'plain')
                part2 = MIMEText(html, 'html','utf-8')

                # Attach parts into message container.
                # According to RFC 2046, the last part of a multipart message, in this case
                # the HTML message, is best and preferred.
                requests.post(
                    "https://api.mailgun.net/v3/darlinglace.de/messages",
                    auth=("api", "key-596fb4fd5ed94eed07b0321fc3a2d54d"),
                    data={"from": "Paula von Darling Lace <postmaster@darlinglace.de>",
                  "to": empfaenger,
                  "subject": subject,
                  "html": html})
                c.execute("""update shipping_confirmation_emails set emailsentout=%s where bestellnummer=%s""",("ja",bestellnummer,))

















    conn.commit()









    

    #__________________________

    c.execute ("""select * from email_passwort_zuruecksetzen """)
    email_passwort_zuruecksetzen=c.fetchall()
    for row in email_passwort_zuruecksetzen:
        if row[2]=="nein":
            empfaenger=row[0]
            code=row[1]
            
            reload(sys)
            sys.setdefaultencoding("ISO-8859-1")
            # me == my email address
            # you == recipient's email address
            me = "Paula von Darling Lace <service@darlinglace.com>"
            you = empfaenger

            print("los")
            print(empfaenger)

            # Create message container - the correct MIME type is multipart/alternative.
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "Passwort vergessen"
            msg['From'] = me
            msg['To'] = empfaenger

            # Create the body of the message (a plain-text and an HTML version).




            
            darling_lace_logo=generate_link_email_marketing("https://www.darlinglace.com",row[3],"passwort_vergessen")
            header_mein_showroom=generate_link_email_marketing("https://www.darlinglace.com/Produktauswahl/Mein%20Showroom/",row[3],"passwort_vergessen")
            header_bh_sets=generate_link_email_marketing("https://www.darlinglace.com/Produktauswahl/BH%20Sets/",row[3],"passwort_vergessen")
            header_slip=generate_link_email_marketing("https://www.darlinglace.com/Produktauswahl/Slips/",row[3],"passwort_vergessen")
            instagram_link=generate_link_email_marketing("https://www.instagram.com/darling_lace/",row[3],"passwort_vergessen")
            facebook_link=generate_link_email_marketing("https://www.facebook.com/Darling-Lace-129368267722230/",row[3],"passwort_vergessen")
            kontaktiere_uns=generate_link_email_marketing("https://www.darlinglace.com/support/",row[3],"passwort_vergessen")
            VIP_club=generate_link_email_marketing("https://www.darlinglace.com/wie_funktioniert_VIP/",row[3],"passwort_vergessen")
            versand_retoure=generate_link_email_marketing("https://www.darlinglace.com/versand_rueckversand/",row[3],"passwort_vergessen")
            ueber_uns=generate_link_email_marketing("https://www.darlinglace.com/ueber_uns/",row[3],"passwort_vergessen")
            datenschutz=generate_link_email_marketing("https://www.darlinglace.com/datenschutz/",row[3],"passwort_vergessen")
            passwort_vergessen=generate_link_email_marketing("https://www.darlinglace.com/passwort_vergessen_bestaetigen/"+code,row[3],"passwort_vergessen")
            email_abbestellen=generate_link_email_marketing("https://www.darlinglace.com/newsletter_abmelden_page/?security_key="+get_newsletterabbestellencode(row[3],c),row[3],"passwort_vergessen")
            
            t=get_template('passwort_zuruecksetzen_email.html')
            html=t.render({'campaign':'passwort_vergessen','email_abbestellen':email_abbestellen,'passwort_vergessen':passwort_vergessen,'email_adresse':empfaenger,'datenschutz':datenschutz,'ueber_uns':ueber_uns,'versand_retoure':versand_retoure,'VIP_club':VIP_club,'kontaktiere_uns':kontaktiere_uns,'facebook_link':facebook_link,'instagram_link':instagram_link,'header_slip':header_slip,'header_bh_sets':header_bh_sets,'header_mein_showroom':header_mein_showroom,'darling_lace_logo':darling_lace_logo,'code':code})







            text = strip_tags(html) 

            html=html.encode('utf8')


        #https://www.darlinglace.com/einladung/
            # Record the MIME types of both parts - text/plain and text/html.
        #    part2 = MIMEText(html.encode('utf-8'), 'plain', 'utf-8')
     #       part1 = MIMEText(text, 'plain')
            part2 = MIMEText(html, 'html','utf-8')

            # Attach parts into message container.
            # According to RFC 2046, the last part of a multipart message, in this case
            # the HTML message, is best and preferred.
     #       msg.attach(part1)
            requests.post(
                "https://api.mailgun.net/v3/darlinglace.de/messages",
                auth=("api", "key-596fb4fd5ed94eed07b0321fc3a2d54d"),
                data={"from": "Paula von Darling Lace <postmaster@darlinglace.de>",
              "to": empfaenger,
              "subject": "Passwort vergessen",
              "html": html})
            c.execute("""update email_passwort_zuruecksetzen set emailsentout=%s where securitycode=%s""",("ja",code,))









    conn.commit()





    #____________________


    c.execute ("""select * from anmeldebestaetigungen """)
    print "anmeldebestaetigungen sent mail"

    anmeldebestaetigungen=c.fetchall()
    for row in anmeldebestaetigungen:
        print row[10]
        print row[0]
        if row[10]=="false":
            
            empfaenger=row[0]
            code=row[1]
            
            reload(sys)
            sys.setdefaultencoding("ISO-8859-1")

            
            # me == my email address
            # you == recipient's email address
            me = "Paula von Darling Lace <service@darlinglace.com>"
            you = empfaenger

            print("los")
            print(empfaenger)

            # Create message container - the correct MIME type is multipart/alternative.
            msg = MIMEMultipart('alternative')
            msg['Subject'] = u'Anmeldung bestätigen'
            msg['From'] = me
            msg['To'] = empfaenger

            # Create the body of the message (a plain-text and an HTML version).



            
            darling_lace_logo=generate_link_email_marketing("https://www.darlinglace.com",row[11],"welcome")
            header_mein_showroom=generate_link_email_marketing("https://www.darlinglace.com/Produktauswahl/Mein%20Showroom/",row[11],"welcome")
            header_bh_sets=generate_link_email_marketing("https://www.darlinglace.com/Produktauswahl/BH%20Sets/",row[11],"welcome")
            header_slip=generate_link_email_marketing("https://www.darlinglace.com/Produktauswahl/Slips/",row[11],"welcome")
            instagram_link=generate_link_email_marketing("https://www.instagram.com/darling_lace/",row[11],"welcome")
            facebook_link=generate_link_email_marketing("https://www.facebook.com/Darling-Lace-129368267722230/",row[11],"welcome")
            kontaktiere_uns=generate_link_email_marketing("https://www.darlinglace.com/support/",row[11],"welcome")
            VIP_club=generate_link_email_marketing("https://www.darlinglace.com/wie_funktioniert_VIP/",row[11],"welcome")
            versand_retoure=generate_link_email_marketing("https://www.darlinglace.com/versand_rueckversand/",row[11],"welcome")
            ueber_uns=generate_link_email_marketing("https://www.darlinglace.com/ueber_uns/",row[11],"welcome")
            datenschutz=generate_link_email_marketing("https://www.darlinglace.com/datenschutz/",row[11],"welcome")
            anmeldung_bestaetigen=generate_link_email_marketing("https://www.darlinglace.com/anmeldung_bestaetigen/"+code,row[11],"welcome")
            email_abbestellen=generate_link_email_marketing("https://www.darlinglace.com/newsletter_abmelden_page/?security_key="+get_newsletterabbestellencode(row[11],c),row[11],"welcome")
            if row[12]=="":
                t=get_template('welcome_email.html')
                html=t.render({'campaign':'welcome','anmeldung_bestaetigen':anmeldung_bestaetigen,'email_adresse':empfaenger,'datenschutz':datenschutz,'ueber_uns':ueber_uns,'versand_retoure':versand_retoure,'VIP_club':VIP_club,'kontaktiere_uns':kontaktiere_uns,'facebook_link':facebook_link,'instagram_link':instagram_link,'header_slip':header_slip,'header_bh_sets':header_bh_sets,'header_mein_showroom':header_mein_showroom,'darling_lace_logo':darling_lace_logo,'code':code})
            else:
                t=get_template('welcome_email_with_password.html')
                html=t.render({'campaign':'welcome','email_abbestellen':email_abbestellen,'password':row[12],'anmeldung_bestaetigen':anmeldung_bestaetigen,'email_adresse':empfaenger,'datenschutz':datenschutz,'ueber_uns':ueber_uns,'versand_retoure':versand_retoure,'VIP_club':VIP_club,'kontaktiere_uns':kontaktiere_uns,'facebook_link':facebook_link,'instagram_link':instagram_link,'header_slip':header_slip,'header_bh_sets':header_bh_sets,'header_mein_showroom':header_mein_showroom,'darling_lace_logo':darling_lace_logo,'code':code})
                
            text = strip_tags(html) 

            html=html.encode('utf8')




        #https://www.darlinglace.com/einladung/
            # Record the MIME types of both parts - text/plain and text/html.
        #    part2 = MIMEText(html.encode('utf-8'), 'plain', 'utf-8')
            part1 = MIMEText(text.encode('utf-8'), 'plain')
            part2 = MIMEText(html, 'html','utf-8')


            requests.post(
                "https://api.mailgun.net/v3/darlinglace.de/messages",
                auth=("api", "key-596fb4fd5ed94eed07b0321fc3a2d54d"),
                data={"from": "Paula von Darling Lace <postmaster@darlinglace.de>",
              "to": empfaenger,
              "subject": u'Anmeldung bestätigen',
              "html": html})
            c.execute("""update anmeldebestaetigungen set firstemailsentout=%s where code=%s""",("true",code,))
            conn.commit()





        
#    mail.close()
    timer=timer+1
    if timer <=10:
        s.enter(10, 1, do_something, (sc,))
if timer <=10:
    s.enter(10, 1, do_something, (s,))
    s.run()
print "timer"
print timer



