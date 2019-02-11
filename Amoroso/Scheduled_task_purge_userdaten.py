
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





conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                            password='okano1988',database='maxfischer2database')
c = conn.cursor(buffered=True)





zaehler=0
c.execute ("""select * from userdaten""")
userdaten=c.fetchall()
for row in userdaten:
    if zaehler<2000:
        if row[0]=="" and row[1]=="" and row[12]=="" and row[27]==-1 and (row[65]=="" or row[65]=="[]") and (row[66]=="" or row[66]=="[]")  and row[75]=="no" and row[85]=="":
            print row[11]
            c.execute("""delete from %s where gutscheincode=%%s""" % ("userdaten"),(row[11],))
            zaehler=zaehler+1

conn.commit()





