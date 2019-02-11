
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

conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                        password='okano1988',database='maxfischer2database')
c = conn.cursor(buffered=True)
c.execute ("""select * from shipping_confirmation_emails """)

shipping_confirmation_emails=c.fetchall()
for row in shipping_confirmation_emails:
    if row[5]=="nein":
        bestellnummer=row[0]
        usercode=row[1]
        to=row[2]
        subject=row[3]
        tracking_number=row[4]

        # me == my email address
        # you == recipient's email address
        me = "service@darlinglace.com"
        you = to

        reload(sys)
        sys.setdefaultencoding("ISO-8859-1")

        
        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = me
        msg['To'] = you

        von=me

        bestelldetails=define_bestelldetails(usercode,bestellnummer,"","",c,get_modelAB(usercode,c),get_subpicture(usercode,c))
        rebates=define_rebates(usercode,bestellnummer,"","","",c,conn,"","no","no","no")
        bestellung=define_bestellung(usercode,bestellnummer,c)

    #try:
        bestelldetails=json.loads(bestelldetails)
        rebates=json.loads(rebates)
        bestellung=json.loads(bestellung)


        link_tracking='https://www.darlinglace.com/account_page/sendungsverfolgung_tracken/'+bestellnummer
        link_hilfe='https://www.darlinglace.com/help/'        
        print(bestellung[0])
        
        # Create the body of the message (a plain-text and an HTML version).
        text = "WIllkommen zu Darling Lace"

        html = """<html><head><link rel='stylesheet' href='https://www.darlinglace.comstatic/order_summary_style_3.css' type='text/css' media='all' /></head><body style="font-family:Helvetica;font-size:14px;">"""
        html=html+"""<link rel='stylesheet' href='/static/order_summary_style_3.css' type='text/css' media='all' />"""
        html=html+"""<style>.bestellnummer_email { 	 text-align:left;font-weight: bold;font-size:18px; }</style>"""
        html=html+"""<style>.button_check {background-color:#DB7093;color:#FFFFFF;font-weight:bold;float:left;border-radius: 5px;cursor:pointer;text-align:center;height:28px;width:130px;padding-top:10px; }</style>""" 

            

        
        html=html+"""<div style='background-color:#404040;width:100%;height:50px;margin-left:5px;margin-right:5px;'>"""    
        html=html+"""<div style='width:20%;margin: 0 auto;float:center;text-align: center;line-height:50px;'>"""

        html=html+"""<a href='https://www.darlinglace.com/' style='text-decoration:none !important; text-decoration:none;color:#ffffff;'><div style='height:50px;cursor:pointer;background: url("https://www.darlinglace.com/static/darling_lace.png");background-size: 150px 30px;background-position: center center; background-repeat:   no-repeat;'  ></div></a></div>"""
        html=html+"""</div></div><br>"""


        html=html+"""<div style='margin: 0 auto;max-width:500px;'><br>"""

        html=html+"""Hi """+bestellung[0]['vorname']+""",<br><br>Danke noch einmal, dass du bei uns eingekauft hast. Deine Bestellung wurde verschickt und befindet sich auf dem Weg zu dir. Klicke <a href='"""+link_tracking+"""'>hier</a>, damit du deine Bestellung tracken kannst.<br>   dass du bei uns eingekauft hast. Du hast eine tolle Auswahl getroffen, welche dir sehr gut passen sollte!<br>Genieß deine neue Lingerie!<br>"""

        html=html+"""<div class="headline" style='float:left;width:100%'><div class="bestellnummer_email" style="float:left;width:50%;text-align:left">Versandbestätigung</div>"""
    #    html=html+"""<div class="headline_text" style='font-size:14px;width:45%;float:right;line-height:20px;'>Bestellnummer: <font color="#DB7093" size="3"><b>"""+bestellung[0]['bestellnummer'].upper()+"""</font></b><br><font  color="#404040">Bestelldatum: """+bestellung[0]['datum']+"""</font></div></div><br>"""

        html=html+"""<div style='width:49%;font-size:14px;text-align:right;float:right;line-height:15px;'><br>Bestellnummer:<br>"""
        html=html+"""<b><font color="#DB7093" size="4">"""+bestellung[0]['bestellnummer']+"""</b></font><br>"""
        html=html+"""<br>Bestelldatum: <br><b>"""+bestellung[0]['datum']+"""</b>"""
        html=html+"""</div>"""
    #+"""<br>Lieferdatum: """+bestellung[0]['liefertermin']




        html=html+"""<div style='width:100%;border-top:1px solid #e6e6e6 ;float:left;margin-top:20px;'><div class="bestellnummer_email">Lieferdetails</div>"""
        html=html+"""<div style='width:50%;font-size:14px;text-align:left;line-height:15px;float:left;'>"""
        html=html+"""Lieferdatum: <br><b>"""+bestellung[0]['liefertermin']+"""</b><br><br>"""
        html=html+"""Versand durch: <br><b>DHL</b><br><br>"""
        html=html+"""</div>"""
        
        html=html+"""<div style='width:50%;font-size:14px;text-align:right;line-height:15px;float:right;'>Lieferadresse:<br><b>"""
        html=html+bestellung[0]['vorname']+""" """+bestellung[0]['nachname']+"""<br>"""
        if bestellung[0]['unternehmensdetails']!="":
            html=html+bestellung[0]['unternehmensdetails']+"""<br>"""
        html=html+bestellung[0]['adresse']+"""<br>"""
        html=html+bestellung[0]['plz']+""" """+bestellung[0]['stadt']+"""<br>"""

        html=html+"""</b></div></div><br>"""    


        

        
        html=html+"""<div style='width:100%;border-top:1px solid #e6e6e6 ;float:left;margin-top:20px;'><div class="bestellnummer_email" style='margin-bottom:10px;'>Bestelldetails</div>"""
        index=0
        for row in bestelldetails:

            print(bestelldetails)
            print(bestelldetails[0])

            html=html+"""<div style='width:100%;margin: 0 auto;float:center;text-align: left;line-height:20px;'>"""
            html=html+"""<div style='float:left;width:100%;margin-bottom:10px;'>"""
            html=html+"""<img src='https://www.darlinglace.com/"""+bestelldetails[index]['picture_link_small']+"""' style='width:100px;float:left;'/>"""
            html=html+"""<div style='margin-left:10px;float:left;'/><b>"""+bestelldetails[index]['style']+"""</b></div>"""
            html=html+"""<div class='anzahl_anzeigen' style='float:right;font-size:14px;'>"""+str(bestelldetails[index]['preis']).replace(".", ",")+""" EUR</div>"""
            html=html+"""<br><div class='details_order'>"""+bestelldetails[index]['bhgroesse']+"""</div> <br>"""
            html=html+"""<div class='details_order'>"""+bestelldetails[index]['slipgroesse']+"""</div><br><br>"""
            html=html+"""<div class='details_order' style='width:120px'>Anzahl: """+str(bestelldetails[index]['anzahl'])+"""</div> </div></div>""";

            index=index+1

        html=html+"""<div style='width:100%;border-top:1px solid #e6e6e6 ;float:left;margin-top:20px;'><div class="bestellnummer_email">Zahlungsdetails</div>"""
        html=html+"""<div style='margin: 0 auto;float:right;line-height:25px;text-align:center;width:250px;font-size:14px;'>"""    

        html=html+"""<div style='float:left;'>Bestellung:</div><div style='float:right;width:50%;text-align:right;'>"""+str('{0:.2f}'.format(rebates[0]['bestellung'])).replace(".", ",")+""" EUR</div><br>""";

        html=html+"""<div style='float:left;'>Lieferung:</div><div style='float:right;width:50%;text-align:right;'>KOSTENLOS</div><br>""";


        if rebates[0]['braforfreevalue']!=0:
            html=html+"""<div style='float:left;'>Sets umsonst (VIP):</div><div style='float:right;width:50%;text-align:right;'>-"""+str('{0:.2f}'.format(rebates[0]['braforfreevalue'])).replace(".", ",")+""" EUR</div><br>""";
        if rebates[0]['storecredit']!=0:
            html=html+"""<div style='float:left;'>VIP Guthaben:</div><div style='float:right;width:50%;text-align:right;'>-"""+str('{0:.2f}'.format(rebates[0]['storecredit'])).replace(".", ",")+""" EUR</div><br>""";



        if rebates[0]['coupon']!=0:
            html=html+"""<div style='float:left;'>Rabatt:</div><div style='float:right;'>-"""+str('{0:.2f}'.format(rebates[0]['coupon'])).replace(".", ",")+""" EUR</div><br>""";	

        if rebates[0]['credit']!=0:
            html=html+"""<div style='float:left;'>Freundschaftswerbung:</div><div style='float:right;'>-"""+str('{0:.2f}'.format(rebates[0]['credit'])).replace(".", ",")+""" EUR</div><br>""";	
                
                

        

        html=html+"""<br><div style='float:left;font-weight: bold;'>Gesamt:</div><div style='float:right;font-weight: bold;'>"""+str('{0:.2f}'.format(rebates[0]['gesamtpreis'])).replace(".", ",")+""" EUR</div><br><br>""";




        html=html+"""</div>""";



        html=html+"""<div style='width:100%;border-top:1px solid #e6e6e6 ;float:left;'><div class="bestellnummer_email"></div>"""
        html=html+"""<div style='width:100%;font-size:14px;text-align:left;line-height:15px;float:left;margin-top:20px;'>"""
        html=html+"""Hast du noch Fragen? Dann besuche gerne unsere <a href='"""+link_hilfe+"""'>Hilfe-Seite</a>!<br><br>Xoxo,<br>Darling Lace"""

        html=html+"""</div>"""
        


        html=html+"""</div><br>"""    




        html=html+"""<div style='width:100%;border-top:1px solid #e6e6e6 ;float:left;margin-top:20px;font-size:10px;margin:0 auto;'><div class="bestellnummer_email" style='font-size:10px;'><br></div>"""
        html=html+"""<div style='width:100%;text-align:center;line-height:15px;'>"""
        html=html+"""Darling Lace GmbH | Chausseestraße 60 | 10115 Berlin | Geschäftsführung: Maximilian Fischer, Kai Winselmann<br>"""
        html=html+"""Handelsregister: Berlin Charlottenburg HRB XXX<br>"""
        html=html+"""<a href='https://www.darlinglace.com/datenschutz/'>Datenschutz</a><br>"""
            
        html=html+"</div></div>" 
        


        html=html+"""</div><br>""" 



    #    html=html+"""<div style='border-bottom:1px solid #e6e6e6 ;'></div></div>""";

    #    html=html+"""<div style='width:100%'><br>Hast du noch Fragen? Dann besuche gerne unsere <a href='"""+link_hilfe+"""'>Hilfe-Seite</a>!<br><br>"""
    #    html=html+"""Viele Grüße,<br>Darling Lace"""
    #    html=html+"""<br><br></div>"""
    #    html=html+"""<div style='border-bottom:1px solid #e6e6e6 ;'></div>""";

    #    html=html+"""<div style='width:100%;margin: 0 auto;float:center;font-size:10px;text-align:center;line-height:15px;'>""" 
    #    html=html+"""Lingerie International GmbH<br>XXX<br>XXX<br>XXX</div>"""   
        html=html+"""</body></html>"""

    #https://www.darlinglace.com/einladung/
        # Record the MIME types of both parts - text/plain and text/html.
    #    part2 = MIMEText(html.encode('utf-8'), 'plain', 'utf-8')
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html','utf-8')

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        msg.attach(part1)
        msg.attach(part2)
        # Send the message via local SMTP server.
        mail = smtplib.SMTP_SSL('smtp.strato.de:465')

        mail.ehlo()



        mail.login('service@darlinglace.com', 'Li_ngerie2017_')
        mail.sendmail(me, you, msg.as_string())
        mail.close()


    #except:
        print("error")






        c.execute("""update shipping_confirmation_emails set emailsentout=%s where bestellnummer=%s""",("ja",bestellnummer,))
conn.commit()
