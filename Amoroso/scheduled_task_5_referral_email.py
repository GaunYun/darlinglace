
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
        me = "service@darlinglace.com"
        you = empfaenger

        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = betreff
        msg['From'] = von
        msg['To'] = empfaenger

        # Create the body of the message (a plain-text and an HTML version).
        text="""Dein Freund """+von+""" nutzt Darling Lace und moechte dich dorthin einladen. Darling Lace bietet dir die neusten Dessous Trends in hoher Qualiät zu attraktiven Preisen. Dazu bieten wir Dir einen persoenlichen Showroom, der dir auf Basis eines Fitting Quiz dir die passenden BHs für dich zeigt! Klicke hier für deinen persoenlichen Gutschein von 15 EUR: https://www.darlinglace.com/einladung/"""+code


        html = """<html><head></head><body style="font-family:Helvetica;font-size:16px;">"""
        html=html+"""<div style='background-color:#404040;width:100%;height:50px'>"""
        html=html+"""<div style='width:20%;margin: 0 auto;float:center;text-align: center;line-height:50px;'>"""

        html=html+"""<a href='https://www.darlinglace.com/' style='text-decoration:none !important; text-decoration:none;color:#ffffff;'><div style='height:50px;cursor:pointer;background: url("https://www.darlinglace.com/static/darling_lace.png");background-size: 150px 30px;background-position: center center; background-repeat:   no-repeat;'  ></div></a></div>"""
        html=html+"""</div><br>"""
        html=html+"""Dein Freund """+von+""" nutzt Darling Lace und moechte dich dorthin einladen.<br><br>Darling Lace bietet dir die neusten Dessous Trends in hoher Qualiät zu attraktiven Preisen. Dazu bieten wir Dir einen persoenlichen Showroom, der dir auf Basis eines Fitting Quiz dir die passenden BHs für dich zeigt!<br><br>Klicke hier für deinen persoenlichen Gutschein von 15 EUR: <br><br><div style='margin: 0 auto;background-color:#DB7093;color:#FFFFFF;font-weight:bold;border-radius: 5px;text-align:center;cursor:pointer;width:250px;height:30px;line-height:30px;' ><a href='https://www.darlinglace.com/einladung/"""+code+"""' style='text-decoration:none !important; text-decoration:none;color:#ffffff;'>Deinen Gutschein abrufen</a></div>"""
        html=html+"""<br><br><br>Persoenliche Nachricht von """+von+""":<br><br>"""+message

        html=html+"""<div style='width:100%;border-top:1px solid #e6e6e6 ;float:left;margin-top:20px;font-size:10px;margin:0 auto;'><div class="bestellnummer_email" style='font-size:10px;'><br></div>"""
        html=html+"""<div style='width:100%;text-align:center;line-height:15px;'>"""
        html=html+"""Darling Lace GmbH | Chausseestraße 60 | 10115 Berlin | Geschäftsführung: Maximilian Fischer, Kai Winselmann<br>"""
        html=html+"""Handelsregister: Berlin Charlottenburg HRB XXX<br>"""
        html=html+"""<a href='https://www.darlinglace.com/datenschutz/'>Datenschutz</a><br>"""
            
        html=html+"</div></div>" 
            
        html=html+"""<script>function logo_click(){ alert("ASD");window.location.href='https://www.darlinglace.com/einladung/';}"""
        html=html+"""function open_link(){ window.location.href='https://www.darlinglace.com/einladung/';}"""
        html=html+"""</script></body></html>"""

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





        c.execute("""update gutscheincodes_sent set emailsent=%s,emailsentdate=%s,emailsenttime=%s where email=%s""",("yes",get_date_stamp_now(),get_time_stamp_now(),row[3]))
conn.commit()
