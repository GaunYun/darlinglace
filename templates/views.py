
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

import json
from django.views.decorators.csrf import csrf_exempt
import socket
import mysql.connector
import datetime
from datetime import timedelta
from django.conf import settings
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
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

reload(sys)  
sys.setdefaultencoding('utf8')

from django.core.urlresolvers import reverse
from django.shortcuts import render


def paypal_verficiation(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
    c = conn.cursor(buffered=True)
	
    paymill_context = paymill.PaymillContext('5ccd454aa30b1614e44193f740762a52')
    transaction_service = paymill_context.get_transaction_service()

    transactions_list = transaction_service.list()
    id = request.GET.get('paymill_trx_id')
    i=0
    status=""
    while i<=len(transactions_list.data)-1:
        if transactions_list.data[i]["id"]==id:
            index=i
            if transactions_list.data[i]["status"]=="closed":

                status= "true"
            else:
                if transactions_list.data[i]["status"]=="failed":
                    status= "false"
        i=i+1
    bestellnummer=transactions_list.data[index]["description"][-8:]
    if status=="false":
        return HttpResponseRedirect("/hello/start_page/")
	
    if status=="true":
        check_pending_payments(bestellnummer,"true",c,conn)
        return HttpResponseRedirect("/hello/account_page/"+bestellnummer)
    if status=="":
        check_pending_payments(bestellnummer,"true",c,conn)
        c.execute("""update pending_payments set accepted=%s where bestellnummer=%s""",("false",bestellnummer,))
        conn.commit()	
        return HttpResponseRedirect("/hello/account_page/bestellungen_ansehen/"+bestellnummer)


def request_paymill_paypal_code(amount_,currency_,return_url_,cancel_url_,description_):
    paymill_context = paymill.PaymillContext('5ccd454aa30b1614e44193f740762a52')
    checksum_service=paymill_context.get_checksum_service()
    checksum=checksum_service.create(checksum_type='paypal', amount=amount_, currency=currency_, return_url=return_url_,
                                           cancel_url=cancel_url_,description=description_)

    return checksum.id

										   

@csrf_exempt
def credit_card(request):
 #   r = request.post('http://192.168.2.100:8000/hello/credit_card/', json={"key": "value"})
#    print(request)
 #   if paymill.validateCardNumber('4111111111111111')==true:
#        print("true")
#    else:
#        print("false")
        
#    paymill_context = paymill.PaymillContext('5ccd454aa30b1614e44193f740762a52')

#    transaction_service = paymill_context.get_transaction_service()
#    transaction_with_token = transaction_service.create_with_token(
#        token='5ccd454aa30b1614e44193f740762a52',
#        amount=4200,
#        currency='EUR',
#        description='Test Transaction'
#    )
    
    t=get_template('test.html')
    html=t.render({})

    return HttpResponse(html)




def check_transaction(payment_id_,amount,currency_,description_,client_id_):

    paymill_context = paymill.PaymillContext('5ccd454aa30b1614e44193f740762a52')
    transaction_service = paymill_context.get_transaction_service()

    transactions_list = transaction_service.list()
    i=0
    print("next")
    while i<=len(transactions_list.data)-1:
        try:
            print(transactions_list.data[i]["description"])
            print(transactions_list.data[i]["currency"]+"=="+currency_)
            print(str(transactions_list.data[i]["amount"])+"=="+str(amount))
            print(transactions_list.data[i]["client"]["id"]+"=="+client_id_)
            print(transactions_list.data[i])
            print(transactions_list.data[i]["payment"])
            print(transactions_list.data[i]["payment"]["id"])
            print(payment_id_)
            if transactions_list.data[i]["description"]==description_ and transactions_list.data[i]["currency"]==currency_ and int(transactions_list.data[i]["amount"])==int(amount) and transactions_list.data[i]["client"]["id"]==client_id_ and transactions_list.data[i]["payment"]["id"]==payment_id_:  

                if transactions_list.data[i]["status"]=="closed":

                    return "true"
                else:
                    if transactions_list.data[i]["status"]=="failed":
                        return "false"
                    else:
                        return ""

            i=i+1
        except:
            i=i+1


    #####check whether transaction was successful
    
    


@csrf_exempt
def credit_card_test(request):
    q=request.POST.get('token', None)


    paymill_context = paymill.PaymillContext('5ccd454aa30b1614e44193f740762a52')

    client_service = paymill_context.get_client_service()
    credit_card_add_new_payment(q,"client_5170293392dfda5607c1")

  #  clients = client_service.list()

   
#   print(clients)

 #   data = clients.data[0]

  #  print(len(clients.data))
   # i=0
   # while i<=len(clients.data)-1:
#        print(clients.data[i]["payment"])
#        print(i)
    #    i=i+1



    #credit_card_create_new_client("max.fischer2@gmail.com")

    
    


    




#    payment_service = paymill_context.get_payment_service()

#    payment_with_token_and_client = payment_service.create(
#    token=q,
#    client_id='client_052f15b3c704a5fc5566'
#    )

#    transaction_service = paymill_context.get_transaction_service()
 #   transaction_with_token = transaction_service.create_with_token(token=q, amount=0001, currency='EUR', description='Test Python')



#    preauthorization_service = paymill_context.get_preauthorization_service()
#    preauthorization_with_token = preauthorization_service.create_with_token(
#        token=q,
#        amount=4200,
#        currency='EUR',
#        description='description example'
#    )



    print(q)



    t=get_template('testa.html')
    html=t.render({'favicon':get_favicon(),'brand_name':'Sensuals'})

    return HttpResponse(html)


	
	
def create_new_client_test(request):
 
    credit_card_create_new_client("max.fischer2@gmail.com")
	
    t=get_template('testa.html')
    html=t.render({'favicon':get_favicon(),'brand_name':'Sensuals'})

    return HttpResponse(html)


def test_update_client_with_email(p):
        c = p.client_service.create(email="test@mail.com")
        c.email = "test2@mail.com"
        assertEqual("test2@mail.com", p.client_service.update(c).email)	
	

def credit_card_create_new_client(client_email):
    paymill_context = paymill.PaymillContext('5ccd454aa30b1614e44193f740762a52')
    client_service = paymill_context.get_client_service()
    client = client_service.create(email=client_email)
    client_details = client_service.detail(client)
	
    return client_details["id"]

	
	
def test_creditcard(request):
    paymill_context = paymill.PaymillContext('5ccd454aa30b1614e44193f740762a52')
    payment_service = paymill_context.get_payment_service()	
    payments_list = payment_service.list()
    i=0
    while i<=len(payments_list.data)-1:
        print(payments_list.data[i])
        print(payments_list.data[i]["client"])
        print(payments_list.data[i]["client"]["id"])
        print(i)
        i=i+1

		
def get_creditcard_payment_data(client_id):
    paymill_context = paymill.PaymillContext('5ccd454aa30b1614e44193f740762a52')
    payment_service = paymill_context.get_payment_service()	
    payments_list = payment_service.list()
    i=0
    while i<=len(payments_list.data)-1:
        print(payments_list.data[i])
        print(payments_list.data[i]["client"])

		    
        print(i)
        i=i+1

		
		
def credit_card_delete_payment_test(token_id):
    print("geht los12")	
    paymill_context = paymill.PaymillContext('5ccd454aa30b1614e44193f740762a52')
    print("geht los13")	
    payment_service = paymill_context.get_payment_service()
    print("geht los1")
    print(token_id)	
	
    class Object(object):
        pass

    a = Object()
    a.id = token_id
    payment_service.remove(a)

	
def credit_card_add_new_payment_test(token_id,client_id_):
    print("geht los12")	
    paymill_context = paymill.PaymillContext('5ccd454aa30b1614e44193f740762a52')
    print("geht los13")	
    payment_service = paymill_context.get_payment_service()
    print("geht los1")
    print(client_id_)
    print(token_id)	
    hallo=payment_with_token_and_client = payment_service.create(
        token=token_id,
        client_id=client_id_

    )
	
    print("haaaallo")
    print(hallo)


	
	



    return "true"

def payment_credit_card_test(request):
    paymill_context = paymill.PaymillContext('5ccd454aa30b1614e44193f740762a52')
    transaction_service = paymill_context.get_transaction_service()
    transactions_list = transaction_service.list()
    credit_card_add_new_transaction("pay_274f6a119abb2fbdda38728b","3912312304","EUR","bla","client_956f9a14cd753011d858")
 #   print(check_transaction("pay_274f6a119abb2fbdda38728b","3912312304","EUR","","client_956f9a14cd753011d858"))


	
	

def credit_card_add_new_transaction(payment_id_,amount,currency_,description_,client_id_):
    paymill_context = paymill.PaymillContext('5ccd454aa30b1614e44193f740762a52')
    transaction_service = paymill_context.get_transaction_service()
    transaction_with_client_and_payment = transaction_service.create_with_payment_id(payment_id=payment_id_, amount=amount, currency=currency_, description=description_,client_id=client_id_)


    return "true"

def admin_uebersicht(request):
    links = []

  
    class Links(object):
        def __init__(self,linkname,link):
            self.linkname=linkname
            self.link=link

    links.append(Links("Export Excels: Userdaten","admin_export_userdaten"))

    links.append(Links("Export Bestellungen","admin_export_bestellungen"))

    links.append(Links("Export Big Data","admin_export_big_data"))

    links.append(Links("Export VIP member","admin_export_vip_member"))

    links.append(Links("Export Stammdaten","admin_export_stammdaten"))

    links.append(Links("Export Supply vs. Demand","admin_export_supply_demand"))

    links.append(Links("Export Ruecksendungen","admin_export_ruecksendungen"))

    links.append(Links("Export Bestelldetails","admin_export_bestelldetails"))


    

    links.append(Links("Import Bestellungen","admin_import_bestellungen"))


    json_string = json.dumps([Links.__dict__ for Links in links])

    t=get_template('admin_uebersicht.html')
    html=t.render({'favicon':get_favicon(),'brand_name':'Sensuals','links':json_string})

    return HttpResponse(html)

def admin_import_bestellungen(request):
    if request.is_ajax() and request.GET:
        wb = load_workbook(filename = 'userdaten.xlsx')

        ws=wb["Sheet1"]
        i=2
        while i!=-1:

            if ws['A'+str(i)]!="":
                identifier = ws['A'+str(i)]
            else:
                i=-1
            

        
        return HttpResponse(json.dumps(""), content_type='application/json')
        
    else:
        raise Http404


    
def admin_export_bestellungen(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)
        conn_2 = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        q= conn_2.cursor()

        workbook = xlsxwriter.Workbook('orders.xlsx')
        worksheet = workbook.add_worksheet()

        q.execute ("""select * from userdaten """)
        for row_3 in q:
            c.execute ("""select * from %s """ % ("bestellt_"+row_3[11]))

            
            num_fields = len(c.description)
            field_names = [i[0] for i in c.description]

            
            row=0
            column=0
            i=0
            while i <= len(field_names)-1:
                worksheet.write(row, column,     field_names[i])
                i=i+1
                column=column+1
                
                
                
            
            row=1
            for row_2 in c:

                i=0
                column=0
                row=row+1
                while i<=len(field_names)-1:


                    if row_2[i]!="":

                        worksheet.write(row, column,     str(row_2[i]))

                            
                    else:
                        worksheet.write(row, column,    "")

                    i=i+1
                    column=column+1

                        
                    
                



        workbook.close()


        return HttpResponse(json.dumps(""), content_type='application/json')
        
    else:
        raise Http404

    
def admin_export_userdaten(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)
        conn_2 = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        q= conn_2.cursor()

        
        workbook = xlsxwriter.Workbook('userdaten.xlsx')
        worksheet = workbook.add_worksheet()

        c.execute ("""select * from userdaten """)
        num_fields = len(c.description)
        field_names = [i[0] for i in c.description]

        row=0
        column=0
        i=0
        while i <= len(field_names)-1:

            worksheet.write(row, column,     field_names[i])
            i=i+1
            column=column+1
            
            
            
        
        row=1
        for row_2 in c:
            i=0
            column=0
            row=row+1
            while i!=-1:

                try:
                    worksheet.write(row, column,     str(row_2[i]))
                    i=i+1
                    column=column+1
                except:
                    i=-1
                   


        workbook.close()


        return HttpResponse(json.dumps(""), content_type='application/json')
        
    else:
        raise Http404


    
def admin_export_big_data(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)
        conn_2 = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        q= conn_2.cursor()

        

        workbook = xlsxwriter.Workbook('big_data_1.xlsx')
        worksheet = workbook.add_worksheet()

        c.execute ("""select * from Big_data_click_on_image """)
        num_fields = len(c.description)
        field_names = [i[0] for i in c.description]

        
        row=0
        column=0
        i=0
        while i <= len(field_names)-1:
            worksheet.write(row, column,     field_names[i])
            i=i+1
            column=column+1
            
            
            
        
        row=1
        for row_2 in c:
            i=0
            column=0
            row=row+1
            while i!=-1:
                try:
                    worksheet.write(row, column,     str(row_2[i]))
                    i=i+1
                    column=column+1
                except:
                    i=-1
                    
                


        workbook = xlsxwriter.Workbook('big_data_2.xlsx')
        worksheet = workbook.add_worksheet()

        c.execute ("""select * from Big_data_click_on_main_page """)
        num_fields = len(c.description)
        field_names = [i[0] for i in c.description]

        
        row=0
        column=0
        i=0
        while i <= len(field_names)-1:
            worksheet.write(row, column,     field_names[i])
            i=i+1
            column=column+1
            
            
            
        
        row=1
        for row_2 in c:
            i=0
            column=0
            row=row+1
            while i!=-1:
                try:
                    worksheet.write(row, column,     str(row_2[i]))
                    i=i+1
                    column=column+1
                except:
                    i=-1
                    


        workbook.close()




        return HttpResponse(json.dumps(""), content_type='application/json')
        
    else:
        raise Http404



def admin_export_vip_member(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)
        conn_2 = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        q= conn_2.cursor()

        
        workbook = xlsxwriter.Workbook('VIP_members.xlsx')
        worksheet = workbook.add_worksheet()

        c.execute ("""select * from VIPmembers """)
        num_fields = len(c.description)
        field_names = [i[0] for i in c.description]

        
        row=0
        column=0
        i=0
        while i <= len(field_names)-1:
            worksheet.write(row, column,     field_names[i])
            i=i+1
            column=column+1
            
            
            
        
        row=1
        for row_2 in c:
            i=0
            column=0
            row=row+1
            while i!=-1:
                try:
                    worksheet.write(row, column,     str(row_2[i]))
                    i=i+1
                    column=column+1
                except:
                    i=-1
                    


        workbook.close()



        return HttpResponse(json.dumps(""), content_type='application/json')
        
    else:
        raise Http404


def admin_export_bestelldetails(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)
        conn_2 = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        q= conn_2.cursor()

        
        workbook = xlsxwriter.Workbook('bestelldetails.xlsx')
        worksheet = workbook.add_worksheet()
        row=0

        c.execute ("""select * from userdaten """)
        for row in c:
            q.execute ("""select * from %s """ % ("bestellt_"+row[11]))
            for row_2 in q:
                w.execute ("""select * from %s """ % (row_2[0]))
        
                

                num_fields = len(w.description)
                field_names = [i[0] for i in w.description]

            
            

            
                if row==0:
                    column=1
                    i=0
                    worksheet.write(row, 0,     "bestellnummer")
                    while i <= len(field_names)-1:
                        worksheet.write(row, column,     field_names[i])
                        i=i+1
                        column=column+1
                    row=row+1
                    
                    
                    
                
                
                for row_3 in w:
                    i=0
                    
                    column=1
                    row=row+1
                    worksheet.write(row, 0,     row_2[20])
                    while i!=-1:
                        try:
                            worksheet.write(row, column,     str(row_3[i]))
                            i=i+1
                            column=column+1
                        except:
                            i=-1
                    


        workbook.close()



        return HttpResponse(json.dumps(""), content_type='application/json')
        
    else:
        raise Http404


    




def admin_export_ruecksendungen(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)
        conn_2 = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        q= conn_2.cursor()

        
        workbook = xlsxwriter.Workbook('ruecksendungen.xlsx')
        worksheet = workbook.add_worksheet()

        c.execute ("""select * from ruecksendungen """)
        num_fields = len(c.description)
        field_names = [i[0] for i in c.description]

        
        row=0
        column=0
        i=0
        while i <= len(field_names)-1:
            worksheet.write(row, column,     field_names[i])
            i=i+1
            column=column+1
            
            
            
        
        row=1
        for row_2 in c:
            i=0
            column=0
            row=row+1
            while i!=-1:
                try:
                    worksheet.write(row, column,     str(row_2[i]))
                    i=i+1
                    column=column+1
                except:
                    i=-1
                    


        workbook.close()



        return HttpResponse(json.dumps(""), content_type='application/json')
        
    else:
        raise Http404


    





def admin_export_stammdaten(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)
        conn_2 = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        q= conn_2.cursor()

        
        workbook = xlsxwriter.Workbook('stammdaten.xlsx')
        worksheet = workbook.add_worksheet()

        c.execute ("""select * from lingerieselection """)
        num_fields = len(c.description)
        field_names = [i[0] for i in c.description]

        
        row=0
        column=0
        i=0
        while i <= len(field_names)-1:
            worksheet.write(row, column,     field_names[i])
            i=i+1
            column=column+1
            
            
            
        
        row=1
        for row_2 in c:
            i=0
            column=0
            row=row+1
            while i!=-1:
                try:
                    worksheet.write(row, column,     str(row_2[i]))
                    i=i+1
                    column=column+1
                except:
                    i=-1
                    


        workbook.close()



        return HttpResponse(json.dumps(""), content_type='application/json')
        
    else:
        raise Http404   





def admin_export_supply_demand(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)
        conn_2 = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        q= conn_2.cursor()

        
        workbook = xlsxwriter.Workbook('supply_demand.xlsx')
        worksheet = workbook.add_worksheet()

        c.execute ("""select * from lingerieselection """)
        row=0
        for row_3 in c:
        
            q.execute ("""select * from %s where color='%s'""" % ("stylecode_"+row_3[11], row_3[12],))
            num_fields = len(c.description)
            field_names = [i[0] for i in q.description]

            
            
            column=0
            i=0
            if row==0:
                while i <= len(field_names)-1:
                    worksheet.write(row, column,     field_names[i])
                    i=i+1
                    column=column+1
                row=row+1
                
                
                
            
            
            for row_2 in q:
                i=0
                column=0
                row=row+1
                while i!=-1:
                    try:
                        worksheet.write(row, column,     str(row_2[i]))
                        i=i+1
                        column=column+1
                    except:
                        i=-1
                    


        workbook.close()



        return HttpResponse(json.dumps(""), content_type='application/json')
        
    else:
        raise Http404


    
    

def get_lingerie_from_search(search_item,user,modelAB,sub_picture,c):
    lingerie = []


    class Lingerie(object):
        def __init__(self,name,sizerange,pic,priceregular,pricesubscription,description,details,active,productgroup,wishlist,descriptionshort,stylecode,colorcode):
            self.name=name
            self.sizerange=sizerange
            self.pic=pic
            self.priceregular=priceregular
            self.pricesubscription=pricesubscription
            self.description=description
            self.details=details
            self.active=active
            self.productgroup=productgroup
            self.wishlist=wishlist
            self.descriptionshort=descriptionshort
            self.stylecode=stylecode
            self.colorcode=colorcode

#    c.execute ("""ALTER TABLE lingerieselection ADD FULLTEXT(name,sizerange,description,descriptionshort,productgroup,dominantfactorcolors,dominantfactorstyle,details)""")       


    if search_item!="":
        search_item=search_item+"*"



        c.execute ("""SELECT * FROM lingerieselection WHERE MATCH(name,sizerange,description,descriptionshort,productgroup,dominantfactorcolors,dominantfactorstyle,details) AGAINST (%s IN BOOLEAN MODE)""",(search_item,))
        lingerieselection=c.fetchall()


        for row in lingerieselection:

            if row[14]=="true":
                priceregular=row[3]-row[13]
                pricesubscription=row[4]-row[13]
            else:
                priceregular=row[3]
                pricesubscription=row[4]
            c.execute ("""select * from %s """ % ("picturelibrary_"+row[11]+"_"+row[12]))
            picturelibrary_daten=c.fetchall()

            pic_1=""
            pic_2=""
            pic_3=""
            zaehler=0
            for row_3 in picturelibrary_daten:
                if (row_3[0]==modelAB and row_3[1]==sub_picture) or (row_3[0]==-1 and row_3[1]==sub_picture):
                    pic_1=pic_1+row_3[2]+","
                
                if (row_3[0]==modelAB and row_3[1]!=sub_picture and sub_picture!=-1 and row_3[1]!=-1) or (row_3[0]==-1 and row_3[1]!=sub_picture and sub_picture!=-1 and row_3[1]!=-1):
                    if pic_2!="":
                        pic_2=pic_2+","
                    pic_2=pic_2+row_3[2]
                    zaehler=zaehler+1

                if row_3[1]==-1:
                    if pic_3!="":
                        pic_3=pic_3+","
                    pic_3=pic_3+row_3[2]
            if zaehler==1:
                pic=pic_1+pic_2+","+pic_3
            else:
                pic=pic_1+pic_2+","+pic_3
            lingerie.append(Lingerie(row[0],row[1],pic,priceregular,pricesubscription,row[5],row[6],row[7],row[8],get_wishlist(row[11],row[12],user,row[8]),row[9],row[11],row[12],))


        json_string = json.dumps([Lingerie.__dict__ for Lingerie in lingerie])
    else:
        
        json_string=""

    return json_string
        

@csrf_exempt
def full_text_search(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)
        search_item=request.GET.get('search_item')


        x=str(request.session.session_key)
                


        c.execute ("""select * from userdaten """)
        for row in c:
            if row[9]==x and x!="None":
                user=row[11]
                modelAB=row[47]
                sub_picture=row[48]
                    
        
        lingerie=get_lingerie_from_search(search_item,user,modelAB,sub_picture,c)


        return HttpResponse(lingerie, content_type='application/json')
    else:
        raise Http404





def define_wishlist(x,modelAB,sub_picture,c):
    wishlist = []
 
 
           
    class Wishlist(object):
        def __init__(self,name,picture,stylecode,colorcode,productgroup):
            self.name=name
            self.picture=picture
            self.stylecode=stylecode
            self.colorcode=colorcode
            self.productgroup=productgroup
 

  


    c.execute ("""select * from userdaten """)

    userdaten=c.fetchall()




    for row in userdaten:
        if row[9]==x and x!="None":
            c.execute ("""select * from %s """ % ("wishlist_"+row[11]))
            wishlist_data=c.fetchall()
            
            for row_2 in wishlist_data:


                c.execute ("""select * from lingerieselection """)
                lingerieselection_data=c.fetchall()


                for row_4 in lingerieselection_data:

                    if row_4[11]==row_2[0] and row_4[12]==row_2[1] and row_2[3]==row_4[8] and row_2[3]==row_4[8]:

                        print("wishlist")
                        print(row_2[3]+"=="+row_4[8])
                        print(row_4[0])
                        c.execute ("""select * from %s """ % ("picturelibrary_"+row_4[11]+"_"+row_4[12]))
                        picturelibrary_data=c.fetchall()

                        group1=row_2[3]
                        pic_1=""
                        pic_2=""
                        pic_3=""
                        zaehler=0
                        for row_3 in picturelibrary_data:
                            if group1!="panties":
                                if ((row_3[0]==modelAB and row_3[1]==sub_picture) or (row_3[0]==-1 and row_3[1]==sub_picture)):

                                    pic_1=pic_1+row_3[2]+","
                            else:

                                if group1==row_3[3] and (row_4[2]==row_3[4]):

                                    pic_1=pic_1+row_3[2]+","                            
                            if ((row_3[0]==modelAB and row_3[1]!=sub_picture and sub_picture!=-1 and row_3[1]!=-1) or (row_3[0]==-1 and row_3[1]!=sub_picture and sub_picture!=-1 and row_3[1]!=-1)) or (group1=="panties" and group1==row_3[3]):
                                if pic_2!="":
                                    pic_2=pic_2+","
                                pic_2=pic_2+row_3[2]
                                zaehler=zaehler+1

                            if row_3[1]==-1:
                                if pic_3!="":
                                    pic_3=pic_3+","
                                pic_3=pic_3+row_3[2]
                        if zaehler==1:
                            pic=pic_1+pic_2+","+pic_3
                        else:
                            pic=pic_1+pic_2+","+pic_3





                            

                        print("pic_1")
                        print(pic_1)

                        pic_1=pic.split(',',1)
                        wishlist.append(Wishlist(row_4[0],pic_1[0],row_2[0],row_2[1],row_2[3]))
 
 
 
 
    json_string = json.dumps([Wishlist.__dict__ for Wishlist in wishlist])
 
    return json_string




def load_style_filter(filter_style,filter_color,filter_feature,filter_size,click_last,filter_padding,link,user,day,month,year,c):
    filter_ = []
 
 
           
    class Filter(object):
        def __init__(self,group,name,show):
            self.group=group
            self.name=name
            self.show=show
 
 

   
 

 
    
 
    list=get_styles(filter_style,filter_color,filter_feature,filter_size,filter_padding,"",0,link,user,day,month,year,c)

    styles=list[0][0]
    color=list[1][0]
    padding=list[2][0]
    feature=list[3][0]
    sizes=list[4][0]


    if link!="Slips":
        i=0
        while i<=5:
            if styles[i][1]==1:
                filter_.append(Filter("Styles",styles[i][0],"true",))
            else:
                filter_.append(Filter("Styles",styles[i][0],"false",))
            i=i+1
     
        i=0
        while i<=11:
            if color[i][1]==1:
                filter_.append(Filter("Color",color[i][0],"true",))
            else:
                filter_.append(Filter("Color",color[i][0],"false",))
            i=i+1
     
        i=0
        while i<=3:
            if padding[i][1]==1:
                filter_.append(Filter("Padding",padding[i][0],"true",))
            else:
                filter_.append(Filter("Padding",padding[i][0],"false",))
            i=i+1
     
        i=0
        while i<=4:
            if feature[i][1]==1:
                filter_.append(Filter("Feature",feature[i][0],"true",))
            else:
                filter_.append(Filter("Feature",feature[i][0],"false",))
            i=i+1
     
     
        i=0   
        while i<=29:
            if sizes[i][1]==1:
                filter_.append(Filter("Sizes",sizes[i][0],"true",))
            else:
                filter_.append(Filter("Sizes",sizes[i][0],"false",))
            i=i+1
    else:
        i=0
        while i<=2:
            if styles[i][1]==1:
                filter_.append(Filter("Styles",styles[i][0],"true",))
            else:
                filter_.append(Filter("Styles",styles[i][0],"false",))
            i=i+1
     
        i=0
        while i<=11:
            if color[i][1]==1:
                filter_.append(Filter("Color",color[i][0],"true",))
            else:
                filter_.append(Filter("Color",color[i][0],"false",))
            i=i+1

     
     
        i=0   
        while i<=3:
            if sizes[i][1]==1:
                filter_.append(Filter("Sizes",sizes[i][0],"true",))
            else:
                filter_.append(Filter("Sizes",sizes[i][0],"false",))
            i=i+1        
 
    json_string = json.dumps([Filter.__dict__ for Filter in filter_])
	

 
    return json_string



def get_styles(filter_style_,filter_color_,filter_feature_,filter_size_,filter_padding_,last_click,id,link,user,day,month,year,c):

   
    styles = [[] for i in range(6)]
    color = [[] for i in range(12)]
    padding = [[] for i in range(4)]
    feature= [[] for i in range(6)]
    sizes= [[] for i in range(90)]
    sizes_dict= {}


    list = [[] for i in range(6)]
    now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))

  
    i=0


    if link!="Slips":
        c.execute ("""select * from style """)
        for row in c:
            styles[i].append(row[0])
            styles[i].append(0)
            i=i+1
     
     
        i=0
        c.execute ("""select * from color """)
        for row in c:
            color[i].append(row[0])
            color[i].append(0)
            i=i+1
     
     
        i=0
        c.execute ("""select * from padding """)
        for row in c:
            padding[i].append(row[0])
            padding[i].append(0)
            i=i+1
     
        i=0
        c.execute ("""select * from feature""")
        for row in c:
            feature[i].append(row[0])
            feature[i].append(0)
            i=i+1
     
        i=0
        c.execute ("""select * from sizes""")
        for row in c:
            sizes_dict[row[0]]=i
            sizes[i].append(row[0])
            sizes[i].append(0)
            i=i+1
    else:
        c.execute ("""select * from stylepanty """)
        for row in c:
            styles[i].append(row[0])
            styles[i].append(0)
            i=i+1
     
     
        i=0
        c.execute ("""select * from color """)
        for row in c:
            color[i].append(row[0])
            color[i].append(0)
            i=i+1

     
        i=0
        c.execute ("""select * from sizespanty""")
        for row in c:
            sizes_dict[row[0]]=i
            sizes[i].append(row[0])
            sizes[i].append(0)
            i=i+1

    now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))

    







    
    index=0
    print("ASD")
    c.execute ("""select * from lingerieselection ORDER BY position ASC""")

    lingerieselection=c.fetchall()
    for row in lingerieselection:
        print(row[0])
        print(link)
        print(row[7])
        if link!="Mein Showroom":

            if link=="BH & Slips" or link=="lingerie":


                if row[7]=="yes":

                               
                    id=0

                    while id<=4:
                        print("id")
                        if filter_color_=="" and filter_style_=="" and filter_feature_=="" and filter_size_=="" and filter_padding_=="":
                            filter_style=filter_style_
                            filter_color=filter_color_
                            filter_feature=filter_feature_
                            filter_size=filter_size_
                            filter_padding=filter_padding_
                            id=5
                        else:
                            if id==0:
                                filter_style=""
                                filter_color=filter_color_
                                filter_feature=filter_feature_
                                filter_size=filter_size_
                                filter_padding=filter_padding_
                            if id==1:

                                filter_style=filter_style_
                                filter_color=""
                                filter_feature=filter_feature_
                                filter_size=filter_size_
                                filter_padding=filter_padding_
                            if id==2:

                                filter_style=filter_style_
                                filter_color=filter_color_
                                filter_feature=filter_feature_
                                filter_size=filter_size_
                                filter_padding=""
                            if id==3:

                                filter_style=filter_style_
                                filter_color=filter_color_
                                filter_feature=""
                                filter_size=filter_size_
                                filter_padding=filter_padding_
                            if id==4:

                                filter_style=filter_style_
                                filter_color=filter_color_
                                filter_feature=filter_feature_
                                filter_size=""
                                filter_padding=filter_padding_
                        i=0
                        

                        while i<=5:
                            if last_click=="":
                                if (row[20+i]=="x" and styles[i][0]==filter_style) or (filter_style=="" and row[20+i]=="x"):
                 
                                    j=0
                                    
                                    while j<=11:
                                        if (row[41]==j and filter_color==color[j][0]) or (filter_color=="" and row[41]==j):
                 
                                            k=0
                                            
                                            while k<=3:
                                                if (row[32+k]=="x" and padding[k][0]==filter_padding) or (filter_padding=="" and row[32+k]=="x"):
                 
                                                    h=0
                                                    
                                                    while h<=5:
                                                        if (row[26+h]=="x" and feature[h][0]==filter_feature) or (filter_feature=="" and row[26+h]=="x"):
                                                            g=0

                                                        
                                                                
                                                            if filter_size=="":





                                                                if id==0:
                                                                    c.execute ("""select * from %s where color='%s'""" % ("stylecode_"+row[11], row[12],))
                                                                    rows=c.fetchall()

                                                                    if len(rows)>0:                                                                  
                                                                        styles[i][1]=1
                                                                if id==1:
                                                                    c.execute ("""select * from %s where color='%s'""" % ("stylecode_"+row[11], row[12],))
                                                                    rows=c.fetchall()
																
                                                                    if len(rows)>0: 
                                                                        color[j][1]=1
                                                                    
                                                                if id==2:
                                                                    
                                                                    c.execute ("""select * from %s where color='%s'""" % ("stylecode_"+row[11], row[12],))
                                                                    rows=c.fetchall()
                                                                    if len(rows)>0:
                                                                        padding[k][1]=1

                                                                if id==3:
                                                                    c.execute ("""select * from %s where color='%s'""" % ("stylecode_"+row[11], row[12],))
                                                                    rows=c.fetchall()
                                                                    if len(rows)>0: 
                                                                        feature[h][1]=1

                                                                if id==4:
                                                                    c.execute ("""select * from %s where color='%s'""" % ("stylecode_"+row[11], row[12],))
                                                                    for row_2 in c: 
                                                                        menge=int(row_2[4])-int(row_2[5])
                                                                        if menge>0:                                                                   
                                                                            try:
                                                                                
                                                                                sizes[sizes_dict[row_2[3]]][1]=1


                                                                                
                                                                            except:
                                                                                id=id
                                                                if id==5:


                                                                    now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))

                                                                    c.execute ("""select * from %s where color='%s' and type='%s'""" % ("stylecode_"+row[11], row[12],"BH"))
                                                                    for row_2 in c: 
                                                                        menge=int(row_2[4])-int(row_2[5])
                                                                        if menge>0:                                                                   
                                                                            try:
                                                                                styles[i][1]=1
                                                                                color[j][1]=1
                                                                                padding[k][1]=1
                                                                                feature[h][1]=1
                                                                                
                                                                                sizes[sizes_dict[row_2[3]]][1]=1


                                                                                
                                                                            except:
                                                                                id=id

                                                        
                                                            else:
                                                                c.execute ("""select * from %s where color='%s' and size='%s'""" % ("stylecode_"+row[11], row[12],filter_size,))
                                                                for row_2 in c:
                                                                    

                                                                    menge=int(row_2[4])-int(row_2[5])
                                                                    if menge>0:


                                                                        if id==0:
                                                                            styles[i][1]=1
                                                                        if id==1:                              
                                                                            color[j][1]=1
                                                                        if id==2:                              
                                                                            padding[k][1]=1
                                                                        if id==3:                              
                                                                            feature[h][1]=1
                                                                        if id==4:
                                                                            
                                                                            try:
                                                                                
                                                                                sizes[sizes_dict[row_2[3]]][1]=1


                                                                                
                                                                            except:
                                                                                id=id

                                                        h=h+1
                                                k=k+1
                                        j=j+1
                            i=i+1
                        id=id+1
            else:
                if row[7]=="yes" and row[8]=="panties":

                               
                    id=0

                    while id<=2:
                        if filter_color_=="" and filter_style_=="" and filter_size_=="":
                            filter_style=filter_style_
                            filter_color=filter_color_
                            filter_size=filter_size_
                            id=3
                        else:
                            if id==0:
                                filter_style=""
                                filter_color=filter_color_
                                filter_size=filter_size_
                            if id==1:

                                filter_style=filter_style_
                                filter_color=""
                                filter_size=filter_size_
                            if id==2:

                                filter_style=filter_style_
                                filter_color=filter_color_
                                filter_size=""

                        i=0
                        

                        while i<=2:
                            if last_click=="":
                                if (row[20+i]=="x" and styles[i][0]==filter_style) or (filter_style=="" and row[20+i]=="x"):
                 
                                    j=0
                                    
                                    while j<=11:
                                        if (row[41]==j and filter_color==color[j][0]) or (filter_color=="" and row[41]==j):
                 

                                            g=0

                                        
                                                
                                            if filter_size=="":





                                                if id==0:
                                                    c.execute ("""select * from %s where color='%s'""" % ("stylecode_"+row[11], row[12],))
                                                    rows=c.fetchall()
                                                    if len(rows)>0:                                                                  
                                                        styles[i][1]=1
                                                if id==1:
                                                    c.execute ("""select * from %s where color='%s'""" % ("stylecode_"+row[11], row[12],))
                                                    rows=c.fetchall()
                                                    if len(rows)>0: 
                                                        color[j][1]=1
                                                    

                                                if id==2:
                                                    c.execute ("""select * from %s where color='%s'""" % ("stylecode_"+row[11], row[12],))
                                                    for row_2 in c: 
                                                        menge=int(row_2[4])-int(row_2[5])
                                                        if menge>0:                                                                   
                                                            try:
                                                                
                                                                sizes[sizes_dict[row_2[3]]][1]=1


                                                                
                                                            except:
                                                                id=id
                                                if id==3:


                                                    now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))


                                                    c.execute ("""select * from %s where color='%s' and type='%s'""" % ("stylecode_"+row[11], row[12],"panties"))
                                                    for row_2 in c: 
                                                        menge=int(row_2[4])-int(row_2[5])
                                                        if menge>0:                                                                   
                                                            try:
                                                                styles[i][1]=1
                                                                color[j][1]=1

                                                                
                                                                sizes[sizes_dict[row_2[3]]][1]=1


                                                                
                                                            except:
                                                                id=id

                                        
                                            else:
                                                c.execute ("""select * from %s where color='%s' and size='%s'""" % ("stylecode_"+row[11], row[12],filter_size,))
                                                for row_2 in c:
                                                    

                                                    menge=int(row_2[4])-int(row_2[5])
                                                    if menge>0:


                                                        if id==0:
                                                            styles[i][1]=1
                                                        if id==1:                              
                                                            color[j][1]=1
                                                        if id==2:                              
                                                            
                                                            try:
                                                                
                                                                sizes[sizes_dict[row_2[3]]][1]=1

                                                            except:
                                                                id=id

                                        j=j+1
                            i=i+1
                        id=id+1                
        else:


            c.execute ("""select * from %s """ % ("showroom_"+user))

            showroom_data=c.fetchall()
            for row_3 in showroom_data:

                if row_3[0]==row[11] and row_3[1]==row[12] and row_3[2]==day and row_3[3]==month and row_3[4]==year: 


                    if row[7]=="yes":

                                   
                        id=0

                        while id<=4:
                            if filter_color_=="" and filter_style_=="" and filter_feature_=="" and filter_size_=="" and filter_padding_=="":
                                filter_style=filter_style_
                                filter_color=filter_color_
                                filter_feature=filter_feature_
                                filter_size=filter_size_
                                filter_padding=filter_padding_
                                id=5
                            else:
                                if id==0:
                                    filter_style=""
                                    filter_color=filter_color_
                                    filter_feature=filter_feature_
                                    filter_size=filter_size_
                                    filter_padding=filter_padding_
                                if id==1:

                                    filter_style=filter_style_
                                    filter_color=""
                                    filter_feature=filter_feature_
                                    filter_size=filter_size_
                                    filter_padding=filter_padding_
                                if id==2:

                                    filter_style=filter_style_
                                    filter_color=filter_color_
                                    filter_feature=filter_feature_
                                    filter_size=filter_size_
                                    filter_padding=""
                                if id==3:

                                    filter_style=filter_style_
                                    filter_color=filter_color_
                                    filter_feature=""
                                    filter_size=filter_size_
                                    filter_padding=filter_padding_
                                if id==4:

                                    filter_style=filter_style_
                                    filter_color=filter_color_
                                    filter_feature=filter_feature_
                                    filter_size=""
                                    filter_padding=filter_padding_
                            i=0
                            

                            while i<=5:
                                if last_click=="":
                                    if (row[20+i]=="x" and styles[i][0]==filter_style) or (filter_style=="" and row[20+i]=="x"):
                     
                                        j=0
                                        
                                        while j<=11:
                                            if (row[41]==j and filter_color==color[j][0]) or (filter_color=="" and row[41]==j):
                     
                                                k=0
                                                
                                                while k<=3:
                                                    if (row[32+k]=="x" and padding[k][0]==filter_padding) or (filter_padding=="" and row[32+k]=="x"):
                     
                                                        h=0
                                                        
                                                        while h<=5:
                                                            if (row[26+h]=="x" and feature[h][0]==filter_feature) or (filter_feature=="" and row[26+h]=="x"):
                                                                g=0

                                                            
                                                                    
                                                                if filter_size=="":





                                                                    if id==0:
                                                                        c.execute ("""select * from %s where color='%s'""" % ("stylecode_"+row[11], row[12],))
                                                                        rows=c.fetchall()
                                                                        if len(rows)>0:                                                                  
                                                                            styles[i][1]=1
                                                                    if id==1:
                                                                        c.execute ("""select * from %s where color='%s'""" % ("stylecode_"+row[11], row[12],))
                                                                        rows=c.fetchall()
                                                                        if len(rows)>0: 
                                                                            color[j][1]=1
                                                                        
                                                                    if id==2:
                                                                        
                                                                        c.execute ("""select * from %s where color='%s'""" % ("stylecode_"+row[11], row[12],))
                                                                        rows=c.fetchall()
                                                                        if len(rows)>0:
                                                                            padding[k][1]=1

                                                                    if id==3:
                                                                        c.execute ("""select * from %s where color='%s'""" % ("stylecode_"+row[11], row[12],))
                                                                        rows=c.fetchall()
                                                                        if len(rows)>0: 
                                                                            feature[h][1]=1

                                                                    if id==4:
                                                                        c.execute ("""select * from %s where color='%s'""" % ("stylecode_"+row[11], row[12],))
                                                                        for row_2 in c: 
                                                                            menge=int(row_2[4])-int(row_2[5])
                                                                            if menge>0:                                                                   
                                                                                try:
                                                                                    
                                                                                    sizes[sizes_dict[row_2[3]]][1]=1


                                                                                    
                                                                                except:
                                                                                    id=id
                                                                    if id==5:


                                                                        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))

                                                                        c.execute ("""select * from %s where color='%s' and type='%s'""" % ("stylecode_"+row[11], row[12],"BH"))
                                                                        for row_2 in c: 
                                                                            menge=int(row_2[4])-int(row_2[5])
                                                                            if menge>0:                                                                   
                                                                                try:
                                                                                    styles[i][1]=1
                                                                                    color[j][1]=1
                                                                                    padding[k][1]=1
                                                                                    feature[h][1]=1
                                                                                    
                                                                                    sizes[sizes_dict[row_2[3]]][1]=1


                                                                                    
                                                                                except:
                                                                                    id=id

                                                            
                                                                else:
                                                                    c.execute ("""select * from %s where color='%s' and size='%s'""" % ("stylecode_"+row[11], row[12],filter_size,))
                                                                    for row_2 in c:
                                                                        

                                                                        menge=int(row_2[4])-int(row_2[5])
                                                                        if menge>0:


                                                                            if id==0:
                                                                                styles[i][1]=1
                                                                            if id==1:                              
                                                                                color[j][1]=1
                                                                            if id==2:                              
                                                                                padding[k][1]=1
                                                                            if id==3:                              
                                                                                feature[h][1]=1
                                                                            if id==4:
                                                                                
                                                                                try:
                                                                                    
                                                                                    sizes[sizes_dict[row_2[3]]][1]=1

                                                                                except:
                                                                                    id=id

                                                            h=h+1
                                                    k=k+1
                                            j=j+1
                                i=i+1
                            id=id+1 
    now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
	
    print(color)

    list[0].append(styles)
    list[1].append(color)
    list[2].append(padding)
    list[3].append(feature)
    list[4].append(sizes)
    return list


 

def get_links(session_id,c):
    links = []
            
    class Links(object):
        def __init__(self,link,name,group1,group2,group3,pictureoverallsrc,headlineoverall,subtitleoverall):
            self.name=name
            self.link=link
            self.name=name
            self.group1=group1
            self.group2=group2
            self.group3=group3
            self.pictureoverallsrc=pictureoverallsrc
            self.headlineoverall=headlineoverall
            self.subtitleoverall=subtitleoverall

 
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                            password='okano1988',database='maxfischer2database')

    c = conn.cursor(buffered=True)






    c.execute ("""select * from userdaten """)

    userdaten=c.fetchall()
    

    for row_2 in userdaten:
        if row_2[9]==session_id:
            
            c.execute ("""select * from links """)
            for row in c:
       
                if row[1]=="Mein Showroom":

                    links.append(Links(row[0],row[1],row_2[26],row[3],row[4],row[5],row[6],row[7],))
                else:
                    
                    links.append(Links(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],))



    json_string = json.dumps([Links.__dict__ for Links in links])


    return json_string


def get_lingerie_sizes(group1,group2,group3,color,size,user,name,name_list,c):
    lingerie = []
            
    class Lingerie(object):
        def __init__(self,name,sizerange,pic,priceregular,pricesubscription,description,details,active,productgroup,wishlist,descriptionshort):
            self.name=name
            self.sizerange=sizerange
            self.pic=pic
            self.priceregular=priceregular
            self.pricesubscription=pricesubscription
            self.description=description
            self.details=details
            self.active=active
            self.productgroup=productgroup
            self.wishlist=wishlist
            self.descriptionshort=descriptionshort
            









    c.execute ("""select * from lingerieselection """)
    for row in c:
        
        if row[7]=="yes":
            if name_list=="":
                if name=="":
                    if row[8]==group1 or row[8]==group2 or row[8]==group3:
                        if row[14]=="true":
                            priceregular=row[3]-row[13]
                            pricesubscription=row[4]-row[13]
                        else:
                            priceregular=row[3]
                            pricesubscription=row[4]                       
                            
                        lingerie.append(Lingerie(row[0],row[1],row[2],priceregular,pricesubscription,row[5],row[6],row[7],row[8],get_wishlist(row[11],row[12],user,row[8]),row[9],))
                else:
                    if row[0]==name:
                        if row[14]=="true":
                            priceregular=row[3]-row[13]
                            pricesubscription=row[4]-row[13]
                        else:
                            priceregular=row[3]
                            pricesubscription=row[4]
                        lingerie.append(Lingerie(row[0],row[1],row[2],priceregular,pricesubscription,row[5],row[6],row[7],row[8],get_wishlist(row[11],row[12],user,row[8]),row[9],))
            else:

                    
                t=0
                while t<=len(name_list)-1:

                    if row[0]==name_list[t]:

                        if row[14]=="true":
                            priceregular=row[3]-row[13]
                            pricesubscription=row[4]-row[13]
                        else:
                            priceregular=row[3]
                            pricesubscription=row[4]
                            
                        lingerie.append(Lingerie(row[0],row[1],row[2],priceregular,pricesubscription,row[5],row[6],row[7],row[8],"",row[9],))
                    t=t+1


    json_string = json.dumps([Lingerie.__dict__ for Lingerie in lingerie])


    return json_string





def get_lingerie_selection_filter(group1,group2,group3,color,size,user,name,day,month,year,filter_style,filter_color,filter_feature,filter_padding,filter_size,modelAB,sub_picture,c):
    lingerie = []


            
    class Lingerie(object):
        def __init__(self,name,sizerange,pic,priceregular,pricesubscription,description,details,active,productgroup,wishlist,descriptionshort,stylecode,colorcode,position):
            self.name=name
            self.sizerange=sizerange
            self.pic=pic
            self.priceregular=priceregular
            self.pricesubscription=pricesubscription
            self.description=description
            self.details=details
            self.active=active
            self.productgroup=productgroup
            self.wishlist=wishlist
            self.descriptionshort=descriptionshort
            self.stylecode=stylecode
            self.colorcode=colorcode
            self.position=position


    styles = [[] for i in range(6)]
    color = [[] for i in range(12)]
    padding = [[] for i in range(4)]
    feature= [[] for i in range(6)]
    sizes= [[] for i in range(90)]
 
    i=0
    c.execute ("""select * from style """)
    for row in c:
        styles[i].append(row[0])
        styles[i].append(0)
        i=i+1
 
 
    i=0
    c.execute ("""select * from color """)
    for row in c:
        color[i].append(row[0])
        color[i].append(0)
        i=i+1
 
 
    i=0
    c.execute ("""select * from padding """)
    for row in c:
        padding[i].append(row[0])
        padding[i].append(0)
        i=i+1
 
    i=0
    c.execute ("""select * from feature""")
    for row in c:
        feature[i].append(row[0])
        feature[i].append(0)
        i=i+1
 
 
 
    i=0
    c.execute ("""select * from feature""")
    for row in c:
        feature[i].append(row[0])
        feature[i].append(0)
        i=i+1
 
 
    i=0
    c.execute ("""select * from sizes""")
    for row in c:
        sizes[i].append(row[0])
        sizes[i].append(0)
        i=i+1



    c.execute ("""select * from lingerieselection """)

    lingerieselection=c.fetchall()


    for row in lingerieselection:

        if row[7]=="yes":
            if name=="":

                if filter_style=="" and filter_color=="" and filter_feature=="" and filter_padding=="" and filter_size=="":

                    if row[8]==group1 or row[8]==group2 or row[8]==group3:
                        
                        if row[14]=="true":

                            priceregular=row[3]-row[13]
                            pricesubscription=row[4]-row[13]
                        else:
                            priceregular=row[3]
                            pricesubscription=row[4]


                        c.execute ("""select * from %s """ % ("picturelibrary_"+row[11]+"_"+row[12]))

                        picturelibrary_data=c.fetchall()


                        pic_1=""
                        pic_2=""
                        pic_3=""
                        zaehler=0
                        for row_3 in picturelibrary_data:
                            if group1!="panties":
                                if ((row_3[0]==modelAB and row_3[1]==sub_picture) or (row_3[0]==-1 and row_3[1]==sub_picture)):

                                    pic_1=pic_1+row_3[2]+","
                            else:

                                if group1==row_3[3] and (row[2]==row_3[4]):

                                    pic_1=pic_1+row_3[2]+","                            
                            if ((row_3[0]==modelAB and row_3[1]!=sub_picture and sub_picture!=-1 and row_3[1]!=-1) or (row_3[0]==-1 and row_3[1]!=sub_picture and sub_picture!=-1 and row_3[1]!=-1)) or (group1=="panties" and group1==row_3[3]):
                                if pic_2!="":
                                    pic_2=pic_2+","
                                pic_2=pic_2+row_3[2]
                                zaehler=zaehler+1

                            if row_3[1]==-1:
                                if pic_3!="":
                                    pic_3=pic_3+","
                                pic_3=pic_3+row_3[2]
                        if zaehler==1:
                            pic=pic_1+pic_2+","+pic_3
                        else:
                            pic=pic_1+pic_2+","+pic_3

                            
                            


        
                        lingerie.append(Lingerie(row[0],row[1],pic,priceregular,pricesubscription,row[5],row[6],row[7],row[8],get_wishlist(row[11],row[12],user,row[8]),row[9],row[11],row[12],row[42],))
                    else:
                        if group1=="Mein Showroom" and row[8]=="lingerie":
                            c.execute ("""select * from %s """ % ("showroom_"+user))

                            showroom_data=c.fetchall()

                            for row_2 in showroom_data:


                                if row_2[0]==row[11] and row_2[1]==row[12] and row_2[2]==day and row_2[3]==month and row_2[4]==year:                          
                                    if row[14]=="true":
                                        priceregular=row[3]-row[13]
                                        pricesubscription=row[4]-row[13]
                                    else:
                                        priceregular=row[3]
                                        pricesubscription=row[4]



                                    c.execute ("""select * from %s """ % ("picturelibrary_"+row[11]+"_"+row[12]))

                                    picturelibrary_data_2=c.fetchall()
                                        

                                    pic_1=""
                                    pic_2=""
                                    pic_3=""
                                    zaehler=0
                                    for row_3 in picturelibrary_data_2:
                                        if (row_3[0]==modelAB and row_3[1]==sub_picture) or (row_3[0]==-1 and row_3[1]==sub_picture):
                                            pic_1=pic_1+row_3[2]+","
                                        
                                        if (row_3[0]==modelAB and row_3[1]!=sub_picture and sub_picture!=-1 and row_3[1]!=-1) or (row_3[0]==-1 and row_3[1]!=sub_picture and sub_picture!=-1 and row_3[1]!=-1):
                                            if pic_2!="":
                                                pic_2=pic_2+","
                                            pic_2=pic_2+row_3[2]
                                            zaehler=zaehler+1

                                        if row_3[1]==-1:
                                            if pic_3!="":
                                                pic_3=pic_3+","
                                            pic_3=pic_3+row_3[2]
                                    if zaehler==1:
                                        pic=pic_1+pic_2+","+pic_3
                                    else:
                                        pic=pic_1+pic_2+","+pic_3

                                            
                                    lingerie.append(Lingerie(row[0],row[1],pic,priceregular,pricesubscription,row[5],row[6],row[7],row[8],get_wishlist(row[11],row[12],user,row[8]),row[9],row[11],row[12],row[42],))
                        else:
                            
                            if group1=="Wunschliste":


                                c.execute ("""select * from %s """ % ("wishlist_"+user))

                                wishlist_data=c.fetchall()


                                for row_2 in wishlist_data:

                                    if row_2[0]==row[11] and row_2[1]==row[12]:

                                        if row[14]=="true":
                                            priceregular=row[3]-row[13]
                                            pricesubscription=row[4]-row[13]
                                        else:
                                            priceregular=row[3]
                                            pricesubscription=row[4]


                                        c.execute ("""select * from %s """ % ("picturelibrary_"+row[11]+"_"+row[12]))

                                        picturelibrary_data_2=c.fetchall()


                                    

                                        pic_1=""
                                        pic_2=""
                                        pic_3=""
                                        zaehler=0
                                        for row_3 in picturelibrary_data_2:
                                            if (row_3[0]==modelAB and row_3[1]==sub_picture) or (row_3[0]==-1 and row_3[1]==sub_picture):
                                                pic_1=pic_1+row_3[2]+","
                                            
                                            if (row_3[0]==modelAB and row_3[1]!=sub_picture and sub_picture!=-1 and row_3[1]!=-1) or (row_3[0]==-1 and row_3[1]!=sub_picture and sub_picture!=-1 and row_3[1]!=-1):
                                                if pic_2!="":
                                                    pic_2=pic_2+","
                                                pic_2=pic_2+row_3[2]
                                                zaehler=zaehler+1

                                            if row_3[1]==-1:
                                                if pic_3!="":
                                                    pic_3=pic_3+","
                                                pic_3=pic_3+row_3[2]
                                        if zaehler==1:
                                            pic=pic_1+pic_2+","+pic_3
                                        else:
                                            pic=pic_1+pic_2+","+pic_3

                                            
                                        lingerie.append(Lingerie(row[0],row[1],pic,priceregular,pricesubscription,row[5],row[6],row[7],row[8],get_wishlist(row[11],row[12],user,row[8]),row[9],row[11],row[12],row[42],))

                                            
                                    
                else:
                    if row[8]==group1 or row[8]==group2 or row[8]==group3:
                        existiert="nein"

                        c.execute ("""select * from %s """ % ("stylecode_"+row[11]))

                        stylecode_data=c.fetchall()

                        for row_2 in stylecode_data:

                            if row[12]==row_2[2] and existiert=="nein":
                                menge=int(row_2[4])-int(row_2[5])
                                if menge>0:
                                    
                                    i=0
                                    while i<=5:
                                        if (row[20+i]=="x" and styles[i][0]==filter_style) or filter_style=="":


                                            j=0
                                            while j<=11:
                                                if (row[41]==j and filter_color==color[j][0]) or filter_color=="":

                                                    k=0
                                                    while k<=3:
                                                        if (row[32+k]=="x" and padding[k][0]==filter_padding) or (filter_padding==""):
                         
                                                            h=0
                                                            
                                                            while h<=5:
                                                                if (row[26+h]=="x" and feature[h][0]==filter_feature) or (filter_feature==""):
                                                                    g=0





                                        
                                                                                



                                                                    if row_2[3]==filter_size or filter_size=="":

                                                                    
                                                                    
                                                                    

                                                                        
                                                                        if row[14]=="true":

                                                                            priceregular=row[3]-row[13]
                                                                            pricesubscription=row[4]-row[13]
                                                                        else:
                                                                            priceregular=row[3]
                                                                            pricesubscription=row[4]




                                                                        c.execute ("""select * from %s """ % ("picturelibrary_"+row[11]+"_"+row[12]))

                                                                        picturelibrary_data_2=c.fetchall()

                                        

                                                                        pic_1=""
                                                                        pic_2=""
                                                                        pic_3=""
                                                                        zaehler=0
                                                                        for row_3 in picturelibrary_data_2:
                                                                            if (row_3[0]==modelAB and row_3[1]==sub_picture) or (row_3[0]==-1 and row_3[1]==sub_picture):
                                                                                pic_1=pic_1+row_3[2]+","
                                                                            
                                                                            if (row_3[0]==modelAB and row_3[1]!=sub_picture and sub_picture!=-1 and row_3[1]!=-1) or (row_3[0]==-1 and row_3[1]!=sub_picture and sub_picture!=-1 and row_3[1]!=-1):
                                                                                if pic_2!="":
                                                                                    pic_2=pic_2+","
                                                                                pic_2=pic_2+row_3[2]
                                                                                zaehler=zaehler+1

                                                                            if row_3[1]==-1:
                                                                                if pic_3!="":
                                                                                    pic_3=pic_3+","
                                                                                pic_3=pic_3+row_3[2]
                                                                        if zaehler==1:
                                                                            pic=pic_1+pic_2+","+pic_3
                                                                        else:
                                                                            pic=pic_1+pic_2+","+pic_3

                                                
                                                                        lingerie.append(Lingerie(row[0],row[1],pic,priceregular,pricesubscription,row[5],row[6],row[7],row[8],get_wishlist(row[11],row[12],user,row[8]),row[9],row[11],row[12],row[42],))
                                                                        i=6
                                                                        j=12
                                                                        k=4
                                                                        g=30
                                                                        h=5
                                                                        existiert="ja"


                                                                h=h+1
                                                        k=k+1
                                                j=j+1

                                        i=i+1
                            
                    else:
                        if group1=="Mein Showroom" and row[8]=="lingerie":

                            
                            c.execute ("""select * from %s """ % ("showroom_"+user))

                            showroom_data=c.fetchall()
      

                            for row_4 in showroom_data:

                                
                                
                                if row_4[0]==row[11] and row_4[1]==row[12] and row_4[2]==day and row_4[3]==month and row_4[4]==year:

          
                                    existiert="nein"



                                    c.execute ("""select * from %s """ % ("stylecode_"+row[11]))

                                    stylecode_data=c.fetchall()

                        

                                    for row_2 in stylecode_data:


                                        if row[12]==row_2[2] and existiert=="nein":
                                            menge=int(row_2[4])-int(row_2[5])
                                            if menge>0:

                                                
                                                i=0
                                                while i<=5:
                                                    if (row[20+i]=="x" and styles[i][0]==filter_style) or filter_style=="":


                                                        j=0
                                                        while j<=11:

                                                            if (row[41]==j and filter_color==color[j][0]) or filter_color=="":
                                                                
                                                                k=0
                                                                while k<=3:
                                                                    if (row[32+k]=="x" and padding[k][0]==filter_padding) or (filter_padding==""):
                                     
                                                                        h=0
                                                                        
                                                                        while h<=5:
                                                                            if (row[26+h]=="x" and feature[h][0]==filter_feature) or (filter_feature==""):
                                                                                g=0
                                                                                





                                                    
                                                                                            
                                                                                if row_2[3]==filter_size or filter_size=="":

                                                                                        

                                                                                        
                                                                                    if row[14]=="true":

                                                                                        priceregular=row[3]-row[13]
                                                                                        pricesubscription=row[4]-row[13]
                                                                                    else:
                                                                                        priceregular=row[3]
                                                                                        pricesubscription=row[4]




                                                                                    c.execute ("""select * from %s """ % ("picturelibrary_"+row[11]+"_"+row[12]))

                                                                                    picturelibrary_data_2=c.fetchall()


                                                                                    pic_1=""
                                                                                    pic_2=""
                                                                                    pic_3=""
                                                                                    zaehler=0
                                                                                    for row_3 in picturelibrary_data_2:

                                                                                        if (row_3[0]==modelAB and row_3[1]==sub_picture) or (row_3[0]==-1 and row_3[1]==sub_picture):
                                                                                            pic_1=pic_1+row_3[2]+","
                                                                                        
                                                                                        if (row_3[0]==modelAB and row_3[1]!=sub_picture and sub_picture!=-1 and row_3[1]!=-1) or (row_3[0]==-1 and row_3[1]!=sub_picture and sub_picture!=-1 and row_3[1]!=-1):
                                                                                            if pic_2!="":
                                                                                                pic_2=pic_2+","
                                                                                            pic_2=pic_2+row_3[2]
                                                                                            zaehler=zaehler+1

                                                                                        if row_3[1]==-1:
                                                                                            if pic_3!="":
                                                                                                pic_3=pic_3+","
                                                                                            pic_3=pic_3+row_3[2]
                                                                                    if zaehler==1:
                                                                                        pic=pic_1+pic_2+","+pic_3
                                                                                    else:
                                                                                        pic=pic_1+pic_2+","+pic_3


                                                                                    lingerie.append(Lingerie(row[0],row[1],pic,priceregular,pricesubscription,row[5],row[6],row[7],row[8],get_wishlist(row[11],row[12],user,row[8]),row[9],row[11],row[12],row[42],))
                                                                                    i=6
                                                                                    j=12
                                                                                    k=4
                                                                                    g=30
                                                                                    h=5


                                                                                    existiert="ja"


                                                                            h=h+1
                                                                    k=k+1
                                                            j=j+1

                                                    i=i+1

                                    
            else:
                if row[0]==name:
                    if row[14]=="true":
                        priceregular=row[3]-row[13]
                        pricesubscription=row[4]-row[13]
                    else:
                        priceregular=row[3]
                        pricesubscription=row[4]





                    c.execute ("""select * from %s """ % ("picturelibrary_"+row[11]+"_"+row[12]))

                    picturelibrary_data_2=c.fetchall()



                    pic_1=""
                    pic_2=""
                    pic_3=""
                    zaehler=0
                    for row_3 in picturelibrary_data_2:
                        if group1!="panties":
                            if ((row_3[0]==modelAB and row_3[1]==sub_picture) or (row_3[0]==-1 and row_3[1]==sub_picture)):
                                pic_1=pic_1+row_3[2]+","

                                
                            if (row_3[0]==modelAB and row_3[1]!=sub_picture and sub_picture!=-1 and row_3[1]!=-1) or (row_3[0]==-1 and row_3[1]!=sub_picture and sub_picture!=-1 and row_3[1]!=-1):
                                if pic_2!="":
                                    pic_2=pic_2+","
                                pic_2=pic_2+row_3[2]
                                zaehler=zaehler+1

                            if row_3[1]==-1:
                                if pic_3!="":
                                    pic_3=pic_3+","
                                pic_3=pic_3+row_3[2]
                        else:

                            if group1==row_3[3] and (row[2]==row_3[4]):

                                pic_1=pic_1+row_3[2]+","



                    if zaehler==1:
                        pic=pic_1+pic_2+","+pic_3
                    else:
                        pic=pic_1+pic_2+","+pic_3


                    lingerie.append(Lingerie(row[0],row[1],pic,priceregular,pricesubscription,row[5],row[6],row[7],row[8],get_wishlist(row[11],row[12],user,row[8]),row[9],row[11],row[12],row[42],))


    
    json_string = json.dumps([Lingerie.__dict__ for Lingerie in lingerie])
    

    return json_string

        

def get_other_colors(style,name,group1,c):
    lingerie = []
            
    class Lingerie(object):
        def __init__(self,style,colorcode,detaildatabase,pic,name):
            self.style=style
            self.colorcode=colorcode
            self.detaildatabase=detaildatabase
            self.pic=pic
            self.name=name

    






    if name!="":
        c.execute ("""select * from stylelibrary """)

        stylelibrary=c.fetchall()
        for row in stylelibrary:

            if row[2]==name:
                style=row[0]

                c.execute ("""select * from stylelibrary """)

                stylelibrary_2=c.fetchall()

        

                for row_2 in stylelibrary_2:
                    if row_2[0]==style:
                        lingerie.append(Lingerie(row_2[0],row_2[1],row_2[2],row_2[3],row[2],))

    else:
        if group1!="":

            c.execute ("""select * from lingerieselection """)

            lingerieselection=c.fetchall()

            for row in lingerieselection:
                existiert="nein"
                if row[7]=="yes":
                    if row[8]==group1:
                        c.execute ("""select * from stylelibrary """)

                        stylelibrary=c.fetchall()


                        for row_2 in stylelibrary:
                            if row_2[2]==row[0]:
                                style=row_2[0]
                                
                                c.execute ("""select * from stylelibrary """)

                                stylelibrary_2=c.fetchall()
                                for row_3 in stylelibrary_2:
                                    if row_3[0]==style and existiert=="nein" and row_3[2]==row[0]:
                                        lingerie.append(Lingerie(row_3[0],row_3[1],row_3[2],row_3[3],row_2[2],))
                                        existiert="ja"

    json_string = json.dumps([Lingerie.__dict__ for Lingerie in lingerie])


    return json_string



def get_pricesforaddlpanty(name,VIP,c):
    prices = []
            
    class Prices(object):
        def __init__(self,priceregular,pricesubscription):
            self.priceregular=priceregular
            self.pricesubscription=pricesubscription


            




    c.execute ("""select * from lingerieselection """)

    lingerieselection=c.fetchall()



    for row in lingerieselection:
        if row[7]=="yes":
            if row[0]==name:
                c.execute ("""select * from lingerieselection """)

                lingerieselection_2=c.fetchall()

                for row_2 in lingerieselection_2:
                    if row_2[7]=="yes":

                        if row_2[0]!=name and row_2[11]==row[11] and row_2[12]==row[12]:

                            prices.append(Prices(row_2[3],row_2[4],))


    json_string = json.dumps([Prices.__dict__ for Prices in prices])


    return json_string



def get_lingerie_selection_sizes(name,link,c):
    c.execute ("""select * from lingerieselection """)

    lingerieselection=c.fetchall()


    for row in lingerieselection:
        if row[7]=="yes":
            if row[0]==name:

                c.execute ("""select * from %s """ % ("stylecode_"+row[11]))
                for row_2 in c:
                    if row[12]==row_2[2]:
                        if link!="panties":
                            menge=int(row_2[4])-int(row_2[5])
                            if menge>0:

                                lingerie.append(Lingerie(row_2[0],row_2[1],row_2[2],row_2[3],))
                        else:
                            if row_2[0]==link:
                                menge=int(row_2[4])-int(row_2[5])
                                if menge>0:

                                    lingerie.append(Lingerie(row_2[0],row_2[1],row_2[2],row_2[3],))                            


    json_string = json.dumps([Lingerie.__dict__ for Lingerie in lingerie])


    return json_string



def get_lingerie_selection_sizes(name,link,c):
    lingerie = []
            
    class Lingerie(object):
        def __init__(self,type,stylecode,color,size):
            self.type=type
            self.stylecode=stylecode
            self.color=color
            self.size=size



            




    c.execute ("""select * from lingerieselection""")

    lingerieselection=c.fetchall()   



    for row in lingerieselection:
        if row[7]=="yes":
            if row[0]==name:

                c.execute ("""select * from %s """ % ("stylecode_"+row[11]))
                for row_2 in c:
                    if row[12]==row_2[2]:
                        if link!="panties":
                            menge=int(row_2[4])-int(row_2[5])
                            if menge>0:

                                lingerie.append(Lingerie(row_2[0],row_2[1],row_2[2],row_2[3],))
                        else:
                            if row_2[0]==link:
                                menge=int(row_2[4])-int(row_2[5])
                                if menge>0:

                                    lingerie.append(Lingerie(row_2[0],row_2[1],row_2[2],row_2[3],))                            


    json_string = json.dumps([Lingerie.__dict__ for Lingerie in lingerie])


    return json_string



def get_lingerie_selection_bewertungen(name,c):


    lingerie = []
            
    class Lingerie(object):
        def __init__(self,namebewerter,bewertung,bewertungsheadline,bewertungstext,bewertungsdatum):
            self.namebewerter=namebewerter
            self.bewertung=bewertung
            self.bewertungsheadline=bewertungsheadline
            self.bewertungstext=bewertungstext
            self.bewertungsdatum=bewertungsdatum









            
    c.execute ("""select * from lingerieselection""")

    lingerieselection=c.fetchall()   
    for row in lingerieselection:

        if row[7]=="yes":
            
            if row[0]==name and row[8]!="panties" and row[8]!="geschenkkarten":

                c.execute ("""select * from %s """ % ("bewertungen_"+row[11]+"_"+row[12]))
                
                for row_2 in c:

                    lingerie.append(Lingerie(row_2[1],row_2[2],row_2[3],row_2[4],row_2[5],))



    json_string = json.dumps([Lingerie.__dict__ for Lingerie in lingerie])


    return json_string





def get_lingerie_selection_gesamtbewertung(name,c):
    lingerie = []
            
    class Lingerie(object):
        def __init__(self,gesamtbewertung,gesamtbewertunganzahl,einsternbewertung,einsternbewertunganzahl,zweisternbewertung,zweisternbewertunganzahl,dreisternbewertung,dreisternbewertunganzahl,viersternbewertung,viersternbewertunganzahl,fuenfsternbewertung,fuenfsternbewertunganzahl):
            self.gesamtbewertung=gesamtbewertung
            self.gesamtbewertunganzahl=gesamtbewertunganzahl
            self.einsternbewertung=einsternbewertung
            self.einsternbewertunganzahl=einsternbewertunganzahl
            self.zweisternbewertung=zweisternbewertung
            self.zweisternbewertunganzahl=zweisternbewertunganzahl            
            self.dreisternbewertung=dreisternbewertung
            self.dreisternbewertunganzahl=dreisternbewertunganzahl
            self.viersternbewertung=viersternbewertung
            self.viersternbewertunganzahl=viersternbewertunganzahl
            self.fuenfsternbewertung=fuenfsternbewertung
            self.fuenfsternbewertunganzahl=fuenfsternbewertunganzahl








            
    c.execute ("""select * from lingerieselection""")

    lingerieselection=c.fetchall()




    for row in lingerieselection:
        if row[7]=="yes":
            if row[0]==name and row[8]!="panties" and row[8]!="geschenkkarten":

                c.execute ("""select * from %s """ % ("bewertungen_"+row[11]+"_"+row[12]))
                gesamtbewertung=0
                gesamtbewertunganzahl=0
                einsternbewertung=0
                einsternbewertunganzahl=0
                zweisternbewertung=0
                zweisternbewertunganzahl=0            
                dreisternbewertung=0
                dreisternbewertunganzahl=0
                viersternbewertung=0
                viersternbewertunganzahl=0
                fuenfsternbewertung=0
                fuenfsternbewertunganzahl=0
                for row_2 in c:

                    if row_2[2]!="":

                        gesamtbewertung=gesamtbewertung+int(row_2[2])
                        gesamtbewertunganzahl=gesamtbewertunganzahl+1

                        if row_2[2]=="1":
                            einsternbewertung=einsternbewertung+int(row_2[2])
                            einsternbewertunganzahl=einsternbewertunganzahl+1
                        if row_2[2]=="2":
                            zweisternbewertung=zweisternbewertung+int(row_2[2])
                            zweisternbewertunganzahl=zweisternbewertunganzahl+1
                        if row_2[2]=="3":
                            dreisternbewertung=dreisternbewertung+int(row_2[2])
                            dreisternbewertunganzahl=dreisternbewertunganzahl+1

                        if row_2[2]=="4":
                            viersternbewertung=viersternbewertung+int(row_2[2])
                            viersternbewertunganzahl=viersternbewertunganzahl+1
                        if row_2[2]=="5":
                            fuenfsternbewertung=fuenfsternbewertung+int(row_2[2])
                            fuenfsternbewertunganzahl=fuenfsternbewertunganzahl+1

                        

                lingerie.append(Lingerie(gesamtbewertung,gesamtbewertunganzahl,einsternbewertung,einsternbewertunganzahl,zweisternbewertung,zweisternbewertunganzahl,dreisternbewertung,dreisternbewertunganzahl,viersternbewertung,viersternbewertunganzahl,fuenfsternbewertung,fuenfsternbewertunganzahl,))



    json_string = json.dumps([Lingerie.__dict__ for Lingerie in lingerie])


    return json_string


@csrf_exempt
def new_value_for_wishlist(request):
    if request.is_ajax() and request.GET:
        
        stylecode=request.GET.get('stylecode')
        colorcode=request.GET.get('colorcode')
        productgroup=request.GET.get('productgroup')
        status=request.GET.get('status')
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')

        c = conn.cursor(buffered=True)


        x=str(request.session.session_key)
        c.execute ("""select * from userdaten """)
        for row in c:
            if row[9]==x and x!="None":
                user=row[11]
                quiz=row[26]
                modelAB=row[47]
                sub_picture=row[48]

        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        Monat = ["Januar", "Februar", "Maerz", "April","Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
        date_short=str(now.day)+". "+Monat[(now.month)-1]+" "+str(now.year)
        
        
        if status=="yes":
            c.execute("""insert into %s values (%%s,%%s,%%s,%%s)""" % ("wishlist_"+user),(stylecode,colorcode,date_short,productgroup,))            

 #           if quiz=="yes":
#                adapt_showroom(user,name,0.01)
#                generate_showroom(x)
                
            conn.commit()
        else:
            c.execute("""delete from %s where stylecode=%%s and colorcode=%%s and productgroup=%%s""" % ("wishlist_"+user),(stylecode,colorcode,productgroup,))
 #           if quiz=="yes":
#                adapt_showroom(user,name,-0.01)
#                generate_showroom(x)
            conn.commit()
        wishlist=define_wishlist(x,modelAB,sub_picture,c)

        return HttpResponse(json.dumps(wishlist), content_type='application/json')

    
    

def get_wishlist(stylecode,colorcode,user,productgroup):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                            password='okano1988',database='maxfischer2database')

    c = conn.cursor(buffered=True)







    c.execute ("""select * from %s """ % ("wishlist_"+user))
    feedback="no"
    for row in c:
        if row[0]==stylecode and row[1]==colorcode and row[3]==productgroup:
            feedback="yes"
    return feedback
        
    



def define_gutscheinkonto(x):
    gutscheinkonto = []
            
    class Gutscheinkonto(object):
        def __init__(self,datum,gutscheinwert,bestellnummer,gutscheincodedesanderen,vorname,nachname):
            self.datum=datum
            self.gutscheinwert=gutscheinwert
            self.bestellnummer=bestellnummer
            self.gutscheincodedesanderen=gutscheincodedesanderen
            self.vorname=vorname
            self.nachname=nachname
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                            password='okano1988',database='maxfischer2database')

    c = conn.cursor(buffered=True)

    conn_2 = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                            password='okano1988',database='maxfischer2database')

    q = conn_2.cursor()
    conn_3 = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                            password='okano1988',database='maxfischer2database')

    d = conn_3.cursor()



    c.execute ("""select * from userdaten """)
    
    gutscheine=""
    status=0
    for row in c:
        if row[9]==x and x!="None":
            status=1

            q.execute ("""select * from %s """ %(row[11]))
            for row_2 in q:

                if row_2[1]!=0 and row_2[2]!="nicht anzeigen":
                    d.execute ("""select * from userdaten """)
                    for row_3 in d:

                        if row_3[11]==str(row_2[3]):
                            if row_3[2]=="" or row_3[3]=="":
                                vorname=str(row_3[0])
                                nachname=""
                            else:
                                vorname=str(row_3[2])
                                nachname=str(row_3[3])
                            
                                
                    gutscheinkonto.append(Gutscheinkonto(row_2[0],row_2[1],row_2[2],row_2[3],vorname,nachname,))


    json_string = json.dumps([Gutscheinkonto.__dict__ for Gutscheinkonto in gutscheinkonto])


    return json_string




def define_rebates(session_key,bestellnummer,string_list_cart,length_string_list,aenderung,c,conn):


    rebates = []
    class Rebates(object):
        def __init__(self,coupon,couponcode,braforfreevalue,braforfreecount,storecredit,credit,bestellung,gesamtpreis,aenderung,aenderung_rechnungsbetrag):
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


    c.execute ("""select * from userdaten """)

    userdaten=c.fetchall()
    

    delta=0
    aenderung_rechnungsbetrag=0

    for row in userdaten:

        if row[9]==session_key:

            if bestellnummer!="":


                c.execute ("""select * from %s ORDER BY idforsorting DESC""" % ("bestellt_"+row[11]))

                bestellt_data=c.fetchall()


                
                for row_2 in bestellt_data:


                    if row_2[20]==bestellnummer:
                        coupon=float(row_2[16])
                        couponcode=row_2[17]
                        storecredit=float(row_2[27])
                        braforfreevalue=float(row_2[26])
                        braforfreecount=float(row_2[25])
                        credit=float(row_2[21])



    

                        if string_list_cart!="":
                            bestellung=0
                        
                            c.execute ("""select * from %s """ % (row_2[0]))
                            for row_3 in c:
                                
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
                            coupon_new=min(coupon,max(bestellung,0))
                            zwischensumme=bestellung-coupon_new

                            credit_new=min(credit,max(zwischensumme,0))
                            zwischensumme=bestellung-coupon_new-credit_new

                            braforfreevalue_new=0
                            braforfreecount_new=0
                            bestellung_alt=0

                            
                            c.execute ("""select * from %s ORDER BY preis DESC""" % (row_2[0]))
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

                                
                            
                            zwischensumme=bestellung-coupon_new-credit_new-braforfreevalue_new

                            storecredit_new=min(storecredit,max(zwischensumme,0))

                            if aenderung=="":


                                
                                c.execute("""update %s set rabatt=%%s, creditused=%%s,braforfreecount=%%s,braforfreevalue=%%s,storecredit=%%s where bestellnummer=%%s""" % ("bestellt_"+row[11]),(coupon_new,credit_new,braforfreecount_new,braforfreevalue_new,storecredit_new,bestellnummer,))                            
                                c.execute("""update userdaten set numberofbraforfree=%s, credit=%s,storecredit=%s where lastsessionid=%s""",(int(row[25])+braforfreecount-braforfreecount_new,int(row[10])+credit-credit_new,int(row[24])+storecredit-storecredit_new,session_key,))


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



                            c.execute ("""select * from %s """ % (row_2[0]))
                            for row_3 in c:
                                bestellung=bestellung+float(row_3[1])*row_3[8]

                    
                            c.execute ("""select * from %s ORDER BY preis DESC""" % (row_2[0]))
                            for row_3 in c:

                                            
                                i=0
                                while i<=int(row_3[1])-1:

                                    if bestellung-coupon_new-credit_new-float(row_3[8])-braforfreevalue_new>=0 and braforfreecount_new<braforfreecount:
                                        braforfreevalue_new=braforfreevalue_new+float(row_3[8])
                                        braforfreecount_new=braforfreecount_new+1
                                    i=i+1
                        zwischensumme=bestellung-coupon_new-credit_new-braforfreevalue_new-storecredit_new+delta



            else:

                credit=float(row[10])
                storecredit=float(row[24])
                couponcode=row[21]
                coupon=float(-gutscheinwert_abrufen(couponcode,c))
                braforfreecount=int(row[25])



                
                bestellung=0
                c.execute ("""select * from %s """ % (session_key))
                for row_3 in c:

                    bestellung=bestellung+float(row_3[1])*row_3[8]
                
                coupon_new=min(coupon,max(bestellung,0))
                zwischensumme=bestellung-coupon_new

                credit_new=min(credit,max(zwischensumme,0))
                zwischensumme=bestellung-coupon_new-credit_new                                
                        


                braforfreevalue_new=0
                braforfreecount_new=0


                c.execute ("""select * from %s ORDER BY preis DESC""" % (session_key))
                for row_3 in c:
                                
                    i=0
                    while i<=int(row_3[1])-1:

                        if bestellung-coupon_new-credit_new-float(row_3[8])-braforfreevalue_new>=0 and braforfreecount_new<braforfreecount:
                            braforfreevalue_new=braforfreevalue_new+float(row_3[8])
                            braforfreecount_new=braforfreecount_new+1
                        i=i+1

                
                zwischensumme=bestellung-coupon_new-credit_new-braforfreevalue_new                                      


                storecredit_new=min(storecredit,max(zwischensumme,0))
                
                zwischensumme=bestellung-coupon_new-credit_new-braforfreevalue_new-storecredit_new



    rebates.append(Rebates(coupon_new,couponcode,braforfreevalue_new,braforfreecount_new,storecredit_new,credit_new,bestellung,zwischensumme,delta,aenderung_rechnungsbetrag,))


    json_string = json.dumps([Rebates.__dict__ for Rebates in rebates])



    return json_string

    


def define_warenkorb(session_key,modelAB,sub_picture,c):
    warenkorb = []
    class Warenkorb(object):
        def __init__(self,style,anzahl,bhgroesse,slipgroesse,color,freiemenge,status,picture,priceregular,pricesubscription,stylecode,colorcode,link1):
            self.style=style
            self.anzahl=anzahl
            self.bhgroesse=bhgroesse
            self.slipgroesse=slipgroesse
            self.color=color
            self.freiemenge=freiemenge
            self.status=status
            self.picture=picture
            self.priceregular=priceregular
            self.pricesubscription=pricesubscription
            self.stylecode=stylecode
            self.colorcode=colorcode
            self.link1=link1            
             
              


    c.execute  ("""select * from %s""" % (session_key))
    current_cart_database=c.fetchall()



    for row in current_cart_database:

        c.execute  ("""select * from lingerieselection """)
        lingerieselection_data=c.fetchall()

        for row_2 in lingerieselection_data:

            if row[0]==row_2[0]:
                
                c.execute  ("""select * from %s """ % ("picturelibrary_"+row_2[11]+"_"+row_2[12]))
                picturelibrary_data=c.fetchall()
                					
						
                group1="lingerie"
                pic_1=""
                pic_2=""
                pic_3=""
                zaehler=0
                for row_3 in picturelibrary_data:
                    if group1!="panties":
                        if ((row_3[0]==modelAB and row_3[1]==sub_picture) or (row_3[0]==-1 and row_3[1]==sub_picture)):

                            pic_1=pic_1+row_3[2]+","
                        else:

                            if group1==row_3[3] and (row[2]==row_3[4]):

                                pic_1=pic_1+row_3[2]+","                            
                        if ((row_3[0]==modelAB and row_3[1]!=sub_picture and sub_picture!=-1 and row_3[1]!=-1) or (row_3[0]==-1 and row_3[1]!=sub_picture and sub_picture!=-1 and row_3[1]!=-1)) or (group1=="panties" and group1==row_3[3]):
                            if pic_2!="":
                                pic_2=pic_2+","
                            pic_2=pic_2+row_3[2]
                            zaehler=zaehler+1

                        if row_3[1]==-1:
                            if pic_3!="":
                                pic_3=pic_3+","
                            pic_3=pic_3+row_3[2]
                    if zaehler==1:
                        pic=pic_1+pic_2+","+pic_3
                    else:
                        pic=pic_1+pic_2+","+pic_3



                pic_1=pic.split(',',1)
 
                warenkorb.append(Warenkorb(row[0],row[1],row[2],row[3],row[4],row[5],row[6],pic_1[0],row_2[3],row_2[4],row_2[11],row_2[12],link_name_bestimmen(row_2[8],c)))

 #   warenkorb.sort(key = lambda x: x.position)
    json_string = json.dumps([Warenkorb.__dict__ for Warenkorb in warenkorb])



    return json_string











def define_bestelldetails(session_key,bestellnummer,gerichtname,bewertung,c):
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

        c.execute ("""select * from userdaten """)

        userdaten=c.fetchall()

        for row in userdaten:
            if row[9]==session_key:
                c.execute ("""select * from %s """ % ("bestellt_"+row[11]))

                bestellt_daten=c.fetchall()

                for row_2 in bestellt_daten:
                    c.execute ("""select * from %s """ % (row_2[0]))

                    session_table=c.fetchall()

                    for row_3 in session_table:
                        
                        c.execute ("""select * from bewertungen """)

                        bewertungen_data=c.fetchall()
                        

                        for row_4 in bewertungen_data:

                            if row_4[6]==row[11]:


                                c.execute   ("""select * from lingerieselection where name='%s'""" % (row_3[0],))

                                lingerieselection_name=c.fetchall()

                                for row_5 in lingerieselection_name:

                                    pictures=row_5[2]
                                    pic=pictures.split(",")


                                    c.execute   ("""select * from %s where color='%s' and size='%s'""" % ("stylecode_"+row_5[11], row_3[4],row_3[2],))

                                    stylecode_daten=c.fetchall()


                                    for row_6 in stylecode_daten:

                                            freie_menge=min(int(row_6[4])-int(row_6[5]),10)
                                            
                                            if row_2[22]=="VIP":                                                  
                                                bestelldetails.append(Bestelldetails(row_3[0],row_3[1],row[18],freie_menge,row_3[4],row_3[6],row_2[20],row_4[3],row_4[4],row_4[5],pic[0],row_5[9],row_5[4],row_3[2],row_3[3],row_6[2],row_5[11],row_4[7],row_4[8],))
                                            else:
                                                bestelldetails.append(Bestelldetails(row_3[0],row_3[1],row[18],freie_menge,row_3[4],row_3[6],row_2[20],row_4[3],row_4[4],row_4[5],pic[0],row_5[9],row_5[3],row_3[2],row_3[3],row_6[2],row_5[11],row_4[7],row_4[8],))
                                                 
    else:
        c.execute ("""select * from userdaten """)

        userdaten=c.fetchall()
        for row in userdaten:
            
            if row[9]==session_key:
                
                c.execute ("""select * from %s """ % ("bestellt_"+row[11]))

                bestellt_daten=c.fetchall()

                for row_2 in bestellt_daten:
                    c.execute ("""select * from %s """ % (row_2[0]))

                    session_table=c.fetchall()
                    
                    for row_3 in session_table:
                        if bestellnummer==row_2[20]:
                            
                            if gerichtname !="":
                                
                                if row_3[0]==gerichtname:


                                    c.execute ("""select * from bewertungen """)

                                    bewertungen_daten=c.fetchall()

                    
        
                                    for row_4 in bewertungen_daten:
                                        if row_4[6]==row[11] and gerichtname==row_4[1]:


                                            c.execute ("""select * from lingerieselection """)

                                            lingerieselection_daten=c.fetchall()

                                            for row_5 in lingerieselection_daten:
                                                if row_5[0]==row_3[0]:



                                                    
                                                    bestelldetails.append(Bestelldetails(row_3[0],row_3[1],row[18],row_3[3],row_3[4],row_3[5],row_3[6],row_4[3],row_4[4],row_4[5],row_4[4],row_3[3],row_5[13],row_5[6],row_4[7],row_4[8],))
                            else:
                                if bewertung=="":
                                    c.execute ("""select * from bewertungen """)

                                    bewertungen_daten=c.fetchall()

                                    
                                    for row_4 in bewertungen_daten:

                                        
                                        if row_4[6]==row[11] and row_2[20]==row_4[0] and row_3[0]==row_4[1] and row_3[4]==row_4[2] and row_3[2]==row_4[9] and row_3[3]==row_4[10]:
                                            #print(row_4[6]+"=="+row[11] +"and"+ row_2[20]+"=="+row_4[0] +"and"+row_3[0]+"=="+row_4[1])
                                            c.execute ("""select * from lingerieselection """)

                                            lingerieselection_daten=c.fetchall()

                                            for row_5 in lingerieselection_daten:
                                                if row_5[0]==row_3[0]:
                                                    pictures=row_5[2]
                                                    pic=pictures.split(",")



                                                    c.execute ("""select * from %s """% ("stylecode_"+row_5[11]))

                                                    stylecode_daten=c.fetchall()
                                                    
                                                    freie_menge=10
                                                    for row_6 in stylecode_daten:
                                                        


                                                        if row_3[4]==row_6[2] and ((row_3[2]==row_6[3] and row_3[7]==row_6[1]) or (row_3[7]==row_6[1] and row_3[3]==row_6[3])):



                                                            if int(row_6[4])-int(row_6[5]) <freie_menge:
                                                                freie_menge=int(row_6[4])-int(row_6[5])
                                                    c.execute ("""select * from %s """% ("stylecode_"+row_5[11]))

                                                    stylecode_daten=c.fetchall()


                                                    for row_6 in stylecode_daten:

                                                        if row_3[4]==row_6[2] and row_3[2]==row_6[3] and row_3[7]==row_6[1] and row_3[7]==row_6[1] and row_3[2]==row_6[3]:



                                                            if row_2[22]=="VIP":                                                  
                                                                bestelldetails.append(Bestelldetails(row_3[0],row_3[1],row[18],freie_menge,row_3[4],row_3[6],row_2[20],row_4[3],row_4[4],row_4[5],pic[0],row_5[9],row_5[4],row_3[2],row_3[3],row_6[2],row_5[11],row_4[7],row_4[8],))

                                                            else:
                                                                bestelldetails.append(Bestelldetails(row_3[0],row_3[1],row[18],freie_menge,row_3[4],row_3[6],row_2[20],row_4[3],row_4[4],row_4[5],pic[0],row_5[9],row_5[3],row_3[2],row_3[3],row_6[2],row_5[11],row_4[7],row_4[8],))



                                else:

                                    c.execute ("""select * from bewertungen """)

                                    bewertungen_daten=c.fetchall()

                                
                                    
                                    for row_4 in bewertungen_daten:
                                        

                                        i=0
                                        status="ok"
                                        while i<=len(style_names)-1:

                                            if row_4[1]==style_names[i]:
                                                status="not"
                                            i=i+1
                                        
                                        if row_4[6]==row[11] and row_2[20]==row_4[0] and row_3[0]==row_4[1] and row_3[4]==row_4[2] and row_3[2]==row_4[9] and row_3[3]==row_4[10] and status=="ok":
                                            style_names.append(row_4[1])
                                            #print(row_4[6]+"=="+row[11] +"and"+ row_2[20]+"=="+row_4[0] +"and"+row_3[0]+"=="+row_4[1])
                                            c.execute ("""select * from lingerieselection """)

                                            lingerieselection_daten=c.fetchall()
                                            for row_5 in lingerieselection_daten:
                                                if row_5[0]==row_3[0]:
                                                    pictures=row_5[2]
                                                    pic=pictures.split(",")
                                                    
                                                    c.execute ("""select * from %s """% ("stylecode_"+row_5[11]))

                                                    stylecode_daten=c.fetchall()
                                                    for row_6 in stylecode_daten:
                                                        

                                                        if row_3[4]==row_6[2] and row_3[2]==row_6[3] and row_3[7]==row_6[1] and row_3[7]==row_6[1] and row_3[2]==row_6[3]:

                                                            freie_menge=min(int(row_6[4])-int(row_6[5]),10)

                                                            if row_2[22]=="VIP":                                                  
                                                                bestelldetails.append(Bestelldetails(row_3[0],row_3[1],row[18],freie_menge,row_3[4],row_3[6],row_2[20],row_4[3],row_4[4],row_4[5],pic[0],row_5[9],row_5[4],row_3[2],row_3[3],row_6[2],row_5[11],row_4[7],row_4[8],))

                                                            else:
                                                                bestelldetails.append(Bestelldetails(row_3[0],row_3[1],row[18],freie_menge,row_3[4],row_3[6],row_2[20],row_4[3],row_4[4],row_4[5],pic[0],row_5[9],row_5[3],row_3[2],row_3[3],row_6[2],row_5[11],row_4[7],row_4[8],))




    json_string = json.dumps([Bestelldetails.__dict__ for Bestelldetails in bestelldetails])


    return json_string



        

def define_ruecksendungen(session_key,c):
    ruecksendungen = []
    
    class Ruecksendungen(object):
        def __init__(self,style,anzahl,bestellnummer,picture_link_small,subtitle,preis,bhgroesse,slipgroesse,dateofproposal,dateofmaxreturn,deliverycode,grund,stylecode,colorcode,wareerhalten,status,id):
            self.style=style
            self.anzahl=anzahl
            self.bestellnummer=bestellnummer
            self.picture_link_small=picture_link_small
            self.subtitle=subtitle
            self.preis=preis
            self.bhgroesse=bhgroesse
            self.slipgroesse=slipgroesse
            self.dateofproposal=dateofproposal
            self.dateofmaxreturn=dateofmaxreturn
            self.deliverycode=deliverycode
            self.grund=grund
            self.stylecode=stylecode
            self.colorcode=colorcode
            self.wareerhalten=wareerhalten
            self.status=status
            self.id=id



    c.execute ("""select * from userdaten """)

    userdaten=c.fetchall()

    for row in userdaten:
        
        if row[9]==session_key:
            
            c.execute ("""select * from ruecksendungen """)

            ruecksendungen=c.fetchall()            

            for row_4 in ruecksendungen:

                if row_4[1]==row[11]:
                            
                    c.execute ("""select * from %s """ % ("bestellt_"+row[11]))

                    bestellt_data=c.fetchall()            

                    for row_2 in bestellt_data:
                        if row_2[20]==row_4[2]:

                            c.execute  ("""select * from %s """ % (row_2[0]))

                            data_table=c.fetchall()                             

                            for row_3 in data_table:

                                c.execute ("""select * from lingerieselection """)
                                for row_5 in c:

                                    if row_5[11]==row_3[7] and row_3[4] ==row_5[12] and row_3[2]==row_4[15] and row_3[3]==row_4[16]:
                                        
                                        pictures=row_5[2]
                                        pic=pictures.split(",")
  
                                        ruecksendungen.append(Ruecksendungen(row_3[0],row_4[9],row_4[2],pic[0],row_5[9],row_4[10],row_3[2],row_3[3],row_4[3],row_4[4],row_4[5],row_4[6],row_4[7],row_4[8],row_4[12],row_4[14],row_4[0],))

    json_string = json.dumps([Ruecksendungen.__dict__ for Ruecksendungen in ruecksendungen])


    return json_string






def define_sendungsverfolgung(session_key,bestellnummer,c):
    sendungsverfolgung = []
    
    class Sendungsverfolgung(object):
        def __init__(self,date,time,location,content,trackingcode,supplier):
            self.date=date
            self.time=time
            self.location=location
            self.content=content
            self.trackingcode=trackingcode
            self.supplier=supplier



    c.execute ("""select * from userdaten """)

    userdaten=c.fetchall()


    for row in userdaten:
        if row[9]==session_key:

            c.execute ("""select * from %s """ % ("bestellt_"+row[11]))

            bestellt_daten=c.fetchall()

            for row_2 in bestellt_daten:
                if row_2[20]==bestellnummer:
                    
                    c.execute ("""select * from %s """ % (row_2[0]))

                    daten_table=c.fetchall()
                    

                    for row_3 in daten_table:

                        c.execute ("""select * from %s """ % (row_2[0]+"_VF"))
                        for row_5 in c:

                            
                            #bestellt_224050260757_g6f5u10veqfgmqkdtkittcj7faha53s0
                            #bestellt_224050260757_g6f5u10veqfgmqkdtkittcj7faha53s0_VF
                            #bestellt_224050260757_g6f5u10veqfgmqkdtkittcj7faha53s0_VF

                            
                            sendungsverfolgung.append(Sendungsverfolgung(row_5[0],row_5[1],row_5[2],row_5[3],row_5[4],row_5[5],))

    json_string = json.dumps([Sendungsverfolgung.__dict__ for Sendungsverfolgung in sendungsverfolgung])


    return json_string



        

def define_bewertung(session_key,gutscheincode_id,c):
    bewertungen = []

    class Bewertung(object):
        def __init__(self,bestellnummer,style,bewertung,bewertungstext,bewertungsdatum,gutscheincode_id):
            self.bestellnummer=bestellnummer
            self.style=style
            self.bewertung=bewertung
            self.bewertungstext=bewertungstext
            self.bewertungsdatum=bewertungsdatum
            self.gutscheincode_id=gutscheincode_id            

    c.execute ("""select * from userdaten """)

    userdaten=c.fetchall()

    for row in userdaten:
        if row[9]==session_key:
            c.execute ("""select * from bewertungen """)
            for row_2 in c:
                if row_2[5]==gutscheincode_id:
                    bewertungen.append(Bewertungen(row_2[0],row_2[1],row_2[2],row_2[3],row_2[4],row_2[5],))


    json_string = json.dumps([Bewertungen.__dict__ for Bewertungen in bewertungen])


    return json_string






    



def define_bestellung(session_key,bestellnummer,c):
    bestellung = []
    class Bestellung(object):
        def __init__(self,sessionidtablename,adresse,stadt,plz,unternehmensdetails,vorname,nachname,telefonnummer,lieferdetails,zahlungsoption,namekarteninhaber,kartennummer,ablaufdatum,pruefnummer,bestellungspreis,lieferkosten,rabatt,rabattcode,datum,uhrzeit,bestellnummer,creditused,status,braforfreevalue,storecredit,braforfreecount,liefertermin):
            self.sessionidtablename=sessionidtablename
            self.adresse=adresse
            self.stadt=stadt
            self.plz=plz
            self.unternehmensdetails=unternehmensdetails
            self.vorname=vorname
            self.nachname=nachname
            self.telefonnummer=telefonnummer
            self.lieferdetails=lieferdetails
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





    


#8L0OXE39

    c.execute ("""select * from userdaten """)

    userdaten=c.fetchall()
    

    for row in userdaten:
        if row[9]==session_key:

            c.execute ("""select * from %s ORDER BY idforsorting DESC""" % ("bestellt_"+row[11]))
            for row_2 in c:

                if row_2[20]==bestellnummer or bestellnummer=="all":
                    try:
                        kartennummer_kurz=row_2[11]
                        kartennummer_kurz=kartennummer_kurz[15:]
                    except:
                        kartennummer_kurz=""
                        
                    bestellung.append(Bestellung(row_2[0],row_2[1],row_2[2],row_2[3],row_2[4],row_2[5],row_2[6],row_2[7],row_2[8],row_2[9],row_2[10],kartennummer_kurz,row_2[11],row_2[13],row_2[14],row_2[15],row_2[16],row_2[17],row_2[18],row_2[19],row_2[20],row_2[21],row_2[23],row_2[26],row_2[27],row_2[25],row_2[28],))


    json_string = json.dumps([Bestellung.__dict__ for Bestellung in bestellung])


    return json_string




def define_zahlungsmethoden(session_key,c):
    zahlungsmethoden = []
    class Zahlungsmethoden(object):
        def __init__(self,email,indexnummer,zahlungsoption,name,kreditkartennummer,ablaufmonat,ablaufjahr,standard,cardtype):
            self.email=email
            self.indexnummer=indexnummer
            self.zahlungsoption=zahlungsoption
            self.name=name
            self.kreditkartennummer=kreditkartennummer
            self.ablaufmonat=ablaufmonat
            self.ablaufjahr=ablaufjahr
            self.standard=standard
            self.cardtype=cardtype
            

    c.execute ("""select * from userdaten """)

    userdaten=c.fetchall()
    

    for row in userdaten:
        if row[9]==session_key:
            c.execute ("""select * from %s """ % (row[17]))
            for row_2 in c:
                print("zahlungsmethoden:")
                print(row_2[0])
                kredikartennummer=row_2[4]
                Monat_kurz = ["01", "02", "03", "04","05", "06", "07", "08", "09", "10", "11", "12"]
                zahlungsmethoden.append(Zahlungsmethoden(row_2[0],row_2[1],row_2[2],row_2[3],kredikartennummer,Monat_kurz[int(row_2[5])-1],row_2[6],row_2[8],row_2[9]))


    json_string = json.dumps([Zahlungsmethoden.__dict__ for Zahlungsmethoden in zahlungsmethoden])


    return json_string




def define_adressbuch(session_key,c):
    adressbuch = []
    class Adressbuch(object):
        def __init__(self,email,indexnummer,vorname,nachname,telefonnummer,adresse,apt,unternehmensdetails,stadt,plz,lieferhinweise,standard):
            self.email=email
            self.indexnummer=indexnummer
            self.vorname=vorname
            self.nachname=nachname
            self.telefonnummer=telefonnummer
            self.adresse=adresse
            self.apt=apt
            self.unternehmensdetails=unternehmensdetails
            self.stadt=stadt
            self.plz=plz
            self.lieferhinweise=lieferhinweise
            self.standard=standard           


    c.execute ("""select * from userdaten """)

    userdaten=c.fetchall()



    for row in userdaten:
        if row[9]==session_key:
            c.execute ("""select * from %s """ % (row[16]))
            for row_2 in c:
                adressbuch.append(Adressbuch(row_2[0],row_2[1],row_2[2],row_2[3],row_2[4],row_2[5],row_2[6],row_2[7],row_2[8],row_2[9],row_2[10],row_2[11]))


    json_string = json.dumps([Adressbuch.__dict__ for Adressbuch in adressbuch])


    return json_string





    
    
                



def define_profil(session_key,c):
    profil = []
    class Profil(object):
        def __init__(self,email,vorname,nachname,lastplz,telefon,lastsessionid,credit,gutscheincode,facebookid,passwordcheck,persmsbenachrichtigtwerden,newsletter):
            self.email=email
            self.vorname=vorname
            self.nachname=nachname
            self.lastplz=lastplz
            self.telefon=telefon
            self.lastsessionid=lastsessionid
            self.credit=credit
            self.gutscheincode=gutscheincode
            self.facebookid=facebookid
            self.passwordcheck=passwordcheck
            self.persmsbenachrichtigtwerden=persmsbenachrichtigtwerden
            self.newsletter=newsletter  




    c.execute ("""select * from userdaten """)
    password="ok"
    for row in c:
        if row[9]==session_key:
            password="ok"
            if row[1]=="":
                password="not ok"

            profil.append(Profil(row[0],row[2],row[3],row[5],row[8],row[9],row[10],row[11],row[12],password,row[20],row[49],))


    json_string = json.dumps([Profil.__dict__ for Profil in profil])


    return json_string



@csrf_exempt
def kollektion_abrufen(request):
    if request.is_ajax() and request.GET:
        group=request.GET.get('group')
        link=request.GET.get('link')
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')

        c = conn.cursor(buffered=True)
        if link=="Mein Showroom":
            page=link_name_bestimmen("no",c)
        else:
            page=link_name_bestimmen(group,c)
            
        
        
    return HttpResponse(json.dumps(page), content_type='application/json')







def define_lingerie(datum,name,name_list):
    gerichte = []
    
    
    class Gericht(object):
        def __init__(self, name,picture_link_super_large,picture_link_large,picture_link_medium,picture_link_small,preis,vegan,vegetarian,glutenfree,dairyfree,nutfree,eggfree,subtitle,bewertung,beschreibung,vorbereitung,ofen,mikrowelle,servieren,ingredientlinktodb,kalorien,protein,kohlenhydrate,kohlenhydratezucker,kohlenhydrateballaststoffe,fett,fettungesaettigt,fettgesaettigt,artdesgerichtes,namekoch,datum,gerichte_uebrig,warenkorb_menge,ingredients):
            self.name=name
            self.picture_link_super_large=picture_link_super_large
            self.picture_link_large=picture_link_large
            self.picture_link_medium=picture_link_medium
            self.picture_link_small=picture_link_small
            self.preis=preis
            self.vegan=vegan
            self.vegetarian=vegetarian
            self.glutenfree=glutenfree
            self.dairyfree=dairyfree
            self.nutfree=nutfree
            self.eggfree=eggfree
            self.subtitle=subtitle
            self.bewertung=bewertung

            self.datum=datum
            self.gerichte_uebrig=gerichte_uebrig
            self.warenkorb_menge=warenkorb_menge
            self.ingredients=ingredients   
            

    u=0

    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                            password='okano1988',database='maxfischer2database')

    c = conn.cursor(buffered=True)

    conn_2 = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                            password='okano1988',database='maxfischer2database')

    q = conn_2.cursor()

    conn_3 = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                            password='okano1988',database='maxfischer2database')

    l = conn_3.cursor()



#define_gerichte(ausgewaehlten_tag_abrufen(auswahl_tag),"all","")
#(datum,name,name_list):

    max_var_gerichtauswahl=29
    k=0
    while k<=len(datum)-1:

        q.execute ("""select * from menu""")
        for row_2 in q:
            if name_list=="":
                if row_2[2]==datum[k]:
                    c.execute ("""select * from gerichtauswahl""")
                    for row in c:

                        l.execute ("""select * from ingredientlist""")
                        ingredients=""
                        for row_3 in l:
                            if name==str(row_3[0]) and name !="":
                                ingredients=ingredients+str(row_3[1])

                                        
                        if (row_2[1] == row[1] and name=="all"):
                            
                            menge=min(row_2[3]-row_2[4]-row_2[5],21)

     
                            gerichte.append(Gericht(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21],row[22],row[23],row[24],row[25],row[26],row[27],row[28],row[29],row[30],row_2[2],menge,0,ingredients))
                        else:
                            if (row_2[1] == row[1] and name==row[1] and name!="" and name!="all"):
                                menge=min(row_2[3]-row_2[4]-row_2[5],21)
    
                                gerichte.append(Gericht(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21],row[22],row[23],row[24],row[25],row[26],row[27],row[28],row[29],row[30],row_2[2],menge,0,ingredients))
            else:
                t=0
                while t<=len(name_list)-1:
                    if row_2[2]==datum[k] and row_2[1]==name_list[t]:
                        c.execute ("""select * from gerichtauswahl""")
                        for row in c:

                            l.execute ("""select * from ingredientlist""")
                            ingredients=""
                            for row_3 in l:
                                if name_list[t]==str(row_3[0]):
                                    ingredients=ingredients+str(row_3[1])

                                            
                            if row_2[1] == row[1]:
                                
                                
                                
                                menge=min(row_2[3]-row_2[4]-row_2[5],21)

                                
                                gerichte.append(Gericht(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21],row[22],row[23],row[24],row[25],row[26],row[27],row[28],row[29],row[30],row_2[2],menge,0,ingredients))
                    t=t+1
        k=k+1








    json_string = json.dumps([Gericht.__dict__ for Gericht in gerichte])






    return json_string

        
        
        

class Me(object):
    def __init__(self):
        self.name = 1
        self.nachname = 2




def freunde_einladen(request,offset):

    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                            password='okano1988',database='maxfischer2database')
    c = conn.cursor(buffered=True)

    request.session.create()
    x=str(request.session.session_key)
    create_user(x,c,conn)    




    

    gutschein_einloesen_do_it(x,offset,"einloesen",c,conn)
            



    return HttpResponseRedirect("/hello/start_page/")

        
        

    

    


def referral_email(code,empfaenger,betreff,message,von):
    # me == my email address
    # you == recipient's email address
    me = "max.fischer2@gmail.com"
    you = empfaenger

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = betreff
    msg['From'] = von
    msg['To'] = empfaenger

    # Create the body of the message (a plain-text and an HTML version).
    text = "WIllkommen zu Sensuals"
    print(betreff)
    html = """<html><head></head><body style="font-family:Helvetica;font-size:16px;">"""
    html=html+"""<div style='background-color:#404040;width:100%;height:50px'>"""
    html=html+"""<div style='width:20%;margin: 0 auto;float:center;text-align: center;line-height:50px;'>"""

    html=html+"""<a href='http://maxfischer2.pythonanywhere.com/hello/start_page/' style='text-decoration:none !important; text-decoration:none;color:#ffffff;'><div style='height:50px;cursor:pointer;background: url("http://maxfischer2.pythonanywhere.com/static/sensuals.png");background-size: 150px 30px;background-position: center center; background-repeat:   no-repeat;'  ></div></a></div>"""
    html=html+"""</div><br>"""
    html=html+"""Dein Freund """+von+""" nutzt Sensuals und moechte dich dorthin einladen.<br><br>Sensuals bietet dir die neusten Dessous Trends in hoher Qualitaet zu attraktiven Preisen. Dazu bieten wir Dir einen persoenlichen Showroom, der dir auf Basis eines Fitting Quizes dir die passenden BHs fuer dich zeigt!<br><br>Klicke hier fuer deinen persoenlichen Gutschein von 15 EUR: <br><br><div style='margin: 0 auto;background-color:#DB7093;color:#FFFFFF;font-weight:bold;border-radius: 5px;text-align:center;cursor:pointer;width:250px;height:30px;line-height:30px;' ><a href='http://maxfischer2.pythonanywhere.com/hello/einladung/"""+code+"""' style='text-decoration:none !important; text-decoration:none;color:#ffffff;'>Deinen Gutschein abrufen</a></div>"""
    html=html+"""<br><br><br>Persoenliche Nachricht von """+von+""":<br><br>"""+message
    html=html+"""<script>function logo_click(){ alert("ASD");window.location.href='http://maxfischer2.pythonanywhere.com/hello/einladung/';}"""
    html=html+"""function open_link(){ window.location.href='http://maxfischer2.pythonanywhere.com/hello/einladung/';}"""
    html=html+"""</script></body></html>"""

#http://maxfischer2.pythonanywhere.com/hello/einladung/
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
    mail = smtplib.SMTP_SSL('smtp.gmail.com:465')

    mail.ehlo()



    mail.login('max.fischer2', '')
    mail.sendmail(me, you, msg.as_string())
    mail.close()



        

@csrf_exempt
def facebook_login(request):

    if request.is_ajax() and request.POST:
        
        vorname=request.POST.get('vorname')
        id_=request.POST.get('id')
        nachname=request.POST.get('nachname')
        email=request.POST.get('email')
        min_alter=request.POST.get('min_alter')
        max_alter=request.POST.get('max_alter')
        geschlecht=request.POST.get('geschlecht')
        
        

        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)

        x=str(request.session.session_key)



        c.execute ("""select * from userdaten """)
        feedback=""
        gutscheine=""
        status=1
        user_existiert="nein"
        id_existiert="nein"

        c.execute ("""select * from userdaten """)

        userdaten=c.fetchall()        
        for row in userdaten:

            if row[0]==str(email):
                user_existiert="ja"

            if row[9]==x and x!="None":
                gutscheincode_old=row[11]              
            print(row[12]+"=="+id_ +"or "+row[0]+"=="+str(email))
            if row[12]==id_:
                id_existiert="ja"


        if id_existiert=="ja" and user_existiert=="nein":
                
            c.execute("""delete from userdaten where lastsessionid=%s""",(x,))
            
                                
            c.execute("""update userdaten set lastsessionid=%s, vorname=%s,nachname=%s,email=%s,minalter=%s,maxalter=%s,geschlecht=%s where facebookid=%s""",(x,str(vorname),str(nachname),str(email),str(min_alter),str(max_alter),str(geschlecht),str(id_),))
            gutscheincode=row[11]

            conn.commit()
            feedback="ok"
            status=0
        else:
            if (id_existiert=="nein" and user_existiert=="ja") or (id_existiert=="ja" and user_existiert=="ja"):            
                c.execute("""delete from userdaten where lastsessionid=%s""",(x,))
                
                                    
                c.execute("""update userdaten set lastsessionid=%s, vorname=%s,nachname=%s,facebookid=%s,minalter=%s,maxalter=%s,geschlecht=%s where email=%s""",(x,str(vorname),str(nachname),str(id_),str(min_alter),str(max_alter),str(geschlecht),str(email),))
                gutscheincode=row[11]

                conn.commit()
                feedback="ok"
                status=0
        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        Monat = ["Januar", "Februar", "Maerz", "April","Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
        now_date=str(now.day)+". "+str(Monat[now.month-1])+" "+str(now.year)



        


            
            

        



        a=get_time_stamp_now()

            
        if status==1:

            c.execute("""update userdaten set vorname=%s,facebookid=%s,nachname=%s,email=%s,minalter=%s,maxalter=%s,geschlecht=%s where lastsessionid=%s""",(str(vorname),str(id_),str(nachname),str(email),str(min_alter),str(max_alter),str(geschlecht),x,))

            c.execute("""insert into aktuellewarenkoerbe values (%s,%s,%s)""" ,(x,a.strftime('%Y-%m-%d %H:%M'),gutscheincode_old,))
            conn.commit()
            feedback="ok"
        if status==0:


            c.execute ("""select * from aktuellewarenkoerbe """)
            status_=0
            for row_3 in c:

                if row_3[2]==gutscheincode:
                    status_=1
                    x_old=row_3[0]


            
            if status_==0:                        
                c.execute("""insert into aktuellewarenkoerbe values (%s,%s,%s)""" ,(x,a.strftime('%Y-%m-%d %H:%M'),gutscheincode,))
                conn.commit()
            else:
                
                c.execute("""update aktuellewarenkoerbe set tablename=%s where gutscheincodeid=%s""",(x,row[11],))
                conn.commit()

                c.execute ("""select * from %s """ %(x_old))

                cart_old=c.fetchall()

                for row_4 in cart_old:
                    eingefuegt="no"



                    c.execute ("""select * from %s """ %(x))

                    cart_new=c.fetchall()

                    for row_5 in cart_new:
                        if row_4[2]==row_5[2] and row_4[3]==row_5[3] and row_4[4]==row_5[4] and row_4[7]==row_5[7]:
                            c.execute("""update %s set anzahl=%%s where bhgroesse=%%s and slipgroesse=%%s and color=%%s and stylecode=%%s"""%(x),(row_4[1],row_4[2],row_4[3],row_4[4],row_4[7],))
                            eingefuegt="yes"

                    if eingefuegt=="no":
                        c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" %(x),(row_4[0],int(row_4[1]),row_4[2],row_4[3],row_4[4],int(row_4[5]),row_4[6],row_4[7],))
                conn.commit()




                c.execute ("""select * from %s """%("wishlist_"+gutscheincode_old))

                wishlist_old=c.fetchall()

                for row_3 in wishlist_old:
                    eingefuegt="no"


                    c.execute ("""select * from %s """%("wishlist_"+gutscheincode))

                    wishlist_new=c.fetchall()                    

                    for row_5 in wishlist_new:
                        if row_5[0]==row_3[0]:
                            eingefuegt="yes"
                            
                    if eingefuegt=="no":
                        c.execute("""insert into %s values (%%s,%%s)""" %("wishlist_"+gutscheincode),(row_4[0],row_4[1],))
                        conn.commit()

                            

            feedback="ok"

        return HttpResponse(json.dumps(feedback), content_type='application/json')
    else:
        raise Http404



            
                

    
    



def gutscheinkonto(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                            password='okano1988',database='maxfischer2database')
    c = conn.cursor(buffered=True)


    x=str(request.session.session_key)

#    c.execute("""insert into gutscheinkonto values (%s,%s,%s,%s,%s)""" ,("max.fischer2@gmail.com","20","Janet"," ","19. Oktober 2016",))
 #   conn.commit()

    #c.execute("""update userdaten set credit=%s where lastsessionid=%s""" ,("40.1",x,))
    #conn.commit()





    #q.execute ("""select * from gutscheinkonto """)
    gutscheine=define_gutscheinkonto(x)


    profildaten=define_profil(x,c)
    if profildaten!="":
        login="true"
        status=1
        try:
            c.execute ("""select * from %s""" % (x))

            cart_gesamt=0
            for row_2 in c:
                cart_gesamt=cart_gesamt+row_2[1]
        except:
            status=0


        
    else:
        login=""
        status=0
                    


                    
            

    update_timestamp(x,c,conn)               
    t=get_template('gutscheinkonto.html')
    html=t.render({'favicon':get_favicon(),'brand_name':'Sensuals','title':"Gutscheinkonto | Sensuals",'bestellungen':define_bestellung(x,"all",c),'wishlist':define_wishlist(x,modelAB,sub_picture,c),'warenkorb':define_warenkorb(x,modelAB,sub_picture,c),'gutscheine':gutscheine,'login':'true','cart_gesamt':cart_gesamt})

    if status==1:
        return HttpResponse(html)
    else:
        return HttpResponseRedirect("/hello/start_page/")



def link_group_bestimmen(name,c):
    c.execute ("""select * from links """)
    for row in c:
        if row[1]==name:
            return row[2]


def link_name_bestimmen(group,c):
    print("link")
    c.execute ("""select * from links """)
    for row in c:
        print(row[2])
        print(group)
        if row[2]==group:
            return row[1]





@csrf_exempt
def filter_abrufen(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)
        
        group1=request.GET.get('group1')
        filter_style=request.GET.get('filter_style')
        filter_color=request.GET.get('filter_color')
        filter_size=request.GET.get('filter_size')
        filter_padding=request.GET.get('filter_padding')
        filter_feature=request.GET.get('filter_feature')
        link=request.GET.get('group1')
        
        x=str(request.session.session_key)
        
        c.execute ("""select * from userdaten """)
        for row in c:
            if row[9]==x and x!="None":
                user=row[11]
                day=row[43]
                month=row[44]
                year=row[45]
		filter=load_style_filter(filter_style,filter_color,filter_feature,filter_size,"",filter_padding,link,user,day,month,year,c)



        return HttpResponse(filter, content_type='application/json')
    else:
        raise Http404






@csrf_exempt
def content_abrufen(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)

        name=request.GET.get('name')
        group1=request.GET.get('group1')
        group2=request.GET.get('group2')
        group3=request.GET.get('group3')




        filter_style=request.GET.get('filter_style')
        filter_color=request.GET.get('filter_color')
        filter_size=request.GET.get('filter_size')
        filter_padding=request.GET.get('filter_padding')
        filter_feature=request.GET.get('filter_feature')

                     
        color=request.GET.get('color')
        size=request.GET.get('size')

        if name!="":
            group1=link_group_bestimmen(name,c)

        
        x=str(request.session.session_key)
        c.execute ("""select * from userdaten """)
        for row in c:
            if row[9]==x and x!="None":
                user=row[11]
                modelAB=row[47]
                sub_picture=row[48]
                day=row[43]
                month=row[44]
                year=row[45]
                


        return HttpResponse(json.dumps(get_lingerie_selection_filter(group1,group2,group3,color,size,user,"",day,month,year,filter_style,filter_color,filter_feature,filter_padding,filter_size,modelAB,sub_picture,c)), content_type='application/json')
    else:
        raise Http404





@csrf_exempt
def bewertung_speichern(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                            password='okano1988',database='maxfischer2database')
    c = conn.cursor(buffered=True)
    if request.is_ajax() and request.POST:
        


        passform=request.POST.get('passform') 

        bewertung=request.POST.get('bewertung')

        bewertungsheadline=request.POST.get('bewertungsheadline') 

        bewertungstext=request.POST.get('bewertungstext')           


        style=request.POST.get('style')
        stylecode=request.POST.get('stylecode')
        color=request.POST.get('color')
        bestellnummer=request.POST.get('bestellnummer')
        gutscheincodeid=request.POST.get('gutscheincodeid')

                  

        c.execute ("""select * from userdaten """)
        x=str(request.session.session_key)
        status=0
        for row in c:
            if row[9]==x and x!="None":
                namebewerter=row[2][2:]+" "+row[3]
                gutscheincodeid=row[11]



            
            

        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))

        Monat = ["Januar", "Februar", "Maerz", "April","Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
        date=str(now.day)+". "+Monat[(now.month)-1]+" "+str(now.year)





        c.execute("""update bewertungen set bewertungstext=%s, bewertungsheadline=%s, bewertung=%s, passform=%s, bewertungsdatum=%s where bestellnummer=%s and style=%s and color=%s""",(bewertungstext,bewertungsheadline,bewertung,passform,date,bestellnummer,style,color,))
        c.execute("""update %s set bewertungstext=%%s, bewertungsheadline=%%s, bewertung=%%s, passform=%%s, bewertungsdatum=%%s where bestellnummer=%%s and gutscheincodeid=%%s""" % ("bewertungen_"+stylecode+"_"+color),(bewertungstext,bewertungsheadline,bewertung,passform,date,bestellnummer,gutscheincodeid,))
        conn.commit()





        






    
        update_timestamp(x,c,conn)

        return HttpResponse(json.dumps(""), content_type='application/json')
    else:
        raise Http404



    

def bewertung_abgeben(request,offset,offset_2):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                            password='okano1988',database='maxfischer2database')
    c = conn.cursor(buffered=True)

    x=str(request.session.session_key)



    bestellungen=define_bestellung(x,"all",c)
    bestelldetails=define_bestelldetails(x,offset,offset_2,c)
    profildaten=define_profil(x,c)
    if profildaten!="":
        login="true"
        status=1
        try:
            c.execute ("""select * from %s""" % (x))

            cart_gesamt=0
            for row_2 in c:
                cart_gesamt=cart_gesamt+row_2[1]
        except:
            status=0


        
    else:
        login=""
        status=0
                    

    update_timestamp(x,c,conn)
    if status==1:
               
        t=get_template('bewertung_abgeben.html')
        html=t.render({'favicon':get_favicon(),'brand_name':'Sensuals','title':"Bewertung abgeben | Sensuals",'bestellungen':bestellungen,'bestelldetails':bestelldetails,'login':login,'cart_gesamt':cart_gesamt})
        return HttpResponse(html)

    else:
        return HttpResponseRedirect("/hello/start_page/")
    


def bewertungen_bearbeiten(request,offset):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                            password='okano1988',database='maxfischer2database')
    c = conn.cursor(buffered=True)



    x=str(request.session.session_key)




    bestellungen=define_bestellung(x,"all",c)
    bestelldetails=define_bestelldetails(x,offset,"","yes",c)
    profildaten=define_profil(x,c)


    c.execute ("""select * from userdaten """)
    for row in c:
        if row[9]==x and x!="None":
            modelAB=row[47]
            sub_picture=row[48]

                
    if profildaten!="":
        login="true"
        status=1
        try:
            c.execute ("""select * from %s""" % (x))

            cart_gesamt=0
            for row_2 in c:
                cart_gesamt=cart_gesamt+row_2[1]
        except:
            status=0


        
    else:
        login=""
        status=0

    update_timestamp(x,c,conn)        
    if status==1:
        t=get_template('bewertungen_ansehen.html')
        html=t.render({'favicon':get_favicon(),'brand_name':'Sensuals','title':"Bewertungen | Sensuals",'links':get_links(x,c),'wishlist':define_wishlist(x,modelAB,sub_picture,c),'warenkorb':define_warenkorb(x,modelAB,sub_picture,c),'bestellungen':bestellungen,'bestelldetails':bestelldetails,'login':login,'cart_gesamt':cart_gesamt})

        return HttpResponse(html)
    else:
        return HttpResponseRedirect("/hello/start_page/")



def table_bestelldetails(session_key,bestellnummer,c):


    c.execute ("""select * from userdaten """)

    userdaten=c.fetchall()

    for row_2 in userdaten:

        if row_2[9]==session_key:
            
            c.execute ("""select * from %s""" % ("bestellt_"+row_2[11]))
            for row in c:

                if row[20]==bestellnummer:
                    return row[0]


def table_bestelldetails_datum(table,c):


    c.execute ("""select * from %s """ % (table))
    datum=[]
    datum_=""
    for row_2 in c:
        if datum_!=row_2[2]:
            datum.append(row_2[2])
            datum_=row_2[2]
    return datum


def table_bestelldetails_namen(table,c):


    c.execute ("""select * from %s """ % (table))
    name=[]
    name_=""
    for row_2 in c:
        if name_!=row_2[0]:
            name.append(row_2[0])
            name_=row_2[0]
    return name


def bestellungen_details_ansehen(request,offset):

    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                            password='okano1988',database='maxfischer2database')
    c = conn.cursor(buffered=True)
    


    

    x=str(request.session.session_key)




    status=0

    bestellung=define_bestellung(x,offset,c)
    bestelldetails=define_bestelldetails(x,offset,"","",c)
    
    o=table_bestelldetails(x,offset,c)

    datum=table_bestelldetails_datum(o,c)

    namen=table_bestelldetails_namen(o,c)


    lingerie=get_lingerie_sizes("","","","","","","",namen,c)

    
    c.execute ("""select * from userdaten """)
    status=0
    login=""
    for row in c:
        if row[9]==x and x!="None":
            if (row[0]!="" and row[12]!="") or (row[0]!="" and row[1]!=""):
                login="true"
                modelAB=row[47]
                sub_picture=row[48]


                

    status=1
    try:
        c.execute ("""select * from %s""" % (x))

        cart_gesamt=0
        for row_2 in c:
            cart_gesamt=cart_gesamt+row_2[1]
    except:
        status=0

        
    t=get_template('order_summary.html')

            




    
    

    


    if status==1:
#        try:
        html=t.render({'favicon':get_favicon(),'brand_name':'Sensuals','title':"Bestellung Zusammenfassung | Sensuals",'rebates':define_rebates(x,offset,"","","",c,conn),'links':get_links(x,c),'wishlist':define_wishlist(x,modelAB,sub_picture,c),'warenkorb':define_warenkorb(x,modelAB,sub_picture,c),'lingerieselection':lingerie,'bestellung':bestellung, 'bestelldetails':bestelldetails,'login':login,'cart_gesamt':cart_gesamt})
        update_timestamp(x,c,conn)

        return HttpResponse(html)
#        except:
        return HttpResponseRedirect("/hello/account_page/")
            
    else:
        return HttpResponseRedirect("/hello/start_page/")


@csrf_exempt
def datum_abrufen_array(x):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                            password='okano1988',database='maxfischer2database')
    c = conn.cursor(buffered=True)

    c.execute ("""select * from %s""" % (x))

    b=""
    max_var_warenkorb =7
    datum=[]
    datum_=""
    h=0
    for row in c:
        j=0
        if (h != 0):
            b=b+";"
        if row[2]!=datum_:
            datum.append(row[2])
            datum_=row[2]
        while(j<=max_var_warenkorb):
            if (j==max_var_warenkorb):
                b=b+str(row[j])
            else:
                b=b+str(row[j])+","
            j=j+1
        h=h+1
    return datum



@csrf_exempt
def groessentabelle_uebersicht(request):
    if request.is_ajax() and request.GET:
       # print("asd")
  
        list = [[] for i in range(55)]
        
        i=0
        while(i<=9):

            
            j=0
            while(j<=4):
                #print(i*5+j)
                list[i*5+j].append(i*5+j+63)
                list[i*5+j].append(i*5+75)
                list[i*5+j].append(i*5+99)
                
                j=j+1
                
            i=i+1



#        print(list)
        return HttpResponse(json.dumps(list), content_type='application/json')
    else:
        raise Http404


@csrf_exempt
def groessentabelle_detailliert(request):
    if request.is_ajax() and request.GET:


        list = [[[] for i in range(49)] for j in range(49)]


        get_cup = {0 : 'AA',
                   1 : 'A',
                   2 : 'B',
                   3 : 'C',
                   4 : 'D',
                   5 : 'E',
                   6 : 'F',
                   7 : 'G',
                   8 : 'H',
                   9 : 'I',
                   10: 'J',
                   11: 'K',
                   12:'K'

                   
                }


        get_bralette = {'65A' : 'XS',
                        '65B' : 'XS',
                        '65C' : 'XS',
                        '70A' : 'XS',
                        '70B' : 'XS',
                        '65D' : 'S',
                        '65E' : 'S',


                        '70C' : 'S',
                        '70D' : 'S',
                        '75A' : 'S',
                        '75B' : 'S',

                        '75C' : 'M',
                        '75D' : 'M',
                        '80A' : 'M',
                        '80B' : 'M',
                        '80C' : 'L',
                        '80D' : 'L',

                        '85A' : 'L',
                        '85B' : 'L',
                        '85C' : 'L',
                        '85D' : 'L',
                        

                        '90B' : 'XL',
                        '90C' : 'XL',
                        '90D' : 'XL'


                   
                } 
        i=0
        zaehler_1=0
        zaehler_2=0

        unterbrust=65
        
        while(i<=48):
            if zaehler_1>4:
                unterbrust=unterbrust+5
                zaehler_1=0
                
            zaehler_1=zaehler_1+1

            
            j=0
            cup=0
            zaehler_2=0
            cup_detail=get_cup[cup]
            while(j<=24):
                if zaehler_2>1:
                    cup=cup+1
                    cup_detail=get_cup[cup]
                    zaehler_2=0

                zaehler_2=zaehler_2+1
                
 #               print(str(unterbrust)+cup_detail)
                list[i][0].append(str(unterbrust)+cup_detail)
                try:
                    bralette_detail=get_bralette[str(unterbrust)+cup_detail]

                    list[i][1].append(bralette_detail)
                except:
                    list[i][1].append("")
                    
                
                j=j+1
                
            i=i+1



#        print(list)
        return HttpResponse(json.dumps(list), content_type='application/json')
    else:
        raise Http404








    

@csrf_exempt
def bestellung_abrufen(request):
    if request.is_ajax() and request.POST:
        bestellnummer=request.POST.get('bestellnummer')
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)
        x=str(request.session.session_key)
        
        bestellung=define_bestellung(x,bestellnummer,c)

        return HttpResponse(json.dumps(bestellung), content_type='application/json')
    else:
        raise Http404

@csrf_exempt
def bestelldetails_abrufen(request):
    if request.is_ajax() and request.POST:
        bestellnummer=request.POST.get('bestellnummer') 
        x=str(request.session.session_key)


        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)
        
        bestelldetails=define_bestelldetails(x,bestellnummer,"","",c)

        return HttpResponse(json.dumps(bestelldetails), content_type='application/json')
    else:
        raise Http404


    








def bestellungen_ansehen(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                            password='okano1988',database='maxfischer2database')
    c = conn.cursor(buffered=True)


    c.execute ("""select * from userdaten """)

    userdaten=c.fetchall()
    

    x=str(request.session.session_key)
    status=0
    login=""
    password="ok" 
    for row in userdaten:
        if row[9]==x and (row[12]!="" or row[0]!=""):
            modelAB=row[47]
            sub_picture=row[48]

            if row[1]=="":
                password="not ok"
            if (row[0]!="" and row[12]!="") or (row[0]!="" and row[1]!=""):
                login="true"

            bestellungen=define_bestellung(x,"all",c)

            bestelldetails=define_bestelldetails(x,"","","",c)

            profildaten=define_profil(x,c)

            
            status=1
            try:
                c.execute ("""select * from %s""" % (x))

                cart_gesamt=0
                for row_2 in c:
                    cart_gesamt=cart_gesamt+row_2[1]
            except:
                status=0

                  
    if len(bestellungen)==2:
        status=2
    update_timestamp(x,c,conn)
    if status==1:
        t=get_template('bestellungen_ansehen.html')
        html=t.render({'favicon':get_favicon(),'brand_name':'Sensuals','title':"Bestellungen | Sensuals",'links':get_links(x,c),'wishlist':define_wishlist(x,modelAB,sub_picture,c),'warenkorb':define_warenkorb(x,modelAB,sub_picture,c),'bestellungen':bestellungen,'bestelldetails':bestelldetails,'login':login,'cart_gesamt':cart_gesamt,'password':password})
        return HttpResponse(html)
    else:
        if status==0:
            return HttpResponseRedirect("/hello/start_page/")
        else:
            if status==2:
                return HttpResponseRedirect("/hello/account_page/")        
    

            

			
			
			
def credit_card_add_new_payment(token_id,client_id_):
    paymill_context = paymill.PaymillContext('5ccd454aa30b1614e44193f740762a52')
    payment_service = paymill_context.get_payment_service()
    payment_with_token_and_client = payment_service.create(
        token=token_id,
        client_id=client_id_
    )


    return "true"
	
	


@csrf_exempt
def zahlungsmethode_speichern_test(request):
    if request.is_ajax() and request.POST:
        
        hinzufuegen=request.POST.get('hinzufuegen')        


        indexnummer=request.POST.get('indexnummer')
        standard=request.POST.get('standard')
        card_type=request.POST.get('card_type')
        token=request.POST.get('token')




        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)



        print("test2")
		
        c.execute ("""select * from userdaten """)

        userdaten=c.fetchall()   

        x=str(request.session.session_key)
        status=0
        existiert="nein"        
        for row in userdaten:
            if row[9]==x and x!="None":
               print(credit_card_add_new_payment_test(token,row[50]))


        return HttpResponse(json.dumps("asd"), content_type='application/json')
    else:
        raise Http404			   

			
		
		
@csrf_exempt
def zahlungsmethode_speichern(request):
    if request.is_ajax() and request.POST:
        print("ASD")
		
        hinzufuegen=request.POST.get('hinzufuegen')        


        indexnummer=request.POST.get('indexnummer')
        standard=request.POST.get('standard')
        card_type=request.POST.get('card_type')
        token=request.POST.get('token')      
        zahlungsoption=request.POST.get('zahlungsoption')      

        
        
        print("grosss")
        print(standard)        
        

        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)





        c.execute ("""select * from userdaten """)

        userdaten=c.fetchall()   

        x=str(request.session.session_key)
        status=0
        existiert="nein"        
        print(hinzufuegen)  
        for row in userdaten:
            if row[9]==x and x!="None":
                if hinzufuegen=="1":
                    print(row[50])				
                    credit_card_add_new_payment_test(token,row[50])

                    print("blub")
                    paymill_context = paymill.PaymillContext('5ccd454aa30b1614e44193f740762a52')
                    payment_service = paymill_context.get_payment_service()    
                    payments_list = payment_service.list()
                    
                    print("blub")                    
                    
                    now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
                    Y=now.year
                    M=now.month
                    D=now.day
                    H=now.hour
                    Mi=now.minute
                    S=now.second
                    d1 = datetime.datetime.strptime(str(Y)+"-"+str(M)+"-"+str(D)+" "+str(H)+":"+str(Mi)+":"+str(S), "%Y-%m-%d %H:%M:%S")
                    d2 = datetime.datetime.strptime("2016-09-25 12:03:01", "%Y-%m-%d %H:%M:%S")

                    diff = d2 -d1                

                    
                    i=0
                    print("blub")
                    while i<=len(payments_list.data)-1:
                        print("blub")
                        
                        c.execute ("""select * from %s""" % (row[17]))
                        print("blub1")
                        zahlungsmethoden=c.fetchall() 
                        print("blub2")

                        if row[50]==payments_list.data[i]["client"]["id"]:						
                            existiert="nein"
                            for row_2 in zahlungsmethoden:    
                                print(payments_list.data[i]["id"]+"=="+row_2[0])
                                if payments_list.data[i]["id"]==row_2[0]:
                                    existiert="ja"
                        else:	
                            existiert=""						
                        print(existiert)
                        print(payments_list.data[i]["id"])
                        if existiert=="nein":
                            print("aSD")
                            print(payments_list.data[i]["id"])
                            print(diff)
                            print(zahlungsoption)
                            print(payments_list.data[i]["card_holder"])
                            print(payments_list.data[i]["last4"])
                            print(payments_list.data[i]["expire_month"])
                            print(payments_list.data[i]["expire_year"])
                            print(standard)
                            print(payments_list.data[i]["card_type"])
                            c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % (row[17]),(payments_list.data[i]["id"],diff,zahlungsoption,payments_list.data[i]["card_holder"],payments_list.data[i]["last4"],payments_list.data[i]["expire_month"],payments_list.data[i]["expire_year"],"",standard,payments_list.data[i]["card_type"]))
                            c.execute("""insert into keyuserdaten values (%s,%s,%s,%s,%s,%s)""" ,(row[0],"",payments_list.data[i]["last4"],"","",row[11],))


                            conn.commit()
                        else:
                            zahlungsmethoden="existiert"                            
                        status=1
                        i=i+1    
        
                if hinzufuegen=="0":

                    zaehler=0
                    threshold=1
                    c.execute ("""select * from %s""" % (row[17]))
                    for row_2 in c:
                        if row_2[4]==kreditkartennummer:
                            zaehler=zaehler+1
                        if row_2[1]==indexnummer:
                            if row_2[4]==kreditkartennummer:
                                threshold=1
                            else:
                                threshold=0


                    if zaehler>threshold:
                        zahlungsmethoden="existiert"
                        existiert="ja"
                    else:

                            
                        c.execute("""update %s set zahlungsoption=%%s, name=%%s,kreditkartennummer=%%s,ablaufmonat=%%s,ablaufjahr=%%s,sicherheitscode=%%s where clientid=%%s and indexnummer=%%s""" % (row[17]),(zahlungsoption,name,kreditkartennummer,ablaufmonat,ablaufjahr,sicherheitscode,row[0],indexnummer,))
                        c.execute("""insert into keyuserdaten values (%s,%s,%s,%s,%s,%s)""" ,(row[0],"",kreditkartennummer,"","",row[11],))
                        conn.commit()


                if hinzufuegen=="-1":
                    c.execute ("""select * from %s""" % (row[17]))
                    data_table=c.fetchall()
					
                    for row_2 in data_table:
                        print(row_2[1]+"=="+indexnummer)
                        if row_2[1]==indexnummer:
                            client_id=row_2[0]
                    print("test")
                    credit_card_delete_payment_test(client_id)
                    c.execute("""delete from %s where clientid=%%s and indexnummer=%%s""" % (row[17]),(client_id,indexnummer,))
                    conn.commit()

                            
                            
                    
                if hinzufuegen=="-2":


                    c.execute ("""select * from %s""" % (row[17]))

                    data_table=c.fetchall()
                    print("change")
                    for row_2 in data_table:
                        print(row[17]+",nein"+ row[0]+","+row_2[1]+","+row_2[5]+","+row_2[6]+":"+row_2[0])					
                        c.execute("""update %s set standard=%%s where indexnummer=%%s""" % (row[17]),("nein", row_2[1],))
                        conn.commit()
                    print(row[17]+","+standard+","+row[0]+","+indexnummer+",bla"+row_2[5]+","+row_2[6])		                        
                    c.execute("""update %s set standard=%%s where indexnummer=%%s""" % (row[17]),(standard, indexnummer,))
                    conn.commit()

        if existiert=="nein":
            zahlungsmethoden=define_zahlungsmethoden(x,c)
        update_timestamp(x,c,conn)
        
        
        
        
        
        
        
        
    	
		


    


        return HttpResponse(json.dumps(zahlungsmethoden), content_type='application/json')
    else:
        raise Http404





def zahlungsmethoden_bearbeiten(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                            password='okano1988',database='maxfischer2database')
    c = conn.cursor(buffered=True)



    c.execute ("""select * from userdaten """)

    userdaten=c.fetchall()   

    x=str(request.session.session_key)
    status=0
    login=""
    password="ok"   
    for row in userdaten:
        if row[9]==x and (row[12]!="" or row[0]!=""):
            zahlungsmethoden=define_zahlungsmethoden(x,c)
            modelAB=row[47]
            sub_picture=row[48]
            if row[1]=="":
                password="not ok"
            if (row[0]!="" and row[12]!="") or (row[0]!="" and row[1]!=""):
                login="true"
            status=1

            try:
                c.execute ("""select * from %s""" % (x))

                cart_gesamt=0
                for row_2 in c:
                    cart_gesamt=cart_gesamt+row_2[1]
            except:
                status=0

            t=get_template('zahlungsmethoden_bearbeiten.html')
            html=t.render({'favicon':get_favicon(),'brand_name':'Sensuals','title':"Zahlungsmethoden | Sensuals",'bestellungen':define_bestellung(x,"all",c),'links':get_links(x,c),'wishlist':define_wishlist(x,modelAB,sub_picture,c),'warenkorb':define_warenkorb(x,modelAB,sub_picture,c),'zahlungsmethoden':zahlungsmethoden,'login':login,'cart_gesamt':cart_gesamt,'password':password})
            


    update_timestamp(x,c,conn)        

    if status==1:
        return HttpResponse(html)
    else:
        return HttpResponseRedirect("/hello/start_page/")



    





def adressbuch_bearbeiten(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                            password='okano1988',database='maxfischer2database')
    c = conn.cursor(buffered=True)

    c.execute ("""select * from userdaten """)

    userdaten=c.fetchall() 

    x=str(request.session.session_key)
    status=0
    login=""
    password="ok"    
    for row in userdaten:
        if row[9]==x and (row[12]!="" or row[0]!=""):
            adressbuch=define_adressbuch(x,c)
            modelAB=row[47]
            sub_picture=row[48]
            if row[1]=="":
                password="not ok"
            if (row[0]!="" and row[12]!="") or (row[0]!="" and row[1]!=""):
                login="true"
            status=1

            try:
                c.execute ("""select * from %s""" % (x))

                cart_gesamt=0
                for row_2 in c:
                    cart_gesamt=cart_gesamt+row_2[1]
            except:
                status=0

            t=get_template('adressen_bearbeiten.html')
            html=t.render({'favicon':get_favicon(),'brand_name':'Sensuals','title':"Adressbuch | Sensuals",'bestellungen':define_bestellung(x,"all",c),'links':get_links(x,c),'wishlist':define_wishlist(x,modelAB,sub_picture,c),'warenkorb':define_warenkorb(x,modelAB,sub_picture,c),'adressbuch':adressbuch,'login':'true','cart_gesamt':cart_gesamt,'password':password})
            

            

    update_timestamp(x,c,conn)
    if status==1:
        return HttpResponse(html)
    else:
        return HttpResponseRedirect("/hello/start_page/")
    
@csrf_exempt
def adresse_speichern(request):
    if request.is_ajax() and request.POST:

        hinzufuegen=request.POST.get('hinzufuegen')        
        vorname=request.POST.get('vorname')
        nachname=request.POST.get('nachname')
        telefonnummer=request.POST.get('telefonnummer')
        adresse=request.POST.get('adresse')
        apt=request.POST.get('apt')
        unternehmensdetails=request.POST.get('unternehmensdetails')
        stadt=request.POST.get('stadt')
        plz=request.POST.get('plz')
        lieferhinweise=request.POST.get('lieferdetails')
        indexnummer=request.POST.get('indexnummer')
        standard=request.POST.get('standard')



        







                    
        
        

        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)


        c.execute ("""select * from userdaten """)

        userdaten=c.fetchall()   

        x=str(request.session.session_key)
        status=0
        for row in userdaten:
            if row[9]==x and x!="None":
                if hinzufuegen=="1":
                    now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
                    Y=now.year
                    M=now.month
                    D=now.day
                    H=now.hour
                    Mi=now.minute
                    S=now.second
                    d1 = datetime.datetime.strptime(str(Y)+"-"+str(M)+"-"+str(D)+" "+str(H)+":"+str(Mi)+":"+str(S), "%Y-%m-%d %H:%M:%S")
                    d2 = datetime.datetime.strptime("2016-09-25 12:03:01", "%Y-%m-%d %H:%M:%S")

                    diff = d2 -d1
        
                    c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % (row[16]),(row[0],diff,vorname,nachname,telefonnummer,adresse,apt,unternehmensdetails,stadt,plz,lieferhinweise,standard,))
                    c.execute("""insert into keyuserdaten values (%s,%s,%s,%s,%s,%s)""" ,(row[0],telefonnummer,"","","",row[11],))


                    if standard =="ja":
                        c.execute("""update userdaten set vorname=%s, nachname=%s, telefon=%s,lastplz=%s where lastsessionid=%s""",(vorname,nachname,telefonnummer,plz,x,))
                        
                    conn.commit()
                    status=1
                if hinzufuegen=="0":
                    c.execute("""update %s set vorname=%%s, nachname=%%s,telefonnummer=%%s,adresse=%%s,apt=%%s,unternehmensdetails=%%s,stadt=%%s,plz=%%s,lieferhinweise=%%s where email=%%s and indexnummer=%%s""" % (row[16]),(vorname,nachname,telefonnummer,adresse,apt,unternehmensdetails,stadt,plz,lieferhinweise,row[0],indexnummer,))
                    c.execute("""insert into keyuserdaten values (%s,%s,%s,%s,%s,%s)""" ,(row[0],telefonnummer,"","","",row[11],))
                    if standard =="ja":
                        c.execute("""update userdaten set vorname=%s, nachname=%s, telefon=%s,lastplz=%s where lastsessionid=%s""",(vorname,nachname,telefonnummer,plz,x,))
                    conn.commit()

                if hinzufuegen=="-1":
                    c.execute("""delete from %s where email=%%s and indexnummer=%%s""" % (row[16]),(row[0],indexnummer,))
                    conn.commit()


                            
                            
                    
                if hinzufuegen=="-2":
                    c.execute ("""select * from %s""" % (row[16]))

                    data_table=c.fetchall() 

                    for row_2 in data_table:
                        c.execute("""update %s set standard=%%s where email=%%s and indexnummer=%%s""" % (row[16]),("nein", row[0],row_2[1],))
                        conn.commit()
                        
                    c.execute("""update %s set standard=%%s where email=%%s and indexnummer=%%s""" % (row[16]),(standard, row[0],indexnummer,))
                    conn.commit()
                    c.execute("""update userdaten set lastplz=%s where lastsessionid=%s""",(plz,x,))
                    conn.commit()
                    
 

    

        update_timestamp(x,c,conn)
        return HttpResponse(json.dumps(define_adressbuch(x,c)), content_type='application/json')
    else:
        raise Http404



def passwort_bearbeiten(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                            password='okano1988',database='maxfischer2database')
    c = conn.cursor(buffered=True)



    c.execute ("""select * from userdaten """)

    userdaten=c.fetchall()   

    x=str(request.session.session_key)
    status=0
    login=""
    password="ok"    
    for row in userdaten:
        if row[9]==x and (row[12]!="" or row[0]!=""):
            modelAB=row[47]
            sub_picture=row[48]
            if row[1]=="":
                password="not ok"
            if (row[0]!="" and row[12]!="") or (row[0]!="" and row[1]!=""):
                login="true"
                

            try:
                c.execute ("""select * from %s""" % (x))

                cart_gesamt=0
                for row_2 in d:
                    cart_gesamt=cart_gesamt+row_2[1]
            except:
                status=0

                
            t=get_template('passwort_aendern.html')
            html=t.render({'favicon':get_favicon(),'brand_name':'Sensuals','title':"Passwort bearbeien | Sensuals",'bestellungen':define_bestellung(x,"all",c),'links':get_links(x,c),'wishlist':define_wishlist(x,modelAB,sub_picture,c),'warenkorb':define_warenkorb(x,modelAB,sub_picture,c),"login":login,"cart_gesamt":cart_gesamt,"password":password})
            status=1


    update_timestamp(x,c,conn)
    if status==1:
        return HttpResponse(html)
    else:
        return HttpResponseRedirect("/hello/start_page/")



@csrf_exempt
def passwort_aktualisieren(request):
    if request.is_ajax() and request.POST:
        altes_passwort=request.POST.get('altes_passwort')
        neues_passwort=request.POST.get('neues_passwort')

        
        
        

        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)

        
        x=str(request.session.session_key)

        c.execute ("""select * from userdaten """)

        status=""
        for row in c:
            if row[9]==x and x!="None":
                if row[1]==altes_passwort:
                    status="ok"
        if status=="ok":
            c.execute("""update userdaten set passwort=%s where lastsessionid=%s""",(neues_passwort,x,))
            conn.commit()
        update_timestamp(x,c,conn)
        return HttpResponse(json.dumps(status), content_type='application/json')
    else:
        raise Http404


@csrf_exempt
def check_mobilnummer(request):
    if request.is_ajax() and request.POST:
        telefonnummer=request.POST.get('telefonnummer')
        print(telefonnummer)		
        telefonnummer=validate_mobilnummer(telefonnummer)
        print(telefonnummer)		
        return HttpResponse(json.dumps(telefonnummer), content_type='application/json')
        

def validate_mobilnummer(telefonnummer):

    try:
        nummer=""
        for match in phonenumbers.PhoneNumberMatcher("+49"+telefonnummer, "DE"):
            nummer=phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164)
        type=phonenumbers.number_type(phonenumbers.parse(nummer, "DE"))
        valid=phonenumbers.is_valid_number(phonenumbers.parse(nummer, "DE"))
        

        formatter = phonenumbers.AsYouTypeFormatter("DE")
        i=0
        while i<=len(nummer)-1:
            nummer_formatted=formatter.input_digit(nummer[i])
            i=i+1
        nummer_formatted=nummer_formatted[4:]

        if str(valid)=="True" and str(type)=="1":
            return nummer_formatted
        else:
            return ""

    except:
        return ""


   


@csrf_exempt
def profil_aktualisieren(request):
    
    if request.is_ajax() and request.POST:
        vorname=request.POST.get('vorname')
        nachname=request.POST.get('nachname')
        passwort=request.POST.get('passwort')
        email=request.POST.get('email')
        telefonnummer=request.POST.get('telefonnummer')
        benachrichtigung=request.POST.get('benachrichtigung')
        newsletter=request.POST.get('newsletter')

        
        
        

        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)

        x=str(request.session.session_key)

        status=""
        try:
            validate_email(email)

        except:
          
            status="e-mail nicht ok"
            
        if telefonnummer!="":
            telefonnummer=validate_mobilnummer(telefonnummer)
            if telefonnummer=="":
                status="mobilnummer nicht korrekt"
            
        if status=="":
            if status=="":
                c.execute ("""select * from userdaten """)

                userdaten=c.fetchall()                
                for row in userdaten:

                    if row[0]==email and row[9]!=x:
                        status="exists already"

                if status=="":
                    c.execute ("""select * from userdaten """)

                    userdaten=c.fetchall()                
                    for row in userdaten:
                        if row[9]==x and x!="None":

                            if row[1]==passwort:
                                status="ok"
                    if status=="ok":
                        if telefonnummer=="":
                            benachrichtigung="false"
               		 
                        c.execute("""update userdaten set vorname=%s, nachname=%s,email=%s,telefon=%s,persmsbenachrichtigtwerden=%s, newslettersignedup=%s where lastsessionid=%s""",(vorname,nachname,email,telefonnummer,benachrichtigung,newsletter,x,))
                        c.execute("""insert into keyuserdaten values (%s,%s,%s,%s,%s,%s)""" ,(row[0],telefonnummer,"","","",row[11],))
                        conn.commit()
                    update_timestamp(x,c,conn)



            
        return HttpResponse(json.dumps(status), content_type='application/json')
    else:
        raise Http404




def verschicke_gutscheine_send_email(request):
    if request.is_ajax() and request.GET:
        empfaenger=request.GET.get('empfaenger')
        betreff=request.GET.get('betreff')
        message=request.GET.get('message')    


        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)


        feedback="ok"
        print(empfaenger)
        if empfaenger!="":
            empfaenger=empfaenger.split(";")

        
            j=0

            print(empfaenger)
            while j<=len(empfaenger)-1:
                print(empfaenger[j])
                empfaenger[j]=empfaenger[j].replace(" ", "")
                print(empfaenger[j])
                try:
                    validate_email(empfaenger[j])
                except:
                    feedback="email falsch"

                j=j+1
        else:
            feedback="keine email"


        if feedback=="ok":

                    
            c.execute ("""select * from userdaten """)
            x=str(request.session.session_key)
            status=0
            for row in c:
                if row[9]==x and x!="None":
                    code=row[11]
                    von=row[0]


            

            j=0
            while j<=len(empfaenger)-1:
                c.execute("""insert into gutscheincodes_sent values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""" ,(code,get_date_stamp_now(),get_time_stamp_now(),empfaenger[j],"no","","",message,betreff,von))
                
               

                j=j+1
            conn.commit()

            check_referral_emails_sent()
            
        return HttpResponse(json.dumps(feedback), content_type='application/json')
    else:
        raise Http404        



       

def verschicke_gutscheine(request):       
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                            password='okano1988',database='maxfischer2database')
    c = conn.cursor(buffered=True)


    x=str(request.session.session_key)

    
    profildaten=define_profil(x,c)

    status=0
    login=""
    c.execute ("""select * from userdaten """)

    userdaten=c.fetchall()
    password="ok"
    for row in userdaten:

        if row[9]==x and x!="None":
            modelAB=row[47]
            sub_picture=row[48]            

            if row[1]=="":
                password="not ok"
            if (row[0]!="" and row[12]!="") or (row[0]!="" and row[1]!=""):
                login="true"
                
            status=1

            if row[0]=="" and row[12]=="":
                status=0
            else:
                



            
 #              try:
                    c.execute ("""select * from %s""" % (x))


                    data_table=c.fetchall()


                    cart_gesamt=0
                    for row_2 in data_table:
                        cart_gesamt=cart_gesamt+row_2[1]
                    t=get_template('verschicke_gutscheine.html')
                    html=t.render({'favicon':get_favicon(),'brand_name':'Sensuals','email_from':row[0],'title':"Freunde einladen | Sensuals",'bestellungen':define_bestellung(x,"all",c),'links':get_links(x,c),'wishlist':define_wishlist(x,modelAB,sub_picture,c),'warenkorb':define_warenkorb(x,modelAB,sub_picture,c),"login":login,"cart_gesamt":cart_gesamt,'password':password})
            
#                except:
#                    status=0
            





    update_timestamp(x,c,conn)
    
    if status==1:
        return HttpResponse(html)
    else:
        return HttpResponseRedirect("/hello/start_page/")




    return HttpResponse(html)
        
    


def profil_bearbeiten(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                            password='okano1988',database='maxfischer2database')
    c = conn.cursor(buffered=True)

    x=str(request.session.session_key)
    
    profildaten=define_profil(x,c)

    status=0
    login=""


    c.execute ("""select * from userdaten """)

    userdaten=c.fetchall()


    password="ok"
    for row in userdaten:

        if row[9]==x and x!="None":
            modelAB=row[47]
            sub_picture=row[48]
            if row[1]=="":
                password="not ok"
            if (row[0]!="" and row[12]!="") or (row[0]!="" and row[1]!=""):
                login="true"
                
            status=1

            if row[0]=="" and row[12]=="":
                status=0
            else:




            
                try:
                    c.execute ("""select * from %s""" % (x))

                    current_cart=c.fetchall()


                    cart_gesamt=0
                    for row_2 in current_cart:
                        cart_gesamt=cart_gesamt+row_2[1]
                    t=get_template('profil_bearbeiten.html')
                    html=t.render({'favicon':get_favicon(),'brand_name':'Sensuals','title':"Profil bearbeien | Sensuals",'bestellungen':define_bestellung(x,"all",c),'links':get_links(x,c),'wishlist':define_wishlist(x,modelAB,sub_picture,c),'warenkorb':define_warenkorb(x,modelAB,sub_picture,c),'profildaten':profildaten,"login":login,"cart_gesamt":cart_gesamt,'password':password})
            
                except:
                    status=0
            





    update_timestamp(x,c,conn)
    
    if status==1:
        return HttpResponse(html)
    else:
        return HttpResponseRedirect("/hello/start_page/")




    return HttpResponse(html)

def VIP_bearbeiten(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                            password='okano1988',database='maxfischer2database')
    c = conn.cursor(buffered=True)

    

    x=str(request.session.session_key)
    skip="false"
    skip_rueckerstattung="false"
    login=""
    status=0
    password="ok"
    try:

        c.execute ("""select * from userdaten """)

        userdaten=c.fetchall()                
        for row in userdaten:

            if row[9]==x and x!="None":
                modelAB=row[47]
                sub_picture=row[48]                
                status=1
                
                if row[1]=="":
                    password="not ok"
                if (row[0]!="" and row[12]!="") or (row[0]!="" and row[1]!=""):
                        login="true"
                    
                store_credit=row[24]
                c.execute ("""select * from VIPmembers """)

                for row_2 in c:

                    if row_2[0]==row[11]:
                        skip=check_month_VIP(row_2[4],row_2[5])
                        skip_rueckerstattung=check_rueckerstattung_month_VIP(row_2[4],row_2[5])

                        bra_for_free=row[25]
                        bra_ordered=row_2[9]%5
                        
                t=get_template('VIP_Mitgliedschaft.html')     
                html=t.render({'favicon':get_favicon(),'brand_name':'Sensuals','title':"VIP bearbeien | Sensuals",'login':login,'skip_rueckerstattung':skip_rueckerstattung,'links':get_links(x,c),'wishlist':define_wishlist(x,modelAB,sub_picture,c),'warenkorb':define_warenkorb(x,modelAB,sub_picture,c),'skip':skip,'guthaben':('%.2f' % store_credit).replace('.', ','),'bra_ordered':bra_ordered,'bra_for_free':bra_for_free})

    except:
        status=0
             
        
              
    if status==1:
        return HttpResponse(html)
    else:
        return HttpResponseRedirect("/hello/start_page/")




                        
def bestellung_zuruecksenden(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                            password='okano1988',database='maxfischer2database')
    c = conn.cursor(buffered=True)


    

    x=str(request.session.session_key)
    status=0
    login=""
    password="ok"    
    c.execute ("""select * from userdaten """)

    userdaten=c.fetchall()                
    for row in userdaten:
        if row[9]==x and (row[12]!="" or row[0]!=""):
            modelAB=row[47]
            sub_picture=row[48]            
            status=1
            if row[1]=="":
                password="not ok"
            if (row[0]!="" and row[12]!="") or (row[0]!="" and row[1]!=""):
                login="true"

                
            bestellungen=define_bestellung(x,"all",c)
            ruecksendungen=define_ruecksendungen(x,c)
            modelAB=row[47]
            sub_picture=row[48]

                  
    if len(bestellungen)==2:
        status=2


    update_timestamp(x,c,conn)
    if status==1:
        t=get_template('Bestellung_zuruecksenden.html') 
        html=t.render({'favicon':get_favicon(),'brand_name':'Sensuals','title':"Zuruecksenden | Sensuals",'links':get_links(x,c),'wishlist':define_wishlist(x,modelAB,sub_picture,c),'warenkorb':define_warenkorb(x,modelAB,sub_picture,c),'bestellungen':bestellungen,'ruecksendungen':ruecksendungen,'login':login,'password':password})
        return HttpResponse(html)
    else:
        if status==0:
            return HttpResponseRedirect("/hello/start_page/")
        else:
            if status==2:
                return HttpResponseRedirect("/hello/account_page/") 


    


@csrf_exempt
def postpone_VIP(request):
    if request.is_ajax() and request.POST:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)

        
        
        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        if now.day>=1 and now.day<=10:
            c.execute ("""select * from userdaten """)
            x=str(request.session.session_key)
            for row in c:
                if row[9]==x and x!="None":
                    gutscheincode=row[11]
                    storecredit=row[24]


            
            
            c.execute("""update VIPmembers set lastskippedmonth=%s, lastskippedyear=%s where gutscheincode=%s""",(now.month,now.year,gutscheincode,))

            c.execute("""update userdaten set storecredit=%s where gutscheincode=%s""",(storecredit-20,gutscheincode,))
            conn.commit()


            data="ok"
        else:
            datat="not ok"


        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404




@csrf_exempt
def get_money_back_VIP(request):
    if request.is_ajax() and request.POST:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)

        
        
        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        if now.day>=11 and now.day<=30:
            c.execute ("""select * from userdaten """)
            x=str(request.session.session_key)
            for row in c:
                if row[9]==x and x!="None":
                    gutscheincode=row[11]
                    storecredit=row[24]


            
            
            c.execute("""update VIPmembers set lastskippedmonth=%s, lastskippedyear=%s where gutscheincode=%s""",(now.month,now.year,gutscheincode,))

            c.execute("""update userdaten set storecredit=%s where gutscheincode=%s""",(storecredit-20,gutscheincode,))
            conn.commit()


            data="ok"
        else:
            datat="not ok"


        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404

    
@csrf_exempt
def guthaben_abrufen(request):
    if request.is_ajax() and request.POST:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)


        c.execute ("""select * from userdaten """)
        x=str(request.session.session_key)
        data=0
        for row in c:
            if row[9]==x and x!="None":
                data=('%.2f' % row[24]).replace('.', ',')


        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404


@csrf_exempt
def check_skip_button(request):
    if request.is_ajax() and request.POST:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)


        c.execute ("""select * from userdaten """)

        userdaten=c.fetchall()



        x=str(request.session.session_key)

        skip="false"
        for row in userdaten:
            if row[9]==x and x!="None":
                c.execute ("""select * from VIPmembers """)
                for row_2 in c:
                    if row_2[0]==row[11]:
                        skip=check_month_VIP(row_2[4],row_2[5])



        return HttpResponse(json.dumps(skip), content_type='application/json')
    else:
        raise Http404



@csrf_exempt
def check_rueckerstattung_button(request):
    if request.is_ajax() and request.POST:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)


        x=str(request.session.session_key)
        c.execute ("""select * from userdaten """)

        userdaten=c.fetchall()

        skip_rueckerstattung="false"
        for row in userdaten:
            if row[9]==x and x!="None":

                c.execute ("""select * from VIPmembers """)
                for row_2 in c:

                    if row_2[0]==row[11]:
                        skip_rueckerstattung=check_rueckerstattung_month_VIP(row_2[4],row_2[5])
                        
    



        return HttpResponse(json.dumps(skip_rueckerstattung), content_type='application/json')
    else:
        raise Http404
    
def get_tracking_number(session_key,bestellnummer,c):

    c.execute ("""select * from userdaten """)

    userdaten=c.fetchall()

    for row in userdaten:
        if row[9]==session_key:

            c.execute ("""select * from %s """ % ("bestellt_"+row[11]))

            bestellt_daten=c.fetchall()
                

            for row_2 in bestellt_daten:
                if row_2[20]==bestellnummer:
                    


                    c.execute ("""select * from %s """ % (row_2[0]))

                    daten_table=c.fetchall()                    

                    for row_3 in daten_table:

                        c.execute ("""select * from %s """ % (row_2[0]+"_VF"))
                        for row_5 in c:
                            return row_5[4]


def sendungsverfolgung_tracken(request,offset):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                            password='okano1988',database='maxfischer2database')

    c = conn.cursor(buffered=True)
    x=str(request.session.session_key)
    try:
        c.execute ("""select * from userdaten """)

        for row in c:
            if row[9]==x and x!="None":
                
                status=1
                
    
                bestellungen=define_bestellung(x,offset,c)
                modelAB=row[47]
                sub_picture=row[48]
                
                sendungsverfolgung=define_sendungsverfolgung(x,offset,c)
                if row[0]=="" and row[12]=="":
                    status=0
    except:
        status=0
    

    if status==1:    
        t=get_template('Sendung_verfolgen.html') 
        html=t.render({'favicon':get_favicon(),'brand_name':'Sensuals','title':"VIP bearbeien | Sensuals",'links':get_links(x,c),'wishlist':define_wishlist(x,modelAB,sub_picture,c),'warenkorb':define_warenkorb(x,modelAB,sub_picture,c),'bestellungen':bestellungen,'sendungsverfolgung':sendungsverfolgung,'tracking_number':get_tracking_number(x,offset,c)})
        return HttpResponse(html)

    else:
        return HttpResponseRedirect("/hello/start_page/")



@csrf_exempt
def check_log_in(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')

        c = conn.cursor(buffered=True)
        x=str(request.session.session_key)
        data="yes"
        c.execute ("""select * from userdaten """)

        for row in c:
            if row[9]==x and x!="None":
                if row[0]=="" and row[12]=="":
                    data="no"       
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404

@csrf_exempt
def ruecksendung_beauftragen(request):
    if request.is_ajax() and request.POST:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)
        bestellnummer=request.POST.get('bestellnummer')
        stylecode=request.POST.get('stylecode')
        colorcode=request.POST.get('colorcode')
        anzahl=request.POST.get('anzahl')
        grund=request.POST.get('grund')
        gesamt=request.POST.get('gesamt')
        bhgroesse=request.POST.get('bhgroesse')
        slipgroesse=request.POST.get('slipgroesse')
        

        h=int(request.POST.get('item-length'))

        x=str(request.session.session_key)
        
        bestellnummer=bestellnummer.split(";")
        stylecode=stylecode.split(";")
        colorcode=colorcode.split(";")
        bhgroesse=bhgroesse.split(";")
        slipgroesse=slipgroesse.split(";")
        
        anzahl=anzahl.split(";")
        grund=grund.split(";")
        gesamt=gesamt.split(";")


        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        Monat = ["Januar", "Februar", "Maerz", "April","Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
        now_date=str(now.day)+". "+str(Monat[now.month-1])+" "+str(now.year)
        future=now + datetime.timedelta(days=14)
        future_date=str(future.day)+". "+str(Monat[future.month-1])+" "+str(future.year)
        
        x=str(request.session.session_key)


        c.execute ("""select * from userdaten """)

        userdaten=c.fetchall()

        for row in userdaten:

            if row[9]==x and x!="None":
                gutscheincode=row[11]
        
        


        j=0
        feedback="ok"
        code=id_generator()
        while j<=h:

            price_per_piece=float(gesamt[j])/int(anzahl[j])
            
            c.execute("""insert into ruecksendungen values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""" ,(code, gutscheincode,bestellnummer[j],now_date,future_date,"dhl",grund[j],stylecode[j],colorcode[j],int(anzahl[j]),price_per_piece,float(gesamt[j]),"false","false","Auf Ruecksendung wartend",bhgroesse[j],slipgroesse[j],))
            conn.commit()

            j=j+1
        
        return HttpResponse(json.dumps(define_ruecksendungen(x,c)), content_type='application/json')
    else:
        raise Http404


def load_account_page(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                            password='okano1988',database='maxfischer2database')
    c = conn.cursor(buffered=True)




    

    x=str(request.session.session_key)
    status=0
    login=""
    password="ok"
    c.execute ("""select * from userdaten """)

    userdaten=c.fetchall()
    for row in userdaten:

        if row[9]==x and x!="None":
            status=1
            modelAB=row[47]
            sub_picture=row[48]
            if row[1]=="":
            
                password="not ok"
            if (row[0]!="" and row[12]!="") or (row[0]!="" and row[1]!=""):
                login="true"
            
            if row[22]=="VIP" and row[23]=="true":
                VIP="true"
            else:
                VIP="false"
            try:
                c.execute ("""select * from %s""" % (x))

                cart_gesamt=0
                for row_2 in c:
                    cart_gesamt=cart_gesamt+row_2[1]
                    
            except:
                status=0


            if row[0]=="" and row[12]=="":
                status=0
                    
            bestellungen=define_bestellung(x,"all",c)
            t=get_template('account_page.html')     
            html=t.render({'favicon':get_favicon(),'brand_name':'Sensuals','title':"Account | Sensuals",'bestellungen':bestellungen,'links':get_links(x,c),'wishlist':define_wishlist(x,modelAB,sub_picture,c),'warenkorb':define_warenkorb(x,modelAB,sub_picture,c),'gutscheincode':row[11],'login':login,'name':row[2]+" "+row[3],'cart_gesamt':cart_gesamt,'VIP':VIP,'password':password})


    update_timestamp(x,c,conn)
    if status==1:
        return HttpResponse(html)
    else:
        return HttpResponseRedirect("/hello/start_page/")

    

def start_page(request):

    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                            password='okano1988',database='maxfischer2database')
    c = conn.cursor(buffered=True)

    status=0

    if not request.session.exists(request.session.session_key):
        request.session.create()
        


    x=str(request.session.session_key)



    c.execute ("""select * from userdaten """)

    for row in c:
        if row[9]==x and row[0]!="":
            
            status=1


    if status==0:
        t=get_template('start_page.html')     
        html=t.render({'favicon':get_favicon(),'brand_name':'Sensuals',})


    if status==1:

        return HttpResponseRedirect("/hello/overview/")
    else:

        return HttpResponse(html)


def update_timestamp(session_key,c,conn):

    a=get_time_stamp_now()
    c.execute("""update aktuellewarenkoerbe set datestamp=%s where tablename=%s""",(a.strftime('%Y-%m-%d %H:%M'),session_key,))

    conn.commit()

def get_link_positioining(offset,c):

    i=0
    c.execute ("""select * from links """)
    for row in c:
        if row[1]==offset:
           return i
        i=i+1


def create_user(x,q,conn_2):



        
    q.execute("""create table if not exists %s (
        style text,
        anzahl int,
        bhgroesse text,
        slipgroesse text,
        color text,
        freiemenge int,
        status text,
        stylecode text,
        preis float)""" % (x))
    code=id_generator()

    now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
    Monat = ["Januar", "Februar", "Maerz", "April","Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
    date_short=str(now.day)+". "+Monat[(now.month)-1]+" "+str(now.year)

    modelAB=random.randint(0,1)
    subpicture=random.randint(0,2)

    clientidpaymill=credit_card_create_new_client(code+"@test.de")

    q.execute("""insert into userdaten values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""" ,("", "","","","","","","","",x,0,code,"","","","","adressbuch_"+code,"zahlungsmethoden_"+code,"nein",date_short,"false","","regular","false","0",0,"no",0,0,0,0,"","","","","","","",0,0,0,0,"","","","","",modelAB,subpicture,"no",clientidpaymill,))

    q.execute("""create table %s (
     stylecode text,
     colorcode text,
     datum text,
     productgroup text)""" % ("wishlist_"+code))

    q.execute("""insert into keyuserdaten values (%s,%s,%s,%s,%s,%s)""" ,("","","","","",code,))
    print(code)
    q.execute("""create table %s (
            datum text,
            gutscheinwert float,
            bestellnummer text,
            gutscheincodedesanderen text)""" % (code))




    
    q.execute("""create table %s (
            clientid text,
            indexnummer text,
            zahlungsoption text,                
            name text,
            kreditkartennummer text,
            ablaufmonat text,
            ablaufjahr text,            
            sicherheitscode text,
            standard text,
            cardtype text)""" % ("zahlungsmethoden_"+code))
    q.execute("""create table %s (
            email text,
            indexnummer text,
            vorname text,                
            nachname text,
            telefonnummer text,
            adresse text,
            apt text,            
            unternehmensdetails text,
            stadt text,
            plz text,
            lieferhinweise text,
            standard text)""" % ("adressbuch_"+code))
    q.execute("""create table %s (
            sessionidtablename text,                
            adresse text,
            stadt text,
            plz text,
            unternehmensdetails text,
            vorname text,
            nachname text,
            telefonnummer text,
            lieferdetails text,
            zahlungsoption text,
            namekarteninhaber text,
            kartennummer text,
            ablaufdatum text,
            pruefnummer text,
            bestellungspreis text,
            lieferkosten text,
            rabatt text,
            rabattcode text,
            datum text,
            uhrzeit text,
            bestellnummer text,
            creditused text,
            shoppingtype text,
            status text,
            idforsorting float,
            braforfreecount int,
            braforfreevalue float,
            storecredit float,
			lieferdatum text)""" % ("bestellt_"+code))
    q.execute("""create table %s (
            stylecode text,                
            colorcode text,
            dayofshowroom text,
            monthofshowroom text,
            yearofshowroom text)""" % ("showroom_"+code))

    conn_2.commit()




        
def generate_lingerie(request,offset):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
    c = conn.cursor(buffered=True)




    t=get_template('test2.html')
  #  foo()
    print("9991")

    x=str(request.session.session_key)

	
    login=""

    c.execute ("""select * from userdaten """)
    status=0
    for row in c:
        print(row[9]+"=="+x)
        if row[9]==x and x!="None":
            user=row[11]

            status=1
            day=row[43]
            month=row[44]
            year=row[45]
            quiz=row[26]
            print(row[0]+"!= and "+row[1]+"!=) or "+row[12]+"!=")
            if (row[0]!="" and row[12]!="") or (row[0]!="" and row[1]!=""):
                login="true"

            modelAB=row[47]
            sub_picture=row[48]
            if row[22]=="VIP" and row[23]=="true":
                VIP="VIP"
            else:
                VIP="Regular"

    
    if status==0:
        if x!="None":
            create_user(x,c,conn)
        else:
            request.session.create()
            x=str(request.session.session_key)
            create_user(x,c,conn)





        c.execute ("""select * from userdaten """)
        for row in c:
            if row[9]==x and x!="None":
                user=row[11]

                status=1
                day=row[43]
                month=row[44]
                year=row[45]
                quiz=row[26]
                if (row[0]!="" and row[12]!="") or (row[0]!="" and row[1]!=""):
                    login="true"
                modelAB=row[47]
                sub_picture=row[48]


                if row[22]=="VIP" and row[23]=="true":
                    VIP="VIP"
                else:
                    VIP="Regular"

 #   try:
    print("9992")
    if offset=="Mein Showroom" and quiz=="no":
        lingerie_offerings="Quiz"
        colors=""
    else:
        print("9993")
        if offset!="Mein Showroom":
            if offset!="Wunschliste":
                print("9994")
                lingerie_offerings=get_lingerie_selection_filter(link_group_bestimmen(offset,c),"","","","",user,"","","","","","","","","",modelAB,sub_picture,c)
                print("9995")
                
                colors=get_other_colors("","",link_group_bestimmen(offset,c),c)
                print("9996")

            else:
                print("colors")
                lingerie_offerings=get_lingerie_selection_filter("Wunschliste","","","","",user,"","","","","","","","","",modelAB,sub_picture,c)
                colors=get_other_colors("","","Wunschliste",c)        
			
        else:
            
            lingerie_offerings=get_lingerie_selection_filter("Mein Showroom","","","","",user,"",day,month,year,"","","","","",modelAB,sub_picture,c)
            
            colors=get_other_colors("","","Mein Showroom",c)

    if len(lingerie_offerings)!=2 or offset=="Mein Showroom":
        html=t.render({'favicon':get_favicon(),'brand_name':'Sensuals','VIP':VIP,'bestellungen':define_bestellung(x,"all",c),'title':offset+" | Sensuals",'wishlist':define_wishlist(x,modelAB,sub_picture,c),'warenkorb':define_warenkorb(x,modelAB,sub_picture,c),'filter':load_style_filter("","","","","","",offset,user,day,month,year,c),'lingerie_offerings':lingerie_offerings,'login':login,'url':get_link_positioining(offset,c),'links':get_links(x,c),'colors':colors})
        conn.close()
        return HttpResponse(html)
    else:
        conn.close()
        return HttpResponseRedirect("/hello/start_page/")

        
 #   except:

#        log_out_do_it(x,c,conn)
#        conn.close()
#        return HttpResponseRedirect("/hello/start_page/")






def start_page_real(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
    c = conn.cursor(buffered=True)


    print("ASD")
    t=get_template('start_page_real.html')
    x=str(request.session.session_key)
 
    
    login="false"
    status=0
    modelAB=""
    sub_picture=""
    
    c.execute ("""select * from userdaten """)
    for row in c:
        print(row[9]+"=="+x)
        if row[9]==x and x!="None":
            user=row[11]
            status=1
            modelAB=row[47]
            sub_picture=row[48]

            if (row[0]!="" and row[12]!="") or (row[0]!="" and row[1]!=""):
                login="true"

    if status==0:
        request.session.create()
        x=str(request.session.session_key)

        create_user(x,c,conn)

         
    c.execute ("""select * from userdaten """)
    for row in c:

        if row[9]==x and x!="None":
            modelAB=row[47]
            sub_picture=row[48]



    print("yeS")

    
 #   try:
    bestellungen=define_bestellung(x,"all",c)
    wishlist=define_wishlist(x,modelAB,sub_picture,c)
    warenkorb=define_warenkorb(x,modelAB,sub_picture,c)
    url=get_link_positioining("",c)
    links=get_links(x,c)
    print(links)
    print("ASD")
    html=t.render({'favicon':get_favicon(),'brand_name':'Sensuals','lingerie_offerings':'','title':"Home | Sensuals",'bestellungen':bestellungen,'wishlist':wishlist,'warenkorb':warenkorb,'login':login,'url':url,'links':links})

    conn.close()
#   update_timestamp(x,c,conn)

    return HttpResponse(html)

 #   except:
 #       log_out_do_it(x,c,conn)
#        return HttpResponseRedirect("/hello/start_page/")



def impressum(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
    c = conn.cursor(buffered=True)



    t=get_template('impressum.html')
    x=str(request.session.session_key)

    
    login="false"
    status=0
    modelAB=""
    sub_picture=""
    
    c.execute ("""select * from userdaten """)
    for row in c:

        if row[9]==x and x!="None":
            user=row[11]
            status=1
            modelAB=row[47]
            sub_picture=row[48]

            if (row[0]!="" and row[12]!="") or (row[0]!="" and row[1]!=""):
                login="true"


    if status==0:
        if x!="None":
            log_out_do_it(x,c,conn)
            request.session.create()
            x=str(request.session.session_key)
            create_user(x,c,conn)
        else:
            log_out_do_it(x,c,conn)
            request.session.create()
            x=str(request.session.session_key)
            create_user(x,c,conn)
         
    c.execute ("""select * from userdaten """)
    for row in c:

        if row[9]==x and x!="None":
            modelAB=row[47]
            sub_picture=row[48]



        


 #   try:

    html=t.render({'favicon':get_favicon(),'brand_name':'Sensuals','lingerie_offerings':'','title':"Impressum | Sensuals",'bestellungen':define_bestellung(x,"all",c),'wishlist':define_wishlist(x,modelAB,sub_picture,c),'warenkorb':define_warenkorb(x,modelAB,sub_picture,c),'login':login,'url':get_link_positioining("",c),'links':get_links(x,c)})


#   update_timestamp(x,c,conn)

    return HttpResponse(html)

 #   except:
 #       log_out_do_it(x,c,conn)
#        return HttpResponseRedirect("/hello/start_page/")




def ueber_uns(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
    c = conn.cursor(buffered=True)



    t=get_template('ueber_uns.html')
    x=str(request.session.session_key)

    
    login="false"
    status=0
    modelAB=""
    sub_picture=""
    
    c.execute ("""select * from userdaten """)
    for row in c:

        if row[9]==x and x!="None":
            user=row[11]
            status=1
            modelAB=row[47]
            sub_picture=row[48]

            if (row[0]!="" and row[12]!="") or (row[0]!="" and row[1]!=""):
                login="true"


    if status==0:
        if x!="None":
            log_out_do_it(x,c,conn)
            request.session.create()
            x=str(request.session.session_key)
            create_user(x,c,conn)
        else:
            log_out_do_it(x,c,conn)
            request.session.create()
            x=str(request.session.session_key)
            create_user(x,c,conn)
         
    c.execute ("""select * from userdaten """)
    for row in c:

        if row[9]==x and x!="None":
            modelAB=row[47]
            sub_picture=row[48]



        


 #   try:

    html=t.render({'favicon':get_favicon(),'brand_name':'Sensuals','lingerie_offerings':'','title':"Über uns | Sensuals",'bestellungen':define_bestellung(x,"all",c),'wishlist':define_wishlist(x,modelAB,sub_picture,c),'warenkorb':define_warenkorb(x,modelAB,sub_picture,c),'login':login,'url':get_link_positioining("",c),'links':get_links(x,c)})


#   update_timestamp(x,c,conn)

    return HttpResponse(html)

 #   except:
 #       log_out_do_it(x,c,conn)
#        return HttpResponseRedirect("/hello/start_page/")





def kontakt_support(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
    c = conn.cursor(buffered=True)



    t=get_template('kontakt_support.html')
    x=str(request.session.session_key)

    
    login="false"
    status=0
    modelAB=""
    sub_picture=""
    
    c.execute ("""select * from userdaten """)
    for row in c:

        if row[9]==x and x!="None":
            user=row[11]
            status=1
            modelAB=row[47]
            sub_picture=row[48]

            if (row[0]!="" and row[12]!="") or (row[0]!="" and row[1]!=""):
                login="true"


    if status==0:
        if x!="None":
            log_out_do_it(x,c,conn)
            request.session.create()
            x=str(request.session.session_key)
            create_user(x,c,conn)
        else:
            log_out_do_it(x,c,conn)
            request.session.create()
            x=str(request.session.session_key)
            create_user(x,c,conn)
         
    c.execute ("""select * from userdaten """)
    for row in c:

        if row[9]==x and x!="None":
            modelAB=row[47]
            sub_picture=row[48]



        


 #   try:

    html=t.render({'favicon':get_favicon(),'brand_name':'Sensuals','lingerie_offerings':'','title':"Kontakt | Sensuals",'bestellungen':define_bestellung(x,"all",c),'wishlist':define_wishlist(x,modelAB,sub_picture,c),'warenkorb':define_warenkorb(x,modelAB,sub_picture,c),'login':login,'url':get_link_positioining("",c),'links':get_links(x,c)})


#   update_timestamp(x,c,conn)

    return HttpResponse(html)

 #   except:
 #       log_out_do_it(x,c,conn)
#        return HttpResponseRedirect("/hello/start_page/")



def kontakt_karriere(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
    c = conn.cursor(buffered=True)



    t=get_template('kontakt_karriere.html')
    x=str(request.session.session_key)

    
    login="false"
    status=0
    modelAB=""
    sub_picture=""
    
    c.execute ("""select * from userdaten """)
    for row in c:

        if row[9]==x and x!="None":
            user=row[11]
            status=1
            modelAB=row[47]
            sub_picture=row[48]

            if (row[0]!="" and row[12]!="") or (row[0]!="" and row[1]!=""):
                login="true"


    if status==0:
        if x!="None":
            log_out_do_it(x,c,conn)
            request.session.create()
            x=str(request.session.session_key)
            create_user(x,c,conn)
        else:
            log_out_do_it(x,c,conn)
            request.session.create()
            x=str(request.session.session_key)
            create_user(x,c,conn)
         
    c.execute ("""select * from userdaten """)
    for row in c:

        if row[9]==x and x!="None":
            modelAB=row[47]
            sub_picture=row[48]



        


 #   try:

    html=t.render({'favicon':get_favicon(),'brand_name':'Sensuals','lingerie_offerings':'','title':"Kontakt | Sensuals",'bestellungen':define_bestellung(x,"all",c),'wishlist':define_wishlist(x,modelAB,sub_picture,c),'warenkorb':define_warenkorb(x,modelAB,sub_picture,c),'login':login,'url':get_link_positioining("",c),'links':get_links(x,c)})


#   update_timestamp(x,c,conn)

    return HttpResponse(html)

 #   except:
 #       log_out_do_it(x,c,conn)
#        return HttpResponseRedirect("/hello/start_page/")




def datenschutz(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
    c = conn.cursor(buffered=True)



    t=get_template('datenschutz.html')
    x=str(request.session.session_key)

    
    login="false"
    status=0
    modelAB=""
    sub_picture=""
    
    c.execute ("""select * from userdaten """)
    for row in c:

        if row[9]==x and x!="None":
            user=row[11]
            status=1
            modelAB=row[47]
            sub_picture=row[48]

            if (row[0]!="" and row[12]!="") or (row[0]!="" and row[1]!=""):
                login="true"


    if status==0:
        if x!="None":
            log_out_do_it(x,c,conn)
            request.session.create()
            x=str(request.session.session_key)
            create_user(x,c,conn)
        else:
            log_out_do_it(x,c,conn)
            request.session.create()
            x=str(request.session.session_key)
            create_user(x,c,conn)
         
    c.execute ("""select * from userdaten """)
    for row in c:

        if row[9]==x and x!="None":
            modelAB=row[47]
            sub_picture=row[48]



        


 #   try:

    html=t.render({'favicon':get_favicon(),'brand_name':'Sensuals','lingerie_offerings':'','title':"Datenschutz | Sensuals",'bestellungen':define_bestellung(x,"all",c),'wishlist':define_wishlist(x,modelAB,sub_picture,c),'warenkorb':define_warenkorb(x,modelAB,sub_picture,c),'login':login,'url':get_link_positioining("",c),'links':get_links(x,c)})


#   update_timestamp(x,c,conn)

    return HttpResponse(html)

 #   except:
 #       log_out_do_it(x,c,conn)
#        return HttpResponseRedirect("/hello/start_page/")



def widerrufsbelehrung(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
    c = conn.cursor(buffered=True)



    t=get_template('widerrufsbelehrung.html')
    x=str(request.session.session_key)

    
    login="false"
    status=0
    modelAB=""
    sub_picture=""
    
    c.execute ("""select * from userdaten """)
    for row in c:

        if row[9]==x and x!="None":
            user=row[11]
            status=1
            modelAB=row[47]
            sub_picture=row[48]

            if (row[0]!="" and row[12]!="") or (row[0]!="" and row[1]!=""):
                login="true"


    if status==0:
        if x!="None":
            log_out_do_it(x,c,conn)
            request.session.create()
            x=str(request.session.session_key)
            create_user(x,c,conn)
        else:
            log_out_do_it(x,c,conn)
            request.session.create()
            x=str(request.session.session_key)
            create_user(x,c,conn)
         
    c.execute ("""select * from userdaten """)
    for row in c:

        if row[9]==x and x!="None":
            modelAB=row[47]
            sub_picture=row[48]



        


 #   try:

    html=t.render({'favicon':get_favicon(),'brand_name':'Sensuals','lingerie_offerings':'','title':"Widerrufsbelehrung | Sensuals",'bestellungen':define_bestellung(x,"all",c),'wishlist':define_wishlist(x,modelAB,sub_picture,c),'warenkorb':define_warenkorb(x,modelAB,sub_picture,c),'login':login,'url':get_link_positioining("",c),'links':get_links(x,c)})


#   update_timestamp(x,c,conn)

    return HttpResponse(html)

 #   except:
 #       log_out_do_it(x,c,conn)
#        return HttpResponseRedirect("/hello/start_page/")



def agb(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
    c = conn.cursor(buffered=True)



    t=get_template('agb.html')
    x=str(request.session.session_key)

    
    login="false"
    status=0
    modelAB=""
    sub_picture=""
    
    c.execute ("""select * from userdaten """)
    for row in c:

        if row[9]==x and x!="None":
            user=row[11]
            status=1
            modelAB=row[47]
            sub_picture=row[48]

            if (row[0]!="" and row[12]!="") or (row[0]!="" and row[1]!=""):
                login="true"


    if status==0:
        if x!="None":
            log_out_do_it(x,c,conn)
            request.session.create()
            x=str(request.session.session_key)
            create_user(x,c,conn)
        else:
            log_out_do_it(x,c,conn)
            request.session.create()
            x=str(request.session.session_key)
            create_user(x,c,conn)
         
    c.execute ("""select * from userdaten """)
    for row in c:

        if row[9]==x and x!="None":
            modelAB=row[47]
            sub_picture=row[48]



        


 #   try:

    html=t.render({'favicon':get_favicon(),'brand_name':'Sensuals','lingerie_offerings':'','title':"AGB | Sensuals",'bestellungen':define_bestellung(x,"all",c),'wishlist':define_wishlist(x,modelAB,sub_picture,c),'warenkorb':define_warenkorb(x,modelAB,sub_picture,c),'login':login,'url':get_link_positioining("",c),'links':get_links(x,c)})


#   update_timestamp(x,c,conn)

    return HttpResponse(html)

 #   except:
 #       log_out_do_it(x,c,conn)
#        return HttpResponseRedirect("/hello/start_page/")



def jobs(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
    c = conn.cursor(buffered=True)



    t=get_template('jobs.html')
    x=str(request.session.session_key)

    
    login="false"
    status=0
    modelAB=""
    sub_picture=""
    
    c.execute ("""select * from userdaten """)
    for row in c:

        if row[9]==x and x!="None":
            user=row[11]
            status=1
            modelAB=row[47]
            sub_picture=row[48]

            if (row[0]!="" and row[12]!="") or (row[0]!="" and row[1]!=""):
                login="true"


    if status==0:
        if x!="None":
            log_out_do_it(x,c,conn)
            request.session.create()
            x=str(request.session.session_key)
            create_user(x,c,conn)
        else:
            log_out_do_it(x,c,conn)
            request.session.create()
            x=str(request.session.session_key)
            create_user(x,c,conn)
         
    c.execute ("""select * from userdaten """)
    for row in c:

        if row[9]==x and x!="None":
            modelAB=row[47]
            sub_picture=row[48]



        


 #   try:

    html=t.render({'favicon':get_favicon(),'brand_name':'Sensuals','lingerie_offerings':'','title':"Jobs | Sensuals",'bestellungen':define_bestellung(x,"all",c),'wishlist':define_wishlist(x,modelAB,sub_picture,c),'warenkorb':define_warenkorb(x,modelAB,sub_picture,c),'login':login,'url':get_link_positioining("",c),'links':get_links(x,c)})


#   update_timestamp(x,c,conn)

    return HttpResponse(html)

 #   except:
 #       log_out_do_it(x,c,conn)
#        return HttpResponseRedirect("/hello/start_page/")

def FAQ(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
    c = conn.cursor(buffered=True)



    t=get_template('FAQ.html')
    x=str(request.session.session_key)

    
    login="false"
    status=0
    modelAB=""
    sub_picture=""
    
    c.execute ("""select * from userdaten """)
    for row in c:

        if row[9]==x and x!="None":
            user=row[11]
            status=1
            modelAB=row[47]
            sub_picture=row[48]

            if (row[0]!="" and row[12]!="") or (row[0]!="" and row[1]!=""):
                login="true"


    if status==0:
        if x!="None":
            log_out_do_it(x,c,conn)
            request.session.create()
            x=str(request.session.session_key)
            create_user(x,c,conn)
        else:
            log_out_do_it(x,c,conn)
            request.session.create()
            x=str(request.session.session_key)
            create_user(x,c,conn)
         
    c.execute ("""select * from userdaten """)
    for row in c:

        if row[9]==x and x!="None":
            modelAB=row[47]
            sub_picture=row[48]



        


 #   try:

    html=t.render({'favicon':get_favicon(),'brand_name':'Sensuals','lingerie_offerings':'','title':"FAQ | Sensuals",'bestellungen':define_bestellung(x,"all",c),'wishlist':define_wishlist(x,modelAB,sub_picture,c),'warenkorb':define_warenkorb(x,modelAB,sub_picture,c),'login':login,'url':get_link_positioining("",c),'links':get_links(x,c)})


#   update_timestamp(x,c,conn)

    return HttpResponse(html)

 #   except:
 #       log_out_do_it(x,c,conn)
#        return HttpResponseRedirect("/hello/start_page/")




def wie_funktioniert_VIP(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
    c = conn.cursor(buffered=True)



    t=get_template('wie_funktioniert_VIP.html')
    x=str(request.session.session_key)

    
    login="false"
    status=0
    modelAB=""
    sub_picture=""
    
    c.execute ("""select * from userdaten """)
    for row in c:

        if row[9]==x and x!="None":
            user=row[11]
            status=1
            modelAB=row[47]
            sub_picture=row[48]

            if (row[0]!="" and row[12]!="") or (row[0]!="" and row[1]!=""):
                login="true"


    if status==0:
        if x!="None":
            log_out_do_it(x,c,conn)
            request.session.create()
            x=str(request.session.session_key)
            create_user(x,c,conn)
        else:
            log_out_do_it(x,c,conn)
            request.session.create()
            x=str(request.session.session_key)
            create_user(x,c,conn)
         
    c.execute ("""select * from userdaten """)
    for row in c:

        if row[9]==x and x!="None":
            modelAB=row[47]
            sub_picture=row[48]



        


 #   try:

    html=t.render({'favicon':get_favicon(),'brand_name':'Sensuals','lingerie_offerings':'','title':"Wie funktioniert VIP? | Sensuals",'bestellungen':define_bestellung(x,"all",c),'wishlist':define_wishlist(x,modelAB,sub_picture,c),'warenkorb':define_warenkorb(x,modelAB,sub_picture,c),'login':login,'url':get_link_positioining("",c),'links':get_links(x,c)})


#   update_timestamp(x,c,conn)

    return HttpResponse(html)

 #   except:
 #       log_out_do_it(x,c,conn)
#        return HttpResponseRedirect("/hello/start_page/")




@csrf_exempt
def login_user(request):
    if request.is_ajax() and request.POST:
        n=request.POST.get('item')
        m=n.split(",")


        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)
        

        

        x=str(request.session.session_key)

        gutscheincode_old=""
        c.execute ("""select * from userdaten """)
        for row in c:
            if row[9]==x and x!="None":
                gutscheincode_old=row[11]

        
        if gutscheincode_old=="":
            if x!="None":
                create_user(x,c,conn)
            else:
                request.session.create()
                x=str(request.session.session_key)
                create_user(x,c,conn)

            c.execute ("""select * from userdaten """)
            for row in c:
                if row[9]==x and x!="None":
                    gutscheincode_old=row[11]

        c.execute ("""select * from userdaten """)

        userdaten=c.fetchall()


        status=0
        status_=0
        abc=""
        plz=""
        for row in userdaten:


            
            if row[0]==m[0] and row[1]==m[1]:
                status=1
                feedback="ok"
                plz=row[5]
                gutscheincode=row[11]

                c.execute("""delete from userdaten where lastsessionid=%s""",(x,))



                    

                c.execute("""update userdaten set lastsessionid=%s where email=%s""",(x,m[0],))
                conn.commit()
                a=get_time_stamp_now()


                c.execute ("""select * from aktuellewarenkoerbe """)

                aktuellewarenkoerbe=c.fetchall()



                for row_3 in aktuellewarenkoerbe:
                    

                    if row_3[2]==row[11]:
                        status_=1
                        x_old=row_3[0]


                if status_==0:                        
                    c.execute("""insert into aktuellewarenkoerbe values (%s,%s,%s)""" ,(x,a.strftime('%Y-%m-%d %H:%M'),row[11],))
                    conn.commit()
                else:
                    
                    c.execute("""update aktuellewarenkoerbe set tablename=%s where gutscheincodeid=%s""",(x,row[11],))
                    conn.commit()
                    

                    print("abc")

                    print("abc1")





                    c.execute ("""select * from %s """ %(x_old))

                    cart_alt=c.fetchall()

                
                    for row_4 in cart_alt:
                        eingefuegt="no"

                        print(row_4[0])


                        c.execute ("""select * from %s """ %(x))

                        cart_neu=c.fetchall()

      
                        for row_5 in cart_neu:
                            
                            if row_4[2]==row_5[2] and row_4[3]==row_5[3] and row_4[4]==row_5[4] and row_4[7]==row_5[7]:
                                c.execute("""update %s set anzahl=%%s where bhgroesse=%%s and slipgroesse=%%s and color=%%s and stylecode=%%s and preis=%%s"""%(x),(row_4[1],row_4[2],row_4[3],row_4[4],row_4[7],row_4[8],))
                                eingefuegt="yes"
                                conn.commit()

                        print(x)
                        if eingefuegt=="no":
                            print("yes0")
                            c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" %(x),(row_4[0],int(row_4[1]),row_4[2],row_4[3],row_4[4],int(row_4[5]),row_4[6],row_4[7],row_4[8],))
                            print("yes1")
                            conn.commit()
                    conn.commit()



                    c.execute ("""select * from %s """%("wishlist_"+gutscheincode_old))

                    wishlist=c.fetchall()

                    for row_3 in wishlist:
                        eingefuegt="no"
                        c.execute ("""select * from %s """ %("wishlist_"+gutscheincode))
                        for row_5 in c:
                            if row_5[0]==row_3[0]:
                                eingefuegt="yes"
                                
                        if eingefuegt=="no":
                            c.execute("""insert into %s values (%%s,%%s)""" %("wishlist_"+gutscheincode),(row_4[0],row_4[1],))






                

        a=0
        u=""
        conn.commit()

        if status==0:
            feedback="wrong data"
        else:
            feedback="overview/BH & Slips"

#        foo()

            

        
        return HttpResponse(json.dumps(feedback), content_type='application/json')
    else:
        raise Http404



@csrf_exempt
def updater_user_registration(request):
    if request.is_ajax() and request.POST:
        n=request.POST.get('item')

        m=n.split(",")



        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)

        feedback=""

        x=str(request.session.session_key)

        try:
            validate_email(m[0])
        except:
            feedback="email falsch"


        if feedback=="":           
            c.execute ("""select * from userdaten """)
            for row in c:
                if row[9]==x and x!="None":
                    gutscheincode=row[11]
                if row[0]==m[0]:
                    status=1
                    feedback="exists already"

            if feedback!="exists already":      
                status=0
   
                if len(m)==2:
                    c.execute("""update userdaten set email=%s, passwort=%s where lastsessionid=%s""",(m[0], m[1],x,))
                else:
                    c.execute("""update userdaten set email=%s where lastsessionid=%s""",(m[0],x,))
                    
                
                c.execute("""insert into aktuellewarenkoerbe values (%s,%s,%s)""" ,(x,"",gutscheincode,))

                conn.commit()
                feedback="overview/Panties"


        
        return HttpResponse(json.dumps(feedback), content_type='application/json')


@csrf_exempt
def register_user(request):
    if request.is_ajax() and request.POST:
        n=request.POST.get('item')
        gutscheincode=request.POST.get('gutscheincode')
        m=n.split(",")



        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)



        validate_email(m[0])
        c.execute ("""select * from userdaten """)
        for row in c:
            if row[0]==m[0]:
                status=1
                feedback="exists already"


        if feedback!="exists already":      
            status=0
#            if not request.session.exists(request.session.session_key):
#                request.session.create()
            x=str(request.session.session_key)

            c.execute("""create table if not exists %s (
                style text,
                anzahl int,
                bhgroesse text,
                slipgroesse text,
                color text,
                freiemenge int,
                status text,
                stylecode text)""" % (x))
            conn.commit()



            credit=0

            geworben="nein"
            genutztergutscheincode=""

            if status==0:
                now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
                Monat = ["Januar", "Februar", "Maerz", "April","Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
                date_short=str(now.day)+". "+Monat[(now.month)-1]+" "+str(now.year)

                c.execute ("""select * from userdaten """)

                userdaten=c.fetchall()
                


                for row in userdaten:

                    if row[11]==gutscheincode:



                        c.execute ("""select * from %s """ % ("bestellt_"+gutscheincode))

                        bestellt_daten=c.fetchall()                       

                        zaehler_4=0
                        for row_3 in bestellt_daten:
                            zaehler_4=zaehler_4+1

                        if zaehler_4!=0:    
                            geworben="ja"
                            credit=10
                            
                            genutztergutscheincode=gutscheincode
                            c.execute("""insert into %s values (%%s,%%s,%%s,%%s)""" % (gutscheincode),(date_short,0,"",row[11],))
                            conn.commit()
                            




                c.execute ("""select * from aktuellewarenkoerbe""")
                status=0
                for row in c:
                    if row[0]==str(x):
                        status=1

                if status==0:
                    a=get_time_stamp_now()
 #                   c.execute("""insert into aktuellewarenkoerbe values (%s,%s,%s)""" ,(x,a.strftime('%Y-%m-%d %H:%M'),code,))
     

                
 #               if credit !=0:
#                    c.execute("""insert into %s values (%%s,%%s,%%s,%%s)""" % (code),(date_short,credit,"nicht anzeigen",gutscheincode,))

                conn.commit()
                feedback="overview/Panties"
 #       except ValidationError as e:
#            feedback="email falsch"
#        except:
#            log_out_do_it(x,c,conn)
#            feedback=""


        
        return HttpResponse(json.dumps(feedback), content_type='application/json')
    else:
        raise Http404





def genuegend_warenmenge_vorhanden(x,gerichtname,anzahl,bestellnummer,add_or_erase,anzahl_new,stylecode,colorcode,bh_groesse,slip_groesse,c):

    c.execute ("""select * from userdaten """)

    userdaten=c.fetchall()

    if bestellnummer!="":
        c.execute ("""select * from userdaten """)

        userdaten=c.fetchall()
        for row_2 in userdaten:
            if row_2[9]==x:
                c.execute ("""select * from %s """% ("bestellt_"+row_2[11]))
                for row in c:
                    if (row[20]==bestellnummer):
                        o=row[0]
    else:
        o=x
        




   

    alter_bestellwert=0
    neuer_bestellwert=0
    
    c.execute ("""select * from %s""" % (o))
    for row in c:

        if str(row[0]) == gerichtname:
            alter_bestellwert=row[1]
            if add_or_erase=="":
                neuer_bestellwert=int(anzahl)
            else:
                if add_or_erase=="add":
                    
                    neuer_bestellwert=alter_bestellwert+1
                else:
                    if add_or_erase=="erase":
                        neuer_bestellwert=alter_bestellwert-1
                    else:
                        if add_or_erase=="change":
                            neuer_bestellwert=int(anzahl_new)
    if add_or_erase=="add" and neuer_bestellwert==0:
        neuer_bestellwert=1    

    feedback=0
    c.execute ("""select * from %s """% ("stylecode_"+stylecode))
    for row_2 in c:
#        print(colorcode +"=="+ str(row_2[2])+" and "+bh_groesse +"=="+ str(row_2[3]) +"or"+ slip_groesse +"=="+ str(row_2[3]))
        if (colorcode == str(row_2[2])) and ((bh_groesse == str(row_2[3])) or (slip_groesse == str(row_2[3]))):
            
            bestelltemengeintransit=row_2[5]+neuer_bestellwert-alter_bestellwert

            if bestelltemengeintransit<=row_2[4]:
                feedback=feedback+1
    if feedback>=2 or (bh_groesse=="" and feedback==1):               
        return "true"
    else:
        return "false"
              




def update_bestellt_table(x,bestellnummer,bestellungspreis,lieferdetails,adresse,plz,stadt,unternehmensdetails,vorname,nachname,c,conn):

    c.execute ("""select * from userdaten """)

    userdaten=c.fetchall()
    

    for row_2 in userdaten:
        if row_2[9]==x:
            c.execute ("""select * from %s """% ("bestellt_"+row_2[11]))

            bestellt_table=c.fetchall()

            for row in bestellt_table:
                if (row[20]==bestellnummer):
                    j=0
                    output=""
                    o=row[0]
                    c.execute("""update %s set bestellungspreis=%%s,lieferdetails=%%s,adresse=%%s,plz=%%s,stadt=%%s,unternehmensdetails=%%s,vorname=%%s,nachname=%%s where bestellnummer=%%s""" % ("bestellt_"+row_2[11]),(bestellungspreis,lieferdetails,adresse,plz,stadt,unternehmensdetails,vorname,nachname,bestellnummer,))
                    conn.commit()   


   
def update_menu_table(x,gerichtname,anzahl,bestellnummer,add_or_erase,anzahl_new,stylecode,colorcode,bh_groesse,slip_groesse,c,conn):




    
    if bestellnummer!="":
        c.execute ("""select * from userdaten """)

        userdaten=c.fetchall()
        for row_2 in userdaten:
            if row_2[9]==x:
                c.execute ("""select * from %s """% ("bestellt_"+row_2[11]))
                for row in c:
                    if (row[20]==bestellnummer):
                        o=row[0]
    else:
        o=x

    if add_or_erase=="add":
        neuer_bestellwert=1
    else:
        neuer_bestellwert=0
    alter_bestellwert=0
    c.execute ("""select * from %s""" % (o))
    for row in c:
        
        if str(row[0]) == gerichtname:
            alter_bestellwert=row[1]
        else:
            if add_or_erase=="":
                neuer_bestellwert=int(anzahl)
            else:
                if add_or_erase=="add":
                    neuer_bestellwert=min(alter_bestellwert+1,10)
                else:
                    if add_or_erase=="erase":
                        neuer_bestellwert=alter_bestellwert-1
                    else:
                        if add_or_erase=="change":
                            neuer_bestellwert=int(anzahl_new)


    c.execute  ("""select * from %s """% ("stylecode_"+stylecode))

    stylecode_=c.fetchall()

    for row_2 in stylecode_:

        if (colorcode == str(row_2[2])) and (bh_groesse == str(row_2[3])):
            bestelltemengebestellt=row_2[5]+neuer_bestellwert-alter_bestellwert

            freiemenge=row_2[4]-bestelltemengebestellt
            print("bestelltemengebestellt")
            print(bestelltemengebestellt)
            print(bh_groesse)
            print(colorcode)
            
            c.execute("""update %s set bestelltemengebestellt=%%s where size=%%s and color=%%s"""% ("stylecode_"+stylecode),(bestelltemengebestellt,bh_groesse,colorcode,))
            conn.commit()
        if (colorcode == str(row_2[2])) and slip_groesse == str(row_2[3]):
            bestelltemengebestellt=row_2[5]+neuer_bestellwert-alter_bestellwert
            freiemenge=row_2[4]-bestelltemengebestellt
            c.execute("""update %s set bestelltemengebestellt=%%s where size=%%s and color=%%s"""% ("stylecode_"+stylecode),(bestelltemengebestellt,slip_groesse,colorcode,))
            conn.commit()
    return freiemenge





@csrf_exempt
def select_shopping_type(request):
    if request.is_ajax() and request.GET:
        shopping_type=request.GET.get('shopping_type')
        x=str(request.session.session_key)

        
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)


        c.execute ("""select * from %s """ %(x))

        cart_daten=c.fetchall()
        

        for row in cart_daten:

            c.execute ("""select * from lingerieselection """)

            lingerieselection=c.fetchall()

            for row_2 in lingerieselection:
                if row[7]==row_2[11] and row[4]==row_2[12]:
                    if shopping_type=="Regular": #pay as you go
                        
                        c.execute("""update %s set preis=%%s where stylecode=%%s and color=%%s""" % (x),(row_2[3],row[7],row[4],))
                    else:
                        c.execute("""update %s set preis=%%s where stylecode=%%s and color=%%s""" % (x),(row_2[4],row[7],row[4],))

        c.execute("""update userdaten set shoppingtype=%s where lastsessionid=%s""",(shopping_type,x,))
        conn.commit()


        return HttpResponse(json.dumps(define_rebates(x,"","","","",c,conn)), content_type='application/json')
    else:
        raise Http404        

def update_detail_bestellung_table(x,stylename,anzahl,bestellnummer,freiemenge,status,existiert,add_or_erase,anzahl_new,stylecode,colorcode,bh_groesse,slip_groesse,regular_price,subscription_price,c,conn):






    if bestellnummer!="":
        c.execute ("""select * from userdaten """)

        userdaten=c.fetchall()
        for row_2 in userdaten:
            if row_2[9]==x:

                c.execute ("""select * from %s """% ("bestellt_"+row_2[11]))
                for row in c:
                    if (row[20]==bestellnummer):
                        o=row[0]
    else:
        o=x
        c.execute ("""select * from %s """ %(x))
        for row in c:
            if row[0]==stylename and row[2]==bh_groesse and row[3]==slip_groesse and row[4]==colorcode:
                anzahl=row[1]


    c.execute ("""select * from userdaten """)
    for row_2 in c:
        if row_2[9]==x:
            shopping_type=row_2[22]
                

                

    if shopping_type=="VIP":
        preis=subscription_price
    else:
        preis=regular_price
    if existiert=="ja":
        if add_or_erase=="":
            c.execute("""update %s set anzahl=%%s,preis=%%s where style=%%s and color=%%s and bhgroesse=%%s and slipgroesse=%%s""" % (o),(int(anzahl),preis,stylename,colorcode,bh_groesse,slip_groesse))
            conn.commit()
        else:
            if add_or_erase=="add":
                c.execute("""update %s set anzahl=%%s,preis=%%s where style=%%s and color=%%s and bhgroesse=%%s and slipgroesse=%%s""" % (o),(int(anzahl)+1,preis,stylename,colorcode,bh_groesse,slip_groesse))
                conn.commit()
            else:
                if add_or_erase=="erase":
                    if anzahl!=1:
                        c.execute("""update %s set anzahl=%%s,preis=%%s where style=%%s and color=%%s and bhgroesse=%%s and slipgroesse=%%s""" % (o),(int(anzahl)-1,preis,stylename,colorcode,bh_groesse,slip_groesse))
                        conn.commit()
                    else:
                        c.execute("""delete from %s where style = %%s and color=%%s and bhgroesse=%%s and slipgroesse=%%s""" % (o),(stylename,colorcode,bh_groesse,slip_groesse))
                        conn.commit()
                else:
                    if add_or_erase=="change":
                        if int(anzahl_new)>0:
                            c.execute("""update %s set anzahl=%%s,preis=%%s where style=%%s and color=%%s and bhgroesse=%%s and slipgroesse=%%s""" % (o),(int(anzahl_new),preis,stylename,colorcode,bh_groesse,slip_groesse))
                            conn.commit()
                        else:
                            c.execute("""delete from %s where style = %%s and color=%%s and bhgroesse=%%s and slipgroesse=%%s""" % (o),(stylename,colorcode,bh_groesse,slip_groesse))
                            conn.commit()
                            
                
    else:
        if add_or_erase=="add":
            c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % (o),(stylename, 1,bh_groesse,slip_groesse,colorcode,freiemenge,status,stylecode,preis))
            conn.commit()




@csrf_exempt
def change_order_check(request):
    
    if request.is_ajax() and request.GET:
        bestellnummer=request.GET.get('bestellnummer')
        unternehmensdetails=request.GET.get('unternehmensdetails')
        adresse=request.GET.get('adresse')
        stadt=request.GET.get('stadt')
        plz=request.GET.get('plz')
        lieferdetails=request.GET.get('lieferdetails')
        bestellungspreis=request.GET.get('bestellungspreis')





        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)






        h=int(request.GET.get('item-length'))
        n=request.GET.get('item')
        x=str(request.session.session_key)
        
        m=n.split(",")

        


        j=0
        feedback="ok"
        while j<=h:
            style=m[j*7+0]
            stylecode=m[j*7+1]
            
            colorcode=m[j*7+2]
            bh_groesse=m[j*7+3]
            slip_groesse=m[j*7+4]
            anzahl=m[j*7+5]
            preis=m[j*7+6]

            if(genuegend_warenmenge_vorhanden(x,style,"","","change",anzahl,stylecode,colorcode,bh_groesse,slip_groesse,c)=="false"):
                feedback="nicht genuegend Warenmenge"
            j=j+1




        update_timestamp(x,c,conn)



        return HttpResponse(json.dumps(feedback), content_type='application/json')
    else:
        raise Http404


            

@csrf_exempt
def change_order(request):
    if request.is_ajax() and request.POST:

        bestellnummer=request.POST.get('bestellnummer')
        unternehmensdetails=request.POST.get('unternehmensdetails')
        adresse=request.POST.get('adresse')
        stadt=request.POST.get('stadt')
        plz=request.POST.get('plz')
        lieferdetails=request.POST.get('lieferdetails')
        vorname=request.POST.get('vorname')
        nachname=request.POST.get('nachname')
        bestellungspreis=request.POST.get('bestellungspreis')

        
        h=int(request.POST.get('item-length'))
        n=request.POST.get('item')
        x=str(request.session.session_key)
        
        m=n.split(",")

        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                            password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)       


        j=0
        feedback="ok"

        while j<=h:
            style=m[j*7+0]
            stylecode=m[j*7+1]
            
            colorcode=m[j*7+2]
            bh_groesse=m[j*7+3]
            slip_groesse=m[j*7+4]
            anzahl=m[j*7+5]
            preis=m[j*7+6]



            if(genuegend_warenmenge_vorhanden(x,style,"","","change",anzahl,stylecode,colorcode,bh_groesse,slip_groesse,c)=="false"):
                feedback="nicht genuegend Warenmenge"
            j=j+1


        if feedback=="ok":

            j=0
            while j<=h:
                style=m[j*7+0]
                stylecode=m[j*7+1]
                colorcode=m[j*7+2]
                bh_groesse=m[j*7+3]
                slip_groesse=m[j*7+4]
                anzahl=m[j*7+5]
                preis=m[j*7+6]



                update_bestellt_table(x,bestellnummer,bestellungspreis,lieferdetails,adresse,plz,stadt,unternehmensdetails,vorname,nachname,c,conn)

                update_menu_table(x,style,"",bestellnummer,"change",anzahl,stylecode,colorcode,"",slip_groesse,c,conn)
                update_menu_table(x,style,"",bestellnummer,"change",anzahl,stylecode,colorcode,bh_groesse,"",c,conn)
                
                update_detail_bestellung_table(x,style,"",bestellnummer,"","Bestellt","ja","change",anzahl,stylecode,colorcode,bh_groesse,slip_groesse,preis,preis,c,conn)
                j=j+1
                      



        update_timestamp(x,c,conn)

        bestelldetails=define_bestelldetails(x,bestellnummer,"","",c)


        return HttpResponse(json.dumps(feedback), content_type='application/json')









    



def gutschein_einloesen_do_it(x,gutscheincode,art,c,conn):
    
    now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
    Monat = ["Januar", "Februar", "Maerz", "April","Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
    now_date=str(now.day)+". "+str(Monat[now.month-1])+" "+str(now.year)

    someday = datetime.date(now.year, now.month, now.day)

                
    


                        
    
    
    output=""
#    try:
    if art=="einloesen":

        c.execute  ("""select * from gutscheine """)

        gutscheine_daten=c.fetchall()

        for row in gutscheine_daten:
            print(gutscheincode+"=="+str(row[0]) +"and"+ row[3]+"==aktiv")
            if gutscheincode==str(row[0]) and row[3]=="aktiv":
                year=row[2][-4:]
                end=row[2].find(".")+1
                day=row[2][:end-1]
                month=monthToNum(row[2][end+1:len(row[2])-5])  
                date_gericht = datetime.date(int(year), int(month), int(day))
                diff = date_gericht-someday


                if diff.days>=0:
                    if row[4]=="ja":
                        c.execute("""update gutscheine set status=%s where gutscheincode=%s""",("nicht aktiv",row[0],))
                        
                        
                    c.execute("""update userdaten set genutztergutscheincode=%s where lastsessionid=%s""",(gutscheincode,x,))
                    conn.commit()
                    output="rabatt,"+str(row[1])
    else:
        c.execute  ("""select * from gutscheine """)

        gutscheine_daten=c.fetchall()
        for row in gutscheine_daten:
            if gutscheincode==str(row[0]):
                c.execute("""update gutscheine set status=%s where gutscheincode=%s""",("aktiv",row[0],))
                c.execute("""update userdaten set genutztergutscheincode=%s where lastsessionid=%s""",("",x,))
                conn.commit()
                output="rabatt,0"
      


    if output=="":
        if art=="einloesen":

            c.execute ("""select * from userdaten """)

            userdaten=c.fetchall()

            for row in userdaten:
                if row[9]==x and x!="None":
                    print(row[18]+"==nein")
                    if row[18]=="nein":
                        

                        c.execute ("""select * from %s """ % ("bestellt_"+row[11]))
                        zaehler_3=0
                        for row_3 in c:
                            zaehler_3=zaehler_3+1
                        
                        c.execute ("""select * from %s """ % ("bestellt_"+gutscheincode))
                        zaehler_4=0
                        for row_3 in c:
                            zaehler_4=zaehler_4+1
                        print(zaehler_3)
                        print(zaehler_4)
                        if zaehler_3==0 and  zaehler_4==0:
                            c.execute ("""select * from userdaten """)

                            userdaten=c.fetchall()
                            for row_2 in userdaten:
                                print(row_2[11]+"=="+gutscheincode +"and"+ row[11]+"!="+gutscheincode)
                                if row_2[11]==gutscheincode and row[11]!=gutscheincode:


                                        
                                    credit_verfuegbar=float(row[10])
                                    now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
                                    Monat = ["Januar", "Februar", "Maerz", "April","Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
                                    date_short=str(now.day)+". "+Monat[(now.month)-1]+" "+str(now.year)
                                    geworben="ja"
                                    credit=15
                                    credit_verfuegbar=credit_verfuegbar+credit
                                    c.execute("""insert into %s values (%%s,%%s,%%s,%%s)""" % (gutscheincode),(date_short,0,"",row[11],))
                                    
                                    c.execute("""insert into %s values (%%s,%%s,%%s,%%s)""" % (row[11]),(date_short,credit,"nicht anzeigen",gutscheincode,))

                                    c.execute("""update userdaten set credit=%s,genutztergutscheincode=%s, geworben=%s where lastsessionid=%s""",(credit_verfuegbar,gutscheincode,geworben,x,))


                                    output="gutschein,"+str(-credit)
                                    conn.commit()

        else:
            c.execute ("""select * from userdaten """)

            userdaten=c.fetchall()
            for row in userdaten:
                if row[9]==x and x!="None":

                    c.execute("""delete from %s where gutscheinwert=%%s and bestellnummer=%%s and gutscheincodedesanderen=%%s"""% (gutscheincode),(0,"",row[11],))
                    c.execute("""delete from %s where gutscheinwert=%%s and bestellnummer=%%s and gutscheincodedesanderen=%%s"""% (row[11]),(15,"nicht anzeigen",gutscheincode,))

                    c.execute("""update userdaten set credit=%s, geworben=%s, genutztergutscheincode=%s where lastsessionid=%s""",(str(0),"nein","",x,))
            
                    conn.commit()
                    output="gutschein,0"
#    except:
#        output=""

    print(output)
    return output



@csrf_exempt
def get_gutschein_value(request):
    if request.is_ajax() and request.GET:
        gutscheincode=request.GET.get('gutscheincode')

        
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)
        gutscheinwert=0

        c.execute ("""select * from gutscheine """)
        for row in c:
            if row[0]==gutscheincode:
                gutscheinwert=row[1]

        return HttpResponse(json.dumps(gutscheinwert), content_type='application/json')
                

                    

@csrf_exempt
def gutschein_einloesen(request):
    if request.is_ajax() and request.GET:
        gutscheincode=request.GET.get('gutscheincode')
        art=request.GET.get('art')
        x=str(request.session.session_key)

        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')

        c = conn.cursor(buffered=True)

        
        output=gutschein_einloesen_do_it(x,gutscheincode,art,c,conn)
        
        



    return HttpResponse(json.dumps(output), content_type='application/json')












        

def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
     return ''.join(random.choice(chars) for _ in range(size))



def kreditkarte_clientid(gutscheincode_id,selected_zahlungsoption,c):


        c.execute ("""select * from %s """ % ("zahlungsmethoden_"+gutscheincode_id))
        zaehler=0
        for row in c:
            if zaehler==int(selected_zahlungsoption):
                return row[0]
            zaehler=zaehler+1


def kreditkartennummer(gutscheincode_id,selected_zahlungsoption,c):


        c.execute ("""select * from %s """ % ("zahlungsmethoden_"+gutscheincode_id))
        zaehler=0
        for row in c:
            if zaehler==int(selected_zahlungsoption):
                return row[4]
            zaehler=zaehler+1


def pruefziffer(gutscheincode_id,selected_zahlungsoption,c):


        c.execute ("""select * from %s """ % ("zahlungsmethoden_"+gutscheincode_id))
        zaehler=0
        for row in c:
            if zaehler==int(selected_zahlungsoption):
                return row[7]
            zaehler=zaehler+1

def name_kreditkarte(gutscheincode_id,selected_zahlungsoption,c):


        c.execute ("""select * from %s """ % ("zahlungsmethoden_"+gutscheincode_id))
        zaehler=0
        for row in c:
            if zaehler==int(selected_zahlungsoption):
                return row[3]
            zaehler=zaehler+1


def ablaufdatum(gutscheincode_id,selected_zahlungsoption,c):


        c.execute ("""select * from %s """ % ("zahlungsmethoden_"+gutscheincode_id))
        zaehler=0
        for row in c:
            if zaehler==int(selected_zahlungsoption):
                return row[5]+" "+row[6]
            zaehler=zaehler+1




        
def check_haushalt_wurde_von_geworben(rabattcode,gutscheincode,adresse,plz,telefonnummer,kreditkartennummer,c):

    output="false"

    if rabattcode!="" and gutscheinwert_abrufen(rabattcode,c)==0 and rabattcode!=" ":
        c.execute ("""select * from keyuserdaten""")
        

        for row in c:

            if row[5]!=gutscheincode:

                
                if telefonnummer==row[1]:
                    output="true"
                    break
                if kreditkartennummer==row[2] and row[2]!="" and row[2]!=" ":
                    output="true"
                    break

   # print(rabattcode+"!="" and "+gutscheinwert_abrufen(rabattcode)+"==0 and "+rabattcode+"!=")
    return output
        

@csrf_exempt		
def paypal_test(request):
    if request.is_ajax() and request.POST:
        checksum_code=request_paymill_paypal_code("1300","EUR","http://maxfischer2.pythonanywhere.com/hello/paypal_verficiation/","http://maxfischer2.pythonanywhere.com/hello/checkout/")
    
        return HttpResponse(json.dumps(checksum_code), content_type='application/json')


@csrf_exempt
def bestellen_pre_test(request):
    if request.is_ajax() and request.POST:

        adresse=request.POST.get('adresse')

        stadt=request.POST.get('stadt')
        plz=request.POST.get('plz')
        unternehmensdetails=request.POST.get('unternehmensdetails')
        vorname=request.POST.get('vorname')
        nachname=request.POST.get('nachname')
        telefonnummer=request.POST.get('telefonnummer')
        lieferdetails=request.POST.get('lieferdetails')
        zahlungsoption=request.POST.get('zahlungsoption')
        preis=request.POST.get('preis')
        lieferkosten=request.POST.get('lieferkosten')
        rabatt=request.POST.get('rabatt')
        rabattcode=request.POST.get('rabattcode')
        warenkorb_gerichte=request.POST.get('warenkorb_gerichte')
        warenkorb_anzahl=request.POST.get('warenkorb_anzahl')
        warenkorb_groesse=request.POST.get('warenkorb_groesse')

        selected_zahlungsoption=request.POST.get('selected_zahlungsoption')
        selected_credit_card=request.POST.get('selected_credit_card')
        shopping_type=request.POST.get('shopping_type')

        braforfreecount=request.POST.get('braforfreecount')

        braforfreevalue=request.POST.get('braforfreevalue')
        storecredit_to_be_used=request.POST.get('storecredit_to_be_used')
        
        


        gerichte=warenkorb_gerichte.split(",")
        groesse=warenkorb_groesse.split(",")
        anzahl=warenkorb_anzahl.split(",")
        gesamtanzahl=0

        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')

        c = conn.cursor(buffered=True)




        x=str(request.session.session_key)



        c.execute ("""select * from userdaten """)

        userdaten=c.fetchall()


        for row in userdaten:
            if row[9]==x and x!="None":
                user=row[11]
                quiz=row[26]
                storecredit_existing=row[24]
                bra_for_free_existing=row[25]
                rabattcode_geworben=""
       
                if row[10]>0:
                    c.execute ("""select * from %s """ % (user))
                    for row_2 in c:
                        if row_2[3]!="" and row_2[3]!="nicht anzeigen":
                            rabattcode_geworben=row_2[3]
                
                namebewerter=row[2][:1]+". "+row[3]
                if check_haushalt_wurde_von_geworben(rabattcode_geworben,row[11],adresse,plz,telefonnummer,kreditkartennummer(row[11],selected_credit_card,c),c)=="false":

                    c.execute ("""select * from %s""" % (x))
                    status_="not ok"
                    for row_2 in c:
                        i=0
                        status_="ok"

                        while i<=len(gerichte)-1:

                            if str(row_2[0])==str(gerichte[i]) and str(row_2[2])==str(groesse[i]):

                                if str(row_2[1])==str(anzahl[i]):
                                    gesamtanzahl=gesamtanzahl+int(anzahl[i])

                                else:
                                    status_="not ok"                                

                            i=i+1
                        if status_=="not ok":
                            break


                    if status_=="ok":
                        bestellnummer=id_generator()
                        
                        print("-1")
                        print(selected_zahlungsoption)
                        if selected_zahlungsoption=="0":

                            c.execute ("""select * from userdaten """)

                            userdaten=c.fetchall()
                            print(float((preis+lieferkosten)))
                            print(float((preis+lieferkosten))*100)
                            print(float((preis+lieferkosten))*100)
                            price_paymill=int(float((preis+lieferkosten))*100)


                            
                            credit_card_add_new_transaction(kreditkarte_clientid(row[11],selected_credit_card,c),price_paymill,"EUR","Bestellung mit Bestellnummer: "+bestellnummer,row[50])


                            bezahlt=""

                            print("bezahlt")
                            while bezahlt=="":

                                print("bezahlt1")
                                feedback_from_transaction=check_transaction(kreditkarte_clientid(row[11],selected_credit_card,c),price_paymill,"EUR","Bestellung mit Bestellnummer: "+bestellnummer,row[50])
                                print("bezahlt2")
                                print(feedback_from_transaction)
                                if feedback_from_transaction=="true":
                                    bezahlt="true"
                                    c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % ("pending_payments"), (x,"true",bestellnummer,adresse,stadt,plz,unternehmensdetails,vorname,nachname,telefonnummer,lieferdetails,zahlungsoption,preis,lieferkosten,rabatt,rabattcode,warenkorb_gerichte,warenkorb_anzahl,warenkorb_groesse,selected_zahlungsoption,shopping_type,braforfreecount,braforfreevalue,storecredit_to_be_used,""))                  
                                    conn.commit()
                                    bestellen(x,c,conn)
                                    
                                if feedback_from_transaction=="false":
                                    bezahlt="false"
                                    c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % ("pending_payments"), (x,"false",bestellnummer,adresse,stadt,plz,unternehmensdetails,vorname,nachname,telefonnummer,lieferdetails,zahlungsoption,preis,lieferkosten,rabatt,rabattcode,warenkorb_gerichte,warenkorb_anzahl,warenkorb_groesse,selected_zahlungsoption,shopping_type,braforfreecount,braforfreevalue,storecredit_to_be_used,""))                  
                                    conn.commit()


                                    
                            print("teeest")
                            if bezahlt=="true":
                                print("lloooooos")
                                return HttpResponse(json.dumps(str(bestellnummer)), content_type='application/json')

#                                print("lloooooos2")
                            else:
                                return HttpResponse(json.dumps(bezahlt), content_type='application/json')						
						
						



                        if selected_zahlungsoption=="1":
                            price_paymill=int(float((preis+lieferkosten))*100)                       
                            c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % ("pending_payments"), (x,"false",bestellnummer,adresse,stadt,plz,unternehmensdetails,vorname,nachname,telefonnummer,lieferdetails,zahlungsoption,price_paymill,lieferkosten,rabatt,rabattcode,warenkorb_gerichte,warenkorb_anzahl,warenkorb_groesse,selected_zahlungsoption,shopping_type,braforfreecount,braforfreevalue,storecredit_to_be_used,""))                  
                            conn.commit()

							
							
							
                            checksum_code=request_paymill_paypal_code(price_paymill,"EUR","http://maxfischer2.pythonanywhere.com/hello/paypal_verficiation/","http://maxfischer2.pythonanywhere.com/hello/checkout/","Bestellung mit Bestellnummer: "+bestellnummer)
    
                            
                            return HttpResponse(json.dumps(checksum_code), content_type='application/json')
                        
                        if selected_zahlungsoption=="2":
                            transaktionsnummer=id_generator()
                            c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % ("pending_payments"), (x,"false",bestellnummer,adresse,stadt,plz,unternehmensdetails,vorname,nachname,telefonnummer,lieferdetails,zahlungsoption,preis,lieferkosten,rabatt,rabattcode,warenkorb_gerichte,warenkorb_anzahl,warenkorb_groesse,selected_zahlungsoption,shopping_type,braforfreecount,braforfreevalue,storecredit_to_be_used,transaktionsnummer))                  
                            conn.commit()

                            sofortueberweisung = []


                            
                          
                            class Sofortueberweisung(object):
                                def __init__(self,name,value):
                                    self.name=name
                                    self.value=value



                            sofortueberweisung.append(Sofortueberweisung("user_id","155319"))
                            sofortueberweisung.append(Sofortueberweisung("project_id",376786))
                            sofortueberweisung.append(Sofortueberweisung("reason_1","Bestellnummer: "+bestellnummer,))

                            

                            
                            sofortueberweisung.append(Sofortueberweisung("reason_2",transaktionsnummer,))
                            sofortueberweisung.append(Sofortueberweisung("amount",preis+lieferkosten))


                            json_string = json.dumps([Sofortueberweisung.__dict__ for Sofortueberweisung in sofortueberweisung])

                            
                            return HttpResponse(json_string, content_type='application/json')


                            

                else:
                    c.execute ("""select * from userdaten """)

                    userdaten=c.fetchall()
                    for row in userdaten:
                        if row[9]==x and x!="None":
                            c.execute("""delete from %s where gutscheinwert=%%s and bestellnummer=%%s and gutscheincodedesanderen=%%s"""% (rabattcode_geworben),(0,"",row[11],))
                            c.execute("""delete from %s where gutscheinwert=%%s and bestellnummer=%%s and gutscheincodedesanderen=%%s"""% (row[11]),(15,"",rabattcode_geworben,))

                            c.execute("""update userdaten set credit=%s, geworben=%s, genutztergutscheincode=%s where lastsessionid=%s""",(str(0),"nein","",x,))
                    
                            conn.commit()
                            status_="kann nicht geworben werden"
                            return HttpResponse(json.dumps(status_), content_type='application/json')


def sofortueberweisung_successful(request,offset):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                            password='okano1988',database='maxfischer2database')

    c = conn.cursor(buffered=True)

    transaktionsnummer=offset[10:18]







    status=0

    c.execute ("""select * from pending_payments """)
    for row_6 in c:
        if row_6[24]==transaktionsnummer:
            check_pending_payments(row_6[2],"true",c,conn)
            status=1
            return HttpResponseRedirect("/hello/account_page/bestellungen_ansehen/"+row_6[2])
        
            
    if status==0:
        return HttpResponseRedirect("/hello/checkout/")





def sofortueberweisung_not_successful(request,offset):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                            password='okano1988',database='maxfischer2database')

    c = conn.cursor(buffered=True)

    transaktionsnummer=offset[10:18]

    c.execute ("""select * from pending_payments """)
    for row_6 in c:
        if row_6[24]==transaktionsnummer:
            check_pending_payments(row_6[2],"false",c,conn)


    return HttpResponseRedirect("/hello/checkout/")


def sofortueberweisung_status(request,offset):
    print("ASD")
    print(offset)
    print(len(offset))
    
    status=offset[43:len(offset)]
    bestellnummer=offset[24:32]

    print(status)
    print(bestellnummer)

    check_pending_payments(bestellnummer,"true",c,conn)


    if status=="pending" or "bezahlt":
        check_pending_payments(bestellnummer,"true",c,conn)
    else:
        check_pending_payments(bestellnummer,"false",c.conn)


    check_pending_payments(bestellnummer,"true",c,conn)
    
    return HttpResponseRedirect("/hello/account_page/bestellungen_ansehen/"+bestellnummer)






def check_pending_payments(bestellnummer,feedback,c,conn):


    print("4")
    if feedback=="true":



        c.execute ("""select * from pending_payments """)

        pending_payments=c.fetchall()
        for row_6 in pending_payments:
            print(row_6[2]+"=="+bestellnummer)
            
            if row_6[2]==bestellnummer:
                print("51")
                c.execute("""update pending_payments set accepted=%s where bestellnummer=%s""",("true",bestellnummer,))
                print("7")
                conn.commit()
                print(row_6[0])
                bestellen(row_6[0],c,conn)
    else:
        c.execute ("""select * from pending_payments """)

        pending_payments=c.fetchall()
        for row_6 in c:
            print(row_6[2]+"=="+bestellnummer)
            
            if row_6[2]==bestellnummer:
                print("51")
                c.execute("""delete from pending_payments where bestellnummer=%s""",(bestellnummer,))
                print("7")
                conn.commit()
                print(row_6[0])

        
                
    
        


def bestellen(session_id,c,conn):
    
    c.execute ("""select * from pending_payments """)

    pending_payments=c.fetchall()
    for row_6 in pending_payments:
        if row_6[0]==session_id and row_6[1]=="true":
            bestellnummer=row_6[2]
            adresse=row_6[3]
            stadt=row_6[4]
            plz=row_6[5]
            unternehmensdetails=row_6[6]
            vorname=row_6[7]
            nachname=row_6[8]
            telefonnummer=row_6[9]
            lieferdetails=row_6[10]
            zahlungsoption=row_6[11]
            preis=row_6[12]
            lieferkosten=row_6[13]
            rabatt=row_6[14]
            rabattcode=row_6[15]
            warenkorb_gerichte=row_6[16]
            warenkorb_anzahl=row_6[17]
            warenkorb_groesse=row_6[18]
            selected_zahlungsoption=row_6[19]
            shopping_type=row_6[20]
            braforfreecount=row_6[21]
            braforfreevalue=row_6[22]
            storecredit_to_be_used=row_6[23]
            


            gerichte=warenkorb_gerichte.split(",")
            groesse=warenkorb_groesse.split(",")
            anzahl=warenkorb_anzahl.split(",")
            gesamtanzahl=0


            c.execute ("""select * from userdaten """)

            userdaten=c.fetchall()
                                             

            for row in userdaten:
                
                if row[9]==session_id and session_id!="None":
                    
                    user=row[11]
                    quiz=row[26]
                    storecredit_existing=row[24]
                    bra_for_free_existing=row[25]
                    rabattcode_geworben=""
           
                    if row[10]>0:
                        c.execute ("""select * from %s """ % (user))
                        for row_2 in c:
                            if row_2[3]!="" and row_2[3]!="nicht anzeigen":
                                rabattcode_geworben=row_2[3]
                    
                    namebewerter=row[2][:1]+". "+row[3]
                    if check_haushalt_wurde_von_geworben(rabattcode_geworben,row[11],adresse,plz,telefonnummer,kreditkartennummer(row[11],selected_zahlungsoption,c),c)=="false":

                        c.execute ("""select * from %s""" % (session_id))
                        status_="not ok"
                        for row_2 in c:
                            i=0
                            status_="ok"

                            while i<=len(gerichte)-1:

                                if str(row_2[0])==str(gerichte[i]) and str(row_2[2])==str(groesse[i]):

                                    if str(row_2[1])==str(anzahl[i]):
                                        gesamtanzahl=gesamtanzahl+int(anzahl[i])

                                    else:
                                        status_="not ok"                                

                                i=i+1
                            if status_=="not ok":
                                break
                        

                        if status_=="ok":
                                 
                            if float(storecredit_existing)<float(storecredit_to_be_used):
                                status_="not enough storecredit"



                            if float(bra_for_free_existing)<float(braforfreecount):
                                status_="not enough bra for free"                       



                        if status_=="ok":
                            current_time=datetime.datetime.now(pytz.timezone('Europe/Berlin')).time()
                            now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))

                            Wochentag = ["Mo", "Di", "Mi", "Do","Fr", "Sa", "So"]
                            Monat = ["Januar", "Februar", "Maerz", "April","Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
                            date=str(now.day)+". "+Monat[(now.month)-1]+" "+str(now.year)
                            date_short=str(now.day)+". "+Monat[(now.month)-1]+" "+str(now.year)
                            
                            time_=str(current_time)

                            time__=time_.replace(":","")
                            time__=time__.replace(".","")

                            
                            




                            session_id_="bestellt_"+time__+"_"+session_id
     
                            status=0
                            credit_used=0

                            credit=row[10]
                            gutscheincode=row[11]
                            billing_amount=float(preis)+float(lieferkosten)


                            if credit>billing_amount:
                                credit_used=billing_amount
                            else:
                                credit_used=credit

                            remaining_credit=credit-credit_used
                            remaining_storecredit=float(storecredit_existing)-float(storecredit_to_be_used)


                            
                            print(session_id_)
                            print(adresse)
                            print(stadt)
                            print(plz)
                            print(unternehmensdetails)
                            print(vorname)
                            print(nachname)
                            print(telefonnummer)
                            print(lieferdetails)
                            print(zahlungsoption)
                            print(name_kreditkarte(row[11],selected_zahlungsoption,c))
                            print(kreditkartennummer(row[11],selected_zahlungsoption,c))
                            print(ablaufdatum(row[11],selected_zahlungsoption,c))
                            print(pruefziffer(row[11],selected_zahlungsoption,c))
                            print(preis)
                            print(lieferkosten)
                            print(rabatt)
                            print(rabattcode)
                            print(date)
                            print("3")
                            print(bestellnummer)
                            print(str(credit_used))
                            print(shopping_type)
                            print("Bestellt")
                            print(time__)
                            print(braforfreecount)
                            print(braforfreevalue)
                            print(storecredit_to_be_used)

                        #   c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % ("bestellt_"+row[11]), (session_id_, adresse,stadt,plz,unternehmensdetails,vorname,nachname,telefonnummer,lieferdetails,zahlungsoption,name_kreditkarte(row[11],selected_zahlungsoption,c),kreditkartennummer(row[11],selected_zahlungsoption,c),ablaufdatum(row[11],selected_zahlungsoption,c),pruefziffer(row[11],selected_zahlungsoption,c),preis,lieferkosten,rabatt,rabattcode,date,"3",bestellnummer,str(credit_used),shopping_type,"Bestellt",time__,braforfreecount,braforfreevalue,storecredit_to_be_used,))
                           
                            lieferdatum=select_lieferdatum(3)
                            print(lieferdatum)
                            c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % ("bestellt_"+row[11]), (session_id_, adresse,stadt,plz,unternehmensdetails,vorname,nachname,telefonnummer,lieferdetails,zahlungsoption,name_kreditkarte(row[11],selected_zahlungsoption,c),kreditkartennummer(row[11],selected_zahlungsoption,c),ablaufdatum(row[11],selected_zahlungsoption,c),pruefziffer(row[11],selected_zahlungsoption,c),preis,lieferkosten,rabatt,rabattcode,date,"3",bestellnummer,str(credit_used),shopping_type,"Bestellt",time__,braforfreecount,braforfreevalue,storecredit_to_be_used,lieferdatum,))
                            
                            if row[23]=="false" and shopping_type=="VIP":

                                c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % ("VIPmembers"), (row[11], "true",date_short,now.month+1,now.month,now.year,0,0,0,0,))

                            c.execute("""update userdaten set genutztergutscheincode=%s, shoppingtype=%s, shoppingtypeentschieden=%s, storecredit=%s where lastsessionid=%s""",("",shopping_type,"true",remaining_storecredit,session_id,))
                            conn.commit()

                            
                            print("ASDW")


                            c.execute ("""select * from %s""" % ("VIPmembers"))

                            VIPmembers=c.fetchall()

                            for row_3 in VIPmembers:

                                if row_3[0]==row[11]:

                                    if str(row_3[7])==str(now.month) and str(row_3[8])==str(now.year):

                                        purchases=row_3[6]+billing_amount
                                    else:
                                        purchases=billing_amount

                                    alt=math.floor(row_3[9]/5)
                                    if int(braforfreecount)==0:
                                        neu=math.floor((gesamtanzahl+row_3[9])/5)
                                    else:
                                        neu=math.floor((gesamtanzahl+row_3[9]-int(braforfreecount))/5)-int(braforfreecount)
                                        
                                    gesamtanzahl=gesamtanzahl+row_3[9]-int(braforfreecount)

                                    delta_neu_alt=neu-alt


                                    c.execute("""update userdaten set numberofbraforfree=%s where lastsessionid=%s""",(row[25]+delta_neu_alt,session_id,))

                                    
                                    c.execute("""update VIPmembers set purchases=%s, purchaseslastmonth=%s, purchaseslastyear=%s, purchasedsincestart=%s where gutscheincode=%s""",(purchases,now.month,now.year,gesamtanzahl,row[11],))
                                    conn.commit()
                            

                            if credit_used!=0:
                                if rabattcode=="":
                                    c.execute("""insert into %s values (%%s,%%s,%%s,%%s)""" % (gutscheincode), (date_short, -credit_used,bestellnummer,"",))
                                    c.execute("""update userdaten set credit=%s where lastsessionid=%s""",(str(remaining_credit),session_id,))
                                    conn.commit()
                                else:
                                    if gutscheinwert_abrufen(rabattcode,c)==0:
                                        c.execute("""insert into %s values (%%s,%%s,%%s,%%s)""" % (gutscheincode), (date_short, -credit,bestellnummer,"nicht anzeigen",))
                                        c.execute("""update userdaten set credit=%s where lastsessionid=%s""",(str(0),session_id,))
                                        conn.commit()
                                    else:
                                        billing_amount=float(preis)+float(lieferkosten)+float(gutscheinwert_abrufen(rabattcode,c))

                                        if credit>billing_amount:
                                            credit_used=billing_amount
                                        else:
                                            credit_used=credit

                                        remaining_credit=credit-credit_used

                                        
                                        
                                        c.execute("""insert into %s values (%%s,%%s,%%s,%%s)""" % (gutscheincode), (date_short, -credit_used,bestellnummer,"",))
                                        
                                        conn.commit()

                                        
                                c.execute ("""select * from %s """ % (gutscheincode))

                                gutscheincode=c.fetchall()                                       


                                for row in gutscheincode:
                                    if row[3]!="" and credit==15 and row[3]!="nicht anzeigen":

                                        c.execute("""update %s set gutscheinwert=%%s, bestellnummer=%%s where gutscheincodedesanderen=%%s""" % (row[3]),(15,"",gutscheincode,))
                                        conn.commit()


                                        c.execute ("""select * from userdaten """)

                                        userdaten=c.fetchall()

                                        for row_2 in userdaten:

                                            if row_2[11]==row[3]:
          
                                                credit_=row_2[10]+15

                                                c.execute("""update userdaten set credit=%s where gutscheincode=%s""",(str(credit_),(row[3]),))
                                            conn.commit()


                            stylecode=""
                            colorcode=""


                            c.execute ("""select * from %s""" % (session_id))

                            sessionid_table=c.fetchall()

                                        

                            
                            for row in sessionid_table:
                                if quiz=="yes":
                                    if stylecode!= row[7] or colorcode!=row[4]:                               
                                        stylecode=row[7]
                                        colorcode=row[4]
     #                                   adapt_showroom(user,row[0],0.02)

                                c.execute("""insert into bewertungen values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (bestellnummer, row[0],row[4], "","","",gutscheincode,"","",row[2],row[3],))

                                
                                c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % ("bewertungen_"+row[7]+"_"+row[4]), (bestellnummer, namebewerter, "","","","",gutscheincode,"",row[2],row[3],))
                                conn.commit()
     #                       if quiz=="yes":
    #                            generate_showroom(x)
                                
                            

                            print("session_id_")
                            print(session_id_)

                            c.execute("ALTER TABLE "+session_id+" RENAME TO "+session_id_)
                            
                            c.execute("""create table %s (
                                date text,
                                time text,
                                location text,
                                content text,
                                trackingcode text,
                                supplier text)""" % (session_id_+"_VF"))
      
                            a=get_time_stamp_now()

                            print("ASDW")                                                                                                                        
                            conn.commit()
                            c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s)""" % (session_id_+"_VF"), (date_short,a.strftime('%H:%M'),"Berlin, Deutschland","Ware wurde bestellt","#123123","DHL",))
                            c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s)""" % (session_id_+"_VF"), ("7. April 2017",a.strftime('%H:%M'),"Berlin, Deutschland","Ware wurde losgeschickt","#123123","DHL",))
                            c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s)""" % (session_id_+"_VF"), ("7. April 2017","13:35","Berlin, Deutschland","Ware ist angekommen","#123123","DHL",))
                            conn.commit()

                        

                            session_id_old=session_id

                            c.execute("""create table %s (
                                style text,
                                anzahl int,
                                bhgroesse text,
                                slipgroesse text,
                                color text,
                                freiemenge int,
                                status text,
                                stylecode text,
                                preis float)""" % (session_id))
                            c.execute("""delete from %s where bestellnummer=%%s"""% ("pending_payments"),(bestellnummer,))
                            conn.commit()



                            print("ASDW")
                            
                            
                            a=get_time_stamp_now()
                            c.execute("""update aktuellewarenkoerbe set datestamp=%s, tablename=%s where tablename=%s""",(a.strftime('%Y-%m-%d %H:%M'),session_id,session_id_old,))
                            conn.commit()

                            print("ASDW")


                    else:


                        c.execute ("""select * from userdaten """)

                        userdaten=c.fetchall()

                        for row in userdaten:
                            if row[9]==session_id and session_id!="None":
                                c.execute("""delete from %s where gutscheinwert=%%s and bestellnummer=%%s and gutscheincodedesanderen=%%s"""% (rabattcode_geworben),(0,"",row[11],))
                                c.execute("""delete from %s where gutscheinwert=%%s and bestellnummer=%%s and gutscheincodedesanderen=%%s"""% (row[11]),(15,"",rabattcode_geworben,))

                                c.execute("""update userdaten set credit=%s, geworben=%s, genutztergutscheincode=%s where lastsessionid=%s""",(str(0),"nein","",session_id,))
                        
                                conn.commit()
                                status_="kann nicht geworben werden"





@csrf_exempt
def warenkorb_aufrufen(request):

    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                            password='okano1988',database='maxfischer2database')

    c = conn.cursor(buffered=True)

    x=str(request.session.session_key)
#    try:

    modelAB=""
    sub_picture=""
    c.execute ("""select * from userdaten """)
    for row in c:
        if row[9]==x and x!="None":
            modelAB=row[47]
            sub_picture=row[48]


    if modelAB=="" or sub_picture=="":
        log_out_do_it(x,c,conn)
        request.session.create()
        x=str(request.session.session_key)
        create_user(x,c,conn)

        x=str(request.session.session_key)
        
        c.execute ("""select * from userdaten """)
        for row in c:
            if row[9]==x and x!="None":
                modelAB=row[47]
                sub_picture=row[48]

    b=""
    max_var_warenkorb =7


    warenkorb=define_warenkorb(x,modelAB,sub_picture,c)



    status=1
    try:
        c.execute ("""select * from %s""" % (x))

        cart_gesamt=0
        for row_2 in c:
            cart_gesamt=cart_gesamt+row_2[1]
    except:
        status=0

    

    c.execute ("""select * from userdaten """)

    userdaten=c.fetchall()
    credit=0
    adressbuch=""
    email="not ok"
    
    login=""
    VIP="false"
    gutscheinwert=0
    gutscheincode=""
    status=0

    
    for row in userdaten:
        print(row[11]+","+row[0])
        if row[9]==x and x!="None":
            credit=row[10]
            status=1
            storecredit=row[24]


            if row[21]!="":
  
                gutscheincode=row[21]
                gutscheinwert=gutscheinwert_abrufen(gutscheincode,c)
            shopping_type="VIP"
            if row[22]=="VIP" and row[23]=="true":
                VIP="true"
                shopping_type="VIP"
            
 #           if row[23]=="false":
#                shopping_type="VIP"
#            else:
#                shopping_type="Regular"
                
            bra_for_free=row[25]
            
            
            
            if row[0]!="":
                email="ok"
            if (row[0]!="" and row[12]!="") or (row[0]!="" and row[1]!=""):
                login="true"





    if len(warenkorb)!=2 and status==1:
        t=get_template('checkout.html')

        html=t.render({'favicon':get_favicon(),'brand_name':'Sensuals','title':"Checkout | Sensuals",'bestellungen':define_bestellung(x,"all",c),'shopping_type':shopping_type,'rebates':define_rebates(x,"","","","",c,conn),'storecredit':storecredit,'bra_for_free':bra_for_free,'VIP':VIP,'wishlist':define_wishlist(x,modelAB,sub_picture,c),'gutscheinwert':gutscheinwert,'gutscheincode':gutscheincode,'cart_gesamt':cart_gesamt,'warenkorb':warenkorb, 'credit':credit,'adressbuch':define_adressbuch(x,c),'zahlungsmethoden':define_zahlungsmethoden(x,c),'login':login,'email':email})
        return HttpResponse(html)
    else:
        return HttpResponseRedirect("/hello/start_page/")
    conn.close()
    update_timestamp(x,c,conn)



def get_favicon():
    return "/static/favicon.ico"

@csrf_exempt
def get_rebates(request):
    if request.is_ajax() and request.GET:
        bestellnummer=request.GET.get('bestellnummer')
        h=int(request.GET.get('item-length'))
        aenderung=request.GET.get('aenderung')
        n=request.GET.get('item')
        m=n.split(",")
        
        x=str(request.session.session_key)

        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='max',
                                password='okano1988',database='maxfischer2database')

        c = conn.cursor(buffered=True)

        rebates=define_rebates(x,bestellnummer,m,h,aenderung,c,conn)
        return HttpResponse(json.dumps(rebates), content_type='application/json')
        
    else:
        raise Http404

def gutscheinwert_abrufen(gutscheincode,c):

    gutscheinwert=0
    c.execute ("""select * from gutscheine """)
    for row in c:
        if row[0]==gutscheincode:
            gutscheinwert=float(row[1])

    return gutscheinwert

    

    

def monthToNum(shortMonth):

    return{
        'Januar' : 1,
        'Februar' : 2,
        'Maerz' : 3,
        'April' : 4,
        'Mai' : 5,
        'Juni' : 6,
        'Juli' : 7,
        'August' : 8,
        'September' : 9, 
        'October' : 10,
        'November' : 11,
        'Dezember' : 12
    }[shortMonth]

def warenkorb_anpassen(style,x,add_or_erase,anzahl,stylecode,colorcode,bh_groesse,slip_groesse,regular_price,subscription_price,c,conn):



    c.execute  ("""select * from %s""" % (x))
    current_cart_database=c.fetchall()

    

    existiert="nein"
    for row in current_cart_database:
        if bh_groesse!="":
            if row[0]==style and row[2]==bh_groesse and row[3]==slip_groesse and row[4]==colorcode:
                existiert="ja"
                break
        else:
            if row[0]==style and row[3]==slip_groesse and row[4]==colorcode:
                existiert="ja"
                break            



    if genuegend_warenmenge_vorhanden(x,style,"","",add_or_erase,anzahl,stylecode,colorcode,bh_groesse,slip_groesse,c)=="true":

        freiemenge=update_menu_table(x,style,"","",add_or_erase,anzahl,stylecode,colorcode,bh_groesse,slip_groesse,c,conn)
        update_detail_bestellung_table(x,style,"","",freiemenge,"Bestellt",existiert,add_or_erase,anzahl,stylecode,colorcode,bh_groesse,slip_groesse,regular_price,subscription_price,c,conn)
        return "ok"
    else:

        return "not ok"

        
        
@csrf_exempt
def warenkorb_abrufen(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='max',
                            password='okano1988',database='maxfischer2database')
    c = conn.cursor(buffered=True)
    
    x=str(request.session.session_key)
    warenkorb=define_warenkorb(x,modelAB,sub_picture,c)

    return HttpResponse(json.dumps(warenkorb), content_type='application/json')



def check_warenmenge(x,stylecode,colorcode,bh_groesse,slip_groesse,c):

    c.execute ("""select * from %s """ %(x))

    current_cart=c.fetchall()    
    anzahl=0

    for row in current_cart:
        if bh_groesse!="":
            if row[7]==stylecode and row[2]==bh_groesse and row[3]==slip_groesse and row[4]==colorcode:
                anzahl=int(row[1])
        else:
            if row[7]==stylecode and row[3]==slip_groesse and row[2]=="" and row[4]==colorcode:
                anzahl=int(row[1])                

    return anzahl

    

@csrf_exempt
def add_todo(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')

        c = conn.cursor(buffered=True)
        
        n=request.GET.get('item')
        gerichtname=request.GET.get('gerichtname')
        add_or_erase=request.GET.get('add_or_erase')
        anzahl=request.GET.get('anzahl')
        stylecode=request.GET.get('stylecode')
        colorcode=request.GET.get('colorcode')
        bh_groesse=request.GET.get('bh_groesse')
        slip_groesse=request.GET.get('slip_groesse')
        regular_price=request.GET.get('regular_price')
        subscription_price=request.GET.get('subscription_price')
        slip_groesse_2=request.GET.get('slip_groesse_2')
        
        bh_groesse_helf=bh_groesse
        slip_groesse_helf=slip_groesse
        gerichtname_helf=gerichtname
        warenkorb=""


        gerichtname_2=""
        c.execute ("""select * from lingerieselection """)
        for row in c:
            if row[11]==stylecode and row[12]==colorcode and gerichtname!=row[0]:
                gerichtname_2=row[0]




       
 #       try:
        
        if slip_groesse_2!="":
            i=0
        else:
            i=1


        print("slip_groesse_2")
        print(slip_groesse_2) 

        print("los")           
        while i<=1:
            x=str(request.session.session_key)
            
            if warenkorb!="maximum warenmenge" and warenkorb!="nicht genuegend warenmenge":
                print(i)
                print(gerichtname_2)
                if i==0 and gerichtname_2!="":
                    print("gerichtname_2")
                    print(gerichtname_2)
                    print("slip_groesse_2")
                    print(slip_groesse_2) 
                    bh_groesse=""
                    gerichtname=gerichtname_2
                    slip_groesse_2=slip_groesse_2.split(" ")
                    slip_groesse=slip_groesse_2[0]

                else:
                    bh_groesse=bh_groesse_helf
                    slip_groesse=slip_groesse_helf
                    gerichtname=gerichtname_helf
                
                

                
                    


                c.execute ("""select * from userdaten """)
                for row in c:
                    if row[9]==x and x!="None":
                        modelAB=row[47]
                        sub_picture=row[48]
                genuegend_warenmenge_vorhanden="false"
                
                if add_or_erase=="add":
                    if check_warenmenge(x,stylecode,colorcode,bh_groesse,slip_groesse,c)>=10:
                        warenkorb="maximum warenmenge"
                        
                if warenkorb=="":
                    if warenkorb_anpassen(gerichtname,x,add_or_erase,anzahl,stylecode,colorcode,bh_groesse,slip_groesse,regular_price,subscription_price,c,conn)=="ok":
                        if i==1:
                            warenkorb=define_warenkorb(x,modelAB,sub_picture,c)


                    else:
                        warenkorb="nicht genuegend warenmenge"
                
            else:

                i==2


            i=i+1
                

                




        update_timestamp(x,c,conn)

        return HttpResponse(json.dumps(warenkorb), content_type='application/json')
#       except:
        return HttpResponseRedirect("/hello/start_page/")

        
    else:
        raise Http404

@csrf_exempt
def quiz_abrufen(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                            password='okano1988',database='maxfischer2database')

    c = conn.cursor(buffered=True)

    
    x=str(request.session.session_key)





    showroom_stil = [[] for i in range(0)]
    showroom_color = [[] for i in range(0)]
    showroom_form = [[] for i in range(0)]
    showroom_position = [[] for i in range(0)]
    showroom_symmetrie = [[] for i in range(0)]
    showroom_sitz = [[] for i in range(0)]


    
    showroom_stil_names = [[] for i in range(0)]
    showroom_color_names = [[] for i in range(0)]
    showroom_form_names = [[] for i in range(0)]
    showroom_position_names = [[] for i in range(0)]
    showroom_symmetrie_names = [[] for i in range(0)]
    showroom_sitz_names = [[] for i in range(0)]




    x=str(request.session.session_key)
    c.execute ("""select * from userdaten """)
    for row in c:
        if row[9]==x and x!="None":
            quiztaken=row[26]

            showroom_stil.append(row[31])
            
            showroom_color.append(row[38])
            showroom_color.append(row[39])
            showroom_color.append(row[40])
            showroom_color.append(row[41])
            
            showroom_form.append(row[32])
            showroom_position.append(row[33])
            showroom_symmetrie.append(row[34])
            showroom_sitz.append(row[35])



            showroom_stil_names.append("sexy")
            showroom_stil_names.append("playful")
            showroom_stil_names.append("classiccute")
            showroom_stil_names.append("romantic")



            showroom_color_names.append("neutrals")
            showroom_color_names.append("bright")
            showroom_color_names.append("deep")
            showroom_color_names.append("printedpattern")

            showroom_form_names.append("Rund")
            showroom_form_names.append("Tropfenform")
            
            showroom_position_names.append("Mittig")
            showroom_position_names.append("Leicht Ost-West")
            showroom_position_names.append("Stark Ost-West")

            showroom_symmetrie_names.append("Symmetrisch")
            showroom_symmetrie_names.append("Asymmetrisch")


            showroom_sitz_names.append("Gestuetzt")
            showroom_sitz_names.append("Halb gestuetzt")
            showroom_sitz_names.append("Nach unten geneigt")

            cup=row[36]
            band=row[37]
            age=row[46]







            



    i=0
    stil_position=-1
    while i<=3:
        if showroom_stil_names[i]==showroom_stil[0]:
            stil_position=i
        i=i+1

    i=0
    color_0=-1
    color_1=-1
    color_2=-1
    color_3=-1
    
    while i<=3:
        if showroom_color[i]==1:
            if i==0:
                color_0=1
            if i==1:
                color_1=1
            if i==2:
                color_2=1
            if i==3:
                color_3=1

        i=i+1


    
    i=0
    form_position=-1
    while i<=1:
        if showroom_form_names[i]==showroom_form[0]:
            form_position=i
        i=i+1



    i=0
    position_position=-1
    while i<=2:
        if showroom_position_names[i]==showroom_position[0]:
            position_position=i
        i=i+1

        

        
    i=0
    symmetrie_position=-1
    while i<=1:
        if showroom_symmetrie_names[i]==showroom_symmetrie[0]:
            symmetrie_position=i
        i=i+1


    i=0
    sitz_position=-1
    while i<=2:
        if showroom_sitz_names[i]==showroom_sitz[0]:
            sitz_position=i
        i=i+1
        






    quiz = []


            
    class Quiz(object):
        def __init__(self,stil,color_0,color_1,color_2,color_3,form,position,symmetrie,sitz,quiztaken,cup,band,age):
            self.stil=stil
            self.color_0=color_0
            self.color_1=color_1
            self.color_2=color_2
            self.color_3=color_3
            self.form=form
            self.position=position
            self.symmetrie=symmetrie
            self.sitz=sitz
            self.quiztaken=quiztaken
            self.cup=cup
            self.band=band
            self.age=age
          
    quiz.append(Quiz(stil_position,color_0,color_1,color_2,color_3,form_position,position_position,symmetrie_position,sitz_position,quiztaken,cup,band,age,))


    
    json_string = json.dumps([Quiz.__dict__ for Quiz in quiz])

    return HttpResponse(json.dumps(json_string), content_type='application/json')


@csrf_exempt
def quiz_beenden(request):
        
    if request.is_ajax() and request.POST:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)
        quiztaken=request.POST.get('quiztaken')
        stil=request.POST.get('stil')
        color_0=request.POST.get('color_0')
        color_1=request.POST.get('color_1')
        color_2=request.POST.get('color_2')
        color_3=request.POST.get('color_3')
        form=request.POST.get('form')
        position=request.POST.get('position')
        symmetrie=request.POST.get('symmetrie')
        sitz=request.POST.get('sitz')
        cup=request.POST.get('cup')
        band=request.POST.get('band')
        age=request.POST.get('age')


        if cup=="" and band!="":
            band=""
        else:
            if cup!="" and band=="":
                cup=""

        
        x=str(request.session.session_key)
        if quiztaken=="no":
            c.execute ("""select * from userdaten """)
            for row in c:
                if row[9]==x and x!="None":
                    quiztaken==row[26]
                


        if quiztaken=="yes":
            c.execute("""update userdaten set quiztaken=%s where lastsessionid=%s""",("yes",x,))
        
        if stil=="0":
            c.execute("""update userdaten set sexy=%s, hotromance=%s, classiccute=%s, playful=%s, dominantfactorstyle=%s where lastsessionid=%s""",(0.5,0.25,0.1,0.15,"sexy",x,))
        if stil=="1":
            c.execute("""update userdaten set sexy=%s, hotromance=%s, classiccute=%s, playful=%s, dominantfactorstyle=%s where lastsessionid=%s""",(0.15,0.15,0.2,0.5,"playful",x,))
        if stil=="2":
            c.execute("""update userdaten set sexy=%s, hotromance=%s, classiccute=%s, playful=%s, dominantfactorstyle=%s where lastsessionid=%s""",(0.1,0.1,0.5,0.3,"classiccute",x,))
        if stil=="3":
            c.execute("""update userdaten set sexy=%s, hotromance=%s, classiccute=%s, playful=%s, dominantfactorstyle=%s where lastsessionid=%s""",(0.25,0.5,0.1,0.15,"romantic",x,))


        
        if color_0!="" or color_1!="" or color_2!="" or color_3!="":          
            c.execute("""update userdaten set neutrals=%s, bright=%s, deep=%s, printedpattern=%s, dominantfactorcolors=%s where lastsessionid=%s""",(float(color_0),float(color_1),float(color_2),float(color_3),"",x,))

        if form=="0":
            c.execute("""update userdaten set Form=%s where lastsessionid=%s""",("Rund",x,))
        if form=="1":
            c.execute("""update userdaten set Form=%s where lastsessionid=%s""",("Tropfenform",x,))



        if position=="0":
            c.execute("""update userdaten set Position=%s where lastsessionid=%s""",("Mittig",x,))
        if position=="1":
            c.execute("""update userdaten set Position=%s where lastsessionid=%s""",("Leicht Ost-West",x,))

        if position=="2":
            c.execute("""update userdaten set Position=%s where lastsessionid=%s""",("Stark Ost-West",x,))


        if symmetrie=="0":
            c.execute("""update userdaten set Symmetrie=%s where lastsessionid=%s""",("Symmetrisch",x,))
        if symmetrie=="1":
            c.execute("""update userdaten set Symmetrie=%s where lastsessionid=%s""",("Asymmetrisch",x,))


        if sitz=="0":
            c.execute("""update userdaten set Sitz=%s where lastsessionid=%s""",("Gestuetzt",x,))
        if sitz=="1":
            c.execute("""update userdaten set Sitz=%s where lastsessionid=%s""",("Halb gestuetzt",x,))

        if sitz=="2":
            c.execute("""update userdaten set Sitz=%s where lastsessionid=%s""",("Nach unten geneigt",x,))

        
        if cup!="-1":
            c.execute("""update userdaten set Cup=%s where lastsessionid=%s""",(cup,x,))


        if age!="-1":
            c.execute("""update userdaten set Age=%s where lastsessionid=%s""",(age,x,))

        if band!="-1":
            c.execute("""update userdaten set Band=%s where lastsessionid=%s""",(band,x,))

            
        conn.commit()
        
        if quiztaken=="yes":
            generate_showroom(x,c,conn)


        return HttpResponse(json.dumps(""), content_type='application/json')

def generate_showroom(session_id,c,conn):





    
    lingerie = [[] for i in range(20)]
    showroom_stil = [[] for i in range(0)]
    showroom_color = [[] for i in range(0)]
    showroom_padding = [[] for i in range(0)]
    showroom_shape = [[] for i in range(0)]

    
    showroom_stil_names = [[] for i in range(0)]
    showroom_color_names = [[] for i in range(0)]
    showroom_padding_names = [[] for i in range(0)]
    showroom_shape_names = [[] for i in range(0)]

    stil=[]
    color=[]

    
    for i in range(4):

        stil.append(0)
        color.append(0)




    c.execute ("""select * from userdaten """)

    userdaten=c.fetchall()



    for row in userdaten:
        if row[9]==session_id:
            showroom_stil.append(row[31])
            showroom_stil.append(row[27])
            showroom_stil.append(row[28])
            showroom_stil.append(row[29])
            showroom_stil.append(row[30])
            


            
            showroom_color.append(row[38])
            showroom_color.append(row[39])
            showroom_color.append(row[40])
            showroom_color.append(row[41])


            form=row[32]
            position=row[33]
            symmetrie=row[34]
            sitz=row[35]
            cup=row[36]
            band=row[37]






    zaehler=0
    k=0
    c.execute ("""select * from showroom_criteria """)

    showroom_criteria=c.fetchall() 

    for row in showroom_criteria:
        

        if row[0]==form and row[1]==position and row[2]==symmetrie and row[3]==sitz and (row[4]==cup or cup==""):
            c.execute ("""select * from lingerieselection """)

            lingerieselection=c.fetchall()            

            
            for row_2 in lingerieselection:
                

                if row_2[8]=="lingerie":
                    print(row_2[0])
                    print(str(row_2[36])+"=="+str(showroom_color[0]) +"and"+ str(showroom_color[0])+"!=0) or (")
                    print(str(row_2[37])+"=="+str(showroom_color[1]) +"and"+ str(showroom_color[1])+"!=0) or (")
                    print(str(row_2[38])+"=="+str(showroom_color[2]) +"and"+ str(showroom_color[2])+"!=0) or (")
                    print(str(row_2[39])+"=="+str(showroom_color[3]) +"and"+ str(showroom_color[3])+"!=0")
                    if (row_2[36]==showroom_color[0] and showroom_color[0]!=0) or (row_2[37]==showroom_color[1] and showroom_color[1]!=0) or (row_2[38]==showroom_color[2] and showroom_color[2]!=0) or (row_2[39]==showroom_color[3] and showroom_color[3]!=0):
                       print("next") 
                       if (row[5]==row_2[20] and row_2[20]!="") or (row[6]==row_2[21] and row_2[21]!="")  or (row[7]==row_2[22] and row_2[22]!="")  or (row[8]==row_2[23] and row_2[23]!="")  or (row[9]==row_2[24] and row_2[24]!="")  or (row[10]==row_2[25] and row_2[25]!=""):
                            print("next1")
                            print(row[16]+"=="+row_2[32] +"and"+ row_2[32]+"!=)  or ("+row[17]+"=="+row_2[33] +"and "+row_2[33]+"!=)  or ("+row[18]+"=="+row_2[34] +"and"+ row_2[34]+"!=)  or ("+row[19]+"=="+row_2[35] +"and"+ row_2[35]+"!=)")
                            if (row[16]==row_2[32] and row_2[32]!="")  or (row[17]==row_2[33] and row_2[33]!="")  or (row[18]==row_2[34] and row_2[34]!="")  or (row[19]==row_2[35] and row_2[35]!=""):
                                print("next2")
                                c.execute ("""select * from %s """ % ("stylecode_"+row_2[11]))
                                print("mengen")
                                stylecode_daten=c.fetchall() 

                                
                                for row_3 in stylecode_daten:

                                    if ((band+cup==row_3[3] or (cup=="")) and row_3[1]==row_2[11] and row_3[2]==row_2[12]) :
                                        menge=int(row_3[4])-int(row_3[5])
                                        print(menge)
                                        if menge>0: 


                                            i=0
                                            existiert="nein"
                                            while i <= zaehler-1:
     
                                                if lingerie[i][0]==row_2[11] and lingerie[i][1]==row_2[12]:
                                                    existiert="ja"
                                                i=i+1
                                            if existiert=="nein":
                                                if zaehler<=5:



                                                    lingerie[zaehler].append(row_2[11])       #style
                                                    lingerie[zaehler].append(row_2[12])       #color
                                                    zaehler=zaehler+1
                                                else:
                                                    if zaehler>5 and zaehler<10:

                                                        if row_2[19]==showroom_stil[0]:

                                                            lingerie[zaehler].append(row_2[11])       #style
                                                            lingerie[zaehler].append(row_2[12])       #color
                                                            zaehler=zaehler+1
          

        
    now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
    Y=now.year
    M=now.month
    D=now.day
    
    existiert="no"
    c.execute ("""select * from userdaten """)
    for row in c:
        if row[9]==session_id:
            gutscheincode=row[11]

               
    c.execute("""delete from %s where dayofshowroom=%%s and monthofshowroom=%%s and yearofshowroom=%%s""" % ("showroom_"+gutscheincode),(D,M,Y,))
    conn.commit()

    i=0

    while i<= zaehler-1:
        c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s)""" % ("showroom_"+gutscheincode),(lingerie[i][0],lingerie[i][1],D,M,Y,))
        i=i+1

    c.execute("""update userdaten set dayofshowroom=%s, monthofshowroom=%s, yearofshowroom=%s where lastsessionid=%s""",(D,M,Y,session_id,))
    conn.commit()


    





             



def link_to_detail_sites(request,offset,redirect_link):

    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                            password='okano1988',database='maxfischer2database')

    c = conn.cursor(buffered=True)





 

    x=str(request.session.session_key)
    e=""
 #   try:





########################################################################################################################################
            



    


    u=0



    c.execute ("""select * from userdaten """)

    userdaten=c.fetchall()

    x=str(request.session.session_key)
    status=0
    login=""
    print("userdaten_login")
    for row in userdaten:
        if row[9]==x and x!="None":
            if (row[0]!="" and row[12]!="") or (row[0]!="" and row[1]!=""):
                login="true"

    x=request.session.session_key

    update_timestamp(x,c,conn)
    
    x=str(request.session.session_key)
    c.execute ("""select * from userdaten """)

    userdaten=c.fetchall()

    for row in userdaten:
        if row[9]==x and x!="None":
            user=row[11]
            facebookid=row[12]
            quiz=row[26]
            modelAB=row[47]
            sub_picture=row[48]


            print(x)
            if row[22]=="VIP" and row[23]=="true":
                VIP="VIP"
            else:
                VIP="Regular"



    try:
    
        t=get_template('gericht_template.html')
        lingerie=get_lingerie_selection_filter(link_group_bestimmen(offset,c),"","","","",user,redirect_link,"","","","","","","","",modelAB,sub_picture,c)

        if len(lingerie)!=2:



            
            html=t.render({'favicon':get_favicon(),'brand_name':'Sensuals','pricesforaddlpanty':get_pricesforaddlpanty(redirect_link,VIP,c),'VIP':VIP,'title':redirect_link+" | Sensuals",'bestellungen':define_bestellung(x,"all",c),'wishlist':define_wishlist(x,modelAB,sub_picture,c),'warenkorb':define_warenkorb(x,modelAB,sub_picture,c),'colors':get_other_colors("",redirect_link,"",c),'warenkorb':define_warenkorb(x,modelAB,sub_picture,c),'gesamtbewertung':get_lingerie_selection_gesamtbewertung(redirect_link,c),'bewertungen_detail':get_lingerie_selection_bewertungen(redirect_link,c),'sizes':get_lingerie_selection_sizes(redirect_link,link_group_bestimmen(offset,c),c),'index':offset, 'login':login,'lingerie_offerings':lingerie,'url':get_link_positioining(offset,c),'links':get_links(x,c)})
            
            return HttpResponse(html)
        else:
            return HttpResponseRedirect("/hello/start_page/")

    except:

        return HttpResponseRedirect("/hello/start_page/")
#    




    ###sicherstellen, dass kein gutscheincode von jemandem eingegeben werden kann, der weniger lange dabei ist, als derjenige, der geworben wird




@csrf_exempt
def big_data_initial_input_detailed_page(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)


        stylecode=request.GET.get('stylecode')
        colorcode=request.GET.get('colorcode')
        windowwidth=request.GET.get('windowwidth')
        windowheight=request.GET.get('windowheight')

        x=str(request.session.session_key)
        c.execute ("""select * from userdaten """)
        for row in c:
            if row[9]==x and x!="None":
                user=row[11]
                facebookid=row[12]
                modelAB=row[47]
                sub_picture=row[48]
                
        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        Monat = ["Januar", "Februar", "Maerz", "April","Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
        now_date=str(now.day)+". "+str(Monat[now.month-1])+" "+str(now.year)
        Y=now.year
        M=now.month
        D=now.day
        H=now.hour
        Mi=now.minute
        time = datetime.datetime.strptime(str(Y)+"-"+str(M)+"-"+str(D)+" "+str(H)+":"+str(Mi), "%Y-%m-%d %H:%M")
        c.execute("""insert into Big_data_click_on_image values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(user,facebookid,modelAB,sub_picture,now_date,time,windowwidth,windowheight,stylecode,colorcode,"","","","",))
        conn.commit()

        return HttpResponse(json.dumps(""), content_type='application/json')
        
    else:
        raise Http404




@csrf_exempt
def big_data_farbe_click(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)


        stylecode=request.GET.get('stylecode')
        colorcode=request.GET.get('colorcode')
        farbe=request.GET.get('farbe')
        windowwidth=request.GET.get('windowwidth')
        windowheight=request.GET.get('windowheight')
            
        x=str(request.session.session_key)
        c.execute ("""select * from userdaten """)
        for row in c:
            if row[9]==x and x!="None":
                user=row[11]
                facebookid=row[12]
                modelAB=row[47]
                sub_picture=row[48]
                
        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        Monat = ["Januar", "Februar", "Maerz", "April","Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
        now_date=str(now.day)+". "+str(Monat[now.month-1])+" "+str(now.year)
        Y=now.year
        M=now.month
        D=now.day
        H=now.hour
        Mi=now.minute
        time = datetime.datetime.strptime(str(Y)+"-"+str(M)+"-"+str(D)+" "+str(H)+":"+str(Mi), "%Y-%m-%d %H:%M")
        c.execute("""insert into Big_data_click_on_image values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(user,facebookid,modelAB,sub_picture,now_date,time,windowwidth,windowheight,stylecode,colorcode,"","","",farbe,))
        conn.commit()

        return HttpResponse(json.dumps(""), content_type='application/json')
        
    else:
        raise Http404

@csrf_exempt
def big_data_picture_clicked(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)


        stylecode=request.GET.get('stylecode')
        colorcode=request.GET.get('colorcode')
        pictureclicked=request.GET.get('pictureclicked')

        windowwidth=request.GET.get('windowwidth')
        windowheight=request.GET.get('windowheight')
            
        x=str(request.session.session_key)
        c.execute ("""select * from userdaten """)
        for row in c:
            if row[9]==x and x!="None":
                user=row[11]
                facebookid=row[12]
                modelAB=row[47]
                sub_picture=row[48]
                
        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        Monat = ["Januar", "Februar", "Maerz", "April","Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
        now_date=str(now.day)+". "+str(Monat[now.month-1])+" "+str(now.year)
        Y=now.year
        M=now.month
        D=now.day
        H=now.hour
        Mi=now.minute
        time = datetime.datetime.strptime(str(Y)+"-"+str(M)+"-"+str(D)+" "+str(H)+":"+str(Mi), "%Y-%m-%d %H:%M")
        
        c.execute("""insert into Big_data_click_on_image values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(user,facebookid,modelAB,sub_picture,now_date,time,windowwidth,windowheight,stylecode,colorcode,pictureclicked,"","","",))
        conn.commit()

        return HttpResponse(json.dumps(""), content_type='application/json')
        
    else:
        raise Http404  



@csrf_exempt
def big_data_cart_put(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)


        stylecode=request.GET.get('stylecode')
        colorcode=request.GET.get('colorcode')
        putincart=request.GET.get('putincart')
        windowwidth=request.GET.get('windowwidth')
        windowheight=request.GET.get('windowheight')
            
        x=str(request.session.session_key)
        c.execute ("""select * from userdaten """)
        for row in c:
            if row[9]==x and x!="None":
                user=row[11]
                facebookid=row[12]
                modelAB=row[47]
                sub_picture=row[48]
                
        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        Monat = ["Januar", "Februar", "Maerz", "April","Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
        now_date=str(now.day)+". "+str(Monat[now.month-1])+" "+str(now.year)
        Y=now.year
        M=now.month
        D=now.day
        H=now.hour
        Mi=now.minute
        time = datetime.datetime.strptime(str(Y)+"-"+str(M)+"-"+str(D)+" "+str(H)+":"+str(Mi), "%Y-%m-%d %H:%M")
        c.execute("""insert into Big_data_click_on_image values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(user,facebookid,modelAB,sub_picture,now_date,time,windowwidth,windowheight,stylecode,colorcode,"",putincart,"","",))
        conn.commit()

        return HttpResponse(json.dumps(""), content_type='application/json')
        
    else:
        raise Http404

@csrf_exempt
def big_data_wishlist_put(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)


        stylecode=request.GET.get('stylecode')
        colorcode=request.GET.get('colorcode')
        putinwishlist=request.GET.get('putinwishlist')
        windowwidth=request.GET.get('windowwidth')
        windowheight=request.GET.get('windowheight')
            
        x=str(request.session.session_key)
        c.execute ("""select * from userdaten """)
        for row in c:
            if row[9]==x and x!="None":
                user=row[11]
                facebookid=row[12]
                modelAB=row[47]
                sub_picture=row[48]
                
        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        Monat = ["Januar", "Februar", "Maerz", "April","Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
        now_date=str(now.day)+". "+str(Monat[now.month-1])+" "+str(now.year)
        Y=now.year
        M=now.month
        D=now.day
        H=now.hour
        Mi=now.minute
        time = datetime.datetime.strptime(str(Y)+"-"+str(M)+"-"+str(D)+" "+str(H)+":"+str(Mi), "%Y-%m-%d %H:%M")
        c.execute("""insert into Big_data_click_on_image values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(user,facebookid,modelAB,sub_picture,now_date,time,windowwidth,windowheight,stylecode,colorcode,"","",putinwishlist,"",))
        conn.commit()

        return HttpResponse(json.dumps(""), content_type='application/json')
        
    else:
        raise Http404



@csrf_exempt
def big_data_initial_input_main_page(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)



        windowwidth=request.GET.get('windowwidth')
        windowheight=request.GET.get('windowheight')
            
        x=str(request.session.session_key)
        c.execute ("""select * from userdaten """)
        for row in c:
            if row[9]==x and x!="None":
                user=row[11]
                facebookid=row[12]
                modelAB=row[47]
                sub_picture=row[48]
                
        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        Monat = ["Januar", "Februar", "Maerz", "April","Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
        now_date=str(now.day)+". "+str(Monat[now.month-1])+" "+str(now.year)
        Y=now.year
        M=now.month
        D=now.day
        H=now.hour
        Mi=now.minute
        time = datetime.datetime.strptime(str(Y)+"-"+str(M)+"-"+str(D)+" "+str(H)+":"+str(Mi), "%Y-%m-%d %H:%M")
        c.execute("""insert into Big_data_click_on_main_page values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(user,facebookid,modelAB,sub_picture,now_date,time,windowwidth,windowheight,"","","","","","",))
        conn.commit()





        
        return HttpResponse(json.dumps(""), content_type='application/json')
        
    else:
        raise Http404


@csrf_exempt
def big_data_wishlist_click_main_page(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)


        stylecode=request.GET.get('stylecode')
        colorcode=request.GET.get('colorcode')
        putinwishlist=request.GET.get('putinwishlist')
        position=request.GET.get('position')
        
        windowwidth=request.GET.get('windowwidth')
        windowheight=request.GET.get('windowheight')
            
        x=str(request.session.session_key)
        c.execute ("""select * from userdaten """)
        for row in c:
            if row[9]==x and x!="None":
                user=row[11]
                facebookid=row[12]
                modelAB=row[47]
                sub_picture=row[48]
                
        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        Monat = ["Januar", "Februar", "Maerz", "April","Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
        now_date=str(now.day)+". "+str(Monat[now.month-1])+" "+str(now.year)
        Y=now.year
        M=now.month
        D=now.day
        H=now.hour
        Mi=now.minute
        time = datetime.datetime.strptime(str(Y)+"-"+str(M)+"-"+str(D)+" "+str(H)+":"+str(Mi), "%Y-%m-%d %H:%M")
        c.execute("""insert into Big_data_click_on_main_page values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(user,facebookid,modelAB,sub_picture,now_date,time,windowwidth,windowheight,stylecode,colorcode,position,"",putinwishlist,"",))
        conn.commit()





        
        return HttpResponse(json.dumps(""), content_type='application/json')
        
    else:
        raise Http404



@csrf_exempt
def big_data_filter_click_main_page(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)



        filter=request.GET.get('filter')

        
        windowwidth=request.GET.get('windowwidth')
        windowheight=request.GET.get('windowheight')
            
        x=str(request.session.session_key)
        c.execute ("""select * from userdaten """)
        for row in c:
            if row[9]==x and x!="None":
                user=row[11]
                facebookid=row[12]
                modelAB=row[47]
                sub_picture=row[48]
                
        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        Monat = ["Januar", "Februar", "Maerz", "April","Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
        now_date=str(now.day)+". "+str(Monat[now.month-1])+" "+str(now.year)
        Y=now.year
        M=now.month
        D=now.day
        H=now.hour
        Mi=now.minute
        time = datetime.datetime.strptime(str(Y)+"-"+str(M)+"-"+str(D)+" "+str(H)+":"+str(Mi), "%Y-%m-%d %H:%M")
        c.execute("""insert into Big_data_click_on_main_page values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(user,facebookid,modelAB,sub_picture,now_date,time,windowwidth,windowheight,"","","",filter,"","",))
        conn.commit()





        
        return HttpResponse(json.dumps(""), content_type='application/json')
        
    else:
        raise Http404


@csrf_exempt
def big_data_color_click_main_page(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)


        stylecode=request.GET.get('stylecode')
        colorcode=request.GET.get('colorcode')
        farbe=request.GET.get('farbe')
        position=request.GET.get('position')
        
        windowwidth=request.GET.get('windowwidth')
        windowheight=request.GET.get('windowheight')
            
        x=str(request.session.session_key)
        c.execute ("""select * from userdaten """)
        for row in c:
            if row[9]==x and x!="None":
                user=row[11]
                facebookid=row[12]
                modelAB=row[47]
                sub_picture=row[48]
                
        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        Monat = ["Januar", "Februar", "Maerz", "April","Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
        now_date=str(now.day)+". "+str(Monat[now.month-1])+" "+str(now.year)
        Y=now.year
        M=now.month
        D=now.day
        H=now.hour
        Mi=now.minute
        time = datetime.datetime.strptime(str(Y)+"-"+str(M)+"-"+str(D)+" "+str(H)+":"+str(Mi), "%Y-%m-%d %H:%M")
        c.execute("""insert into Big_data_click_on_main_page values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(user,facebookid,modelAB,sub_picture,now_date,time,windowwidth,windowheight,stylecode,colorcode,position,"","",farbe,))
        conn.commit()





        
        return HttpResponse(json.dumps(""), content_type='application/json')
        
    else:
        raise Http404


@csrf_exempt
def big_data_picture_click_main_page(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database')
        c = conn.cursor(buffered=True)


        stylecode=request.GET.get('stylecode')
        colorcode=request.GET.get('colorcode')
        position=request.GET.get('position')
        
        windowwidth=request.GET.get('windowwidth')
        windowheight=request.GET.get('windowheight')
            
        x=str(request.session.session_key)
        c.execute ("""select * from userdaten """)
        for row in c:
            if row[9]==x and x!="None":
                user=row[11]
                facebookid=row[12]
                modelAB=row[47]
                sub_picture=row[48]
                
        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        Monat = ["Januar", "Februar", "Maerz", "April","Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
        now_date=str(now.day)+". "+str(Monat[now.month-1])+" "+str(now.year)
        Y=now.year
        M=now.month
        D=now.day
        H=now.hour
        Mi=now.minute
        time = datetime.datetime.strptime(str(Y)+"-"+str(M)+"-"+str(D)+" "+str(H)+":"+str(Mi), "%Y-%m-%d %H:%M")
        c.execute("""insert into Big_data_click_on_main_page values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(user,facebookid,modelAB,sub_picture,now_date,time,windowwidth,windowheight,stylecode,colorcode,position,"","","",))
        conn.commit()





        
        return HttpResponse(json.dumps(""), content_type='application/json')
        
    else:
        raise Http404
    





        
def adapt_showroom(user,style_name,percent):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                            password='okano1988',database='maxfischer2database')
    c = conn.cursor(buffered=True)


    c.execute ("""select * from lingerieselection """)
    for row in c:
        if row[0]==style_name:
            stil=row[19]
            color=row[35]
            shape=row[25]
            padding=row[30]
    

    showroom_stil = [[] for i in range(0)]
    showroom_color = [[] for i in range(0)]
    showroom_padding = [[] for i in range(0)]
    showroom_shape = [[] for i in range(0)]

    
    showroom_stil_names = [[] for i in range(0)]
    showroom_color_names = [[] for i in range(0)]
    showroom_padding_names = [[] for i in range(0)]
    showroom_shape_names = [[] for i in range(0)]


    c.execute ("""select * from userdaten """)
    for row in c:

        if row[11]==user:


            
            
            showroom_stil_names.append("sexy")
            showroom_stil_names.append("romantic")
            showroom_stil_names.append("classiccute")
            showroom_stil_names.append("playful")

            showroom_color_names.append("neutrals")
            showroom_color_names.append("bright")
            showroom_color_names.append("deep")
            showroom_color_names.append("printedpattern")

            showroom_shape_names.append("demi")
            showroom_shape_names.append("balconette")
            showroom_shape_names.append("bralette")
            showroom_shape_names.append("plunge")
            showroom_shape_names.append("fullcoverage")

            showroom_padding_names.append("unlined")
            showroom_padding_names.append("lightlylined")
            showroom_padding_names.append("padded")
            showroom_padding_names.append("2cups")
            
            i=0
            stil_dominant=0
            delta=0
            teiler=3
            while i<=3:
                if showroom_stil_names[i]!=stil:
                    if row[27+i]==0:
                        teiler=max(teiler-1,1)
                i=i+1
            i=0
            while i<=3:
                if(delta<min(max(0,row[27+i]+percent),100)):
                    delta=min(max(0,row[27+i]+percent),100)
                    stil_dominant=i
                        
                if showroom_stil_names[i]==stil:
                    showroom_stil.append(min(max(0,row[27+i]+percent),100))
                else:
                    showroom_stil.append(min(max(0,row[27+i]-percent/teiler),100))
                i=i+1



            
            i=0
            color_dominant=0
            delta=0
            teiler=3
            while i<=3:
                if showroom_color_names[i]!=color:
                    if row[44+i]==0:
                        teiler=max(teiler-1,1)
                i=i+1
            i=0
            
            while i<=3:
                if(delta<min(max(0,row[44+i]+percent),100)):
                    delta=min(max(0,row[44+i]+percent),100)
                    color_dominant=i
                if showroom_color_names[i]==color:
                    showroom_color.append(min(max(0,row[44+i]+percent),100))
                else:
                    showroom_color.append(min(max(0,row[44+i]-percent/teiler),100))
                i=i+1

            i=0
            padding_dominant=0
            delta=0
            teiler=3
            while i<=3:
                
                if showroom_padding_names[i]!=padding:

                    if row[38+i]==0:
                        teiler=max(teiler-1,1)
                i=i+1
            i=0
            
            while i<=3:
                if(delta<min(max(0,row[39+i]+percent),100)):
                    delta=min(max(0,row[39+i]+percent),100)
                    padding_dominant=i
                if showroom_padding_names[i]==padding:
                    showroom_padding.append(min(max(0,row[39+i]+percent),100))
                else:
                    showroom_padding.append(min(max(0,row[39+i]-percent/teiler),100))
                i=i+1

            i=0
            padding_shape=0
            delta=0
            teiler=4
            while i<=4:
                if showroom_shape_names[i]!=shape:
                    if row[33+i]==0:
                        teiler=max(teiler-1,1)
                i=i+1
            i=0
            
            while i<=4:
                if(delta<min(max(0,row[33+i]+percent),100)):
                    delta=min(max(0,row[33+i]+percent),100)
                    shape_dominant=i
                if showroom_shape_names[i]==shape:
                    showroom_shape.append(min(max(0,row[33+i]+percent),100))
                else:
                    showroom_shape.append(min(max(0,row[33+i]-percent/teiler),100))
                i=i+1


    c.execute ("""select * from userdaten """)

    userdaten=c.fetchall()

    for row in userdaten:
        if row[11]==user:
            x=row[9]
            c.execute("""update userdaten set dominantfactorstyle=%s, sexy=%s, hotromance=%s, classiccute=%s, playful=%s where gutscheincode=%s""",(showroom_stil_names[stil_dominant],showroom_stil[0],showroom_stil[1],showroom_stil[2],showroom_stil[3],user,))
            c.execute("""update userdaten set dominantfactorshape=%s, demi=%s, balconette=%s, bralette=%s, plunge=%s, fullcoverage=%s where gutscheincode=%s""",(showroom_shape_names[shape_dominant],showroom_shape[0],showroom_shape[1],showroom_shape[2],showroom_shape[3],showroom_shape[4],user,))
            c.execute("""update userdaten set dominantfactorpadding=%s,unlined=%s, lightlylined=%s, padded=%s, 2cups=%s where gutscheincode=%s""",(showroom_padding_names[padding_dominant],showroom_padding[0],showroom_padding[1],showroom_padding[2],showroom_padding[3],user,))
            c.execute("""update userdaten set dominantfactorcolors=%s,neutrals=%s, bright=%s, deep=%s, printedpattern=%s where gutscheincode=%s""",(showroom_color_names[color_dominant],showroom_color[0],showroom_color[1],showroom_color[2],showroom_color[3],user,))
            conn.commit()

            

    generate_showroom(x,c,conn)





@csrf_exempt
def index_2(request,offset):


    html=""
    i=0
    max=0
    u=1

    
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                            password='okano1988',database='maxfischer2database')



    c = conn.cursor(buffered=True)

    print("ASD")

        

    
    x=str(request.session.session_key)

    if(u==1):
        c.execute("""drop table if exists lingerieselection""")
        c.execute("""drop table if exists offerings""")   

        c.execute("""drop table if exists bestellt""")
        c.execute("""drop table if exists gutscheine""")

        c.execute("""drop table if exists userdaten""")

        c.execute("""drop table if exists zahlungsmethoden""")
        c.execute("""drop table if exists bewertungen""")
        c.execute("""drop table if exists gutscheineverschickt""")
        c.execute("""drop table if exists gutscheinkonto""")
        c.execute("""drop table if exists adressbuch""")
        c.execute("""drop table if exists plz""")
        c.execute("""drop table if exists stylelibrary""")
        c.execute("""drop table if exists keyuserdaten""")
        c.execute("""drop table if exists kalender""")
        c.execute("""drop table if exists Janet""")
        c.execute("""drop table if exists links""")
        c.execute("""drop table if exists stylecode_AAA""")
        c.execute("""drop table if exists stylecode_AAB""")
        c.execute("""drop table if exists stylecode_AAC""")
        c.execute("""drop table if exists stylecode_AAD""")
        c.execute("""drop table if exists stylecode_AAE""")
        c.execute("""drop table if exists stylecode_AAF""")
        c.execute("""drop table if exists stylecode_AAG""")
        c.execute("""drop table if exists stylecode_AAH""")
        c.execute("""drop table if exists stylecode_geschenkkarte""")


        
        
        
        c.execute("""drop table if exists bewertungen_AAA_111""")
        c.execute("""drop table if exists bewertungen_AAB_112""")
        c.execute("""drop table if exists bewertungen_AAB_113""")
        c.execute("""drop table if exists geschenkkarte_50""")
        c.execute("""drop table if exists geschenkkarte_20""")
        c.execute("""drop table if exists Big_data_click_on_image""")


        c.execute("""drop table if exists picturelibrary_AAA_110""")
        c.execute("""drop table if exists picturelibrary_AAA_111""")
        c.execute("""drop table if exists picturelibrary_AAB_112""")
        c.execute("""drop table if exists picturelibrary_AAB_113""")
        c.execute("""drop table if exists picturelibrary_AAC_114""")
        c.execute("""drop table if exists picturelibrary_AAC_115""")
        c.execute("""drop table if exists picturelibrary_AAD_116""")
        c.execute("""drop table if exists picturelibrary_AAD_117""")
        c.execute("""drop table if exists picturelibrary_AAD_118""")
        c.execute("""drop table if exists picturelibrary_AAE_119""")
        c.execute("""drop table if exists picturelibrary_AAF_120""")
        c.execute("""drop table if exists picturelibrary_AAF_121""")
        c.execute("""drop table if exists picturelibrary_AAF_122""")
        c.execute("""drop table if exists picturelibrary_AAG_123""")
        c.execute("""drop table if exists picturelibrary_AAG_124""")
        c.execute("""drop table if exists picturelibrary_AAG_125""")
        c.execute("""drop table if exists picturelibrary_AAH_126""")
        c.execute("""drop table if exists picturelibrary_AAH_127""")
        c.execute("""drop table if exists picturelibrary_AAH_128""")
        c.execute("""drop table if exists picturelibrary_AAC_129""")

        c.execute("""drop table if exists picturelibrary_geschenkkarte_50""")
        c.execute("""drop table if exists picturelibrary_geschenkkarte_20""")

        
        c.execute("""drop table if exists geschenkkarte_50""")
        c.execute("""drop table if exists geschenkkarte_20""")

        
        c.execute("""drop table if exists VIPmembers""")
        c.execute("""drop table if exists ruecksendungen""")
        c.execute("""drop table if exists showroom_criteria""")

        c.execute("""drop table if exists color""")
        c.execute("""drop table if exists style""")
        c.execute("""drop table if exists stylepanty""")
        c.execute("""drop table if exists padding""")
        c.execute("""drop table if exists pending_payments""")
        
        c.execute("""drop table if exists feature""") 
        c.execute("""drop table if exists sizes""")
        c.execute("""drop table if exists sizespanty""")
        c.execute("""drop table if exists Big_data_click_on_main_page""")
        c.execute("""drop table if exists VIPchangelog""")
        c.execute("""drop table if exists gutscheincodes_sent""")
        
        
        
                
        
        c.execute("""drop table if exists %s""" % (x))
        




        
    


        conn.commit()
        
        c.execute("""create table userdaten (
            email text,
            passwort text,
            vorname text,                
            nachname text,
            lastadresse text,
            lastplz text,
            laststadt text,            
            userbildlink text,
            telefon text,
            lastsessionid text,
            credit float,
            gutscheincode text,
            facebookid text,
            maxalter text,
            minalter text,
            geschlecht text,
            adressbuch text,
            zahlungsmethoden text,
            geworben text,
            datum text,
            persmsbenachrichtigtwerden text,
            genutztergutscheincode text,
            shoppingtype text,
            shoppingtypeentschieden text,
            storecredit float,
            numberofbraforfree int,
            quiztaken text,
            sexy float,
            hotromance float,
            classiccute float,
            playful float,
            dominantfactorstyle text,
            Form text,
            Position text,
            Symmetrie text,
            Sitz text,
            Cup text,
            Band text,
            neutrals float,
            bright float,
            deep float,
            printedpattern float,
            dominantfactorcolors text,
            dayofshowroom text,
            monthofshowroom text,
            yearofshowroom text,
            age text,
            modelAB int,
            subpicture int,
            newslettersignedup text,
			clientidpaymill text)""")



        print("ASDaaa1")


        c.execute("""create table pending_payments (
            sessionid text,
            accepted text,
            bestellnummer text,
            adresse text,
            stadt text,
            plz text,
            unternehmensdetails text,
            vorname text,
            nachname text,
            telefonnummer text,
            lieferdetails text,
            zahlungsoption text,
            preis text,
            lieferkosten text,
            rabatt text,
            rabattcode text,
            warenkorbgerichte text,
            warenkorbanzahl text,
            warenkorbgroesse text,
            selectedzahlungsoption text,
            shoppingtype text,
            braforfreecount text,
            braforfreevalue text,
            storecredittobeused text,
            transaktionsnummer text)""")

        
        c.execute("""create table keyuserdaten (
            email text,
            telefon text,
            kreditkartennummer text,
            paypalkonto text,
            girokontonummer text,
            gutscheincode text)""")



        c.execute("""create table VIPchangelog (
            month text,
            year text)""")

        c.execute("""create table gutscheincodes_sent (
            gutscheincode text,
            date text,
            time text,
            email text,
            emailsent text,
            emailsentdate text,
            emailsenttime text,
            message text,
            betreff text,
            emailsender text)""")

        print("ASDaaa2")
        
        c.execute("""create table ruecksendungen (
            id text,
            gutscheincode text,
            bestellnummer text,
            dateofproposal text,
            dateofmaxreturn text,
            deliverycode text,
            grund text,
            stylecode text,
            colorcode text,          
            anzahl int,
            priceperpiece float,
            gesamt float,
            wareerhalten text,
            geldzurueckueberwiesen text,
            status text,
            bhgroesse text,
            slipgroesse text)""")

        c.execute("""create table lingerieselection (
                name text,
                sizerange text,
                pantytype text,
                priceregular float,
                pricesubscription float,
                description text,
                details text,
                active text,
                productgroup text,
                descriptionshort text,
                detaildatabase text,
                stylecode text,
                colorcode text,
                bargainpricereduction float,
                bargainpriceactive text,
                sexy float,
                hotromance float,
                classiccute float,
                playful float,
                dominantfactorstyle text,
                StyleTShirtOrHipster text,
                StylePlungeOrCheeky text,
                StyleBalconetteOrTanga text,
                StyleBralette text,
                StyleFull text,
                StyleDemi text,
                FeatureStrapless text,
                FeatureRacerback text,
                FeatureLongline text,
                FeatureWirefree text,
                FeatureTriangle text,
                FeatureNone text,
                PaddingUnlined text,
                PaddingLightlypadded text,
                PaddingPushup text,
                Padding2cupslarger text,
                neutrals float,
                bright float,
                deep float,
                printedpattern float,
                dominantfactorcolors text,
                color int,
                position int)""")

        print("ASDaaa3")
        c.execute ("""ALTER TABLE lingerieselection ADD FULLTEXT(name,sizerange,description,descriptionshort,productgroup,dominantfactorcolors,dominantfactorstyle,details)""")       


        c.execute("""create table showroom_criteria (
                Form text,
                Position text,
                Symmetrie text,
                Sitz text,
                Cup text,
                StyleTShirt text,
                StylePlunge text,
                StyleBalconette text,
                StyleBralette text,
                StyleFull text,
                StyleDemi text,
                FeatureStrapless text,
                FeatureRacerback text,
                FeatureLongline text,
                FeatureWirefree text,
                FeatureTriangle text,
                PaddingUnlined text,
                PaddingLightlypadded text,
                PaddingPushup text,
                Padding2cupslarger text)""")

        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Symmetrisch","Halb gestuetzt","B","x","x","x","","","x","x","","x","","","","x","","")""")


        c.execute("""create table Big_data_click_on_image (
                gutscheincode text,
                facebookid text,
                modelAB int,
                subpicture int,
                date text,
                time text,
                windowwidth text,
                windowheight text,
                stylecode text,
                colorcode text,
                pictureclicked text,
                putincart text,
                putinwishlist text,
                othercolorclicked text)""")



        c.execute("""create table Big_data_click_on_main_page (
                gutscheincode text,
                facebookid text,
                modelAB int,
                subpicture int,
                date text,
                time text,
                windowwidth int,
                windowheight int,
                stylecode text,
                colorcode text,
                positionofpicture text,
                filterclicked text,
                putinwishlist text,
                othercolorclicked text)""")


        
        
        c.execute("""create table VIPmembers (
                gutscheincode text,
                active text,
                membersince text,
                nextvipmonth text,
                lastskippedmonth text,
                lastskippedyear text,
                purchases float,
                purchaseslastmonth text,
                purchaseslastyear text,
                purchasedsincestart int)""")



        
        c.execute("""create table stylelibrary (
                style text,
                colorcode text,
                detaildatabase text,
                pic text)""")

        c.execute("""create table color (
                colordeutsch text,
                colorid int)""")
        c.execute("""create table style (
                styledeutsch text,
                styleid int)""")


        c.execute("""create table stylepanty (
                styledeutsch text,
                styleid int)""")


        
        c.execute("""insert into color values ("Blau", "0")""")
        c.execute("""insert into color values ("Braun", "1")""")
        c.execute("""insert into color values ("Grau", "2")""")
        c.execute("""insert into color values ("Gruen", "3")""")
        c.execute("""insert into color values ("Hautfarben", "4")""")
        c.execute("""insert into color values ("Lila", "5")""")
        c.execute("""insert into color values ("Muster", "6")""")
        c.execute("""insert into color values ("Orange", "7")""")
        c.execute("""insert into color values ("Pink", "8")""")
        c.execute("""insert into color values ("Rot", "9")""")
        c.execute("""insert into color values ("Schwarz", "10")""")
        c.execute("""insert into color values ("Weiss", "11")""")


        

        print("ASDaaa4")
        c.execute("""insert into style values ("T-Shirt", "0")""")
        c.execute("""insert into style values ("Tiefer Ausschnitt", "1")""")
        c.execute("""insert into style values ("Balconette", "2")""")
        c.execute("""insert into style values ("Bralette", "3")""")
        c.execute("""insert into style values ("Vollschalen", "4")""")
        c.execute("""insert into style values ("Halbschale", "5")""")



        c.execute("""insert into stylepanty values ("Hipster", "0")""")
        c.execute("""insert into stylepanty values ("Cheeky", "1")""")
        c.execute("""insert into stylepanty values ("String Tanga", "2")""")




        c.execute("""create table padding (
                paddingdeutsch text,
                paddingid int)""")

        c.execute("""insert into padding values ("Ungefuettert", "0")""")
        c.execute("""insert into padding values ("Leicht gepolstert", "1")""")
        c.execute("""insert into padding values ("Gepolstert", "2")""")
        c.execute("""insert into padding values ("Doppelt gepolstert", "3")""")


        c.execute("""create table feature (
                featuredeutsch text,
                featureid int)""")
 
        c.execute("""insert into feature values ("Traegerlos", "0")""")
        c.execute("""insert into feature values ("Racerback", "1")""")
        c.execute("""insert into feature values ("Lang geschnitten", "2")""")
        c.execute("""insert into feature values ("Buegellos", "3")""")
        c.execute("""insert into feature values ("Triangle", "4")""")
        c.execute("""insert into feature values ("Kein Feature", "5")""")
 
 
        c.execute("""create table sizespanty (
                sizes text,
                featureid int)""") 
 


        c.execute("""insert into sizespanty values ("XS", "0")""")
        c.execute("""insert into sizespanty values ("S", "1")""")
        c.execute("""insert into sizespanty values ("M", "2")""")
        c.execute("""insert into sizespanty values ("L", "3")""")
        c.execute("""insert into sizespanty values ("XL", "4")""")


        
        c.execute("""create table sizes (
                cupband text,
                featureid int)""")
 
 

 
 
        get_cup = {
                   0 : 'A',
                   1 : 'B',
                   2 : 'C',
                   3 : 'D',
                   4 : 'E',
                   5 : 'F',
                   6 : 'G',
                   7 : 'H',
                   8 : 'I'

 
                  
                }              
        i=0
        zaehler_1=0
        zaehler_2=0
        zaehler_3=0
        unterbrust=65
       
        while(i<=4):
            
 
           

            cup=0

            
            while(cup<=5):
                cup_detail=get_cup[cup]
 
               
 
                c.execute("""insert into %s values (%%s,%%s)""" % ("sizes"),(str(unterbrust)+cup_detail,zaehler_3,))
                zaehler_3=zaehler_3+1

               
                cup=cup+1
               
            i=i+1
            unterbrust=unterbrust+5





        
        print("ASDaaa5")
 
        c.execute("""insert into stylelibrary values ("AAA", "110","Daphne","/static/janet_red.jpeg")""")
        c.execute("""insert into stylelibrary values ("AAA", "111","Janet","/static/janet_brown.jpeg")""")
        c.execute("""insert into stylelibrary values ("AAB", "112","Lilly","/static/janet_brown.jpeg")""")
        c.execute("""insert into stylelibrary values ("AAB", "113","Florina","/static/janet_brown.jpeg")""")
        c.execute("""insert into stylelibrary values ("AAC", "114","Kellie","/static/janet_brown.jpeg")""")
        c.execute("""insert into stylelibrary values ("AAC", "115","Allara","/static/janet_brown.jpeg")""")
        c.execute("""insert into stylelibrary values ("AAC", "129","Beatriz","/static/janet_brown.jpeg")""")
        c.execute("""insert into stylelibrary values ("AAD", "116","Ulrike","/static/janet_brown.jpeg")""")
        c.execute("""insert into stylelibrary values ("AAD", "117","Samantha","/static/janet_brown.jpeg")""")
        c.execute("""insert into stylelibrary values ("AAD", "118","Sina","/static/janet_brown.jpeg")""")
        c.execute("""insert into stylelibrary values ("AAE", "119","Lidia","/static/janet_brown.jpeg")""")
        c.execute("""insert into stylelibrary values ("AAF", "120","Bella","/static/janet_brown.jpeg")""")
        c.execute("""insert into stylelibrary values ("AAF", "121","Cheyanne","/static/janet_brown.jpeg")""")
        c.execute("""insert into stylelibrary values ("AAF", "122","Ilanni","/static/janet_brown.jpeg")""")
        c.execute("""insert into stylelibrary values ("AAG", "123","Alexsi","/static/janet_brown.jpeg")""")
        c.execute("""insert into stylelibrary values ("AAG", "124","Angelica","/static/janet_brown.jpeg")""")
        c.execute("""insert into stylelibrary values ("AAG", "125","Brinley","/static/janet_brown.jpeg")""")
 
        c.execute("""insert into stylelibrary values ("AAH", "126","Alandra","/static/janet_brown.jpeg")""")
        c.execute("""insert into stylelibrary values ("AAH", "127","Bianca","/static/janet_brown.jpeg")""")
        c.execute("""insert into stylelibrary values ("AAH", "128","Isadora","/static/janet_brown.jpeg")""")
 
 
        c.execute("""create table links (
                link text,
                name text,
                group1 text,
                group2 text,
                group3 text,
                pictureoverallsrc text,
                headlineoverall text,
                subtitleoverall text)""")
       
        c.execute("""insert into links values ("test", "BH & Slips","lingerie","","","/static/overall_picture_bra.jpg","BHs & Slips","Entdecke unsere neusten Trends & Styles")""")


        c.execute("""insert into links values ("test", "Slips","panties","","","/static/overall_picture_bra.jpg","Slips","Entdecke unsere aktuellen Slips")""")
        
        c.execute("""insert into links values ("test", "Mein Showroom","no","","","/static/overall_picture_bra.jpg","Dein Showroom","Entdecke Deinen Showroom")""")
        c.execute("""insert into links values ("test", "Geschenkkarten","geschenkkarten","","","/static/overall_picture_bra.jpg","Geschenkkarten","Verschenke einen Gutschein fuer die schoensten Lingerie Styles")""")
 


        
        c.execute("""insert into lingerieselection values ("Janet", "65A-85F","/static/Janet_1.jpg,/static/Janet_2.jpg,/static/Janet_3.jpg,/static/Janet_4.jpg,/static/Janet_5.jpg","34.95","24.95","With its plunging neckline and shimmering lace, nothing says sultry like our midnight magic Sveltana! This super sexy teddy features an open back, a cheeky lace bottom, and a playful tulle bow at your waist. Plus the halter and back closure adjust to create a flattering fit for every body type.","Unlined teddy<br>Fully adjustable straps","yes","lingerie"," sexy, coverage, unlined, bright ","Janet","AAA","111","10","false","0.7","0.1","0.1","0.1","sexy","","","","","x","","","","","","","x","x","","","","0.0","1.0","0.0","0.0","bright","9","0")""")
        c.execute("""insert into lingerieselection values ("Daphne", "65A-85F","/static/Daphne_1.jpg,/static/Daphne_2.jpg,/static/Daphne_3.jpg,/static/Daphne_4.jpg,/static/Daphne_5.jpg,/static/Daphne_6.jpg,/static/Daphne_7.jpg,/static/Daphne_8.jpg ","34.95","24.95","With its plunging neckline and shimmering lace, nothing says sultry like our midnight magic Sveltana! This super sexy teddy features an open back, a cheeky lace bottom, and a playful tulle bow at your waist. Plus the halter and back closure adjust to create a flattering fit for every body type.","Unlined teddy<br>Fully adjustable straps","yes","lingerie","sexy, coverage, unlined, deep","Daphne","AAA","110","10","false","0.7","0.1","0.1","0.1","sexy","","","","","x","","","","","","","x","x","","","","0.0","0.0","1.0","0.0","deep","10","1")""")
        c.execute("""insert into lingerieselection values ("Lilly", "65A-85F","/static/Lilly_1.jpg,/static/Lilly_2.jpg,/static/Lilly_3.jpg","34.95","24.95","With its plunging neckline and shimmering lace, nothing says sultry like our midnight magic Sveltana! This super sexy teddy features an open back, a cheeky lace bottom, and a playful tulle bow at your waist. Plus the halter and back closure adjust to create a flattering fit for every body type.","Unlined teddy<br>Fully adjustable straps","yes","lingerie","playful, balconette, padded, deep","Lilly","AAB","112","10","false","0.1","0.0","0.3","0.6","playful","","","x","","","","","","","","","x","","","x","","0.0","0.0","1.0","0.0","deep","2","2")""")
        c.execute("""insert into lingerieselection values ("Florina", "65A-85F","/static/Florina_1.jpg,/static/Florina_2.jpg,/static/Florina_3.jpg","34.95","24.95","With its plunging neckline and shimmering lace, nothing says sultry like our midnight magic Sveltana! This super sexy teddy features an open back, a cheeky lace bottom, and a playful tulle bow at your waist. Plus the halter and back closure adjust to create a flattering fit for every body type.","Unlined teddy<br>Fully adjustable straps","yes","lingerie","playful, balconette, padded, bright","Florina","AAB","113","10","false","0.1","0.0","0.3","0.6","playful","","","x","","","","x","","","","","","","","x","","0.0","1.0","0.0","0.0","bright","3","3")""")
        c.execute("""insert into lingerieselection values ("Kellie", "65A-85F","/static/Kellie_1.jpg,/static/Kellie_2.jpg,/static/Kellie_3.jpg,/static/Kellie_4.jpg,/static/Kellie_5.jpg,/static/Kellie_6.jpg","34.95","24.95","With its plunging neckline and shimmering lace, nothing says sultry like our midnight magic Sveltana! This super sexy teddy features an open back, a cheeky lace bottom, and a playful tulle bow at your waist. Plus the halter and back closure adjust to create a flattering fit for every body type.","Unlined teddy<br>Fully adjustable straps","yes","lingerie"," sexy, plunge, 2cups, bright","Kellie","AAC","114","10","false","0.7","0.3","0.0","0.0","sexy","x","","","","","","","x","","","","","","","x","","0.0","1.0","0.0","0.0","bright","3","4")""")
        c.execute("""insert into lingerieselection values ("Allara", "65A-85F","/static/Allara_1.jpg,/static/Allara_2.jpg,/static/Allara_3.jpg,/static/Allara_4.jpg,/static/Allara_5.jpg,/static/Allara_6.jpg","34.95","24.95","With its plunging neckline and shimmering lace, nothing says sultry like our midnight magic Sveltana! This super sexy teddy features an open back, a cheeky lace bottom, and a playful tulle bow at your waist. Plus the halter and back closure adjust to create a flattering fit for every body type.","Unlined teddy<br>Fully adjustable straps","yes","lingerie","sexy, plunge, padded, pattern","Allara","AAC","115","10","false","0.7","0.3","0.0","0.0","sexy","","x","","","","","","x","","","","","","","x","","0.0","0.0","0.0","1.0","printedpattern","6","5")""")
        c.execute("""insert into lingerieselection values ("Beatriz", "65A-85F","/static/Beatriz_1.jpg,/static/Beatriz_2.jpg,/static/Beatriz_3.jpg,/static/Beatriz_4.jpg,/static/Beatriz_5.jpg,/static/Beatriz_6.jpg","34.95","24.95","With its plunging neckline and shimmering lace, nothing says sultry like our midnight magic Sveltana! This super sexy teddy features an open back, a cheeky lace bottom, and a playful tulle bow at your waist. Plus the halter and back closure adjust to create a flattering fit for every body type.","Unlined teddy<br>Fully adjustable straps","yes","lingerie","sexy, plunge, padded, pattern","Beatriz","AAC","129","10","false","0.7","0.3","0.0","0.0","sexy","","x","","","","","","","","","","x","","","","x","0.0","0.0","0.0","1.0","printedpattern","0","6")""")
        c.execute("""insert into lingerieselection values ("Ulrike", "65A-85F","/static/Ulrike_1.jpg,/static/Ulrike_2.jpg,/static/Ulrike_3.jpg,/static/Ulrike_4.jpg,/static/Ulrike_5.jpg,/static/Ulrike_6.jpg","34.95","24.95","With its plunging neckline and shimmering lace, nothing says sultry like our midnight magic Sveltana! This super sexy teddy features an open back, a cheeky lace bottom, and a playful tulle bow at your waist. Plus the halter and back closure adjust to create a flattering fit for every body type.","Unlined teddy<br>Fully adjustable straps","yes","lingerie","romance, bralette, unlined, natural","Ulrike","AAD","116","10","false","0.2","0.8","0.0","0.0","romantic","","","","x","","","","","","x","","","x","","","","1.0","0.0","0.0","0.0","natural","8","7")""")
        c.execute("""insert into lingerieselection values ("Samantha", "65A-85F","/static/Samantha_1.jpg,/static/Samantha_2.jpg,/static/Samantha_3.jpg,/static/Samantha_4.jpg,/static/Samantha_5.jpg,/static/Samantha_6.jpg","34.95","24.95","With its plunging neckline and shimmering lace, nothing says sultry like our midnight magic Sveltana! This super sexy teddy features an open back, a cheeky lace bottom, and a playful tulle bow at your waist. Plus the halter and back closure adjust to create a flattering fit for every body type.","Unlined teddy<br>Fully adjustable straps","yes","lingerie","romance, bralette, unlined, deep ","Samantha","AAD","117","10","false","0.2","0.8","0.0","0.0","romantic","","","","x","","","","","","x","","","x","","","","0.0","0.0","1.0","0.0","deep","10","8")""")
        c.execute("""insert into lingerieselection values ("Sina", "65A-85F","/static/Sina_1.jpg,/static/Sina_2.jpg,/static/Sina_3.jpg,/static/Sina_4.jpg,/static/Sina_5.jpg,/static/Sina_6.jpg","34.95","24.95","With its plunging neckline and shimmering lace, nothing says sultry like our midnight magic Sveltana! This super sexy teddy features an open back, a cheeky lace bottom, and a playful tulle bow at your waist. Plus the halter and back closure adjust to create a flattering fit for every body type.","Unlined teddy<br>Fully adjustable straps","yes","lingerie"," romance, bralette, unlined, bright ","Sina","AAD","118","10","false","0.2","0.8","0.0","0.0","romantic","","","","x","","","","","","","","x","x","","","","0.0","1.0","0.0","0.0","bright","9","9")""")
        c.execute("""insert into lingerieselection values ("Lidia", "65A-85F","/static/Lidia_1.jpg,/static/Lidia_2.jpg,/static/Lidia_3.jpg,/static/Lidia_4.jpg,/static/Lidia_5.jpg,/static/Lidia_6.jpg,/static/Lidia_7.jpg","34.95","24.95","With its plunging neckline and shimmering lace, nothing says sultry like our midnight magic Sveltana! This super sexy teddy features an open back, a cheeky lace bottom, and a playful tulle bow at your waist. Plus the halter and back closure adjust to create a flattering fit for every body type.","Unlined teddy<br>Fully adjustable straps","yes","lingerie","sexy, plunge, padded, deep ","Lidia","AAE","119","10","false","0.9","0.1","0.0","0.0","sexy","x","","","","","","","x","","","","","","","x","","0.0","0.0","1.0","0.0","deep","10","10")""")
        c.execute("""insert into lingerieselection values ("Bella", "65A-85F","/static/Bella_1.jpg,/static/Bella_2.jpg,/static/Bella_3.jpg,/static/Bella_4.jpg,/static/Bella_5.jpg,/static/Bella_6.jpg,/static/Bella_7.jpg,/static/Bella_8.jpg ","34.95","24.95","With its plunging neckline and shimmering lace, nothing says sultry like our midnight magic Sveltana! This super sexy teddy features an open back, a cheeky lace bottom, and a playful tulle bow at your waist. Plus the halter and back closure adjust to create a flattering fit for every body type.","Unlined teddy<br>Fully adjustable straps","yes","lingerie"," classiccute, plunge, padded, deep ","Bella","AAF","120","10","false","0.0","0.2","0.5","0.3","classiccute","","x","","","","","","","","","","x","","","x","","0.0","0.0","1.0","0.0","deep","10","11")""")
        c.execute("""insert into lingerieselection values ("Cheyanne", "65A-85F","/static/Cheyanne_1.jpg,/static/Cheyanne_2.jpg,/static/Cheyanne_3.jpg,/static/Cheyanne_4.jpg,/static/Cheyanne_5.jpg,/static/Cheyanne_6.jpg,/static/Cheyanne_7.jpg,/static/Cheyanne_8.jpg ","34.95","24.95","With its plunging neckline and shimmering lace, nothing says sultry like our midnight magic Sveltana! This super sexy teddy features an open back, a cheeky lace bottom, and a playful tulle bow at your waist. Plus the halter and back closure adjust to create a flattering fit for every body type.","Unlined teddy<br>Fully adjustable straps","yes","lingerie"," classiccute, plunge, padded, deep ","Cheyanne","AAF","121","10","false","0.0","0.2","0.5","0.3","classiccute","","x","","","","","","","","","","x","","","x","","0.0","0.0","1.0","0.0","deep","10","12")""")
        c.execute("""insert into lingerieselection values ("Ilanni", "65A-85F","/static/Ilanni_1.jpg,/static/Ilanni_2.jpg,/static/Ilanni_3.jpg,/static/Ilanni_4.jpg,/static/Ilanni_5.jpg,/static/Ilanni_6.jpg","34.95","24.95","With its plunging neckline and shimmering lace, nothing says sultry like our midnight magic Sveltana! This super sexy teddy features an open back, a cheeky lace bottom, and a playful tulle bow at your waist. Plus the halter and back closure adjust to create a flattering fit for every body type.","Unlined teddy<br>Fully adjustable straps","yes","lingerie"," classiccute, plunge, padded, bright ","Cheyanne","AAF","122","10","false","0.0","0.2","0.5","0.3","classiccute","","x","","","","","","","","","","x","","","x","","0.0","1.0","0.0","0.0","bright","11","13")""")
        c.execute("""insert into lingerieselection values ("Alexsi", "65A-85F","/static/Alexsi_1.jpg,/static/Alexsi_2.jpg,/static/Alexsi_3.jpg,/static/Alexsi_4.jpg,/static/Alexsi_5.jpg,/static/Alexsi_6.jpg,/static/Alexsi_7.jpg ,/static/Alexsi_8.jpg","34.95","24.95","With its plunging neckline and shimmering lace, nothing says sultry like our midnight magic Sveltana! This super sexy teddy features an open back, a cheeky lace bottom, and a playful tulle bow at your waist. Plus the halter and back closure adjust to create a flattering fit for every body type.","Unlined teddy<br>Fully adjustable straps","yes","lingerie","sexy, balconette, padded, neutrals ","Alexsi","AAG","123","10","false","0.8","0.2","0.0","0.0","sexy","","","x","","","","","","","","","x","","","x","","1.0","0.0","0.0","0.0","natural","4","14")""")
        c.execute("""insert into lingerieselection values ("Angelica", "65A-85F","/static/Angelica_1.jpg,/static/Angelica_2.jpg,/static/Angelica_3.jpg,/static/Angelica_4.jpg,/static/Angelica_5.jpg,/static/Angelica_6.jpg,/static/Angelica_7.jpg ,/static/Angelica_8.jpg","34.95","24.95","With its plunging neckline and shimmering lace, nothing says sultry like our midnight magic Sveltana! This super sexy teddy features an open back, a cheeky lace bottom, and a playful tulle bow at your waist. Plus the halter and back closure adjust to create a flattering fit for every body type.","Unlined teddy<br>Fully adjustable straps","yes","lingerie","sexy, balconette, padded, bright ","Angelica","AAG","124","10","false","0.8","0.2","0.0","0.0","sexy","","","x","","","","","","","","","x","","","x","","0.0","1.0","0.0","0.0","bright","9","15")""")
        c.execute("""insert into lingerieselection values ("Brinley", "65A-85F","/static/Brinley_1.jpg,/static/Brinley_2.jpg,/static/Brinley_3.jpg,/static/Brinley_4.jpg,/static/Brinley_5.jpg,/static/Brinley_6.jpg","34.95","24.95","With its plunging neckline and shimmering lace, nothing says sultry like our midnight magic Sveltana! This super sexy teddy features an open back, a cheeky lace bottom, and a playful tulle bow at your waist. Plus the halter and back closure adjust to create a flattering fit for every body type.","Unlined teddy<br>Fully adjustable straps","yes","lingerie","sexy, balconette, padded, bright ","Brinley","AAG","125","10","false","0.8","0.2","0.0","0.0","sexy","","","x","","","","","","","","","x","","","x","","0.0","1.0","0.0","0.0","bright","8","16")""")
        c.execute("""insert into lingerieselection values ("Alandra", "65A-85F","/static/Alandra_1.jpg,/static/Alandra_2.jpg,/static/Alandra_3.jpg,/static/Alandra_4.jpg,/static/Alandra_5.jpg,/static/Alandra_6.jpg,/static/Alandra_7.jpg ,/static/Alandra_8.jpg ","34.95","24.95","With its plunging neckline and shimmering lace, nothing says sultry like our midnight magic Sveltana! This super sexy teddy features an open back, a cheeky lace bottom, and a playful tulle bow at your waist. Plus the halter and back closure adjust to create a flattering fit for every body type.","Unlined teddy<br>Fully adjustable straps","yes","lingerie"," romantic, balconette, lightlylined, pattern ","Alandra","AAH","126","10","false","0.2","0.5","0.0","0.3","romantic","","","x","","","","","","x","","","","","x","","","0.0","0.0","0.0","1.0","printedpattern","0","17")""")
        c.execute("""insert into lingerieselection values ("Bianca", "65A-85F","/static/Bianca_1.jpg,/static/Bianca_2.jpg,/static/Bianca_3.jpg,/static/Alandra_4.jpg,/static/Bianca_5.jpg,/static/Bianca_6.jpg,/static/Bianca_7.jpg ,/static/Bianca_8.jpg ","34.95","24.95","With its plunging neckline and shimmering lace, nothing says sultry like our midnight magic Sveltana! This super sexy teddy features an open back, a cheeky lace bottom, and a playful tulle bow at your waist. Plus the halter and back closure adjust to create a flattering fit for every body type.","Unlined teddy<br>Fully adjustable straps","yes","lingerie"," romantic, balconette, lightlylined, pattern","Bianca","AAH","127","10","false","0.2","0.5","0.0","0.3","romantic","","","x","","","","","","x","","","","","x","","","0.0","0.0","0.0","1.0","printedpattern","10","18")""")
        c.execute("""insert into lingerieselection values ("Isadora", "65A-85F","/static/Isadora_1.jpg,/static/Isadora_2.jpg,/static/Isadora_3.jpg,/static/Alandra_4.jpg,/static/Isadora_5.jpg,/static/Isadora_6.jpg,/static/Isadora_7.jpg ,/static/Isadora_8.jpg ","34.95","24.95","With its plunging neckline and shimmering lace, nothing says sultry like our midnight magic Sveltana! This super sexy teddy features an open back, a cheeky lace bottom, and a playful tulle bow at your waist. Plus the halter and back closure adjust to create a flattering fit for every body type.","Unlined teddy<br>Fully adjustable straps","yes","lingerie"," romantic, balconette, lightlylined, bright ","Isadora","AAH","128","10","false","0.2","0.5","0.0","0.3","romantic","","","x","","","","","","x","","","","","x","","","0.0","1.0","0.0","0.0","bright","11","19")""") 
       



        c.execute("""insert into lingerieselection values ("Isadora Cheeky", "XS-L","cheeky","9.95","6.95","tbd","tbd","yes","panties","tbd","Isadora","AAH","128","3","false","0","0","0","0","","","x","","","","","","","","","","","","","","","0","0","0","0","","11","1")""") 
       
        c.execute("""insert into lingerieselection values ("Geschenkkarte 50 EUR", "","","50.00","50.00","tbd","tbd","yes","geschenkkarten","","Geschenkkarte 50 EUR","geschenkkarte","50","0","false","0","0","0","0","","","","","","","","","","","","","","","","","","0","0","0","0","","0","1")""") 
       
        c.execute("""insert into lingerieselection values ("Geschenkkarte 20 EUR", "","","20.00","20.00","tbd","tbd","yes","geschenkkarten","","Geschenkkarte 50 EUR","geschenkkarte","20","0","false","0","0","0","0","","","","","","","","","","","","","","","","","","0","0","0","0","","0","1")""") 
                                       


        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Asymmetrisch","Gestuetzt","A","x","","","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Asymmetrisch","Gestuetzt","B","x","x","x","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Asymmetrisch","Gestuetzt","C","x","x","x","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Asymmetrisch","Gestuetzt","D","","x","","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Asymmetrisch","Halb gestuetzt","A","x","","","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Asymmetrisch","Halb gestuetzt","B","x","x","x","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Asymmetrisch","Halb gestuetzt","C","x","x","x","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Asymmetrisch","Halb gestuetzt","D","","x","","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Asymmetrisch","Nach unten geneigt","A","x","","","","","","x","x","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Asymmetrisch","Nach unten geneigt","B","x","x","x","","","","x","x","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Asymmetrisch","Nach unten geneigt","C","x","x","x","","","","x","x","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Asymmetrisch","Nach unten geneigt","D","","x","","","","","x","x","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Symmetrisch","Gestuetzt","A","x","","","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Symmetrisch","Gestuetzt","B","x","x","x","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Symmetrisch","Gestuetzt","C","x","x","x","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Symmetrisch","Gestuetzt","D","","x","","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Symmetrisch","Halb gestuetzt","A","x","","","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Symmetrisch","Halb gestuetzt","B","x","x","x","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Symmetrisch","Halb gestuetzt","C","x","x","x","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Symmetrisch","Halb gestuetzt","D","","x","","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Symmetrisch","Nach unten geneigt","A","x","","","","","","x","x","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Symmetrisch","Nach unten geneigt","B","x","x","x","","","","x","x","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Symmetrisch","Nach unten geneigt","C","x","x","x","","","","x","x","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Symmetrisch","Nach unten geneigt","D","","x","","","","","x","x","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Asymmetrisch","Gestuetzt","A","x","","","","","x","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Asymmetrisch","Gestuetzt","B","x","x","x","","","x","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Asymmetrisch","Gestuetzt","C","x","x","x","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Asymmetrisch","Gestuetzt","D","","x","","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Asymmetrisch","Halb gestuetzt","A","x","","","","","x","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Asymmetrisch","Halb gestuetzt","B","x","x","x","","","x","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Asymmetrisch","Halb gestuetzt","C","x","x","x","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Asymmetrisch","Halb gestuetzt","D","","x","","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Asymmetrisch","Nach unten geneigt","A","x","","","","","","x","x","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Asymmetrisch","Nach unten geneigt","B","x","x","x","","","","x","x","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Asymmetrisch","Nach unten geneigt","C","x","x","x","","","","x","x","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Asymmetrisch","Nach unten geneigt","D","","x","","","","","x","x","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Symmetrisch","Gestuetzt","A","x","","","","","x","x","","x","","","","x","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Symmetrisch","Gestuetzt","B","x","x","x","","","x","x","","x","","","","x","","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Symmetrisch","Gestuetzt","C","x","x","x","","","","x","","x","","","","x","","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Symmetrisch","Gestuetzt","D","","x","","","","","x","","x","","","","x","","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Symmetrisch","Halb gestuetzt","A","x","","","","","x","x","","x","","","","x","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Symmetrisch","Halb gestuetzt","B","x","x","x","","","x","x","","x","","","","x","","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Symmetrisch","Halb gestuetzt","C","x","x","x","","","","x","","x","","","","x","","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Symmetrisch","Halb gestuetzt","D","","x","","","","","x","","x","","","","x","","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Symmetrisch","Nach unten geneigt","A","x","","","","","","x","x","x","","","","x","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Symmetrisch","Nach unten geneigt","B","x","x","x","","x","","x","x","x","","","","x","","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Symmetrisch","Nach unten geneigt","C","x","x","x","","x","","x","x","x","","","","x","","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Symmetrisch","Nach unten geneigt","D","","x","","","x","","x","x","x","","","","x","","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Asymmetrisch","Gestuetzt","A","x","","","","","x","x","","x","","x","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Asymmetrisch","Gestuetzt","B","x","","x","","","x","x","","x","","x","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Asymmetrisch","Gestuetzt","C","x","","x","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Asymmetrisch","Gestuetzt","D","","x","","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Asymmetrisch","Halb gestuetzt","A","x","","","","","x","x","","x","","x","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Asymmetrisch","Halb gestuetzt","B","x","","x","","","x","x","","x","","x","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Asymmetrisch","Halb gestuetzt","C","x","","x","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Asymmetrisch","Halb gestuetzt","D","","x","","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Asymmetrisch","Nach unten geneigt","A","x","","","","","","x","x","x","","x","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Asymmetrisch","Nach unten geneigt","B","x","","x","","","","x","x","x","","x","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Asymmetrisch","Nach unten geneigt","C","x","","x","","","","x","x","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Asymmetrisch","Nach unten geneigt","D","","x","","","","","x","x","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Symmetrisch","Gestuetzt","A","x","","","x","x","x","x","","x","x","x","x","x","","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Symmetrisch","Gestuetzt","B","x","","x","x","x","x","x","","x","","x","x","x","","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Symmetrisch","Gestuetzt","C","x","","x","x","x","","x","","x","","","x","x","","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Symmetrisch","Gestuetzt","D","","","","x","x","","x","","x","","","x","x","","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Symmetrisch","Halb gestuetzt","A","x","","","x","x","x","x","","x","x","x","x","x","","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Symmetrisch","Halb gestuetzt","B","x","","x","x","x","x","x","","x","","x","x","x","","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Symmetrisch","Halb gestuetzt","C","x","","x","x","x","","x","","x","","","x","x","","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Symmetrisch","Halb gestuetzt","D","","","","x","x","","x","","x","","","x","x","","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Symmetrisch","Nach unten geneigt","A","x","","","x","x","","x","x","x","x","x","x","x","","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Symmetrisch","Nach unten geneigt","B","x","","x","x","x","","x","x","x","","x","x","x","","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Symmetrisch","Nach unten geneigt","C","x","","x","x","x","","x","x","x","","","x","x","","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Symmetrisch","Nach unten geneigt","D","","","","x","x","","x","x","x","","","x","x","","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Asymmetrisch","Gestuetzt","A","x","","","","","","x","","x","x","","","","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Asymmetrisch","Gestuetzt","B","x","x","x","","","","x","","x","x","","","","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Asymmetrisch","Gestuetzt","C","x","x","x","","","","x","","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Asymmetrisch","Gestuetzt","D","","x","","","","","x","","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Asymmetrisch","Halb gestuetzt","A","x","","","","","","x","","x","x","","","","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Asymmetrisch","Halb gestuetzt","B","x","x","x","","","","x","","x","x","","","","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Asymmetrisch","Halb gestuetzt","C","x","x","x","","","","x","","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Asymmetrisch","Halb gestuetzt","D","","x","","","","","x","","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Asymmetrisch","Nach unten geneigt","A","x","","","","","","x","x","x","x","","","","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Asymmetrisch","Nach unten geneigt","B","x","x","x","","","","x","x","x","x","","","","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Asymmetrisch","Nach unten geneigt","C","x","x","x","","","","x","x","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Asymmetrisch","Nach unten geneigt","D","","x","","","","","x","x","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Symmetrisch","Gestuetzt","A","x","","","","","","x","","x","x","","","","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Symmetrisch","Gestuetzt","B","x","x","x","","","","x","","x","x","","","","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Symmetrisch","Gestuetzt","C","x","x","x","","","","x","","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Symmetrisch","Gestuetzt","D","","x","","","","","x","","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Symmetrisch","Halb gestuetzt","A","x","","","","","","x","","x","x","","","","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Symmetrisch","Halb gestuetzt","B","x","x","x","","","","x","","x","x","","","","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Symmetrisch","Halb gestuetzt","C","x","x","x","","","","x","","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Symmetrisch","Halb gestuetzt","D","","x","","","","","x","","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Symmetrisch","Nach unten geneigt","A","x","","","","","","x","x","x","x","","","","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Symmetrisch","Nach unten geneigt","B","x","x","x","","","","x","x","x","x","","","","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Symmetrisch","Nach unten geneigt","C","x","x","x","","","","x","x","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Symmetrisch","Nach unten geneigt","D","","x","","","","","x","x","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Asymmetrisch","Gestuetzt","A","x","","","","","","x","","x","x","","","","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Asymmetrisch","Gestuetzt","B","x","x","x","","","","x","","x","x","","","","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Asymmetrisch","Gestuetzt","C","x","x","x","","","","x","","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Asymmetrisch","Gestuetzt","D","","x","","","","","x","","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Asymmetrisch","Halb gestuetzt","A","x","","","","","","x","","x","x","","","","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Asymmetrisch","Halb gestuetzt","B","x","x","x","","","","x","","x","x","","","","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Asymmetrisch","Halb gestuetzt","C","x","x","x","","","","x","","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Asymmetrisch","Halb gestuetzt","D","","x","","","","","x","","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Asymmetrisch","Nach unten geneigt","A","x","","","","","","x","x","x","x","","","","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Asymmetrisch","Nach unten geneigt","B","x","x","x","","","","x","x","x","x","","","","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Asymmetrisch","Nach unten geneigt","C","x","x","x","","","","x","x","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Asymmetrisch","Nach unten geneigt","D","","x","","","","","x","x","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Symmetrisch","Gestuetzt","A","x","","","","","","x","","x","x","","","x","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Symmetrisch","Gestuetzt","B","x","x","x","","x","","x","","x","x","","","x","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Symmetrisch","Gestuetzt","C","x","x","x","","x","","x","","x","x","","","x","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Symmetrisch","Gestuetzt","D","","x","","","x","","x","","x","x","","","x","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Symmetrisch","Halb gestuetzt","A","x","","","","","","x","","x","x","","","x","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Symmetrisch","Halb gestuetzt","B","x","x","x","","x","","x","","x","x","","","x","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Symmetrisch","Halb gestuetzt","C","x","x","x","","x","","x","","x","x","","","x","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Symmetrisch","Halb gestuetzt","D","","x","","","x","","x","","x","x","","","x","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Symmetrisch","Nach unten geneigt","A","x","","","","","","x","x","x","x","","","x","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Symmetrisch","Nach unten geneigt","B","x","x","x","","x","","x","x","x","x","","","x","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Symmetrisch","Nach unten geneigt","C","x","x","x","","x","","x","x","x","x","","","x","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Symmetrisch","Nach unten geneigt","D","","x","","","x","","x","x","x","x","","","x","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Asymmetrisch","Gestuetzt","A","x","","","","","","x","","x","x","x","","","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Asymmetrisch","Gestuetzt","B","x","","x","","","","x","","x","x","x","","","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Asymmetrisch","Gestuetzt","C","x","","x","","","","x","","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Asymmetrisch","Gestuetzt","D","","x","","","","","x","","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Asymmetrisch","Halb gestuetzt","A","x","","","","","","x","","x","x","x","","","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Asymmetrisch","Halb gestuetzt","B","x","","x","","","","x","","x","x","x","","","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Asymmetrisch","Halb gestuetzt","C","x","","x","","","","x","","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Asymmetrisch","Halb gestuetzt","D","","x","","","","","x","","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Asymmetrisch","Nach unten geneigt","A","x","","","","","","x","x","x","x","x","","","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Asymmetrisch","Nach unten geneigt","B","x","","x","","","","x","x","x","x","x","","","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Asymmetrisch","Nach unten geneigt","C","x","","x","","","","x","x","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Asymmetrisch","Nach unten geneigt","D","","x","","","","","x","x","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Symmetrisch","Gestuetzt","A","x","","","x","","","x","","x","x","x","","x","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Symmetrisch","Gestuetzt","B","x","","x","x","x","","x","","x","x","x","","x","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Symmetrisch","Gestuetzt","C","x","","x","x","x","","x","","x","x","","","x","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Symmetrisch","Gestuetzt","D","","","","x","x","","x","","x","x","","","x","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Symmetrisch","Halb gestuetzt","A","x","","","x","","","x","","x","x","x","","x","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Symmetrisch","Halb gestuetzt","B","x","","x","x","x","","x","","x","x","x","","x","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Symmetrisch","Halb gestuetzt","C","x","","x","x","x","","x","","x","x","","","x","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Symmetrisch","Halb gestuetzt","D","","","","x","x","","x","","x","x","","","x","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Symmetrisch","Nach unten geneigt","A","x","","","x","","","x","x","x","x","x","","x","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Symmetrisch","Nach unten geneigt","B","x","","x","x","x","","x","x","x","x","x","","x","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Symmetrisch","Nach unten geneigt","C","x","","x","x","x","","x","x","x","x","","","x","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Symmetrisch","Nach unten geneigt","D","","","","x","x","","x","x","x","x","","","x","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Asymmetrisch","Gestuetzt","AA","x","","","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Asymmetrisch","Halb gestuetzt","AA","x","","","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Asymmetrisch","Nach unten geneigt","AA","x","","","","","","x","x","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Symmetrisch","Gestuetzt","AA","x","","","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Symmetrisch","Halb gestuetzt","AA","x","","","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Symmetrisch","Nach unten geneigt","AA","x","","","","","","x","x","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Asymmetrisch","Gestuetzt","AA","x","","","","","x","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Asymmetrisch","Halb gestuetzt","AA","x","","","","","x","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Asymmetrisch","Nach unten geneigt","AA","x","","","","","","x","x","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Symmetrisch","Gestuetzt","AA","x","","","x","","x","x","","x","","","x","x","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Symmetrisch","Halb gestuetzt","AA","x","","","x","","x","x","","x","","","x","x","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Symmetrisch","Nach unten geneigt","AA","x","","","x","","","x","x","x","","","x","x","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Asymmetrisch","Gestuetzt","AA","x","","","","","x","x","","x","","x","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Asymmetrisch","Halb gestuetzt","AA","x","","","","","x","x","","x","","x","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Asymmetrisch","Nach unten geneigt","AA","x","","","","","","x","x","x","","x","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Symmetrisch","Gestuetzt","AA","x","","","x","x","x","x","","x","x","x","x","x","","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Symmetrisch","Halb gestuetzt","AA","x","","","x","x","x","x","","x","x","x","x","x","","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Symmetrisch","Nach unten geneigt","AA","x","","","x","x","","x","x","x","x","x","x","x","","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Asymmetrisch","Gestuetzt","AA","x","","","","","","x","","x","x","","","","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Asymmetrisch","Halb gestuetzt","AA","x","","","","","","x","","x","x","","","","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Asymmetrisch","Nach unten geneigt","AA","x","","","","","","x","x","x","x","","","","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Symmetrisch","Gestuetzt","AA","x","","","","","","x","","x","x","","","","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Symmetrisch","Halb gestuetzt","AA","x","","","","","","x","","x","x","","","","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Symmetrisch","Nach unten geneigt","AA","x","","","","","","x","x","x","x","","","","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Asymmetrisch","Gestuetzt","AA","x","","","","","","x","","x","x","","","","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Asymmetrisch","Halb gestuetzt","AA","x","","","","","","x","","x","x","","","","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Asymmetrisch","Nach unten geneigt","AA","x","","","","","","x","x","x","x","","","","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Symmetrisch","Gestuetzt","AA","x","","","x","","","x","","x","x","","x","x","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Symmetrisch","Halb gestuetzt","AA","x","","","x","","","x","","x","x","","x","x","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Symmetrisch","Nach unten geneigt","AA","x","","","x","","","x","x","x","x","","x","x","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Asymmetrisch","Gestuetzt","AA","x","","","","","","x","","x","x","x","","","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Asymmetrisch","Halb gestuetzt","AA","x","","","","","","x","","x","x","x","","","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Asymmetrisch","Nach unten geneigt","AA","x","","","","","","x","x","x","x","x","","","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Symmetrisch","Gestuetzt","AA","x","","","x","","","x","","x","x","x","x","x","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Symmetrisch","Halb gestuetzt","AA","x","","","x","","","x","","x","x","x","x","x","x","x")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Symmetrisch","Nach unten geneigt","AA","x","","","x","","","x","x","x","x","x","x","x","x","x")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Asymmetrisch","Gestuetzt","E","","x","","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Asymmetrisch","Halb gestuetzt","E","","x","","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Asymmetrisch","Nach unten geneigt","E","","x","","","","","x","x","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Symmetrisch","Gestuetzt","E","","x","","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Symmetrisch","Halb gestuetzt","E","","x","","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Symmetrisch","Nach unten geneigt","E","","x","","","","","x","x","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Asymmetrisch","Gestuetzt","E","","x","","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Asymmetrisch","Halb gestuetzt","E","","x","","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Asymmetrisch","Nach unten geneigt","E","","x","","","","","x","x","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Symmetrisch","Gestuetzt","E","","x","","","x","","x","","x","","","","x","","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Symmetrisch","Halb gestuetzt","E","","x","","","x","","x","","x","","","","x","","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Symmetrisch","Nach unten geneigt","E","","x","","","x","","x","x","x","","","","x","","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Asymmetrisch","Gestuetzt","E","","x","","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Asymmetrisch","Halb gestuetzt","E","","x","","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Asymmetrisch","Nach unten geneigt","E","","x","","","","","x","x","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Symmetrisch","Gestuetzt","E","","","","x","x","","x","","x","","","x","x","","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Symmetrisch","Halb gestuetzt","E","","","","x","x","","x","","x","","","x","x","","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Symmetrisch","Nach unten geneigt","E","","","","x","x","","x","x","x","","","x","x","","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Asymmetrisch","Gestuetzt","E","","x","","","","","x","","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Asymmetrisch","Halb gestuetzt","E","","x","","","","","x","","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Asymmetrisch","Nach unten geneigt","E","","x","","","","","x","x","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Symmetrisch","Gestuetzt","E","","x","","","","","x","","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Symmetrisch","Halb gestuetzt","E","","x","","","","","x","","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Symmetrisch","Nach unten geneigt","E","","x","","","","","x","x","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Asymmetrisch","Gestuetzt","E","","x","","","","","x","","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Asymmetrisch","Halb gestuetzt","E","","x","","","","","x","","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Asymmetrisch","Nach unten geneigt","E","","x","","","","","x","x","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Symmetrisch","Gestuetzt","E","","x","","","x","","x","","x","x","","","x","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Symmetrisch","Halb gestuetzt","E","","x","","","x","","x","","x","x","","","x","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Symmetrisch","Nach unten geneigt","E","","x","","","x","","x","x","x","x","","","x","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Asymmetrisch","Gestuetzt","E","","x","","","","","x","","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Asymmetrisch","Halb gestuetzt","E","","x","","","","","x","","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Asymmetrisch","Nach unten geneigt","E","","x","","","","","x","x","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Symmetrisch","Gestuetzt","E","","","","x","x","","x","","x","x","","","x","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Symmetrisch","Halb gestuetzt","E","","","","x","x","","x","","x","x","","","x","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Symmetrisch","Nach unten geneigt","E","","","","x","x","","x","x","x","x","","","x","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Asymmetrisch","Gestuetzt","F","","x","","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Asymmetrisch","Halb gestuetzt","F","","x","","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Asymmetrisch","Nach unten geneigt","F","","x","","","","","x","x","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Symmetrisch","Gestuetzt","F","","x","","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Symmetrisch","Halb gestuetzt","F","","x","","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Symmetrisch","Nach unten geneigt","F","","x","","","","","x","x","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Asymmetrisch","Gestuetzt","F","","x","","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Asymmetrisch","Halb gestuetzt","F","","x","","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Asymmetrisch","Nach unten geneigt","F","","x","","","","","x","x","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Symmetrisch","Gestuetzt","F","","x","","","x","","x","","x","","","","x","","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Symmetrisch","Halb gestuetzt","F","","x","","","x","","x","","x","","","","x","","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Symmetrisch","Nach unten geneigt","F","","x","","","x","","x","x","x","","","","x","","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Asymmetrisch","Gestuetzt","F","","x","","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Asymmetrisch","Halb gestuetzt","F","","x","","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Asymmetrisch","Nach unten geneigt","F","","x","","","","","x","x","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Symmetrisch","Gestuetzt","F","","","","","x","","x","","x","","","x","x","","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Symmetrisch","Halb gestuetzt","F","","","","","x","","x","","x","","","x","x","","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Symmetrisch","Nach unten geneigt","F","","","","","x","","x","x","x","","","x","x","","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Asymmetrisch","Gestuetzt","F","","x","","","","","x","","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Asymmetrisch","Halb gestuetzt","F","","x","","","","","x","","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Asymmetrisch","Nach unten geneigt","F","","x","","","","","x","x","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Symmetrisch","Gestuetzt","F","","x","","","","","x","","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Symmetrisch","Halb gestuetzt","F","","x","","","","","x","","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Symmetrisch","Nach unten geneigt","F","","x","","","","","x","x","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Asymmetrisch","Gestuetzt","F","","x","","","","","x","","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Asymmetrisch","Halb gestuetzt","F","","x","","","","","x","","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Asymmetrisch","Nach unten geneigt","F","","x","","","","","x","x","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Symmetrisch","Gestuetzt","F","","x","","","x","","x","","x","x","","","x","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Symmetrisch","Halb gestuetzt","F","","x","","","x","","x","","x","x","","","x","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Symmetrisch","Nach unten geneigt","F","","x","","","x","","x","x","x","x","","","x","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Asymmetrisch","Gestuetzt","F","","x","","","","","x","","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Asymmetrisch","Halb gestuetzt","F","","x","","","","","x","","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Asymmetrisch","Nach unten geneigt","F","","x","","","","","x","x","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Symmetrisch","Gestuetzt","F","","","","","x","","x","","x","x","","","x","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Symmetrisch","Halb gestuetzt","F","","","","","x","","x","","x","x","","","x","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Symmetrisch","Nach unten geneigt","F","","","","","x","","x","x","x","x","","","x","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Asymmetrisch","Gestuetzt","G","","x","","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Asymmetrisch","Halb gestuetzt","G","","x","","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Asymmetrisch","Nach unten geneigt","G","","x","","","","","x","x","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Symmetrisch","Gestuetzt","G","","x","","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Symmetrisch","Halb gestuetzt","G","","x","","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Stark Ost-West","Symmetrisch","Nach unten geneigt","G","","x","","","","","x","x","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Asymmetrisch","Gestuetzt","G","","x","","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Asymmetrisch","Halb gestuetzt","G","","x","","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Asymmetrisch","Nach unten geneigt","G","","x","","","","","x","x","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Symmetrisch","Gestuetzt","G","","x","","","x","","x","","x","","","","x","","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Symmetrisch","Halb gestuetzt","G","","x","","","x","","x","","x","","","","x","","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Leicht Ost-West","Symmetrisch","Nach unten geneigt","G","","x","","","x","","x","x","x","","","","x","","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Asymmetrisch","Gestuetzt","G","","x","","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Asymmetrisch","Halb gestuetzt","G","","x","","","","","x","","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Asymmetrisch","Nach unten geneigt","G","","x","","","","","x","x","x","","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Symmetrisch","Gestuetzt","G","","","","","x","","x","","x","","","x","x","","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Symmetrisch","Halb gestuetzt","G","","","","","x","","x","","x","","","x","x","","")""")
        c.execute("""insert into showroom_criteria values ("Rund","Mittig","Symmetrisch","Nach unten geneigt","G","","","","","x","","x","x","x","","","x","x","","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Asymmetrisch","Gestuetzt","G","","x","","","","","x","","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Asymmetrisch","Halb gestuetzt","G","","x","","","","","x","","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Asymmetrisch","Nach unten geneigt","G","","x","","","","","x","x","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Symmetrisch","Gestuetzt","G","","x","","","","","x","","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Symmetrisch","Halb gestuetzt","G","","x","","","","","x","","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Stark Ost-West","Symmetrisch","Nach unten geneigt","G","","x","","","","","x","x","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Asymmetrisch","Gestuetzt","G","","x","","","","","x","","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Asymmetrisch","Halb gestuetzt","G","","x","","","","","x","","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Asymmetrisch","Nach unten geneigt","G","","x","","","","","x","x","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Symmetrisch","Gestuetzt","G","","x","","","x","","x","","x","x","","","x","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Symmetrisch","Halb gestuetzt","G","","x","","","x","","x","","x","x","","","x","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Leicht Ost-West","Symmetrisch","Nach unten geneigt","G","","x","","","x","","x","x","x","x","","","x","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Asymmetrisch","Gestuetzt","G","","x","","","","","x","","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Asymmetrisch","Halb gestuetzt","G","","x","","","","","x","","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Asymmetrisch","Nach unten geneigt","G","","x","","","","","x","x","x","x","","","","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Symmetrisch","Gestuetzt","G","","","","","x","","x","","x","x","","","x","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Symmetrisch","Halb gestuetzt","G","","","","","x","","x","","x","x","","","x","x","")""")
        c.execute("""insert into showroom_criteria values ("Tropfenform","Mittig","Symmetrisch","Nach unten geneigt","G","","","","","x","","x","x","x","x","","","x","x","")""")       
                
 
        conn.commit()
 
   
 
    if (u==1):
        c.execute("""create table stylecode_AAA (
                type text,
                stylecode text,
                color text,
                size text,
                produktionsmenge int,
                bestelltemengebestellt int)""")
        c.execute("""create table stylecode_AAB (
                type text,
                stylecode text,
                color text,
                size text,
                produktionsmenge int,
                bestelltemengebestellt int)""")
        c.execute("""create table stylecode_AAC (
                type text,
                stylecode text,
                color text,
                size text,
                produktionsmenge int,
                bestelltemengebestellt int)""")
 
        c.execute("""create table stylecode_AAD (
                type text,
                stylecode text,
                color text,
                size text,
                produktionsmenge int,
                bestelltemengebestellt int)""")
        c.execute("""create table stylecode_AAE (
                type text,
                stylecode text,
                color text,
                size text,
                produktionsmenge int,
                bestelltemengebestellt int)""")
        c.execute("""create table stylecode_AAF (
                type text,
                stylecode text,
                color text,
                size text,
                produktionsmenge int,
                bestelltemengebestellt int)""")
        c.execute("""create table stylecode_AAG (
                type text,
                stylecode text,
                color text,
                size text,
                produktionsmenge int,
                bestelltemengebestellt int)""")
        c.execute("""create table stylecode_AAH (
                type text,
                stylecode text,
                color text,
                size text,
                produktionsmenge int,
                bestelltemengebestellt int)""")
 


        c.execute("""create table stylecode_geschenkkarte(
                type text,
                stylecode text,
                color text,
                size text,
                produktionsmenge int,
                bestelltemengebestellt int)""")









  
        list = [[] for i in range(49)]






        get_cup = {
                   0 : 'A',
                   1 : 'B',
                   2 : 'C',
                   3 : 'D',
                   4 : 'E',
                   5 : 'F',
                   6 : 'G',
                   7 : 'H',
                   8 : 'I'

 
                  
                }              
        i=0
        zaehler_1=0
        zaehler_2=0
        zaehler_3=0
        unterbrust=65
       
        while(i<=4):
            
 
           

            cup=0

            
            while(cup<=5):
                cup_detail=get_cup[cup]
 
               
 
                list[i].append(str(unterbrust)+cup_detail)
                zaehler_3=zaehler_3+1

               
                cup=cup+1
               
            i=i+1
            unterbrust=unterbrust+5


            






        bhs = [[] for i in range(49)]
        

        bhs[0].append("AAA111")
        bhs[1].append("AAB112")
        bhs[2].append("AAB113")
        bhs[3].append("AAC114")
        bhs[4].append("AAC115")
        bhs[5].append("AAD116")
        bhs[6].append("AAD117")
        bhs[7].append("AAD118")
        bhs[8].append("AAE119")
        bhs[9].append("AAF120")
        bhs[10].append("AAF121")
        bhs[11].append("AAF122")
        bhs[12].append("AAG123")
        bhs[13].append("AAG124")
        bhs[14].append("AAG125")
        bhs[15].append("AAH126")
        bhs[16].append("AAH127")
        bhs[17].append("AAH128")
        bhs[18].append("AAC129")
        bhs[19].append("AAA110")
        

        j=0

        while j<=19:
            i=0
            if j!=5 and j!=6 and j!=7: 
                while i<=4:
                    k=0
                    while k<=5:

                        c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s)""" % ("stylecode_"+bhs[j][0][:3]),("BH",bhs[j][0][:3],bhs[j][0][3:6],list[i][k],"100","0"))
                        k=k+1
                    i=i+1
            else:
                c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s)""" % ("stylecode_"+bhs[j][0][:3]),("BH",bhs[j][0][:3],bhs[j][0][3:6],"XS","100","0"))
                c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s)""" % ("stylecode_"+bhs[j][0][:3]),("BH",bhs[j][0][:3],bhs[j][0][3:6],"S","100","0"))
                c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s)""" % ("stylecode_"+bhs[j][0][:3]),("BH",bhs[j][0][:3],bhs[j][0][3:6],"M","100","0"))
                c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s)""" % ("stylecode_"+bhs[j][0][:3]),("BH",bhs[j][0][:3],bhs[j][0][3:6],"L","100","0"))
                c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s)""" % ("stylecode_"+bhs[j][0][:3]),("BH",bhs[j][0][:3],bhs[j][0][3:6],"XL","100","0"))
                
            j=j+1
        


 
 
 
        c.execute("""insert into stylecode_AAA values ("panties", "AAA","110", "S","100","0")""")
        c.execute("""insert into stylecode_AAA values ("panties", "AAA","111", "S","100","0")""")
        c.execute("""insert into stylecode_AAB values ("panties", "AAB","112", "M","100","0")""")
        c.execute("""insert into stylecode_AAB values ("panties", "AAB","113", "M","100","0")""")
        c.execute("""insert into stylecode_AAC values ("panties", "AAC","114", "M","100","0")""")
        c.execute("""insert into stylecode_AAC values ("panties", "AAC","115", "M","100","0")""")
        c.execute("""insert into stylecode_AAC values ("panties", "AAC","129", "M","100","0")""")
 

        c.execute("""insert into stylecode_AAD values ("panties", "AAD","116", "M","100","0")""")
        c.execute("""insert into stylecode_AAD values ("panties", "AAD","117", "M","100","0")""")
        c.execute("""insert into stylecode_AAD values ("panties", "AAD","118", "M","100","0")""")
        c.execute("""insert into stylecode_AAE values ("panties", "AAE","119", "M","100","0")""")
        c.execute("""insert into stylecode_AAF values ("panties", "AAF","120", "M","100","0")""")
        c.execute("""insert into stylecode_AAF values ("panties", "AAF","121", "M","100","0")""")
        c.execute("""insert into stylecode_AAF values ("panties", "AAF","122", "M","100","0")""")
        c.execute("""insert into stylecode_AAG values ("panties", "AAG","123", "M","100","0")""")
        c.execute("""insert into stylecode_AAG values ("panties", "AAG","124", "M","100","0")""")
        c.execute("""insert into stylecode_AAG values ("panties", "AAG","125", "M","100","0")""")
        c.execute("""insert into stylecode_AAH values ("panties", "AAH","126", "M","100","0")""")
        c.execute("""insert into stylecode_AAH values ("panties", "AAH","127", "M","100","0")""")
        c.execute("""insert into stylecode_AAH values ("panties", "AAH","128", "M","100","0")""")
        c.execute("""insert into stylecode_AAC values ("panties", "AAC","129", "M","100","0")""")

        c.execute("""insert into stylecode_geschenkkarte values ("", "geschenkkarte","50", "","10000","0")""")
        c.execute("""insert into stylecode_geschenkkarte values ("", "geschenkkarte","20", "","10000","0")""")
 
 
        c.execute("""create table if not exists bewertungen_AAA_110 (
                bestellnummer text,
                namebewerter text,
                bewertung text,
                bewertungsheadline text,
                bewertungstext text,
                bewertungsdatum text,
                gutscheincodeid text,
                passform text,
                bhgroesse text,
                slipgroesse text)""")
 
 
        c.execute("""create table if not exists bewertungen_AAA_111 (
                bestellnummer text,
                namebewerter text,
                bewertung text,
                bewertungsheadline text,
                bewertungstext text,
                bewertungsdatum text,
                gutscheincodeid text,
                passform text,
                bhgroesse text,
                slipgroesse text)""")
 
 
       
        c.execute("""create table if not exists bewertungen_AAB_112 (
                bestellnummer text,
                namebewerter text,
                bewertung text,
                bewertungsheadline text,
                bewertungstext text,
                bewertungsdatum text,
                gutscheincodeid text,
                passform text,
                bhgroesse text,
                slipgroesse text)""")
 
       
        c.execute("""create table if not exists bewertungen_AAB_113 (
                bestellnummer text,
                namebewerter text,
                bewertung text,
                bewertungsheadline text,
                bewertungstext text,
                bewertungsdatum text,
                gutscheincodeid text,
                passform text,
                bhgroesse text,
                slipgroesse text)""")
 
        c.execute("""create table if not exists bewertungen_AAC_114 (
                bestellnummer text,
                namebewerter text,
                bewertung text,
                bewertungsheadline text,
                bewertungstext text,
                bewertungsdatum text,
                gutscheincodeid text,
                passform text,
                bhgroesse text,
                slipgroesse text)""")
 
        c.execute("""create table if not exists bewertungen_AAC_115 (
                bestellnummer text,
                namebewerter text,
                bewertung text,
                bewertungsheadline text,
                bewertungstext text,
                bewertungsdatum text,
                gutscheincodeid text,
                passform text,
                bhgroesse text,
                slipgroesse text)""")
 
        c.execute("""create table if not exists bewertungen_AAD_116 (
                bestellnummer text,
                namebewerter text,
                bewertung text,
                bewertungsheadline text,
                bewertungstext text,
                bewertungsdatum text,
                gutscheincodeid text,
                passform text,
                bhgroesse text,
                slipgroesse text)""")
        c.execute("""create table if not exists bewertungen_AAD_117 (
                bestellnummer text,
                namebewerter text,
                bewertung text,
                bewertungsheadline text,
                bewertungstext text,
                bewertungsdatum text,
                gutscheincodeid text,
                passform text,
                bhgroesse text,
                slipgroesse text)""")
        c.execute("""create table if not exists bewertungen_AAD_118 (
                bestellnummer text,
                namebewerter text,
                bewertung text,
                bewertungsheadline text,
                bewertungstext text,
                bewertungsdatum text,
                gutscheincodeid text,
                passform text,
                bhgroesse text,
                slipgroesse text)""")
        c.execute("""create table if not exists bewertungen_AAE_119 (
                bestellnummer text,
                namebewerter text,
                bewertung text,
                bewertungsheadline text,
                bewertungstext text,
                bewertungsdatum text,
                gutscheincodeid text,
                passform text,
                bhgroesse text,
                slipgroesse text)""")
 
 
        c.execute("""create table if not exists bewertungen_AAF_120 (
                bestellnummer text,
                namebewerter text,
                bewertung text,
                bewertungsheadline text,
                bewertungstext text,
                bewertungsdatum text,
                gutscheincodeid text,
                passform text,
                bhgroesse text,
                slipgroesse text)""")
        c.execute("""create table if not exists bewertungen_AAF_121 (
                bestellnummer text,
                namebewerter text,
                bewertung text,
                bewertungsheadline text,
                bewertungstext text,
                bewertungsdatum text,
                gutscheincodeid text,
                passform text,
                bhgroesse text,
                slipgroesse text)""")
        c.execute("""create table if not exists bewertungen_AAF_122 (
                bestellnummer text,
                namebewerter text,
                bewertung text,
                bewertungsheadline text,
                bewertungstext text,
                bewertungsdatum text,
                gutscheincodeid text,
                passform text,
                bhgroesse text,
                slipgroesse text)""")
        c.execute("""create table if not exists bewertungen_AAG_123 (
                bestellnummer text,
                namebewerter text,
                bewertung text,
                bewertungsheadline text,
                bewertungstext text,
                bewertungsdatum text,
                gutscheincodeid text,
                passform text,
                bhgroesse text,
                slipgroesse text)""")
        c.execute("""create table if not exists bewertungen_AAG_124 (
                bestellnummer text,
                namebewerter text,
                bewertung text,
                bewertungsheadline text,
                bewertungstext text,
                bewertungsdatum text,
                gutscheincodeid text,
                passform text,
                bhgroesse text,
                slipgroesse text)""")
        c.execute("""create table if not exists bewertungen_AAG_125 (
                bestellnummer text,
                namebewerter text,
                bewertung text,
                bewertungsheadline text,
                bewertungstext text,
                bewertungsdatum text,
                gutscheincodeid text,
                passform text,
                bhgroesse text,
                slipgroesse text)""")
 
        c.execute("""create table if not exists bewertungen_AAH_126 (
                bestellnummer text,
                namebewerter text,
                bewertung text,
                bewertungsheadline text,
                bewertungstext text,
                bewertungsdatum text,
                gutscheincodeid text,
                passform text,
                bhgroesse text,
                slipgroesse text)""")
 
        c.execute("""create table if not exists bewertungen_AAH_127 (
                bestellnummer text,
                namebewerter text,
                bewertung text,
                bewertungsheadline text,
                bewertungstext text,
                bewertungsdatum text,
                gutscheincodeid text,
                passform text,
                bhgroesse text,
                slipgroesse text)""")
 
        c.execute("""create table if not exists bewertungen_AAH_128 (
                bestellnummer text,
                namebewerter text,
                bewertung text,
                bewertungsheadline text,
                bewertungstext text,
                bewertungsdatum text,
                gutscheincodeid text,
                passform text,
                bhgroesse text,
                slipgroesse text)""")
        c.execute("""create table if not exists bewertungen_AAC_129 (
                bestellnummer text,
                namebewerter text,
                bewertung text,
                bewertungsheadline text,
                bewertungstext text,
                bewertungsdatum text,
                gutscheincodeid text,
                passform text,
                bhgroesse text,
                slipgroesse text)""")



        c.execute("""create table if not exists bewertungen_geschenkkarte_50 (
                bestellnummer text,
                namebewerter text,
                bewertung text,
                bewertungsheadline text,
                bewertungstext text,
                bewertungsdatum text,
                gutscheincodeid text,
                passform text,
                bhgroesse text,
                slipgroesse text)""")


        c.execute("""create table if not exists bewertungen_geschenkkarte_20 (
                bestellnummer text,
                namebewerter text,
                bewertung text,
                bewertungsheadline text,
                bewertungstext text,
                bewertungsdatum text,
                gutscheincodeid text,
                passform text,
                bhgroesse text,
                slipgroesse text)""")

        
        c.execute("""insert into bewertungen_AAA_111 values ("HGJAKK", "M. Fischer","4", "Super BH","Super Passform","31. Januar 2017","asdasd","1","75A","S")""")
        c.execute("""insert into bewertungen_AAA_111 values ("HGJAKK", "M. Fischer","2", "Super BH","Super Passform","31. Januar 2017","asdasd","","75A","S")""")
        c.execute("""insert into bewertungen_AAA_111 values ("HGJAKK", "M. Fischer","5", "Super","Super!","15. Januar 2017","asdasd","1","75A","S")""")
        c.execute("""insert into bewertungen_AAA_111 values ("HGJAKK", "M. Fischer","2", "Super BH","Super geschnitten","31. Januar 2017","asdasd","1","75A","S")""")
        c.execute("""insert into bewertungen_AAA_111 values ("HGJAKK", "M. Fischer","1", "Super BH","Super Passform","31. Januar 2017","asdasd","2","75A","S")""")



        
        

        c.execute("""create table if not exists picturelibrary_AAA_110 (
                modelAB int,
                subpicture int,
                link text,
                type text,
                pantytype text)""")
 
 
        c.execute("""create table if not exists picturelibrary_AAA_111 (
                modelAB int,
                subpicture int,
                link text,
                type text,
                pantytype text)""")
 
 
       
        c.execute("""create table if not exists picturelibrary_AAB_112 (
                modelAB int,
                subpicture int,
                link text,
                type text,
                pantytype text)""")
 
       
        c.execute("""create table if not exists picturelibrary_AAB_113 (
                modelAB int,
                subpicture int,
                link text,
                type text,
                pantytype text)""")
 
        c.execute("""create table if not exists picturelibrary_AAC_114 (
                modelAB int,
                subpicture int,
                link text,
                type text,
                pantytype text)""")
 
        c.execute("""create table if not exists picturelibrary_AAC_115 (
                modelAB int,
                subpicture int,
                link text,
                type text,
                pantytype text)""")
 
        c.execute("""create table if not exists picturelibrary_AAD_116 (
                modelAB int,
                subpicture int,
                link text,
                type text,
                pantytype text)""")
        c.execute("""create table if not exists picturelibrary_AAD_117 (
                modelAB int,
                subpicture int,
                link text,
                type text,
                pantytype text)""")
        c.execute("""create table if not exists picturelibrary_AAD_118 (
                modelAB int,
                subpicture int,
                link text,
                type text,
                pantytype text)""")
        c.execute("""create table if not exists picturelibrary_AAE_119 (
                modelAB int,
                subpicture int,
                link text,
                type text,
                pantytype text)""")
 
 
        c.execute("""create table if not exists picturelibrary_AAF_120 (
                modelAB int,
                subpicture int,
                link text,
                type text,
                pantytype text)""")
        c.execute("""create table if not exists picturelibrary_AAF_121 (
                modelAB int,
                subpicture int,
                link text,
                type text,
                pantytype text)""")
        c.execute("""create table if not exists picturelibrary_AAF_122 (
                modelAB int,
                subpicture int,
                link text,
                type text,
                pantytype text)""")
        c.execute("""create table if not exists picturelibrary_AAG_123 (
                modelAB int,
                subpicture int,
                link text,
                type text,
                pantytype text)""")
        c.execute("""create table if not exists picturelibrary_AAG_124 (
                modelAB int,
                subpicture int,
                link text,
                type text,
                pantytype text)""")
        c.execute("""create table if not exists picturelibrary_AAG_125 (
                modelAB int,
                subpicture int,
                link text,
                type text,
                pantytype text)""")
 
        c.execute("""create table if not exists picturelibrary_AAH_126 (
                modelAB int,
                subpicture int,
                link text,
                type text,
                pantytype text)""")
 
        c.execute("""create table if not exists picturelibrary_AAH_127 (
                modelAB int,
                subpicture int,
                link text,
                type text,
                pantytype text)""")
 
        c.execute("""create table if not exists picturelibrary_AAH_128 (
                modelAB int,
                subpicture int,
                link text,
                type text,
                pantytype text)""")
        c.execute("""create table if not exists picturelibrary_AAC_129 (
                modelAB int,
                subpicture int,
                link text,
                type text,
                pantytype text)""")
        



        c.execute("""create table if not exists picturelibrary_geschenkkarte_50 (
                modelAB int,
                subpicture int,
                link text,
                type text,
                pantytype text)""")
        c.execute("""create table if not exists picturelibrary_geschenkkarte_20 (
                modelAB int,
                subpicture int,
                link text,
                type text,
                pantytype text)""")

        
        c.execute("""insert into picturelibrary_AAA_111 values ("-1", "0","/static/Janet_1.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAA_111 values ("-1", "1","/static/Janet_2.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAA_111 values ("-1", "2","/static/Janet_3.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAA_111 values ("-1", "-1","/static/Janet_4.jpg","panties","")""")
        c.execute("""insert into picturelibrary_AAA_111 values ("-1", "-1","/static/Janet_5.jpg","panties","")""")


        c.execute("""insert into picturelibrary_AAA_110 values ("-1", "0","/static/Daphne_1.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAA_110 values ("-1", "1","/static/Daphne_2.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAA_110 values ("-1", "2","/static/Daphne_3.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAA_110 values ("-1", "-1","/static/Daphne_4.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAA_110 values ("-1", "-1","/static/Daphne_5.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAA_110 values ("-1", "-1","/static/Daphne_6.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAA_110 values ("-1", "-1","/static/Daphne_7.jpg","panties","")""")
        c.execute("""insert into picturelibrary_AAA_110 values ("-1", "-1","/static/Daphne_8.jpg","panties","")""")


        c.execute("""insert into picturelibrary_AAB_112 values ("-1", "0","/static/Lilly_1.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAB_112 values ("-1", "1","/static/Lilly_2.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAB_112 values ("-1", "-1","/static/Lilly_3.jpg","panties","")""")

        c.execute("""insert into picturelibrary_AAB_113 values ("-1", "0","/static/Florina_1.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAB_113 values ("-1", "1","/static/Florina_2.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAB_113 values ("-1", "-1","/static/Florina_3.jpg","panties","")""")

        c.execute("""insert into picturelibrary_AAC_114 values ("0", "0","/static/Kellie_1.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAC_114 values ("0", "1","/static/Kellie_2.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAC_114 values ("1", "0","/static/Kellie_3.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAC_114 values ("1", "1","/static/Kellie_4.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAC_114 values ("0", "-1","/static/Kellie_5.jpg","panties","")""")
        c.execute("""insert into picturelibrary_AAC_114 values ("0", "-1","/static/Kellie_6.jpg","panties","")""")

        c.execute("""insert into picturelibrary_AAC_115 values ("-1", "0","/static/Allara_1.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAC_115 values ("-1", "1","/static/Allara_2.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAC_115 values ("-1", "-1","/static/Allara_3.jpg","panties","")""")
        c.execute("""insert into picturelibrary_AAC_115 values ("-1", "-1","/static/Allara_4.jpg","panties","")""")


        c.execute("""insert into picturelibrary_AAC_129 values ("0", "0","/static/Beatriz_1.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAC_129 values ("0", "1","/static/Beatriz_2.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAC_129 values ("0", "2","/static/Beatriz_3.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAC_129 values ("0", "-1","/static/Beatriz_4.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAC_129 values ("0", "-1","/static/Beatriz_5.jpg","panties","")""")
        c.execute("""insert into picturelibrary_AAC_129 values ("0", "-1","/static/Beatriz_6.jpg","panties","")""")

        c.execute("""insert into picturelibrary_AAD_116 values ("-1", "0","/static/Ulrike_1.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAD_116 values ("-1", "1","/static/Ulrike_2.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAD_116 values ("-1", "2","/static/Ulrike_3.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAD_116 values ("-1", "-1","/static/Ulrike_4.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAD_116 values ("-1", "-1","/static/Ulrike_5.jpg","panties","")""")
        c.execute("""insert into picturelibrary_AAD_116 values ("-1", "-1","/static/Ulrike_6.jpg","panties","")""")

        c.execute("""insert into picturelibrary_AAD_117 values ("-1", "0","/static/Samantha_1.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAD_117 values ("-1", "1","/static/Samantha_2.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAD_117 values ("-1", "-1","/static/Samantha_3.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAD_117 values ("-1", "-1","/static/Samantha_4.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAD_117 values ("-1", "-1","/static/Samantha_5.jpg","panties","")""")
        c.execute("""insert into picturelibrary_AAD_117 values ("-1", "-1","/static/Samantha_6.jpg","panties","")""")


        c.execute("""insert into picturelibrary_AAD_118 values ("-1", "0","/static/Sina_1.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAD_118 values ("-1", "1","/static/Sina_2.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAD_118 values ("-1", "2","/static/Sina_3.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAD_118 values ("-1", "-1","/static/Sina_4.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAD_118 values ("-1", "-1","/static/Sina_5.jpg","panties","")""")
        c.execute("""insert into picturelibrary_AAD_118 values ("-1", "-1","/static/Sina_6.jpg","panties","")""")

        c.execute("""insert into picturelibrary_AAE_119 values ("0", "0","/static/Lidia_1.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAE_119 values ("0", "1","/static/Lidia_2.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAE_119 values ("1", "0","/static/Lidia_3.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAE_119 values ("1", "1","/static/Lidia_4.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAE_119 values ("0", "-1","/static/Lidia_5.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAE_119 values ("0", "-1","/static/Lidia_6.jpg","panties","")""")
        c.execute("""insert into picturelibrary_AAE_119 values ("0", "-1","/static/Lidia_7.jpg","panties","")""")
        

        c.execute("""insert into picturelibrary_AAF_120 values ("0", "0","/static/Bella_1.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAF_120 values ("0", "1","/static/Bella_2.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAF_120 values ("1", "0","/static/Bella_3.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAF_120 values ("1", "1","/static/Bella_4.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAF_120 values ("0", "-1","/static/Bella_5.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAF_120 values ("0", "-1","/static/Bella_6.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAF_120 values ("0", "-1","/static/Bella_7.jpg","panties","")""")
        c.execute("""insert into picturelibrary_AAF_120 values ("0", "-1","/static/Bella_8.jpg","panties","")""")



        c.execute("""insert into picturelibrary_AAF_121 values ("0", "0","/static/Cheyanne_1.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAF_121 values ("1", "0","/static/Cheyanne_2.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAF_121 values ("1", "1","/static/Cheyanne_3.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAF_121 values ("0", "-1","/static/Cheyanne_4.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAF_121 values ("0", "-1","/static/Cheyanne_5.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAF_121 values ("0", "-1","/static/Cheyanne_6.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAF_121 values ("0", "-1","/static/Cheyanne_7.jpg","panties","")""")
        c.execute("""insert into picturelibrary_AAF_121 values ("0", "-1","/static/Cheyanne_8.jpg","panties","")""")




        c.execute("""insert into picturelibrary_AAF_122 values ("0", "0","/static/Ilanni_1.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAF_122 values ("0", "1","/static/Ilanni_2.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAF_122 values ("1", "0","/static/Ilanni_3.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAF_122 values ("1", "1","/static/Ilanni_4.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAF_122 values ("0", "-1","/static/Ilanni_5.jpg","panties","")""")
        c.execute("""insert into picturelibrary_AAF_122 values ("0", "-1","/static/Ilanni_6.jpg","panties","")""")


        c.execute("""insert into picturelibrary_AAG_123 values ("-1", "0","/static/Alexsi_1.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAG_123 values ("-1", "1","/static/Alexsi_2.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAG_123 values ("-1", "2","/static/Alexsi_3.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAG_123 values ("-1", "-1","/static/Alexsi_4.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAG_123 values ("-1", "-1","/static/Alexsi_5.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAG_123 values ("-1", "-1","/static/Alexsi_6.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAG_123 values ("-1", "-1","/static/Alexsi_7.jpg","panties","")""")
        c.execute("""insert into picturelibrary_AAG_123 values ("-1", "-1","/static/Alexsi_8.jpg","panties","")""")


        c.execute("""insert into picturelibrary_AAG_124 values ("0", "0","/static/Angelica_1.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAG_124 values ("0", "1","/static/Angelica_2.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAG_124 values ("1", "0","/static/Angelica_3.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAG_124 values ("1", "1","/static/Angelica_4.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAG_124 values ("0", "-1","/static/Angelica_5.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAG_124 values ("0", "-1","/static/Angelica_6.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAG_124 values ("0", "-1","/static/Angelica_7.jpg","panties","")""")
        c.execute("""insert into picturelibrary_AAG_124 values ("0", "-1","/static/Angelica_8.jpg","panties","")""")


        c.execute("""insert into picturelibrary_AAG_125 values ("-1", "0","/static/Brinley_1.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAG_125 values ("-1", "1","/static/Brinley_2.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAG_125 values ("-1", "2","/static/Brinley_3.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAG_125 values ("-1", "-1","/static/Brinley_4.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAG_125 values ("-1", "-1","/static/Brinley_5.jpg","panties","")""")
        c.execute("""insert into picturelibrary_AAG_125 values ("-1", "-1","/static/Brinley_6.jpg","panties","")""")



        c.execute("""insert into picturelibrary_AAH_126 values ("-1", "0","/static/Alandra_1.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAH_126 values ("-1", "1","/static/Alandra_2.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAH_126 values ("-1", "2","/static/Alandra_3.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAH_126 values ("-1", "-1","/static/Alandra_4.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAH_126 values ("-1", "-1","/static/Alandra_5.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAH_126 values ("-1", "-1","/static/Alandra_6.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAH_126 values ("-1", "-1","/static/Alandra_7.jpg","panties","")""")
        c.execute("""insert into picturelibrary_AAH_126 values ("-1", "-1","/static/Alandra_8.jpg","panties","")""")


        c.execute("""insert into picturelibrary_AAH_127 values ("0", "0","/static/Bianca_1.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAH_127 values ("0", "1","/static/Bianca_2.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAH_127 values ("1", "0","/static/Bianca_3.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAH_127 values ("1", "1","/static/Bianca_4.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAH_127 values ("0", "-1","/static/Bianca_5.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAH_127 values ("0", "-1","/static/Bianca_6.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAH_127 values ("0", "-1","/static/Bianca_7.jpg","panties","")""")
        c.execute("""insert into picturelibrary_AAH_127 values ("0", "-1","/static/Bianca_8.jpg","panties","")""")



        c.execute("""insert into picturelibrary_AAH_128 values ("-1", "0","/static/Isadora_1.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAH_128 values ("-1", "1","/static/Isadora_2.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAH_128 values ("-1", "2","/static/Isadora_3.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAH_128 values ("-1", "-1","/static/Isadora_4.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAH_128 values ("-1", "-1","/static/Isadora_5.jpg","lingerie","")""")
        c.execute("""insert into picturelibrary_AAH_128 values ("-1", "-1","/static/Isadora_6.jpg","panties","cheeky")""")
        c.execute("""insert into picturelibrary_AAH_128 values ("-1", "-1","/static/Isadora_7.jpg","panties","")""")
        c.execute("""insert into picturelibrary_AAH_128 values ("-1", "-1","/static/Isadora_8.jpg","panties","")""")        



        c.execute("""insert into picturelibrary_geschenkkarte_50 values ("-1", "0","/static/Isadora_1.jpg","geschenkkarte","")""")
        c.execute("""insert into picturelibrary_geschenkkarte_50 values ("-1", "1","/static/Isadora_1.jpg","geschenkkarte","")""")
        c.execute("""insert into picturelibrary_geschenkkarte_20 values ("-1", "0","/static/Isadora_2.jpg","geschenkkarte","")""")
        c.execute("""insert into picturelibrary_geschenkkarte_20 values ("-1", "1","/static/Isadora_2.jpg","geschenkkarte","")""") 
        print("ASDaaa6")

        conn.commit()


        


        


        c.execute("""create table if not exists bewertungen (
                bestellnummer text,
                style text,
                color text,
                bewertung text,
                bewertungstext text,
                bewertungsdatum text,
                gutscheincodeid text,
                passform text,
                bewertungsheadline text,
                bhgroesse text,
                slipgroesse text)""")

        conn.commit()


        c.execute("""create table gutscheineverschickt (
            senderemail text,
            empfaengeremail text,
            vorname text,                
            nachname text,
            datum text,
            code text,
            orderstatus text)""")
        conn.commit()
        





        


 



        



        c.execute("""create table if not exists gutscheine (
                gutscheincode text,
                rabatt text,
                zeitleiste text,
                status text,
                einmalig text)""")

        conn.commit()

        c.execute("""insert into gutscheine values ("PAY5LESS","-5","31. Dezember 2017","aktiv","nein")""")
        c.execute("""insert into gutscheine values ("PAY2LESS","-2","31. Dezember 2017","aktiv","nein")""")
        conn.commit()

        c.execute("""create table if not exists gutscheinkonto (
                email text,
                zahlung text,
                name text,
                bestellnummer text,
                datum text)""")
        conn.commit()



   
    
    
    

    c.execute("""create table if not exists aktuellewarenkoerbe (
            tablename text,
            datestamp text,
            gutscheincodeid text)""")
    conn.commit()

    update_timestamp(x,c,conn)





    c.execute("""create table if not exists plz (
            sessionid text,
            plz int)""")




        
        

    conn_2 = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                            password='okano1988',database='maxfischer2database')

    q = conn_2.cursor()

    status=0

 
    c.execute ("""select * from userdaten """)
    x=str(request.session.session_key)
    
    for row in c:
        if row[9]==x and x!="None":
            status=1
            y=row[5]
            if (row[0]!="" and row[12]!="") or (row[0]!="" and row[1]!=""):
                login="true"

    if status==0:
        c.execute ("""select * from plz""")
        y=""
        for row in c:
            if row[0]==x and x!="None":
                y=row[1]
                login="false"
                status=1


    
    if status==1:

    #########################################    freimengen_in_warenkorb_aktualisieren ##########################################
        try:
            conn_3 = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                    password='okano1988',database='maxfischer2database')

            t = conn_3.cursor()
            
            

            t.execute ("""select * from %s""" % (x))
            for row in c:
                q.execute ("""select * from menu""")
                for row_2 in q:
                    if (str(row[0]) == str(row_2[1]) and str(row[2]) == str(row_2[2])):
                        freiemenge=row_2[3]-row_2[4]-row_2[5]
                        t.execute("""update %s set freiemenge=%s where style=%s and datum=%s""",(x,freiemenge,row_2[1],row_2[2],))




        ########################################################################################################################################

            
            
            c.execute ("""select * from %s""" % (x))
            b=""
            max_var_warenkorb =4
            h=0
            for row in c:
                j=0
                if (h != 0):
                    b=b+";"
                while(j<=max_var_warenkorb):
                    if (j==max_var_warenkorb):
                        b=b+str(row[j])
                    else:
                        b=b+str(row[j])+","
                    j=j+1   
                h=h+1
        except:
            status=2


    if status==1:
        try:
            b=define_warenkorb(x,modelAB,sub_picture,c)
        except:
            status=0

    conn.close()     
    q.close()
    if status==1:
        try:
            
            t=get_template('test2.html')
            html=t.render({'favicon':get_favicon(),'brand_name':'Sensuals','warenkorb':b, 'date': p,'feedback':x,'login':login,'gerichte_raw':define_gerichte(ausgewaehlten_tag_abrufen(offset),"all","")})

            return HttpResponse(html)
        except:
            return HttpResponseRedirect("/hello/start_page/")
            
    else:
        if status==0:

            return HttpResponseRedirect("/hello/start_page/")
        else:
            return HttpResponseRedirect("/hello/log_out/")




def log_out_do_it(x,c,conn):
    c.execute ("""select * from userdaten """)

    userdaten=c.fetchall()

    
    for row in userdaten:
        
        if row[9]==x and x!="None":

            c.execute("""update userdaten set lastsessionid=%s where gutscheincode=%s""",("",row[11],))
            print("log_out")
            print(x)
            conn.commit()



            
    c.execute ("""select * from userdaten """)
    for row in c:
        print(row[9]) 
        
           


def log_out(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                        password='okano1988',database='maxfischer2database')
    c = conn.cursor(buffered=True)

    x=str(request.session.session_key)
    c.execute ("""select * from userdaten """)
    for row in c:
        print(row[9]+","+row[11])
    print("log-out")
    c.execute("""update userdaten set lastsessionid=%s where lastsessionid=%s""",("",x,))
    conn.commit()

    request.session.create()
    x=str(request.session.session_key)
    create_user(x,c,conn)

    
    c.execute ("""select * from userdaten """)
    for row in c:
        print(row[9]+","+row[11]) 

        

    
    




    return HttpResponseRedirect("/hello/start_page/")


def perform_security_check(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                        password='okano1988',database='maxfischer2database')
    c = conn.cursor(buffered=True)

    x=str(request.session.session_key)
    c.execute ("""select * from userdaten """)
    zaehler=0
    for row in c:
        if row[9]==x and x!="None":
            zaehler=zaehler+1

    if zaehler>1:
        c.execute("""update userdaten set lastsessionid=%s where lastsessionid=%s""",("",x,))
        conn.commit()



def call_timer(request):
    print("start")
    foo()

    return HttpResponseRedirect("/hello/start_page/")   

    
def foo():    


    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                            password='okano1988',database='maxfischer2database')
    c = conn.cursor(buffered=True)

    print("foooooo")


    now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
    
    c.execute ("""select * from VIPchangelog """)
    feedback="not ok"
    for row in c:
        if row[0]==str(now.month) and row[1]==str(now.year):
            feedback="ok"





    
    if feedback=="not ok":

        c.execute ("""select * from VIPmembers """)

        VIPmembers=c.fetchall()
        for row in VIPmembers:

            if row[1]=="true":
                c.execute ("""select * from userdaten """)

                userdaten=c.fetchall()
                for row_2 in userdaten:

                    if row_2[11]==row[0]:
                        storecredit=row_2[24]

                        c.execute("""update userdaten set storecredit=%s where gutscheincode=%s""",(storecredit+20,row_2[11],))
                        
                        if now.month==12:
                            nextvipmonth=1
                        else:
                            nextvipmonth=now.month+1
                            
                        c.execute("""update VIPmembers set nextvipmonth=%s,purchases=%s where gutscheincode=%s""",(str(nextvipmonth),0,row_2[11],))
                        conn.commit()
        c.execute("""insert into VIPchangelog values (%s,%s)""",(str(now.month),str(now.year),))
        conn.commit()
    check_availability(c,conn)
    check_referral_emails_sent()
            

    print("foooooo2")


    
    threading.Timer(5.0, foo).start()

    print("foooooo2")
    
def check_availability(c,conn):



    c.execute ("""select * from lingerieselection """)

    lingerieselection=c.fetchall()


    for row in lingerieselection:

        menge_bh=0
        menge_panty=0
        c.execute ("""select * from %s """ % ("stylecode_"+row[11]))
        for row_2 in c:
            if row[12]==row_2[2]:
                if row_2[0]=="BH":
                    menge_bh=menge_bh+int(row_2[4])-int(row_2[5])
                else:
                    menge_panty=menge_panty+int(row_2[4])-int(row_2[5])


        if menge_bh>0 and menge_panty>0:
            c.execute("""update lingerieselection set active=%s where name=%s""",("yes",row[0],))
        else:
            c.execute("""update lingerieselection set active=%s where name=%s""",("no",row[0],))
            
    conn.commit()                    

def check_referral_emails_sent():
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                            password='okano1988',database='maxfischer2database')
    c = conn.cursor(buffered=True)






        
    c.execute ("""select * from gutscheincodes_sent """)

    gutscheincodes_sent=c.fetchall()
    for row in gutscheincodes_sent:
        if row[4]=="no":
            referral_email(row[0],row[3],row[8],row[7],row[9])
            c.execute("""update gutscheincodes_sent set emailsent=%s,emailsentdate=%s,emailsenttime=%s where email=%s""",("yes",get_date_stamp_now(),get_time_stamp_now(),row[3]))


    conn.commit()

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












def freimengen_in_warenkorb_aktualisieren():



    conn.close()
    d.close()

    return q


                

				
				
def select_lieferdatum(days_):
    now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
    i=0    
    while (i<=days_-1):
        future=now + datetime.timedelta(days=i)
        TagInWoche=future.weekday()

        if(TagInWoche==5 or TagInWoche==6):
            days_=days_+1
        i=i+1

			
    Monat = ["Januar", "Februar", "Maerz", "April","Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
    future_date=str(future.day)+". "+str(Monat[future.month-1])+" "+str(future.year)
    return future_date


def ausgewaehlten_tag_abrufen(ausgewaehlter_tag):
    Wochentag = ["MO", "DI", "MI", "DO","FR", "SA", "SO"]
    Monat = ["Januar", "Februar", "Maerz", "April","Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
    
    datum_output=""
    ausgewaehlter_tag=int(ausgewaehlter_tag)
    i=0
    wochentag=-1

    now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
    
    while (i<=10):
        future=now + datetime.timedelta(days=i)
        TagInWoche=future.weekday()

        if(TagInWoche==5 or TagInWoche==6):
            datum_output=datum_output+"Wochenende"+","
            datum_output=datum_output+str(future.day)+","
            datum_output=datum_output+str(future.weekday())+","
            datum_output=datum_output+str(future.month-1)+","
            datum_output=datum_output+str(future.year)+","
            datum_output=datum_output+"0"

            if(i==0):
                DatumZukunft_ = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
                DatumZukunft_=DatumZukunft_- datetime.timedelta(days=1)
                datum_output=datum_output+","+str(DatumZukunft_.weekday())
            datum_output=datum_output+";"
	    
                
        else:
            datum_output=datum_output+"Wochentag"+","
            datum_output=datum_output+str(future.day)+","
            datum_output=datum_output+str(future.weekday())+","
            datum_output=datum_output+str(future.month-1)+","
            datum_output=datum_output+str(future.year)+","
            wochentag=wochentag+1;

            if (wochentag==ausgewaehlter_tag):
                datum_output=datum_output+"1;"
                output=[]
                output.append(str(future.day)+". "+Monat[future.month-1]+" "+str(future.year))
            else:
                datum_output=datum_output+"0;"
        i=i+1
            


    return output




def ausgewaehlten_wochentag_abrufen(ausgewaehlter_tag):
    Wochentag = ["Montag", "Dienstag", "Mittwoch", "Donnerstag","Freitag", "Samstag", "Sonntag"]
    Monat = ["Januar", "Februar", "Maerz", "April","Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
    
    datum_output=""
    ausgewaehlter_tag=int(ausgewaehlter_tag)
    i=0
    wochentag=-1

    now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
    
    while (i<=10):
        future=now + datetime.timedelta(days=i)
        TagInWoche=future.weekday()

        if(TagInWoche==5 or TagInWoche==6):
            datum_output=datum_output+"Wochenende"+","
            datum_output=datum_output+str(future.day)+","
            datum_output=datum_output+str(future.weekday())+","
            datum_output=datum_output+str(future.month-1)+","
            datum_output=datum_output+str(future.year)+","
            datum_output=datum_output+"0"

            if(i==0):
                DatumZukunft_ = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
                DatumZukunft_=DatumZukunft_- datetime.timedelta(days=1)
                datum_output=datum_output+","+str(DatumZukunft_.weekday())
            datum_output=datum_output+";"
	    
                
        else:
            datum_output=datum_output+"Wochentag"+","
            datum_output=datum_output+str(future.day)+","
            datum_output=datum_output+str(future.weekday())+","
            datum_output=datum_output+str(future.month-1)+","
            datum_output=datum_output+str(future.year)+","
            wochentag=wochentag+1;
            
            if (wochentag==ausgewaehlter_tag):
                datum_output=datum_output+"1;"
                output=Wochentag[future.weekday()]
            else:
                datum_output=datum_output+"0;"
        i=i+1
            


    return output





def check_month_VIP(month,year):
    now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))

    if now.day>=1 and now.day<=10:
        if now.year>int(year):
            return "true"
        else:
            if now.month+now.year>int(month)+int(year):
                return "true"
            else:
                return "false"
    else:
        return "false"


def check_rueckerstattung_month_VIP(month,year):
    now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))

    if now.day>=11 and now.day<=31:
        if now.year>int(year):
            return "true"
        else:
            if now.month+now.year>int(month)+int(year):
                return "true"
            else:
                return "false"
    else:
        return "false"


