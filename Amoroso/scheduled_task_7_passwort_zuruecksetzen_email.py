
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
        me = "service@darlinglace.com"
        you = empfaenger

        print("los")
        print(empfaenger)

        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Passwort vergessen"
        msg['From'] = me
        msg['To'] = empfaenger

        # Create the body of the message (a plain-text and an HTML version).

        
        text="""Dein Passwort kann zurückgesetzt werden. Bitte klicke auf folgenden Link klicken: https://www.darlinglace.com/passwort_vergessen_bestaetigen/"""+code+""", um dein Passwort zu ändern."""



        
        html = """<html><head></head><body style="font-family:Helvetica;font-size:16px;">"""
        html=html+"""<div style='margin: 0 auto;max-width:500px;'><br>"""
        

        html=html+"""Dein Passwort kann zurückgesetzt werden. Bitte klicke auf folgenden <a href='https://www.darlinglace.com/passwort_vergessen_bestaetigen/"""+code+"""' style='text-decoration:none !important;'>Link</a>, um dein Passwort zu ändern.</div>"""
        html=html+"""</div>"""


        html=html+"""<div style='width:100%;border-top:1px solid #e6e6e6 ;float:left;margin-top:20px;font-size:10px;margin:0 auto;'><div class="bestellnummer_email" style='font-size:10px;'><br></div>"""
        html=html+"""<div style='width:100%;text-align:center;line-height:15px;'>"""
        html=html+"""Darling Lace GmbH | Chausseestraße 60 | 10115 Berlin | Geschäftsführung: Maximilian Fischer, Kai Winselmann<br>"""
        html=html+"""Handelsregister: Berlin Charlottenburg HRB XXX<br>"""
        html=html+"""<a href='https://www.darlinglace.com/datenschutz/'>Datenschutz</a><br>"""
            
        html=html+"</div></div>" 
        
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






        c.execute("""update email_passwort_zuruecksetzen set emailsentout=%s where security_code=%s""",("ja",code,))
conn.commit()
