
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
c.execute ("""select * from lingerieselection """)
lingerieselection=c.fetchall()
print(lingerieselection)

now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
date_now=day=str(now.year)+str(now.month-1)+str(now.day)
date_now_format = datetime.datetime.strptime(date_now, '%Y-%m-%d')

c.execute ("""select * from anmeldebestaetigungen """)
anmeldebestaetigungen=c.fetchall()
for row in anmeldebestaetigungen:
    if row[3]=="" and row[5]=="":
        if row[8]<1:
            date_anmeldebestaetigungen_format = datetime.datetime.strptime(row[9], "%Y%m%d").date()
            delta = date_now_format - date_anmeldebestaetigungen_format
            if delta>=3:


                code=row[1]
                empfaenger=row[0]
                



                # me == my email address
                # you == recipient's email address
                me = "service@darlinglace.com"
                you = empfaenger

                # Create message container - the correct MIME type is multipart/alternative.
                msg = MIMEMultipart('alternative')
                msg['Subject'] = "Anmeldung bestätigen"
                msg['From'] = me
                msg['To'] = empfaenger

                # Create the body of the message (a plain-text and an HTML version).

                
                text = "WIllkommen zu Darling Lace"

                reload(sys)
                sys.setdefaultencoding("ISO-8859-1")
                
                html = """<html><head></head><body style="font-family:Helvetica;font-size:16px;">"""
                html=html+"""<div style='margin: 0 auto;max-width:500px;'><br>"""
                

                html=html+"""Hallo und willkommen bei Darling Lace<br><br>Vielen Dank für Deine Anmeldung. Wir freuen uns sehr, dass Du bei uns nach der neusten und für dich passenden Lingerie kaufen möchtest. <br><br>"""
                html=html+"""Bitte bestätige Deine E-Mail Adresse um Dein Darling Lace Konto zu altivieren und die neuste Lingerie oder auch Erinnerungen an Deinen Warenkorb per E-Mail zu erhalten<br><br>Bitte klicke auf folgenden <a href='https://www.darlinglace.com/anmeldung_bestaetigen/"""+code+"""' style='text-decoration:none !important;'>Link</a>, um Deine Anmeldung zu bestaetigen.</div>"""

                html=html+"""</div>"""    
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

                new_remindercount=row[8]+1

                c.execute("""update %s set remindercount=%%s,lastreminderdate=%%s where email=%%s and code=%%s""" % ("anmeldebestaetigungen"),(new_remindercount,date_now,row[0],row[1],))
                conn.commit() 
    
