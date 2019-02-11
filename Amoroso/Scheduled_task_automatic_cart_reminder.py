
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







ab_path = "/home/maxfischer2/Amoroso/"
sys.path.append(ab_path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()










def generate_link_email_marketing(link,userid,email_name):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                            password='okano1988',database='maxfischer2database')
    c = conn.cursor(buffered=True)



    hashcode=hashlib.sha512(link+userid+email_name).hexdigest()



    count_rows_email_marketing_links=c.execute ("""select * from email_marketing_links where hashcode=%s """,(hashcode,))
    c.execute(count_rows_email_marketing_links)
    zaehler_email_marketing_links=int(c.rowcount)
    if zaehler_email_marketing_links==0:
        c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s)""" % ("email_marketing_links"), (hashcode,link,userid,email_name,0,))
        conn.commit()

    return hashcode

    




conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                        password='okano1988',database='maxfischer2database')
c = conn.cursor(buffered=True)








current_time=datetime.datetime.now(pytz.timezone('Europe/Berlin')).time()
now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
date_=str(now.year)+"."+str((now.month)-1)+"."+str(now.day)
time_=str(current_time)
time__=time_.replace(":","")
time___=time__.replace(".","")




s = str(now.day)+"/"+str(now.month)+"/"+str(now.year)
d = datetime.datetime.strptime(s, "%d/%m/%Y")
time__=time.mktime(d.timetuple())









c.execute ("""select * from userdaten""")
userdaten=c.fetchall()
for row in userdaten:
    
    if row[74]=="" and row[66]!="" and row[66]!="[]" and row[85]!="":
        
        existiert="nein"
        c.execute ("""select * from cart_reminder where userid=%s""",(row[11],))
        for row_2 in c:
            existiert="ja"
            zaehler=row_2[1]
            print row[85]
            if zaehler<2:

                if int(row_2[2])-time__>60*60*24*2:
                    c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s)""" % ("cart_reminder_send_email"),(row[11],date_,time___,"no",row[85],row[64],))
                    c.execute("""update cart_reminder set time=%s and zaehler=%s where userid=%s""",(time__,zaehler+1,row[11],))
                    conn.commit()

                    print row_2[2]
                    print time__                  
        

        if existiert=="nein":
            c.execute("""insert into %s values (%%s,%%s,%%s)""" % ("cart_reminder"),(row[11],1,time__,))
            c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s)""" % ("cart_reminder_send_email"),(row[11],date_,time___,"no",row[85],row[64],))
            conn.commit()
            



c.execute ("""select * from cart_reminder_send_email where sendemail=%s""",("no",))
cart_reminder_send_email=c.fetchall()
for row in cart_reminder_send_email:
    text=""
    print row[0]+","+row[1]+","+row[2]+","+row[3]+","+row[4]


    try:
        
        me = "Paula von Darling Lace <service@darlinglace.com>"
        you = row[4]
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Dein Warenkorb bei Darling Lace"
        msg['From'] = me
        msg['To'] = you
        userid=row[0]
        newsletter_code=row[5]


        




                
        darling_lace_logo=generate_link_email_marketing("https://www.darlinglace.com",userid,"cart_summary")
        header_mein_showroom=generate_link_email_marketing("https://www.darlinglace.com/Produktauswahl/Mein%20Showroom/",userid,"cart_summary")
        header_bh_sets=generate_link_email_marketing("https://www.darlinglace.com/Produktauswahl/BH%20Sets/",userid,"cart_summary")
        header_slip=generate_link_email_marketing("https://www.darlinglace.com/Produktauswahl/Slips/",userid,"cart_summary")
        instagram_link=generate_link_email_marketing("https://www.instagram.com/darling_lace/",userid,"cart_summary")
        facebook_link=generate_link_email_marketing("https://www.facebook.com/Darling-Lace-129368267722230/",userid,"cart_summary")
        kontaktiere_uns=generate_link_email_marketing("https://www.darlinglace.com/support/",userid,"cart_summary")
        VIP_club=generate_link_email_marketing("https://www.darlinglace.com/wie_funktioniert_VIP/",userid,"cart_summary")
        versand_retoure=generate_link_email_marketing("https://www.darlinglace.com/versand_rueckversand/",userid,"cart_summary")
        ueber_uns=generate_link_email_marketing("https://www.darlinglace.com/ueber_uns/",userid,"cart_summary")
        datenschutz=generate_link_email_marketing("https://www.darlinglace.com/datenschutz/",userid,"cart_summary")
        
        zum_warenkorb=generate_link_email_marketing("https://www.darlinglace.com/cart/",userid,"cart_summary")
        lara_plunge=generate_link_email_marketing("https://www.darlinglace.com/Produktauswahl/BH%20Sets/Lara%20Plunge/",userid,"cart_summary")
        eva_balconette=generate_link_email_marketing("https://www.darlinglace.com/Produktauswahl/BH%20Sets/Eva%20Balconette/",userid,"cart_summary")
        jil_unlined=generate_link_email_marketing("https://www.darlinglace.com/Produktauswahl/BH%20Sets/Jil%20Unlined/",userid,"cart_summary")
        mia_push_up=generate_link_email_marketing("https://www.darlinglace.com/Produktauswahl/BH%20Sets/Mia%20Push-Up/",userid,"cart_summary")


        email_abbestellen=generate_link_email_marketing("https://www.darlinglace.com/newsletter_abmelden_page/?security_key="+newsletter_code,userid,"cart_summary")
        
        bestellung_bestellen_email=get_template('cart_erinnerung_email.html')
        html=bestellung_bestellen_email.render({'email':you,'campaign':"cart_summary",'userid':userid,'email_abbestellen':email_abbestellen,'lara_plunge':lara_plunge,'eva_balconette':eva_balconette,'jil_unlined':jil_unlined,'mia_push_up':mia_push_up,'zum_warenkorb':zum_warenkorb,'email_adresse':you,'datenschutz':datenschutz,'ueber_uns':ueber_uns,'versand_retoure':versand_retoure,'VIP_club':VIP_club,'kontaktiere_uns':kontaktiere_uns,'facebook_link':facebook_link,'instagram_link':instagram_link,'header_slip':header_slip,'header_bh_sets':header_bh_sets,'header_mein_showroom':header_mein_showroom,'darling_lace_logo':darling_lace_logo})



        text = strip_tags(html) 

        html=html.encode('utf8')              



        mail = smtplib.SMTP_SSL('smtp.strato.de:465')
        mail.ehlo()
        mail.login('kundensupport@darlinglace.com', 'Lingerie2017')



    #https://www.darlinglace.com/einladung/
        # Record the MIME types of both parts - text/plain and text/html.
    #    part2 = MIMEText(html.encode('utf-8'), 'plain', 'utf-8')



        part2 = MIMEText(html, 'html','utf-8')


        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.


        msg.attach(part2)


        # Send the message via local SMTP server.



#        mail.sendmail(me, you, msg.as_string())
        c.execute("""update cart_reminder_send_email set sendemail=%s where userid=%s""",("yes",userid,))
        conn.commit()
    except:
        text=text

        


        

                    





