
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

for row in lingerieselection:

    menge_bh=0
    menge_panty=0
    c.execute ("""select * from %s """ % ("stylecode"))
    for row_2 in c:
        if row[12]==row_2[2] and row[11]==row_2[1]:
            if row_2[0]=="BH":
                menge_bh=menge_bh+int(row_2[4])-int(row_2[5])
            else:
                menge_panty=menge_panty+int(row_2[4])-int(row_2[5])


    if menge_bh>0 and menge_panty>0:
        c.execute("""update lingerieselection set active=%s where name=%s""",("yes",row[0],))
    else:
        c.execute("""update lingerieselection set active=%s where name=%s""",("no",row[0],))


            
#    check_referral_emails_sent()



