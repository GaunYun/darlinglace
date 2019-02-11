
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
from zenpy import Zenpy
from zenpy.lib.api_objects import Ticket, User


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
creds = {
    'email' : 'service@darlinglace.com',
    'token' : 'oY8q9R9T4io7ZwQ1KdDktKwXgF3sWhMneMECjpL0',
    'subdomain': 'darlinglace'
}
zenpy_client = Zenpy(**creds)


date_=str(now.year)+"."+str((now.month)-1)+"."+str(now.day)

if now.day>10:    
    c.execute ("""select * from userdaten """)
    userdaten=c.fetchall()
    feedback=""
    for row in userdaten:
        if row[22]=="VIP" and row[23]=="true":
            
            c.execute ("""select * from VIP_model_store_credit where gutscheincode=%s """,(row[11],))
            VIP_model_store_credit=c.fetchall()
            abgebucht="false"

            neukunde="false"
            print("neukunde")
            date_VIP=row[24].split(".")
            print(date_VIP[1]+"=="+str(now.month-1) +"and"+ date_VIP[0]+"=="+str(now.year))
            if date_VIP[1]==str(now.month-1) and date_VIP[0]==str(now.year):
                neukunde="true"
            if neukunde=="false":
                for row_2 in VIP_model_store_credit:
                    print(row_2[0])
                    date_VIP_2=row_2[0].split(".")
                    print(date_VIP_2[1]+"=="+str(now.month-1) +"and"+ date_VIP_2[0]+"=="+str(now.year) +"and"+str(row_2[3])+"!=0 and"+ str(row_2[4])+"!=")
                    if (date_VIP_2[1]==str(now.month-1) and date_VIP_2[0]==str(now.year) and row_2[3]!=0 and row_2[4]!="") or (date_VIP_2[1]==str(now.month-1) and date_VIP_2[0]==str(now.year) and row_2[4]=="VIP Model Abbuchung pending"):
                        abgebucht="true"

                
                c.execute ("""select * from VIP_model_store_credit where gutscheincode=%s """,(row[11],))
                VIP_model_store_credit=c.fetchall()
                already_skipped="false"
                for row_2 in VIP_model_store_credit:
                    if now.day>=1 and now.day<=10:
                        if date_VIP_2[1]==str(now.month-1) and date_VIP_2[0]==str(now.year) and (row_2[6]=="true" or row_2[4]!=""):
                            already_skipped="true"


                
                if abgebucht=="false" and already_skipped=="false":
                    if row[56]!="klarna" and row[56]!="paypal" and row[56]!="sofort":
                        print("transaction_id")
                        
                        paymill_context = paymill.PaymillContext('82239adeff57ef5d51ec2e5d11fd915d')
                        transaction_service = paymill_context.get_transaction_service()
                        transaction_with_client_and_payment = transaction_service.create_with_payment_id(payment_id=row[56], amount=2995, currency="EUR", description="Darling Lace VIP Store Credit: "+ str(now.month)+"/"+str(now.year),client_id=row[50])

                        class Object(object):
                            pass

                        transaction_key = Object()
                        transaction_key.id =  transaction_with_client_and_payment["id"]
                        
                        print(transaction_key.id)
                        transaction_id= transaction_key

                        

                        bezahlt=""
                        while bezahlt=="":

                         
                            transactions_list=transaction_service.detail(transaction_id)
                            print(transactions_list["description"])

                            if transactions_list["status"]=="closed":

                                feedback_from_transaction= "true"
                            else:
                                if transactions_list["status"]=="failed":
                                    feedback_from_transaction= "false"
                                else:
                                    feedback_from_transaction= ""
                                

                            if feedback_from_transaction=="true":
                                bezahlt="true"
                                c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % ("VIP_model_store_credit"),(date_,date_,time__,29.95,"VIP Model Abbuchung","no","",0,0,transaction_id.id,date_.replace(".", ""),row[11],))
                    else:
                        c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % ("VIP_model_store_credit"),(date_,date_,time__,0,"VIP Model Abbuchung pending","no","",0,0,row[56],date_.replace(".", ""),row[11],))
                        c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s)""" % ("offenen_eigene_rechnungen_VIP"),(date_,date_,row[11],"yes",29.95))

                        von="Internes To Do: VIP Model Abbuchung pending"
                        email="service@darlinglace.com"
                        betreff="Abbuchung VIP Model "+str(now.month)+"/"+str(now.year)+" pending: Kundennummer #"+row[11]

                        message = """Abbuchnung von 29,95 EUR fuer VIP Model """+str(now.month)+"/"+str(now.year)+""" noch durchzufuehren. Email-Adresse des Kunden ist """+row[0]+""". Zahlungsmittel ist """+row[56]

                        creds = {
                            'email' : 'service@darlinglace.com',
                            'token' : 'oY8q9R9T4io7ZwQ1KdDktKwXgF3sWhMneMECjpL0',
                            'subdomain': 'darlinglace'
                        }
                        zenpy_client = Zenpy(**creds)
                        zenpy_client.tickets.create(
                            Ticket(description=message,subject=betreff,
                                   requester=User(name=von, email=email))
                        )                                                            
conn.commit()

