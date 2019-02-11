
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

now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
current_time=datetime.datetime.now(pytz.timezone('Europe/Berlin')).time()

time_=str(current_time)

time__=time_.replace(":","")
time__=time__.replace(".","")



date_=str(now.year)+str((now.month)-1)+str(now.day)

print(now.day)
if now.day>10:    
    c.execute ("""select * from userdaten """)
    userdaten=c.fetchall()
    feedback=""
    for row in userdaten:
        if row[22]=="VIP" and row[23]=="true":
            c.execute ("""select * from %s""" % ("VIP_model_store_credit"+row[11]))
            VIP_model_store_credit=c.fetchall()
            abgebucht="false"


 
            for row_2 in VIP_model_store_credit:
                if row[0][4:6]==str(now.month-1) and row[0][0:4]==str(now.year) and row_2[3]!=0 and row_2[4]!="":
                    abgebucht="true"


            c.execute ("""select * from %s""" % ("VIP_model_store_credit"+row[11]))
            VIP_model_store_credit=c.fetchall()
            already_skipped="false"
            print("check_month_VIP")
            for row_2 in VIP_model_store_credit:
                if now.day>=1 and now.day<=10:
                    if row_2[0][4:6]==str(now.month-1) and row_2[0][0:4]==str(now.year) and (row_2[6]=="true" or row_2[4]!=""):
                        print("true")
                        already_skipped="true"

            if abgebucht=="false" and already_skipped=="false":
                print("transaction_id")
                
                paymill_context = paymill.PaymillContext('5ccd454aa30b1614e44193f740762a52')
                transaction_service = paymill_context.get_transaction_service()
                transaction_with_client_and_payment = transaction_service.create_with_payment_id(payment_id=row[56], amount=2995, currency="EUR", description="Darling Lace VIP Store Credit: "+ str(now.month)+"/"+str(now.year),client_id=row[50])
                print(transaction_with_client_and_payment["id"])
                
                print("transaction_janu")
                
                class Object(object):
                    pass

                transaction_key = Object()
                transaction_key.id =  transaction_with_client_and_payment["id"]
                
                print(transaction_key.id)
                transaction_id= transaction_key

                

                bezahlt=""
                while bezahlt=="":




                 #   transactions_list = transaction_service.list()
                 
                    transactions_list=transaction_service.detail(transaction_id)
                    print(transactions_list["description"])

                    if transactions_list["status"]=="closed":

                        feedback_from_transaction= "true"
                    else:
                        if transactions_list["status"]=="failed":
                            feedback_from_transaction= "false"
                        else:
                            feedback_from_transaction= ""
                        

                    print("bezahlt2")
                    print(feedback_from_transaction)
                    if feedback_from_transaction=="true":
                        bezahlt="true"
                        c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % ("VIP_model_store_credit"+row[11]),(date_,date_,time__,29.95,"","no","",0,0,transaction_id.id,date_.replace(".", "")))
                        conn.commit()

