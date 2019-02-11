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
import hashlib
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
import hashlib
import smtplib
import certifi
import urllib3
from OpenSSL import SSL
import idna
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
import pytz
from django.views.decorators.gzip import gzip_page
import math
import requests
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
import xlsxwriter
import easypost
from zenpy import Zenpy
from zenpy.lib.api_objects import Ticket, User

from facebookads.adobjects.adspixel import AdsPixel
from facebookads.adobjects.adaccount import AdAccount

import shippo
import unittest
import os

from tempfile import NamedTemporaryFile
from mailmerge import MailMerge

# encoding=utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
reload(sys)
sys.setdefaultencoding("ISO-8859-1")

from django.core.urlresolvers import reverse
from django.shortcuts import render

#import pysitemap
import klarnacheckout
#import pysitemap

import klarna
from exchangelib import DELEGATE, IMPERSONATION, Account, Credentials, ServiceAccount, \
    EWSDateTime, EWSTimeZone, Configuration, NTLM, CalendarItem, Message, \
    Mailbox, Attendee, Q, ExtendedProperty, FileAttachment, ItemAttachment, \
    HTMLBody, Build, Version



def email_marketing(request, offset):
    dhl_fill_out_form("Maxi", "Fischer", "Lindwurmstrasse", "99", "80337", "Munich", "max.fischer2@gmail.com", "Bla")
    t = get_template(offset + '.html')
    html = t.render({})
    return HttpResponse(html)


def dhl_fill_out_form(first_name, last_name, strasse, hausnummer, plz, stadt, email, bestellnummer):
    import mechanize
    import unidecode

    print first_name
    print last_name
    print strasse
    print hausnummer
    print plz
    print stadt
    print email
    print bestellnummer

    link = "https://amsel.dpwn.net/abholportal/gw/lp/portal/kaiwinselmann/customer/RpOrder.action?delivery=RetourenLager01&ADDR_SEND_FIRST_NAME=" + first_name + "&ADDR_SEND_LAST_NAME=" + last_name + "&ADDR_SEND_STREET=" + strasse + "%20" + hausnummer + "&ADDR_SEND_ZIP=" + plz + "&ADDR_SEND_CITY=" + stadt + "&ADDR_SEND_EMAIL=" + email + "&SHIPMENT_REFERENCE=ABC&ADDR_SEND_STREET_ADD=" + bestellnummer
    link = unidecode.unidecode(link)

    von = "Internes To Do: Ruecksendelabel pending"
    email = "service@darlinglace.com"
    betreff = "Internes To Do: VIP Model Ruecksendelabel pending"

    message = """Ruecksendelabel muss zugeschickt werden an """ + link

    creds = {
        'email': 'service@darlinglace.com',
        'token': 'oY8q9R9T4io7ZwQ1KdDktKwXgF3sWhMneMECjpL0',
        'subdomain': 'darlinglace'
    }
    zenpy_client = Zenpy(**creds)
    zenpy_client.tickets.create(
        Ticket(description=message, subject=betreff,
               requester=User(name=von, email=email))
    )

    br = mechanize.Browser()
    br.set_handle_robots(False)

    print(link)
    br.open(link)
    time.sleep(2)
    br.select_form(nr=0)
    req = br.submit()
    time.sleep(2)

    von = "Internes To Do: Ruecksendelabel erzeugt"
    email = "service@darlinglace.com"
    betreff = "Internes To Do: VIP Model Ruecksendelabel erzeugt"

    message = """Ruecksendelabel wurde verschickt """

    creds = {
        'email': 'service@darlinglace.com',
        'token': 'oY8q9R9T4io7ZwQ1KdDktKwXgF3sWhMneMECjpL0',
        'subdomain': 'darlinglace'
    }
    zenpy_client = Zenpy(**creds)
    zenpy_client.tickets.create(
        Ticket(description=message, subject=betreff,
               requester=User(name=von, email=email))
    )


def generate_order_klarna(user, c, email_, mobile, anrede, vorname, nachname, strasse, hausnummer, plz, stadt, land,
                          unternehmensdetails_rechnung, ip_adresse, rebates, lieferkosten, geburtsdatum_tag,
                          geburtsdatum_monat, geburtsdatum_jahr):
    if anrede == "Herr":
        geschlecht = 1
    else:
        geschlecht = 0

    land = "Deutschland"

    table_country_code = {'Deutschland': 'DE',
                          'Deutschland ': 'DE',
                          'Oesterreich': 'AT',
                          'Schweiz': 'CH',
                          'Germany': 'DE',
                          'Germany ': 'DE',
                          'Austria': 'AT',
                          'Switzerland': 'CH',
                          'Österreich': 'AT',
                          'Swiss': 'CH'
                          }

    config = klarna.Config(
        eid=70492,
        secret='VzRcsRPkLIF4qrT',
        country=table_country_code[land],
        language='DE',
        currency='EUR',
        mode='live',
        pcstorage='json',
        pcuri='/srv/pclasses.json',
        scheme='https',
        candice=True)

    k = klarna.Klarna(config)
    k.init()

    c.execute("""select * from cart_details where gutscheincode=%s and bestellt=%s""", (user, "nein",))
    for row in c:
        k.add_article(
            qty=row[1],
            title=row[0] + ", " + row[2] + " " + row[3],
            price=row[8] * row[1],
            articleNumber=row[7] + row[4],
            vat=19,
            discount=0,
            flags=32)

    if rebates > 0:
        k.add_article(
            qty=1,
            title="Rabatte",
            price=-rebates,
            vat=19,
            discount=0,
            flags=32)

    if float(lieferkosten) > 0:
        k.add_article(
            qty=1,
            title="Lieferkosten",
            price=float(lieferkosten),
            vat=19,
            discount=0,
            flags=40)

    mobile = "0" + (mobile.replace(" ", ""))

    addr = klarna.Address(
        email=email_,
        telno='',
        cellno=mobile,
        title=anrede,
        fname=vorname,
        lname=nachname,
        careof='',
        street=strasse,
        zip=plz,
        city=stadt,
        country=table_country_code[land],
        house_number=hausnummer,  # For DE and NL we need to specify house_number.
        house_extension=None)  # Only required for NL.

    k.shipping = addr
    k.billing = addr

    print "geburtsdatum_tag+geburtsdatum_monat+geburtsdatum_jahr"
    print geburtsdatum_tag + geburtsdatum_monat + geburtsdatum_jahr
    k.clientip = ip_adresse
    try:
        order = k.reserve_amount(
            geburtsdatum_tag + geburtsdatum_monat + geburtsdatum_jahr,
            geschlecht,
            pclass=klarna.PClass.Type.INVOICE
        )
    except:
        order = "keine akzeptanz durch klarna"
    print order

    print(order)
    return order


def test_klarna(request):
    config = klarna.Config(
        eid=70492,
        secret='VzRcsRPkLIF4qrT',
        country='DE',
        language='DE',
        currency='EUR',
        mode='live',
        pcstorage='json',
        pcuri='/srv/pclasses.json',
        scheme='https',
        candice=True)

    k = klarna.Klarna(config)
    k.init()

    k.add_article(
        qty=1,
        title="Handling fee",
        price=1.5,
        vat=19,
        discount=0,
        flags=32)

    addr = klarna.Address(
        email='always_accepted@klarna.com',
        telno='',
        cellno='015 2211 3356',
        title='Frau',
        fname='Testperson-de',
        lname='Approved',
        careof='',
        street='Hellersbergstraße',
        zip='14601',
        city='Neuss',
        country='DE',
        house_number='14',  # For DE and NL we need to specify house_number.
        house_extension=None)  # Only required for NL.

    k.shipping = addr
    k.billing = addr

    k.clientip = '83.10.0.5'

    order = k.reserve_amount(
        '07071960',
        0,
        pclass=klarna.PClass.Type.INVOICE
    )

    oder_activation = k.activate(order[0], flags=8)


def test_rechnung(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2', \
                                   password='okano1988', database='maxfischer2database')
    c = conn.cursor(buffered=True)
    config = klarna.Config(
        eid=70492,
        secret='VzRcsRPkLIF4qrT',
        country='DE',
        language='DE',
        currency='EUR',
        mode='live',
        pcstorage='json',
        pcuri='/srv/pclasses.json',
        scheme='https',
        candice=True)

    k = klarna.Klarna(config)
    k.init()

    oder_activation = k.activate("2381647170", flags=8)


def generate_rechnung(c, conn, bestellnummer):
    c.execute("""select * from rechnungsnummer """)
    rechnungsnummer_table = c.fetchall()
    feedback = ""
    for row in rechnungsnummer_table:
        if row[1] == bestellnummer:
            rechnungsnummer = row[0]
            userid = row[2]

    template_1 = "Rechnung Template.docx"
    document_1 = MailMerge(template_1)

    c.execute("""select * from bestellt where gutscheincode=%s """, (userid,))
    bestellt_daten = c.fetchall()
    list = []
    for row_2 in bestellt_daten:
        c.execute("""select * from cart_details where gutscheincode=%s and bestellt=%s""", (userid, "ja",))
        detail_table = c.fetchall()
        for row_3 in detail_table:
            price = str('{0:.2f}'.format(row_3[8])).replace(".", ",")
            list.append(
                {'prod_desc': row_3[0] + ", " + row_3[2] + " " + row_3[3], 'quantity': str(row_3[1]), 'tax_rate': '19',
                 'price': price})

    c.execute("""select * from bestellt where gutscheincode=%s""", (userid,))
    bestellt_daten = c.fetchall()
    for row_2 in bestellt_daten:
        if row_2[21] == bestellnummer:
            brutto_betrag = str('{0:.2f}'.format(
                define_rebates(userid, bestellnummer, "", "", "", c, conn, "", "yes", "no", "no"))).replace(".", ",")
            rabatte_betrag = str('{0:.2f}'.format(
                define_rebates(userid, bestellnummer, "", "", "", c, conn, "", "no", "yes", "no"))).replace(".", ",")
            lieferkosten_betrag = str('{0:.2f}'.format(
                define_rebates(userid, bestellnummer, "", "", "", c, conn, "", "no", "no", "yes"))).replace(".", ",")
            netto_betrag = str('{0:.2f}'.format(
                define_rebates(userid, bestellnummer, "", "", "", c, conn, "", "yes", "no", "no") / 1.19)).replace(".",
                                                                                                                   ",")
            sum_tax_betrag = str('{0:.2f}'.format(
                define_rebates(userid, bestellnummer, "", "", "", c, conn, "", "yes", "no", "no") - define_rebates(
                    userid, bestellnummer, "", "", "", c, conn, "", "yes", "no", "no") / 1.19)).replace(".", ",")

            document_1.merge(First_Name=row_2[6],
                             Last_Name=row_2[7],
                             Additional_Details=row_2[5],
                             Street=row_2[1],
                             PLZ=row_2[3],
                             City=row_2[2],
                             Country=row_2[4],
                             Date=row_2[19],
                             Rg_Nr=str(rechnungsnummer),
                             Kunde_Nr=userid,
                             Auftrag_Nr=row_2[21],
                             L_Adr_1=row_2[1],
                             L_Adr_2=row_2[5],
                             L_Street=row_2[1],
                             L_PLZ=row_2[3],
                             L_City=row_2[2],
                             L_Country=row_2[4],
                             brutto=brutto_betrag,
                             rabatte=rabatte_betrag,
                             lieferkosten=lieferkosten_betrag,
                             netto=netto_betrag,
                             sum_tax=sum_tax_betrag, )

    document_1.merge_rows('prod_desc', list)

    # Save the document as example 1
    document_1.write('Rechnung' + str(rechnungsnummer) + '.docx')


def paypal_verficiation(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2', \
                                   password='okano1988', database='maxfischer2database')
    c = conn.cursor(buffered=True)

    paymill_context = paymill.PaymillContext('82239adeff57ef5d51ec2e5d11fd915d')
    transaction_service = paymill_context.get_transaction_service()

    x = str(request.session.session_key)
    id = request.GET.get('paymill_trx_id')

    #    transactions_list=transaction_service.detail(transaction_id)

    #    transaction_key = {"id":"tran_8579d63977b7e51ab7631d2f06ae"}

    class Object(object):
        pass

    transaction_key = Object()
    transaction_key.id = id
    user = get_userid_from_session_id(c, x)

    transactions_list = transaction_service.detail(transaction_key)

    c.execute("""select * from pending_payments """)

    status = ""
    print "paypal"
    if transactions_list["status"] == "closed":

        status = "true"
    else:
        if transactions_list["status"] == "failed":
            status = "false"

    bestellnummer = transactions_list["description"][-7:]
    c.execute("""update pending_payments set transaktionsnummer=%s where bestellnummer=%s""", (id, bestellnummer,))
    conn.commit()
    print status
    if status == "false":
        return HttpResponseRedirect("/")

    if status == "true":
        check_pending_payments(bestellnummer, "true", c, conn, user)
        return HttpResponseRedirect("/account_page/bestellungen_ansehen/" + bestellnummer)
    if status == "":
        check_pending_payments(bestellnummer, "true", c, conn, user)
        c.execute("""update pending_payments set accepted=%s, transaktionsnummer=%s where bestellnummer=%s""",
                  ("false", id, bestellnummer,))
        conn.commit()
        c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s)""" % ("order_confirmation_emails"), (
        bestellnummer, get_userdata(user, c, 11), get_userdata(user, c, 0), "Deine Bestellung bei Darling Lace", "nein",
        "no",))
        conn.close()
        return HttpResponseRedirect("/account_page/bestellungen_ansehen/" + bestellnummer)


def request_paymill_paypal_code(amount_, currency_, return_url_, cancel_url_, description_):
    paymill_context = paymill.PaymillContext('82239adeff57ef5d51ec2e5d11fd915d')
    checksum_service = paymill_context.get_checksum_service()
    checksum = checksum_service.create(checksum_type='paypal', amount=amount_, currency=currency_,
                                       return_url=return_url_,
                                       cancel_url=cancel_url_, description=description_)

    return checksum


@csrf_exempt
def credit_card(request):
    #   r = request.post('http://192.168.2.100:8000/credit_card/', json={"key": "value"})
    #    print(request)
    #   if paymill.validateCardNumber('4111111111111111')==true:
    #        print("true")
    #    else:
    #        print("false")

    #    paymill_context = paymill.PaymillContext('82239adeff57ef5d51ec2e5d11fd915d')

    #    transaction_service = paymill_context.get_transaction_service()
    #    transaction_with_token = transaction_service.create_with_token(
    #        token='82239adeff57ef5d51ec2e5d11fd915d',
    #        amount=4200,
    #        currency='EUR',
    #        description='Test Transaction'
    #    )

    t = get_template('test.html')
    html = t.render(
        {'email': get_userdata(user, c, 0), 'vorname': get_userdata(user, c, 2), 'nachname': get_userdata(user, c, 3),
         'stadt': get_userdata(user, c, 6), 'plz': get_userdata(user, c, 5)})

    return HttpResponse(html)


# def check_transaction(payment_id_,amount,currency_,description_,client_id_):
def check_transaction(transaction_id):
    paymill_context = paymill.PaymillContext('82239adeff57ef5d51ec2e5d11fd915d')
    transaction_service = paymill_context.get_transaction_service()

    #   transactions_list = transaction_service.list()

    transactions_list = transaction_service.detail(transaction_id)

    if transactions_list["status"] == "closed":

        return "true"
    else:
        if transactions_list["status"] == "failed":
            return "false"
        else:
            return ""

    #####check whether transaction was successful


@csrf_exempt
def credit_card_test(request):
    q = request.POST.get('token', None)

    paymill_context = paymill.PaymillContext('82239adeff57ef5d51ec2e5d11fd915d')

    client_service = paymill_context.get_client_service()
    credit_card_add_new_payment(q, "client_5170293392dfda5607c1")

    #  clients = client_service.list()

    #   print(clients)

    #   data = clients.data[0]

    #  print(len(clients.data))
    # i=0
    # while i<=len(clients.data)-1:
    #        print(clients.data[i]["payment"])
    #        print(i)
    #    i=i+1

    # credit_card_create_new_client("service@darlinglace.com")

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

    t = get_template('testa.html')
    html = t.render(
        {'email': get_userdata(user, c, 0), 'vorname': get_userdata(user, c, 2), 'nachname': get_userdata(user, c, 3),
         'stadt': get_userdata(user, c, 6), 'plz': get_userdata(user, c, 5), 'favicon': get_favicon(),
         'path': request.path, 'brand_name': 'Darling Lace'})
    conn.close()
    return HttpResponse(html)


def create_new_client_test(request):
    credit_card_create_new_client("service@darlinglace.com")

    t = get_template('testa.html')
    html = t.render(
        {'email': get_userdata(user, c, 0), 'vorname': get_userdata(user, c, 2), 'nachname': get_userdata(user, c, 3),
         'stadt': get_userdata(user, c, 6), 'plz': get_userdata(user, c, 5), 'favicon': get_favicon(),
         'path': request.path, 'brand_name': 'Darling Lace'})
    conn.close()
    return HttpResponse(html)


def test_update_client_with_email(p):
    c = p.client_service.create(email="test@mail.com")
    c.email = "test2@mail.com"
    assertEqual("test2@mail.com", p.client_service.update(c).email)


def credit_card_create_new_client(client_email):
    paymill_context = paymill.PaymillContext('82239adeff57ef5d51ec2e5d11fd915d')
    client_service = paymill_context.get_client_service()
    client = client_service.create(email=client_email)
    client_details = client_service.detail(client)

    return client_details["id"]


def test_creditcard(request):
    paymill_context = paymill.PaymillContext('82239adeff57ef5d51ec2e5d11fd915d')
    payment_service = paymill_context.get_payment_service()
    payments_list = payment_service.list()
    i = 0
    while i <= len(payments_list.data) - 1:
        i = i + 1


def get_creditcard_payment_data(client_id):
    paymill_context = paymill.PaymillContext('82239adeff57ef5d51ec2e5d11fd915d')
    payment_service = paymill_context.get_payment_service()
    payments_list = payment_service.list()
    i = 0
    while i <= len(payments_list.data) - 1:
        i = i + 1


def credit_card_delete_payment_test(token_id):
    paymill_context = paymill.PaymillContext('82239adeff57ef5d51ec2e5d11fd915d')
    payment_service = paymill_context.get_payment_service()

    class Object(object):
        pass

    a = Object()
    a.id = token_id
    payment_service.remove(a)


def credit_card_add_new_payment_test(token_id, client_id_):
    paymill_context = paymill.PaymillContext('82239adeff57ef5d51ec2e5d11fd915d')
    payment_service = paymill_context.get_payment_service()
    payment_with_token_and_client = payment_service.create(
        token=token_id,
        client_id=client_id_

    )

    return payment_with_token_and_client


def payment_credit_card_test(request):
    paymill_context = paymill.PaymillContext('82239adeff57ef5d51ec2e5d11fd915d')
    transaction_service = paymill_context.get_transaction_service()
    transactions_list = transaction_service.list()
    credit_card_add_new_transaction("pay_274f6a119abb2fbdda38728b", "3912312304", "EUR", "bla",
                                    "client_956f9a14cd753011d858")


#   print(check_transaction("pay_274f6a119abb2fbdda38728b","3912312304","EUR","","client_956f9a14cd753011d858"))


def payment_credit_card_paypal_refund(transaction_id_, amount_):
    paymill_context = paymill.PaymillContext('82239adeff57ef5d51ec2e5d11fd915d')
    refund_service = paymill_context.get_refund_service()

    price_paymill = int(float(amount_) * 100)
    refund_transaction = refund_service.refund_transaction(
        transaction_id=transaction_id_,
        amount=price_paymill
    )


def get_start_date_of_subscription():
    now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
    i = 0
    year = now.year + 1
    month = now.month + 1
    if now.month + 1 > 12:
        month = 1
        year = now.year + 1

    Monat = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    unix = time.mktime(time.strptime('01/' + Monat[month - 1] + '/' + str(year), "%d/%m/%Y"))

    return unix


def credit_card_add_new_transaction(payment_id_, amount, currency_, description_, client_id_):
    paymill_context = paymill.PaymillContext('82239adeff57ef5d51ec2e5d11fd915d')
    transaction_service = paymill_context.get_transaction_service()
    transaction_with_client_and_payment = transaction_service.create_with_payment_id(payment_id=payment_id_,
                                                                                     amount=amount, currency=currency_,
                                                                                     description=description_,
                                                                                     client_id=client_id_)

    class Object(object):
        pass

    transaction_key = Object()
    transaction_key.id = transaction_with_client_and_payment["id"]

    return transaction_key


def get_lingerie_from_search(search_item, user, modelAB, sub_picture, c):
    lingerie = []

    class Lingerie(object):
        def __init__(self, name, sizerange, pic, priceregular, pricesubscription, description, details, active,
                     productgroup, wishlist, descriptionshort, stylecode, colorcode, position, stylegroup, link):
            self.name = name
            self.sizerange = sizerange
            self.pic = pic
            self.priceregular = priceregular
            self.pricesubscription = pricesubscription
            self.description = description
            self.details = details
            self.active = active
            self.productgroup = productgroup
            self.wishlist = wishlist
            self.descriptionshort = descriptionshort
            self.stylecode = stylecode
            self.colorcode = colorcode
            self.position = position
            self.stylegroup = stylegroup
            self.link = link

    try:

        c.execute(
            """ALTER TABLE lingerieselection ADD FULLTEXT(name,sizerange,description,descriptionshort,productgroup,dominantfactorcolors,dominantfactorstyle,details)""")
    except:
        search_item = search_item

    if search_item != "":
        search_item = search_item + "*"

        c.execute(
            """SELECT * FROM lingerieselection WHERE MATCH(name,sizerange,description,descriptionshort,productgroup,dominantfactorcolors,dominantfactorstyle,details) AGAINST (%s IN BOOLEAN MODE)""",
            (search_item,))
        lingerieselection = c.fetchall()

        for row in lingerieselection:
            link = link_name_bestimmen(row[8])
            stylegroup = get_main_style_group(row[21], row[22], row[23], row[24])

            if row[14] == "true":
                priceregular = row[3] - row[13]
                pricesubscription = row[4] - row[13]
            else:
                priceregular = row[3]
                pricesubscription = row[4]

            lingerie.append(Lingerie(row[0], row[1],
                                     get_pictures_from_consolidated_table(c, row[12], row[13], modelAB, sub_picture,
                                                                          row[2], "all", "big"), priceregular,
                                     pricesubscription, row[5], row[6], row[7], row[8],
                                     get_wishlist(row[12], row[13], user, row[8]), row[9], row[12], row[13], row[51],
                                     stylegroup, link, ))

        json_string = json.dumps([Lingerie.__dict__ for Lingerie in lingerie])
    else:

        json_string = ""

    return json_string


@csrf_exempt
def full_text_search(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2', \
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)
        search_item = request.GET.get('search_item')

        x = str(request.session.session_key)

        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            userdaten = c.fetchall()
            for row in userdaten:
                user = row[11]
                modelAB = row[47]
                sub_picture = row[48]

        lingerie = get_lingerie_from_search(search_item, user, modelAB, sub_picture, c)

        conn.close()
        return HttpResponse(lingerie, content_type='application/json')
    else:
        raise Http404


def define_wishlist_object(user, modelAB, sub_picture, c, conn):
    wishlist = []

    class Wishlist(object):
        def __init__(self, name, picture, stylecode, colorcode, productgroup, pricesubscription, link1):
            self.name = name
            self.picture = picture
            self.stylecode = stylecode
            self.colorcode = colorcode
            self.productgroup = productgroup
            self.pricesubscription = pricesubscription
            self.link1 = link1

    c.execute("""select * from wishlist where gutscheincode=%s """, (user,))
    wishlist_data = c.fetchall()
    for row_2 in wishlist_data:
        c.execute("""select * from lingerieselection where stylecode=%s and colorcode=%s and productgroup=%s""",
                  (row_2[0], row_2[1], row_2[3]))
        lingerieselection_data = c.fetchall()
        for row_4 in lingerieselection_data:
            wishlist.append(Wishlist(row_4[0],
                                     get_pictures_from_consolidated_table(c, row_4[12], row_4[13], modelAB, sub_picture,
                                                                          row_4[2], "first", "small"), row_2[0],
                                     row_2[1], row_2[3], row_4[4], link_name_bestimmen(row_4[8])))

    json_string = json.dumps([Wishlist.__dict__ for Wishlist in wishlist])

    c.execute("""update userdaten set wishlist=%s where gutscheincode=%s""", (json_string, user,))
    conn.commit()

    return json_string


def define_wishlist(user, modelAB, sub_picture, c):
    wishlist = []

    class Wishlist(object):
        def __init__(self, name, picture, stylecode, colorcode, productgroup, pricesubscription, link1):
            self.name = name
            self.picture = picture
            self.stylecode = stylecode
            self.colorcode = colorcode
            self.productgroup = productgroup
            self.pricesubscription = pricesubscription
            self.link1 = link1

    c.execute("""select * from wishlist where gutscheincode=%s """, (user,))
    wishlist_data = c.fetchall()
    for row_2 in wishlist_data:
        c.execute("""select * from lingerieselection where stylecode=%s and colorcode=%s and productgroup=%s""",
                  (row_2[0], row_2[1], row_2[3]))
        lingerieselection_data = c.fetchall()
        for row_4 in lingerieselection_data:
            wishlist.append(Wishlist(row_4[0],
                                     get_pictures_from_consolidated_table(c, row_4[12], row_4[13], modelAB, sub_picture,
                                                                          row_4[2], "first", "small"), row_2[0],
                                     row_2[1], row_2[3], row_4[4], link_name_bestimmen(row_4[8])))
    json_string = json.dumps([Wishlist.__dict__ for Wishlist in wishlist])

    return json_string


def load_style_filter(filter_style, filter_color, filter_size, click_last, filter_padding, link, user, day, month, year,
                      c):
    reload(sys)
    sys.setdefaultencoding("ISO-8859-1")

    filter_ = []

    class Filter(object):
        def __init__(self, group, name, show, selected):
            self.group = group
            self.name = name
            self.show = show
            self.selected = selected

    print link

    if link == "Slips":
        link = "panties"

    list = get_styles(filter_style, filter_color, filter_size, filter_padding, "", 0, link, user, day, month, year, c)

    print "load_style_filter"

    styles = list[0][0]
    color = list[1][0]
    padding = list[2][0]
    sizes = list[3][0]

    if link != "panties":
        i = 0
        while i <= 12:
            if styles[i][1] == 1:
                if styles[i][0] == filter_style:
                    filter_.append(Filter("Styles", styles[i][0], "true", "true"))
                else:
                    filter_.append(Filter("Styles", styles[i][0], "true", "false"))
            else:
                filter_.append(Filter("Styles", styles[i][0], "false", "false"))
            i = i + 1

        i = 0
        while i <= 6:
            if color[i][1] == 1:
                if color[i][0] == filter_color:
                    filter_.append(Filter("Color", color[i][0], "true", "true"))
                else:
                    filter_.append(Filter("Color", color[i][0], "true", "false"))
            else:
                filter_.append(Filter("Color", color[i][0], "false", "false"))
            i = i + 1

        i = 0
        while i <= 3:
            if padding[i][1] == 1:
                if padding[i][0] == filter_padding:
                    filter_.append(Filter("Padding", padding[i][0], "true", "true"))
                else:
                    filter_.append(Filter("Padding", padding[i][0], "true", "false"))
            else:
                filter_.append(Filter("Padding", padding[i][0], "false", "false"))
            i = i + 1

        i = 0
        while i <= 59:
            if sizes[i][1] == 1:
                if sizes[i][0] == filter_size:
                    filter_.append(Filter("Sizes", sizes[i][0], "true", "true"))
                else:
                    filter_.append(Filter("Sizes", sizes[i][0], "true", "false"))
            else:
                filter_.append(Filter("Sizes", sizes[i][0], "false", "false"))
            i = i + 1
    else:
        print "load_style_filter geht los"
        i = 0
        while i <= 4:
            if styles[i][1] == 1:
                if styles[i][0] == filter_style:
                    filter_.append(Filter("Styles", styles[i][0], "true", "true"))
                else:
                    filter_.append(Filter("Styles", styles[i][0], "true", "false"))
            else:
                filter_.append(Filter("Styles", styles[i][0], "false", "false"))
            i = i + 1

        i = 0
        while i <= 6:
            if color[i][1] == 1:
                if color[i][0] == filter_color:
                    filter_.append(Filter("Color", color[i][0], "true", "true"))
                else:
                    filter_.append(Filter("Color", color[i][0], "true", "false"))
            else:
                filter_.append(Filter("Color", color[i][0], "false", "false"))
            i = i + 1

        i = 0
        while i <= 6:
            if sizes[i][1] == 1:
                if sizes[i][0] == filter_size:
                    filter_.append(Filter("Sizes", sizes[i][0], "true", "true"))
                else:
                    filter_.append(Filter("Sizes", sizes[i][0], "true", "false"))
            else:
                filter_.append(Filter("Sizes", sizes[i][0], "false", "false"))
            i = i + 1

    json_string = json.dumps([Filter.__dict__ for Filter in filter_])

    print(json_string)

    return json_string


def get_styles(filter_style_, filter_color_, filter_size_, filter_padding_, last_click, id, link, user, day, month,
               year, c):
    reload(sys)
    sys.setdefaultencoding("ISO-8859-1")

    styles = [[] for i in range(13)]
    color = [[] for i in range(14)]
    padding = [[] for i in range(4)]
    sizes = [[] for i in range(90)]
    sizes_dict = {}

    list = [[] for i in range(5)]
    now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))

    i = 0

    if link != "panties":
        c.execute("""select * from style """)
        for row in c:
            styles[i].append(row[0])
            styles[i].append(0)
            i = i + 1

        i = 0
        c.execute("""select * from color """)
        for row in c:
            color[i].append(row[0])
            color[i].append(0)
            color[i].append(row[1])
            i = i + 1

        i = 0
        c.execute("""select * from padding """)
        for row in c:
            padding[i].append(row[0])
            padding[i].append(0)
            i = i + 1

        i = 0
        c.execute("""select * from sizes""")
        for row in c:
            sizes_dict[row[0]] = i
            sizes[i].append(row[0])
            sizes[i].append(0)
            i = i + 1
    else:
        c.execute("""select * from stylepanty """)
        for row in c:
            styles[i].append(row[0])
            styles[i].append(0)
            i = i + 1

        i = 0
        c.execute("""select * from color """)
        for row in c:
            color[i].append(row[0])
            color[i].append(0)
            color[i].append(row[1])
            i = i + 1

        i = 0
        c.execute("""select * from sizespanty""")
        for row in c:
            sizes_dict[row[0]] = i
            sizes[i].append(row[0])
            sizes[i].append(0)
            i = i + 1

    now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))

    print("filter")
    print(styles)
    index = 0
    c.execute("""select * from lingerieselection ORDER BY position ASC""")

    lingerieselection = c.fetchall()
    for row in lingerieselection:
        if link != "Mein Showroom":

            if link == "BH Sets" or link == "lingerie":

                if row[7] == "yes":

                    id = 0

                    while id <= 3:
                        print(id)
                        if filter_color_ == "" and filter_style_ == "" and filter_size_ == "" and filter_padding_ == "":
                            filter_style = filter_style_
                            filter_color = filter_color_
                            filter_size = filter_size_
                            filter_padding = filter_padding_
                            id = 4
                        else:
                            if id == 0:
                                filter_style = ""
                                filter_color = filter_color_
                                filter_size = filter_size_
                                filter_padding = filter_padding_
                            if id == 1:
                                filter_style = filter_style_
                                filter_color = ""
                                filter_size = filter_size_
                                filter_padding = filter_padding_
                            if id == 2:
                                filter_style = filter_style_
                                filter_color = filter_color_
                                filter_size = filter_size_
                                filter_padding = ""
                            if id == 3:
                                filter_style = filter_style_
                                filter_color = filter_color_
                                filter_size = ""
                                filter_padding = filter_padding_
                        i = 0

                        print(row[0])
                        while i <= 12:
                            if last_click == "":

                                if i > 4:
                                    zaehler = i + 5
                                else:
                                    zaehler = i
                                if (row[20 + zaehler] == "x" and styles[i][0] == filter_style) or (
                                        filter_style == "" and row[20 + zaehler] == "x"):
                                    j = 0

                                    while j <= 6:
                                        if (row[50] == color[j][2] and filter_color == color[j][0]) or (
                                                filter_color == "" and row[50] == color[j][2]):

                                            k = 0

                                            while k <= 3:
                                                if (row[40 + k] == "x" and padding[k][0] == filter_padding) or (
                                                        filter_padding == "" and row[40 + k] == "x"):

                                                    g = 0

                                                    if filter_size == "":

                                                        if id == 0:
                                                            c.execute(
                                                                """select * from %s where color='%s' and stylecode='%s'""" % (
                                                                "stylecode", row[13], row[12],))
                                                            rows = c.fetchall()

                                                            if len(rows) > 0:
                                                                styles[i][1] = 1
                                                        if id == 1:
                                                            c.execute(
                                                                """select * from %s where color='%s' and stylecode='%s'""" % (
                                                                "stylecode", row[13], row[12],))
                                                            rows = c.fetchall()

                                                            if len(rows) > 0:
                                                                color[j][1] = 1

                                                        if id == 2:

                                                            c.execute(
                                                                """select * from %s where color='%s' and stylecode='%s'""" % (
                                                                "stylecode", row[13], row[12],))
                                                            rows = c.fetchall()
                                                            if len(rows) > 0:
                                                                padding[k][1] = 1

                                                        if id == 3:
                                                            c.execute(
                                                                """select * from %s where color='%s' and stylecode='%s'""" % (
                                                                "stylecode", row[13], row[12],))
                                                            for row_2 in c:
                                                                menge = int(row_2[4]) - int(row_2[5])
                                                                if menge > 0:
                                                                    try:

                                                                        sizes[sizes_dict[row_2[3]]][1] = 1



                                                                    except:
                                                                        id = id
                                                        if id == 4:

                                                            now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))

                                                            c.execute(
                                                                """select * from %s where color='%s' and type='%s' and stylecode='%s'""" % (
                                                                "stylecode", row[13], "BH", row[12],))
                                                            for row_2 in c:
                                                                menge = int(row_2[4]) - int(row_2[5])
                                                                if menge > 0:
                                                                    try:
                                                                        styles[i][1] = 1
                                                                        color[j][1] = 1
                                                                        padding[k][1] = 1

                                                                        sizes[sizes_dict[row_2[3]]][1] = 1



                                                                    except:
                                                                        id = id


                                                    else:
                                                        c.execute(
                                                            """select * from %s where color='%s' and size='%s' and stylecode='%s'""" % (
                                                            "stylecode", row[13], filter_size, row[12],))
                                                        for row_2 in c:

                                                            menge = int(row_2[4]) - int(row_2[5])
                                                            if menge > 0:

                                                                if id == 0:
                                                                    styles[i][1] = 1
                                                                if id == 1:
                                                                    color[j][1] = 1
                                                                if id == 2:
                                                                    padding[k][1] = 1
                                                                if id == 3:

                                                                    try:

                                                                        sizes[sizes_dict[row_2[3]]][1] = 1



                                                                    except:
                                                                        id = id

                                                k = k + 1
                                        j = j + 1
                            i = i + 1
                        id = id + 1
            else:
                if row[7] == "yes" and row[8] == "panties":

                    id = 0

                    while id <= 2:
                        if filter_color_ == "" and filter_style_ == "" and filter_size_ == "":
                            filter_style = filter_style_
                            filter_color = filter_color_
                            filter_size = filter_size_
                            id = 2
                        else:
                            if id == 0:
                                filter_style = ""
                                filter_color = filter_color_
                                filter_size = filter_size_
                            if id == 1:
                                filter_style = filter_style_
                                filter_color = ""
                                filter_size = filter_size_
                            if id == 2:
                                filter_style = filter_style_
                                filter_color = filter_color_
                                filter_size = ""

                        i = 0

                        print "biiig_test"
                        while i <= 4:
                            if last_click == "":

                                if (row[25 + i] == "x" and styles[i][0] == filter_style) or (
                                        filter_style == "" and row[25 + i] == "x"):
                                    print("next1" + str(id))
                                    j = 0

                                    while j <= 6:
                                        if (row[50] == color[j][2] and filter_color == color[j][0]) or (
                                                filter_color == "" and row[50] == color[j][2]):
                                            print("next2" + str(id))

                                            if filter_size == "":
                                                print("next3" + str(id))

                                                if id == 0:
                                                    c.execute(
                                                        """select * from %s where color='%s' and stylecode='%s'""" % (
                                                        "stylecode", row[13], row[12],))
                                                    rows = c.fetchall()
                                                    if len(rows) > 0:
                                                        styles[i][1] = 1
                                                if id == 1:
                                                    c.execute(
                                                        """select * from %s where color='%s' and stylecode='%s'""" % (
                                                        "stylecode", row[13], row[12],))
                                                    rows = c.fetchall()
                                                    if len(rows) > 0:
                                                        color[j][1] = 1

                                                if id == 2:
                                                    print "paaanties2" + row[13]
                                                    c.execute(
                                                        """select * from %s where color='%s' and stylecode='%s'""" % (
                                                        "stylecode", row[13], row[12],))
                                                    for row_2 in c:
                                                        menge = int(row_2[4]) - int(row_2[5])
                                                        if menge > 0:

                                                            styles[i][1] = 1
                                                            color[j][1] = 1
                                                            try:
                                                                groesse = row_2[3]
                                                                groesse = groesse.split(" ")
                                                                print(groesse)
                                                                sizes[sizes_dict[groesse[1]]][1] = 1



                                                            except:
                                                                id = id



                                            else:
                                                c.execute(
                                                    """select * from %s where color='%s' and size='%s' and type='%s'""" % (
                                                    "stylecode", row[13], filter_size, "panties",))
                                                for row_2 in c:

                                                    menge = int(row_2[4]) - int(row_2[5])
                                                    if menge > 0:

                                                        if id == 0:
                                                            styles[i][1] = 1
                                                        if id == 1:
                                                            color[j][1] = 1
                                                        if id == 2:

                                                            try:

                                                                groesse = row_2[3]
                                                                groesse = groesse.split(" ")
                                                                sizes[sizes_dict[groesse[1]]][1] = 1
                                                            except:
                                                                id = id

                                        j = j + 1
                            i = i + 1
                        id = id + 1
        else:

            c.execute("""select * from showroom where gutscheincode=%s """, (user,))
            showroom_data = c.fetchall()
            for row_3 in showroom_data:

                if row_3[0] == row[11] and row_3[1] == row[12] and row_3[2] == day and row_3[3] == month and row_3[
                    4] == year:

                    if row[7] == "yes":

                        id = 0

                        while id <= 3:
                            if filter_color_ == "" and filter_style_ == "" and filter_size_ == "" and filter_padding_ == "":
                                filter_style = filter_style_
                                filter_color = filter_color_
                                filter_size = filter_size_
                                filter_padding = filter_padding_
                                id = 4
                            else:
                                if id == 0:
                                    filter_style = ""
                                    filter_color = filter_color_
                                    filter_size = filter_size_
                                    filter_padding = filter_padding_
                                if id == 1:
                                    filter_style = filter_style_
                                    filter_color = ""
                                    filter_size = filter_size_
                                    filter_padding = filter_padding_
                                if id == 2:
                                    filter_style = filter_style_
                                    filter_color = filter_color_
                                    filter_size = filter_size_
                                    filter_padding = ""
                                if id == 3:
                                    filter_style = filter_style_
                                    filter_color = filter_color_
                                    filter_feature = filter_feature_
                                    filter_size = ""
                                    filter_padding = filter_padding_
                            i = 0

                            while i <= 12:
                                if last_click == "":

                                    if i > 4:
                                        zaehler = i + 5
                                    else:
                                        zaehler = i
                                    if (row[20 + zaehler] == "x" and styles[i][0] == filter_style) or (
                                            filter_style == "" and row[20 + zaehler] == "x"):
                                        #                                   print(row[21+zaehler]+"==x and "+styles[i][0]+"=="+filter_style+") or ("+filter_style+"== and "+row[21+zaehler]+"==x")
                                        j = 0

                                        while j <= 6:
                                            # print(str(row[50])+"=="+str(color[j][2]) +"and "+str(filter_color)+"=="+str(color[j][0]) +"or "+str(filter_color)+"== and "+str(row[50])+"=="+str(color[j][2]))
                                            if (row[50] == color[j][2] and filter_color == color[j][0]) or (
                                                    filter_color == "" and row[50] == color[j][2]):

                                                k = 0

                                                while k <= 3:
                                                    if (row[40 + k] == "x" and padding[k][0] == filter_padding) or (
                                                            filter_padding == "" and row[40 + k] == "x"):

                                                        if filter_size == "":

                                                            if id == 0:
                                                                c.execute(
                                                                    """select * from %s where color='%s' and stylecode='%s'""" % (
                                                                    "stylecode", row[13], row[12],))
                                                                rows = c.fetchall()
                                                                if len(rows) > 0:
                                                                    styles[i][1] = 1
                                                            if id == 1:
                                                                c.execute(
                                                                    """select * from %s where color='%s' and stylecode='%s'""" % (
                                                                    "stylecode", row[13], row[12],))
                                                                rows = c.fetchall()
                                                                if len(rows) > 0:
                                                                    color[j][1] = 1

                                                            if id == 2:

                                                                c.execute(
                                                                    """select * from %s where color='%s' and stylecode='%s'""" % (
                                                                    "stylecode", row[13], row[12],))
                                                                rows = c.fetchall()
                                                                if len(rows) > 0:
                                                                    padding[k][1] = 1

                                                            if id == 3:
                                                                c.execute(
                                                                    """select * from %s where color='%s' and stylecode='%s'""" % (
                                                                    "stylecode", row[13], row[12],))
                                                                for row_2 in c:
                                                                    menge = int(row_2[4]) - int(row_2[5])
                                                                    if menge > 0:
                                                                        try:

                                                                            sizes[sizes_dict[row_2[3]]][1] = 1



                                                                        except:
                                                                            id = id
                                                            if id == 4:

                                                                now = datetime.datetime.now(
                                                                    pytz.timezone('Europe/Berlin'))

                                                                c.execute(
                                                                    """select * from %s where color='%s' and type='%s' and stylecode='%s'""" % (
                                                                    "stylecode", row[13], "BH", row[12],))
                                                                for row_2 in c:
                                                                    menge = int(row_2[4]) - int(row_2[5])
                                                                    if menge > 0:
                                                                        try:
                                                                            styles[i][1] = 1
                                                                            color[j][1] = 1
                                                                            padding[k][1] = 1

                                                                            sizes[sizes_dict[row_2[3]]][1] = 1



                                                                        except:
                                                                            id = id


                                                        else:
                                                            c.execute(
                                                                """select * from %s where color='%s' and size='%s' and stylecode='%s'""" % (
                                                                "stylecode", row[13], filter_size, row[12],))
                                                            for row_2 in c:

                                                                menge = int(row_2[4]) - int(row_2[5])
                                                                if menge > 0:

                                                                    if id == 0:
                                                                        styles[i][1] = 1
                                                                    if id == 1:
                                                                        color[j][1] = 1
                                                                    if id == 2:
                                                                        padding[k][1] = 1
                                                                    if id == 3:

                                                                        try:

                                                                            sizes[sizes_dict[row_2[3]]][1] = 1

                                                                        except:
                                                                            id = id

                                                    k = k + 1
                                            j = j + 1
                                i = i + 1
                            id = id + 1
    now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
    print("fertig")

    list[0].append(styles)
    list[1].append(color)
    list[2].append(padding)
    list[3].append(sizes)
    print(list)
    return list


def get_links(quiztaken):
    links = []

    class Links(object):
        def __init__(self, link, name, group1, group2, group3, pictureoverallsrc, headlineoverall, subtitleoverall,
                     groessen, pictureoverallsrcmobile, linkausgeschrieben):
            self.name = name
            self.link = link
            self.name = name
            self.group1 = group1
            self.group2 = group2
            self.group3 = group3
            self.pictureoverallsrc = pictureoverallsrc
            self.headlineoverall = headlineoverall
            self.subtitleoverall = subtitleoverall
            self.groessen = groessen
            self.pictureoverallsrcmobile = pictureoverallsrcmobile
            self.linkausgeschrieben = linkausgeschrieben

    text_kleine_groessen = ("""			<div id='horizontal_line'>&nbsp;</div>

			<div style='font-weight:500;font-size:14px;'>Unsere BHs mit kleinen Cups passen nicht nur, sondern verzaubern auch noch Dein Dekolleté</div><br>
			Wir wissen, wie schwer es ist, gut passende BHs für kleine Cups zu finden. Viele BHs für kleine Cups sehen zwar gut aus, geben Die aber häufig nicht die gewünschte Form. Bei uns wirst Du endlich fündig auf der Suche nach BHs für kleine Größen, die schön aussehen und Dir gleichzeitig eine schöne Form geben. Wir haben in unserem Sortiment Wert darauf gelegt Dir eine möglichst große Auswahl an Designs und Farben zu präsentieren. Du hast die Wahl zwischen eher schlichten BHs bis hin zu romantischen und sexy BHs, die Dir ein aufregendes Dekolleté geben.  <br><br><br>



			<div style='font-weight:500;font-size:14px;'>Große Auswahl an Modellen - Genau für Deine Passform</div><br>
			Wenn Du die erotische Zauberwaffe suchst haben wir sie gefunden: BHs mit einem tiefen Ausschnitt (unsere plunge Modelle). Diese eignen sich hervorragend zu tief ausgeschnittenen Kleidern und T-Shirts und verpassen Dir ein traumhaftes Dekolleté. Dazu wundervoll passend im BH Set haben wir sexy Höschen wie den Thong oder Bodyshort.

			Ebenso eignen sich BHs mit einem Push-Up wundervoll für ein ausgefülltes Dekellotée. Hier haben wir eine breite Farbpalette für Dich zusammengestellt, die Dir möglichst viel Abwechslung geben soll. 

				Wenn Du es eher schlichter magst, wirst Du bei uns natürlich auch fündig. Wir haben auch basic BHs im Angebot, sodass Du für den Alltag bestens ausgestattet sein solltest.
	""").encode('utf8')

    text_balconette = ("""			<div id='horizontal_line'>&nbsp;</div>

			<div style='font-weight:300;font-size:14px;'>Wenn Du Dinge magst, die sich feminin und super luxuriös anfühlen, dann wirst Du den Balconnet-Stil wahrscheinlich lieben. Die Balconette kann auch mit abnehmbaren Trägern geliefert werden, so dass Du sie mit Trägern tragen oder aus dem BH ausclipsen kannst, um Deine liebsten trägerlosen Looks zu tragen. Dieser Stil offenbart mehr als andere Stile, da die Höhe der Cups kürzer ist und die Träger breiter als normal sind, was bedeutet, dass dieser BH-Stil auch unter den tiefsten Ausschnitten verborgen bleiben kann. Die zusammengenähten Cups geben eine erhöhte Form und mehr Unterstützung, und einige kommen mit entfernbaren Pads. Dies ermöglicht es Dir die kleine Polsterung auf der Innenseite jedes Cups zu entfernen.""").encode(
        'utf8')

    text_push_up = ("""			<div id='horizontal_line'>&nbsp;</div>

			<div style='font-weight:300;font-size:14px;'><b>Push Up BHs - Das richtige für Dich?</b><br>
Hast Du Dich von Push Up BHs ferngehalten, weil Du Dir nicht sicher warst, ob Push-Up BHs für Dich geeignet waren? Nun, es ist Zeit, diese Sorgen ruhen zu lassen und den Sprung zu wagen!
Denn Push-Up-BHs sind eine großartige Ergänzung für Deine Unterwäsche- und Dessous-Kollektion. Push Up BHs geben Deinen Brüsten nicht nur einen natürlichen Auftrieb, sie lassen sie auch voller erscheinen (einige Push-up-BHs können sogar eine Körbchengröße bzw. einen Cup hinzufügen!).<br>
Push-up-BHs drücken Deine Brüste im Allgemeinen nach oben und unten, um das Dekolleté auf natürliche Weise zu verstärken. Die Polsterung an der Innenseite der Cups besteht aus Silikongel oder Schaum, um das Brustgewebe anzuheben und das Volumen sichtbar zu erhöhen. Basierend auf der Dicke der Polsterung, können Push-up-BHs von 3 Arten sein.<br><br>
<b>Arten von Push-up-BHs:</b><br>
Level 1 - diese Push-Ups geben einen sanften Auftrieb. Ein Drittel des Push Up BHs ist gepolstert. Dieser Typ fügt eine halbe Körbchengröße hinzu und verleiht Deinen Brüsten einen natürlichen Auftrieb. Wenn Du volle oder halbvolle Brüste hast, nimm diesen Push Up BH. Dieser BH verleiht Deiner Brust einen leicht abgerundeten Look und betont Dein Dekolleté.<br>







Level 2 - diese Push-Ups geben einen moderaten Auftrieb. Die Polsterung in diesem Typ endet knapp unterhalb der Brustwarze und fügt eine Cup-Größe hinzu. Also, wenn Deine Brustgröße 70B wäre, würden sie wie 70C aussehen. Wenn Du eine East West Brust hast (mehr als drei Fingerlücken zwischen Deinen Brüsten), entscheide Dich sich für diese Art von Push-up-BH; es wird Dir einen sexy Lift und Dekolleté geben.<br>







Level 3 - diese BHs vergrößern Dein Dekolleté, da sie zwei Cup-Größen hinzufügen! Wenn Deine Brustgröße 70B wäre, würden sie wie eine 70D aussehen. Wenn Du flache Brüste hast, ist dieser Push-Up Deine Wahl. Dieser BH wird Deinen Brüsten einen schönen runden Look geben und Dein Dekolleté wunderschön aufwerten. Wenn Du volle Brüste hast, halte Dich von Push-up-BHs der Stufe 3 fern, sie werden unangenehmes Volumen hinzufügen.""").encode(
        'utf8')

    text_grosse_groessen = ("""			<div id='horizontal_line'>&nbsp;</div>

			<div style='font-weight:300;font-size:14px;'>Wenn Du vollbusig bist, brauchst Du viel mehr Unterstützung, um sicherzustellen, dass Du sich wohl fühlst. Aber! Das bedeutet nicht, dass Du auf sexy Dessous verzichten musst. Full Cup BHs sind der perfekte Fix für den Alltag! Diese BHs sind ideal für vollbusige Frauen, da diese BHs Stabilität geben und gleichzeitig Deine Brüste formen. Full Cup BHs haben Cups, die die gesamte Brust bedecken, was verhindert, dass weiches Brustgewebe über die Cups rutscht. Full Cup BHs sind normalerweise fester im Unterband und werden mit einer dreiteiligen Cup-Konstruktion hergestellt. Da sie auch dehnbarere Materialien tragen, umarmen sie jede Kurve auf die bestmögliche Weise.""").encode(
        'utf8')

    text_schwarze_BH = ("""			<div id='horizontal_line'>&nbsp;</div>

			<div style='font-weight:300;font-size:14px;'>Keine Mode-Regel ist völlig geradlinig. Schwarz ist natürlich eine ideale Wahl, wenn Du ein dunkles Hemd trägst, wie zum Beispiel burgunder, braun oder marineblau. Wenn Du ein schwarzes Oberteil trägst, ist es durchaus akzeptabel, einen schwarzen BH darunter zu tragen, ohne ein Leibchen dazwischen zu legen, selbst wenn der schwarze BH durchschaut. Achte darauf, einen BH zu wählen, der volle Unterstützung bietet.""").encode(
        'utf8')

    links.append(
        Links("", "BH Sets", "lingerie", "", "", "/static/landing_page/180118_Titelbild_BH_Sets_Desktop.jpg", "BH Sets",
              ("Von Bralettes bis zu Push-Up BHs, unsere BHs bieten wir in einer großen Auswahl an Designs an.").encode(
                  'utf8'), ("Größen 65AA-95G").encode('utf8'),
              "/static/landing_page/180118_Titelbild_BH_Sets_Mobile.jpg", ("BH Sets").encode('utf8'), ))
    links.append(Links("", "Mein Showroom", quiztaken, "", "", "/static/overall_picture_bra.jpg", "Mein Showroom",
                       ("Entdecke Deinen Showroom mit persönlicher Passform-Beratung").encode('utf8'),
                       ("Jeden Monat neu").encode('utf8'), "/static/overall_picture_bra.jpg",
                       ("Mein Showroom").encode('utf8'), ))
    links.append(Links("", "Push-Up_BH", "lingerie", "", text_push_up,
                       "/static/landing_page/180118_Titelbild_Balconette_Desktop.jpg", "Push-Up BHs",
                       ("Push-Up BHs von klassisch bis sexy! Dein Ausschnitt wird traumhaft aussehen!").encode('utf8'),
                       ("Größen 65AA-85E").encode('utf8'), "/static/landing_page/180118_Titelbild_Balconette_Mobil.jpg",
                       ("Push-Up").encode('utf8'), ))
    links.append(Links("", "Balconette", "lingerie", "", text_balconette,
                       "/static/landing_page/180118_Titelbild_Balconette_Desktop.jpg", "Balconette BHs",
                       ("Unsere Balconette BHs geben Halt und einen sexy Ausschnitt.").encode('utf8'),
                       ("Größen 70B-85E").encode('utf8'), "/static/landing_page/180118_Titelbild_Balconette_Mobil.jpg",
                       ("Balconette").encode('utf8'), ))

    links.append(Links("", "schwarze_BH", "lingerie", "", text_schwarze_BH,
                       "/static/landing_page/180118_Titelbild_schwarze_BHs_Desktop.jpg", "Schwarze BHs",
                       ("Black is Beautiful. Schwarze BHs in allen Styles immer mit passendem Slip.").encode('utf8'),
                       ("Größen 65B-95F").encode('utf8'),
                       "/static/landing_page/180118_Titelbild_schwarze_BHs_Mobile_2.jpg",
                       ("Schwarze BHs").encode('utf8'), ))

    links.append(Links("", "kleine_groessen", "lingerie", "", text_kleine_groessen,
                       "/static/landing_page/180118_Titelbild_kleine_Groesse_Desktop.jpg",
                       ("Kleine Cups").encode('utf8'),
                       ("Wir zaubern Dir mit unseren BHs extra für kleine Cups einen zauberhaften Ausschnitt!").encode(
                           'utf8'), ("Größen 65AA-70A").encode('utf8'),
                       "/static/landing_page/180118_Titelbild_kleine_Groesse_Mobile.jpg",
                       ("Kleine Größen").encode('utf8'), ))
    links.append(Links("", "grosse_groessen", "lingerie", "", text_grosse_groessen,
                       "/static/landing_page/180118_Titelbild_grosse_groessen_Desktop.jpg",
                       ("Große Größen BHs").encode('utf8'), (
                       "Unsere BHs geben Dir Halt und Unterstützung. Egal ob schlicht oder sexy, wir haben den BH, den Du brauchst.").encode(
            'utf8'), ("Größen 75E bis 95F").encode('utf8'),
                       "/static/landing_page/180118_Titelbild_grosse_groessen_Mobil.jpg",
                       ("Große Größen").encode('utf8'), ))
    links.append(
        Links("", "Slips", "panties", "", "", "/static/landing_page/171214 Banner Picture TLBC red_1200.jpg", "Slips",
              "Entdecke unsere aktuellen Slips. Ob Thong, Tanga, Bikini oder Boyshort, wir haben sie alle!",
              ("Größen XS-XXL").encode('utf8'), "/static/landing_page/180118_Titelbild_BH_Sets_Desktop.jpg",
              ("Slips").encode('utf8'), ))
    links.append(Links("", "Unser VIP Club", quiztaken, "", "", "", "", "", "", "", "Unser VIP Club", ))

    #   links.append(Links("","VIP Box","","","","/static/overall_picture_bra.jpg","VIP Box","Entdecke Deinen Showroom",))

    #   links.append(Links("","Geschenkkarten","geschenkkarten","","","/static/overall_picture_bra.jpg","Mein Showroom","Entdecke Deinen Showroom",))

    json_string = json.dumps([Links.__dict__ for Links in links])

    return json_string


def get_lingerie_sizes(group1, group2, group3, color, size, user, name, name_list, c):
    lingerie = []

    class Lingerie(object):
        def __init__(self, name, sizerange, pic, priceregular, pricesubscription, description, details, active,
                     productgroup, wishlist, descriptionshort):
            self.name = name
            self.sizerange = sizerange
            self.pic = pic
            self.priceregular = priceregular
            self.pricesubscription = pricesubscription
            self.description = description
            self.details = details
            self.active = active
            self.productgroup = productgroup
            self.wishlist = wishlist
            self.descriptionshort = descriptionshort

    c.execute("""select * from lingerieselection """)
    for row in c:

        if row[7] == "yes":
            if name_list == "":
                if name == "":
                    if row[8] == group1 or row[8] == group2 or row[8] == group3:
                        if row[14] == "true":
                            priceregular = row[3] - row[13]
                            pricesubscription = row[4] - row[13]
                        else:
                            priceregular = row[3]
                            pricesubscription = row[4]

                        lingerie.append(
                            Lingerie(row[0], row[1], row[2], priceregular, pricesubscription, row[5], row[6], row[7],
                                     row[8], get_wishlist(row[12], row[13], user, row[8]), row[9], ))
                else:
                    if row[0] == name:
                        if row[14] == "true":
                            priceregular = row[3] - row[13]
                            pricesubscription = row[4] - row[13]
                        else:
                            priceregular = row[3]
                            pricesubscription = row[4]
                        lingerie.append(
                            Lingerie(row[0], row[1], row[2], priceregular, pricesubscription, row[5], row[6], row[7],
                                     row[8], get_wishlist(row[12], row[13], user, row[8]), row[9], ))
            else:

                t = 0
                while t <= len(name_list) - 1:

                    if row[0] == name_list[t]:

                        if row[14] == "true":
                            priceregular = row[3] - row[13]
                            pricesubscription = row[4] - row[13]
                        else:
                            priceregular = row[3]
                            pricesubscription = row[4]

                        lingerie.append(
                            Lingerie(row[0], row[1], row[2], priceregular, pricesubscription, row[5], row[6], row[7],
                                     row[8], "", row[9], ))
                    t = t + 1

    json_string = json.dumps([Lingerie.__dict__ for Lingerie in lingerie])

    return json_string


def get_main_style_group(bralette, plunge, balconette, fullcup):
    stylegroup = ""

    if plunge == "x":
        stylegroup = "Plunge"
    if balconette == "x":
        stylegroup = "Balconette"
    if bralette == "x":
        stylegroup = "Bralette"
    if fullcup == "x":
        stylegroup = "Full Cup"

    return stylegroup


def get_lingerie_selection_filter(group1, group2, group3, color, size, user, name, day, month, year, filter_style,
                                  filter_color, filter_padding, filter_size, modelAB, sub_picture, c):
    lingerie = []

    class Lingerie(object):
        def __init__(self, name, sizerange, pic, priceregular, pricesubscription, description, details, active,
                     productgroup, wishlist, descriptionshort, stylecode, colorcode, position, stylegroup, link,
                     stylegroupcode):
            self.name = name
            self.sizerange = sizerange
            self.pic = pic
            self.priceregular = priceregular
            self.pricesubscription = pricesubscription
            self.description = description
            self.details = details
            self.active = active
            self.productgroup = productgroup
            self.wishlist = wishlist
            self.descriptionshort = descriptionshort
            self.stylecode = stylecode
            self.colorcode = colorcode
            self.position = position
            self.stylegroup = stylegroup
            self.link = link
            self.stylegroupcode = stylegroupcode

    styles = [[] for i in range(13)]
    color = [[] for i in range(15)]
    padding = [[] for i in range(4)]
    sizes = [[] for i in range(90)]

    if group1 != "panties":
        i = 0
        filter_style_index = -1
        c.execute("""select * from style """)
        for row in c:
            print row[0] + "==" + filter_style
            if row[0] == filter_style:
                filter_style_index = i
            i = i + 1
    else:
        i = 0
        filter_style_index = -1
        c.execute("""select * from stylepanty """)
        for row in c:
            if row[0] == filter_style:
                filter_style_index = i
            i = i + 1

    print "def get_lingerie_selection_filter"

    i = 0
    filter_color_index = -1
    print "filter_color_index"
    c.execute("""select * from color """)
    for row in c:
        print row[0] + "==" + filter_color
        if row[0] == filter_color:
            filter_color_index = row[1]
        i = i + 1
    print filter_color_index

    i = 0
    filter_padding_index = -1
    c.execute("""select * from padding """)
    for row in c:
        if row[0] == filter_padding:
            filter_padding_index = i

        i = i + 1

    if group1 == "Mein Showroom":
        c.execute("""select * from showroom where gutscheincode=%s ORDER BY score DESC""", (user,))

        showroom_data = c.fetchall()

        for row_2 in showroom_data:
            c.execute("""select * from lingerieselection ORDER BY position ASC""")
            lingerieselection = c.fetchall()
            for row in lingerieselection:
                link = link_name_bestimmen(row[8])
                stylegroup = get_main_style_group(row[21], row[22], row[23], row[24])

                if row[8] == "lingerie":

                    if row_2[0] == row[12] and row_2[1] == row[13] and row_2[2] == day and row_2[3] == month and row_2[
                        4] == year:
                        if row[14] == "true":
                            priceregular = row[3] - row[14]
                            pricesubscription = row[4] - row[14]
                        else:
                            priceregular = row[3]
                            pricesubscription = row[4]

                        if name == "":
                            details = ""
                            description = ""
                        else:
                            description = row[5]
                            details = row[6]

                        lingerie.append(Lingerie(row[0], row[1],
                                                 get_pictures_from_consolidated_table(c, row[12], row[13], modelAB,
                                                                                      sub_picture, row[2], "all",
                                                                                      "small"), priceregular,
                                                 pricesubscription, description, details, row[7], row[8], "", row[9],
                                                 row[12], row[13], row[51], stylegroup, link, row[57], ))

    c.execute("""select * from lingerieselection ORDER BY position ASC""")

    lingerieselection = c.fetchall()

    for row in lingerieselection:
        link = link_name_bestimmen(row[8])
        stylegroup = get_main_style_group(row[21], row[22], row[23], row[24])
        if row[7] == "yes":
            if name == "":
                print("lingerieselection")

                if filter_style == "" and filter_color == "" and filter_padding == "" and filter_size == "":

                    if row[8] == group1 or row[8] == group2 or row[8] == group3:

                        if row[14] == "true":

                            priceregular = row[3] - row[13]
                            pricesubscription = row[4] - row[13]
                        else:
                            priceregular = row[3]
                            pricesubscription = row[4]
                        print row[0]

                        if name == "":
                            details = ""
                            description = ""
                        else:
                            description = row[5]
                            details = row[6]

                        lingerie.append(Lingerie(row[0], row[1],
                                                 get_pictures_from_consolidated_table(c, row[12], row[13], modelAB,
                                                                                      sub_picture, row[2], "all",
                                                                                      "small"), priceregular,
                                                 pricesubscription, description, details, row[7], row[8], "", row[9],
                                                 row[12], row[13], row[51], stylegroup, link, row[57], ))
                    else:

                        if group1 == "Wunschliste":

                            c.execute("""select * from wishlist where gutscheincode=%s """, (user,))

                            wishlist_data = c.fetchall()

                            for row_2 in wishlist_data:

                                if row_2[0] == row[12] and row_2[1] == row[13] and row[8] == row_2[3]:

                                    if row[14] == "true":
                                        priceregular = row[3] - row[14]
                                        pricesubscription = row[4] - row[14]
                                    else:
                                        priceregular = row[3]
                                        pricesubscription = row[4]

                                    if name == "":
                                        details = ""
                                        description = ""
                                    else:
                                        description = row[5]
                                        details = row[6]
                                    lingerie.append(Lingerie(row[0], row[1],
                                                             get_pictures_from_consolidated_table(c, row[12], row[13],
                                                                                                  modelAB, sub_picture,
                                                                                                  row[2], "all",
                                                                                                  "small"),
                                                             priceregular, pricesubscription, description, details,
                                                             row[7], row[8], "", row[9], row[12], row[13], row[51],
                                                             stylegroup, link, row[57], ))



                else:

                    print "if row[8]==group1 or row[8]==group2 or row[8]==group3:"
                    if row[8] == group1 or row[8] == group2 or row[8] == group3:

                        size_check = "not ok"
                        print filter_size
                        if filter_size != "":
                            size_check = check_quantities_of_style(c, row[12], row[13], filter_size, group1, row[2])
                        else:
                            size_check = "ok"
                        print size_check

                        if size_check == "ok":
                            if group1 == "lingerie":
                                if filter_style_index > 4:
                                    zaehler = filter_style_index + 5
                                else:
                                    zaehler = filter_style_index
                                print "filter_color_index"
                                print filter_color_index
                                if (row[20 + zaehler] == "x" or filter_style_index == -1) and (
                                        row[50] == filter_color_index or filter_color_index == -1) and (
                                        row[40 + filter_padding_index] == "x" or filter_padding_index == -1):
                                    if row[15] == "true":
                                        priceregular = row[3] - row[14]
                                        pricesubscription = row[4] - row[14]
                                    else:
                                        priceregular = row[3]
                                        pricesubscription = row[4]
                                    print ("append")

                                    if name == "":
                                        details = ""
                                        description = ""
                                    else:
                                        description = row[5]
                                        details = row[6]

                                    lingerie.append(Lingerie(row[0], row[1],
                                                             get_pictures_from_consolidated_table(c, row[12], row[13],
                                                                                                  modelAB, sub_picture,
                                                                                                  row[2], "all",
                                                                                                  "small"),
                                                             priceregular, pricesubscription, description, details,
                                                             row[7], row[8], "", row[9], row[12], row[13], row[51],
                                                             stylegroup, link, row[57], ))
                            else:
                                if (row[25 + filter_style_index] == "x" or filter_style_index == -1) and (
                                        row[50] == filter_color_index or filter_color_index == -1):
                                    if row[15] == "true":
                                        priceregular = row[3] - row[14]
                                        pricesubscription = row[4] - row[14]
                                    else:
                                        priceregular = row[3]
                                        pricesubscription = row[4]
                                    print ("append")

                                    if name == "":
                                        details = ""
                                        description = ""
                                    else:
                                        description = row[5]
                                        details = row[6]
                                    lingerie.append(Lingerie(row[0], row[1],
                                                             get_pictures_from_consolidated_table(c, row[12], row[13],
                                                                                                  modelAB, sub_picture,
                                                                                                  row[2], "all",
                                                                                                  "small"),
                                                             priceregular, pricesubscription, description, details,
                                                             row[7], row[8], "", row[9], row[12], row[13], row[51],
                                                             stylegroup, link, row[57], ))





            else:
                if row[0] == name:
                    if row[8] == group1 or row[8] == group2 or row[8] == group3:
                        if row[14] == "true":
                            priceregular = row[3] - row[13]
                            pricesubscription = row[4] - row[13]
                        else:
                            priceregular = row[3]
                            pricesubscription = row[4]

                        if name == "":
                            details = ""
                            description = ""
                        else:
                            description = row[5]
                            details = row[6]

                        lingerie.append(Lingerie(row[0], row[1],
                                                 get_pictures_from_consolidated_table(c, row[12], row[13], modelAB,
                                                                                      sub_picture, row[2], "all",
                                                                                      "big"), priceregular,
                                                 pricesubscription, description, details, row[7], row[8], "", row[9],
                                                 row[12], row[13], row[51], stylegroup, link, row[57], ))

    json_string = json.dumps([Lingerie.__dict__ for Lingerie in lingerie])

    return json_string


def check_quantities_of_style(c, stylecode, colorcode, filter_size, productgroup, pantytype):
    print "if type(filter_size) is list:"
    print filter_size

    if type(filter_size) is list:
        print "true"
        i = 0
        feedback = "not ok"
        while i <= len(filter_size) - 1:
            if check_quantities_of_style_in_detail(c, stylecode, colorcode, filter_size[i], productgroup,
                                                   pantytype) == "ok":
                feedback = "ok"
            i = i + 1
    else:
        print "false"
        feedback = check_quantities_of_style_in_detail(c, stylecode, colorcode, filter_size, productgroup, pantytype)

    print feedback
    return feedback


def check_quantities_of_style_in_detail(c, stylecode, colorcode, filter_size, productgroup, pantytype):
    if productgroup == "lingerie":
        c.execute("""select * from matching_table_stammdaten_stylecodes where stylecode=%s and colorcode=%s  """,
                  (stylecode, colorcode,))

        matching_table_stammdaten_stylecodes = c.fetchall()
        cup_table = {'AA': 0,
                     'A': 1,
                     'B': 2,
                     'C': 3,
                     'D': 4,
                     'E': 5,
                     'F': 6,
                     'G': 7,

                     }

        band_table = {'65': 0,
                      '70': 1,
                      '75': 2,
                      '80': 3,
                      '85': 4,
                      '90': 5,
                      '95': 6,

                      }
        band = filter_size[:2]
        cup = filter_size[2:]

        cup_number = cup_table[cup]
        band_number = band_table[band]
        feedback = "not ok"
        print "check_quantities_of_style"
        for row in matching_table_stammdaten_stylecodes:
            print row[band_number * 8 + cup_number]
            if row[band_number * 8 + cup_number + 4] == "1":
                feedback = "ok"
        return feedback
    else:
        print "check_quantities_of_style"
        c.execute("""select * from matching_table_stammdaten_stylecodes where stylecode=%s and colorcode=%s  """,
                  (stylecode, colorcode,))

        matching_table_stammdaten_stylecodes = c.fetchall()
        style_table_panty = {'Bikini': 0,
                             'Hipster': 1,
                             'Boyshort': 2,
                             'Thong': 3,

                             }

        size_table_panty = {
            'XXS': 0,
            'XS': 1,
            'S': 2,
            'M': 3,
            'L': 4,
            'XL': 5,
            'XXL': 6,

        }

        print pantytype
        print filter_size
        type_number = style_table_panty[pantytype]
        size_number = size_table_panty[filter_size]

        print type_number
        print size_number

        feedback = "not ok"
        print "check_quantities_of_style"
        for row in matching_table_stammdaten_stylecodes:
            print row[type_number * 7 + size_number + 64]
            if row[type_number * 7 + size_number + 64] == "1":
                feedback = "ok"
        return feedback


def get_pictures_from_consolidated_table(c, stylecode, colorcode, modelAB, sub_picture, pantytype, firstorall,
                                         bigorsmall):
    c.execute(
        """select * from consolidated_picturelibrary where modelAB=%s and subpicture=%s and stylecode=%s and colorcode=%s and firtorall=%s and bigorsmall=%s """,
        (modelAB, sub_picture, stylecode, colorcode, firstorall, bigorsmall,))

    consolidated_picturelibrary = c.fetchall()
    picture = ""
    for row in consolidated_picturelibrary:
        picture = row[6]
    return picture


def get_link_based_on_lingerie_name(request):
    if request.is_ajax() and request.GET:
        lingerie_name = request.GET.get('lingerie_name')

        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2', \
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)
        x = str(request.session.session_key)

        c.execute("""select * from lingerieselection """)

        lingerieselection = c.fetchall()
        link = "/"
        for row in lingerieselection:
            if row[0] == lingerie_name:
                c.execute("""select * from links """)
                links = c.fetchall()
                for row_2 in links:

                    if row_2[2] == row[8]:
                        link = "/Produktauswahl/" + row_2[1] + "/" + lingerie_name

        conn.close()
        return HttpResponse(json.dumps(link), content_type='application/json')


def get_other_colors(style, name, group1, c):
    lingerie = []

    class Lingerie(object):
        def __init__(self, style, colorcode, detaildatabase, pic, name, stylegroupcode):
            self.style = style
            self.colorcode = colorcode
            self.detaildatabase = detaildatabase
            self.pic = pic
            self.name = name
            self.stylegroupcode = stylegroupcode

    print("get_other_colors")

    if name != "":
        c.execute("""select * from lingerieselection where active=%s and productgroup=%s""", ("yes", group1))

        lingerieselection = c.fetchall()
        for row in lingerieselection:
            if row[0] == name:
                if group1 == "lingerie":
                    stylegroupcode = row[57]
                else:
                    stylegroupcode = row[57]

                print("step2")
                c.execute("""select * from lingerieselection where active=%s and productgroup=%s""", ("yes", group1))
                lingerieselection_2 = c.fetchall()

                for row_2 in lingerieselection_2:
                    if group1 == "lingerie":
                        print(row_2[57] + "==" + stylegroupcode)
                        if row_2[57] == stylegroupcode:
                            print(row_2[57] + "==" + stylegroupcode)
                            print("ASD")
                            lingerie.append(
                                Lingerie(row_2[12], row_2[13], row_2[0], row_2[55], row_2[0], stylegroupcode, ))
                    else:
                        if group1 == "panties":
                            if row_2[57] == stylegroupcode:
                                lingerie.append(
                                    Lingerie(row_2[12], row_2[13], row_2[0], row_2[55], row_2[0], stylegroupcode, ))

    else:
        if group1 != "":

            c.execute("""select * from lingerieselection where productgroup=%s and active=%s """, (group1, "yes"))
            lingerieselection = c.fetchall()

            for row in lingerieselection:
                existiert = "nein"
                stylegroupcode = row[57]

                c.execute("""select * from lingerieselection where productgroup=%s and active=%s """, (group1, "yes"))
                lingerieselection_2 = c.fetchall()

                for row_2 in lingerieselection_2:
                    if row_2[57] == stylegroupcode and existiert == "nein" and row_2[0] == row[0]:
                        print("haeh")
                        lingerie.append(Lingerie(row_2[12], row_2[13], row_2[0], row_2[55], row_2[0], stylegroupcode, ))
                        existiert = "ja"

    json_string = json.dumps([Lingerie.__dict__ for Lingerie in lingerie])
    print(json_string)

    return json_string


def get_pricesforaddlpanty(name, VIP, c):
    prices = []

    class Prices(object):
        def __init__(self, priceregular, pricesubscription):
            self.priceregular = priceregular
            self.pricesubscription = pricesubscription

    c.execute("""select * from lingerieselection """)

    lingerieselection = c.fetchall()

    for row in lingerieselection:
        if row[7] == "yes":
            if row[0] == name:
                c.execute("""select * from lingerieselection """)

                lingerieselection_2 = c.fetchall()

                for row_2 in lingerieselection_2:
                    if row_2[7] == "yes":
                        if (row_2[0] != name and row_2[13] == row[13] and row_2[8] == "panties") or (
                                row_2[0] == name and row_2[13] == row[13] and row_2[8] == "panties"):
                            prices.append(Prices(row_2[3], row_2[4], ))

    json_string = json.dumps([Prices.__dict__ for Prices in prices])

    return json_string


def get_price(stylecode, colorcode, VIP, c, productgroup):
    price = 0
    if productgroup == "panties":
        c.execute("""select * from lingerieselection where colorcode=%s and productgroup=%s """,
                  (colorcode, productgroup,))
        lingerieselection = c.fetchall()
        for row in lingerieselection:
            if row[7] == "yes":
                if VIP == "VIP":
                    price = row[4]
                else:
                    price = row[3]
    else:
        c.execute("""select * from lingerieselection where colorcode=%s and stylecode=%s and productgroup=%s """,
                  (colorcode, stylecode, productgroup,))
        lingerieselection = c.fetchall()
        for row in lingerieselection:
            if row[7] == "yes":
                if VIP == "VIP":
                    price = row[4]
                else:
                    price = row[3]

    return price


def get_lingerie_selection_sizes(name, link, c):
    lingerie = []

    class Lingerie(object):
        def __init__(self, type, stylecode, color, size):
            self.type = type
            self.stylecode = stylecode
            self.color = color
            self.size = size

    print("get_lingerie_selection_sizes")

    c.execute("""select * from lingerieselection""")

    lingerieselection = c.fetchall()

    for row in lingerieselection:
        if row[7] == "yes":
            if row[0] == name:
                print("ASD")
                c.execute("""select * from %s """ % ("stylecode"))
                for row_2 in c:
                    if link != "panties":
                        if row_2[0] == "BH":
                            if row[13] == row_2[2] and row[12] == row_2[1]:
                                #                               print(row[13]+"=="+row_2[2] +"and"+ row[12]+"=="+row_2[1])
                                menge = int(row_2[4]) - int(row_2[5])
                                if menge > 0:
                                    lingerie.append(Lingerie(row_2[0], row_2[1], row_2[2], row_2[3], ))
                        else:
                            if row[13] == row_2[2]:
                                #                               print(row[13]+"=="+row_2[2] +"and"+ row[12]+"=="+row_2[1])
                                menge = int(row_2[4]) - int(row_2[5])
                                print(row[2] + " " + row_2[3])
                                if menge > 0:
                                    lingerie.append(Lingerie(row_2[0], row_2[1], row_2[2], row_2[3], ))
                    else:
                        if row[13] == row_2[2] and row[12] == row_2[1]:
                            if row_2[0] == link:
                                menge = int(row_2[4]) - int(row_2[5])
                                if menge > 0:
                                    lingerie.append(Lingerie(row_2[0], row_2[1], row_2[2], row_2[3], ))

    json_string = json.dumps([Lingerie.__dict__ for Lingerie in lingerie])

    return json_string


def get_lingerie_selection_bewertungen(name, c):
    lingerie = []

    class Lingerie(object):
        def __init__(self, namebewerter, bewertung, bewertungsheadline, bewertungstext, bewertungsdatum):
            self.namebewerter = namebewerter
            self.bewertung = bewertung
            self.bewertungsheadline = bewertungsheadline
            self.bewertungstext = bewertungstext
            self.bewertungsdatum = bewertungsdatum

    c.execute("""select * from lingerieselection""")

    lingerieselection = c.fetchall()
    for row in lingerieselection:

        if row[7] == "yes":

            if row[0] == name and row[8] != "panties" and row[8] != "geschenkkarten":

                c.execute("""select * from %s """ % ("bewertungen"))

                for row_2 in c:
                    if row_2[10] == "yes" and row[12] == row_2[11] and row[13] == row_2[12]:
                        lingerie.append(Lingerie(row_2[1], row_2[2], row_2[3], row_2[4], row_2[5], ))

    json_string = json.dumps([Lingerie.__dict__ for Lingerie in lingerie])

    return json_string


def get_lingerie_selection_gesamtbewertung(name, c):
    lingerie = []

    class Lingerie(object):
        def __init__(self, gesamtbewertung, gesamtbewertunganzahl, einsternbewertung, einsternbewertunganzahl,
                     zweisternbewertung, zweisternbewertunganzahl, dreisternbewertung, dreisternbewertunganzahl,
                     viersternbewertung, viersternbewertunganzahl, fuenfsternbewertung, fuenfsternbewertunganzahl):
            self.gesamtbewertung = gesamtbewertung
            self.gesamtbewertunganzahl = gesamtbewertunganzahl
            self.einsternbewertung = einsternbewertung
            self.einsternbewertunganzahl = einsternbewertunganzahl
            self.zweisternbewertung = zweisternbewertung
            self.zweisternbewertunganzahl = zweisternbewertunganzahl
            self.dreisternbewertung = dreisternbewertung
            self.dreisternbewertunganzahl = dreisternbewertunganzahl
            self.viersternbewertung = viersternbewertung
            self.viersternbewertunganzahl = viersternbewertunganzahl
            self.fuenfsternbewertung = fuenfsternbewertung
            self.fuenfsternbewertunganzahl = fuenfsternbewertunganzahl

    c.execute("""select * from lingerieselection""")

    lingerieselection = c.fetchall()

    for row in lingerieselection:
        if row[7] == "yes":
            if row[0] == name and row[8] != "panties" and row[8] != "geschenkkarten":

                c.execute("""select * from %s """ % ("bewertungen"))
                gesamtbewertung = 0
                gesamtbewertunganzahl = 0
                einsternbewertung = 0
                einsternbewertunganzahl = 0
                zweisternbewertung = 0
                zweisternbewertunganzahl = 0
                dreisternbewertung = 0
                dreisternbewertunganzahl = 0
                viersternbewertung = 0
                viersternbewertunganzahl = 0
                fuenfsternbewertung = 0
                fuenfsternbewertunganzahl = 0
                for row_2 in c:
                    if row_2[10] == "yes" and row[12] == row_2[11] and row[13] == row_2[12]:
                        if row_2[2] != "":

                            gesamtbewertung = gesamtbewertung + int(row_2[2])
                            gesamtbewertunganzahl = gesamtbewertunganzahl + 1

                            if row_2[2] == "1":
                                einsternbewertung = einsternbewertung + int(row_2[2])
                                einsternbewertunganzahl = einsternbewertunganzahl + 1
                            if row_2[2] == "2":
                                zweisternbewertung = zweisternbewertung + int(row_2[2])
                                zweisternbewertunganzahl = zweisternbewertunganzahl + 1
                            if row_2[2] == "3":
                                dreisternbewertung = dreisternbewertung + int(row_2[2])
                                dreisternbewertunganzahl = dreisternbewertunganzahl + 1

                            if row_2[2] == "4":
                                viersternbewertung = viersternbewertung + int(row_2[2])
                                viersternbewertunganzahl = viersternbewertunganzahl + 1
                            if row_2[2] == "5":
                                fuenfsternbewertung = fuenfsternbewertung + int(row_2[2])
                                fuenfsternbewertunganzahl = fuenfsternbewertunganzahl + 1

                lingerie.append(
                    Lingerie(gesamtbewertung, gesamtbewertunganzahl, einsternbewertung, einsternbewertunganzahl,
                             zweisternbewertung, zweisternbewertunganzahl, dreisternbewertung, dreisternbewertunganzahl,
                             viersternbewertung, viersternbewertunganzahl, fuenfsternbewertung,
                             fuenfsternbewertunganzahl, ))

    json_string = json.dumps([Lingerie.__dict__ for Lingerie in lingerie])

    return json_string


def does_wishlist_value_already_exist(user, stylecode, colorcode, productgroup, c):
    c.execute("""select * from wishlist where gutscheincode=%s """, (user,))

    wishlist_data = c.fetchall()
    feedback = "false"
    for row in wishlist_data:
        if row[0] == stylecode and row[1] == colorcode and row[3] == productgroup:
            feedback = "true"
    return feedback


@csrf_exempt
def new_value_for_wishlist(request):
    if request.is_ajax() and request.GET:
        stylecode = request.GET.get('stylecode')
        colorcode = request.GET.get('colorcode')
        productgroup = request.GET.get('productgroup')
        status = request.GET.get('status')
        putinwishlist = request.GET.get('putinwishlist')
        windowwidth = request.GET.get('windowwidth')
        windowheight = request.GET.get('windowheight')
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2', \
                                       password='okano1988', database='maxfischer2database')

        c = conn.cursor(buffered=True)

        x = str(request.session.session_key)

        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        Monat = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober",
                 "November", "Dezember"]
        now_date = str(now.day) + ". " + str(Monat[now.month - 1]) + " " + str(now.year)
        Y = now.year
        M = now.month
        D = now.day
        H = now.hour
        Mi = now.minute
        time = datetime.datetime.strptime(str(Y) + "-" + str(M) + "-" + str(D) + " " + str(H) + ":" + str(Mi),
                                          "%Y-%m-%d %H:%M")

        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            userdaten = c.fetchall()
            for row in userdaten:
                user = row[11]
                facebookid = row[12]
                quiz = row[26]
                modelAB = row[47]
                sub_picture = row[48]
                wishlist_quantity = row[16]

        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        Monat = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober",
                 "November", "Dezember"]
        date_short = str(now.day) + ". " + Monat[(now.month) - 1] + " " + str(now.year)

        c.execute("""insert into Big_data_click_on_image values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (
        user, facebookid, modelAB, sub_picture, now_date, time, windowwidth, windowheight, stylecode, colorcode, "", "",
        putinwishlist, "",))

        if status == "yes":
            if does_wishlist_value_already_exist(user, stylecode, colorcode, productgroup, c) == "false":
                c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s)""" % ("wishlist"),
                          (stylecode, colorcode, date_short, productgroup, user))
                conn.commit()
        else:
            c.execute(
                """delete from %s where stylecode=%%s and colorcode=%%s and productgroup=%%s and gutscheincode=%%s""" % (
                "wishlist"), (stylecode, colorcode, productgroup, user,))
            conn.commit()
        wishlist = define_wishlist_object(user, modelAB, sub_picture, c, conn)
        conn.close()
        return HttpResponse(json.dumps(wishlist), content_type='application/json')


def get_wishlist(stylecode, colorcode, user, productgroup):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2', \
                                   password='okano1988', database='maxfischer2database')

    c = conn.cursor(buffered=True)

    c.execute("""select * from wishlist where gutscheincode=%s """, (user,))
    feedback = "no"
    for row in c:
        if row[0] == stylecode and row[1] == colorcode and row[3] == productgroup:
            feedback = "yes"
    return feedback


def define_gutscheinkonto(x):
    gutscheinkonto = []

    class Gutscheinkonto(object):
        def __init__(self, datum, gutscheinwert, bestellnummer, gutscheincodedesanderen, vorname, nachname):
            self.datum = datum
            self.gutscheinwert = gutscheinwert
            self.bestellnummer = bestellnummer
            self.gutscheincodedesanderen = gutscheincodedesanderen
            self.vorname = vorname
            self.nachname = nachname

    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2', \
                                   password='okano1988', database='maxfischer2database')

    c = conn.cursor(buffered=True)

    conn_2 = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                     user='maxfischer2', \
                                     password='okano1988', database='maxfischer2database')

    q = conn_2.cursor()
    conn_3 = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                     user='maxfischer2', \
                                     password='okano1988', database='maxfischer2database')

    d = conn_3.cursor()

    c.execute("""select * from userdaten """)

    gutscheine = ""
    status = 0
    for row in c:
        if row[9] == x and x != "None":
            status = 1

            q.execute("""select * from %s """ % (row[11]))
            for row_2 in q:

                if row_2[1] != 0 and row_2[2] != "nicht anzeigen":
                    d.execute("""select * from userdaten """)
                    for row_3 in d:

                        if row_3[11] == str(row_2[3]):
                            if row_3[2] == "" or row_3[3] == "":
                                vorname = str(row_3[0])
                                nachname = ""
                            else:
                                vorname = str(row_3[2])
                                nachname = str(row_3[3])

                    gutscheinkonto.append(Gutscheinkonto(row_2[0], row_2[1], row_2[2], row_2[3], vorname, nachname, ))

    json_string = json.dumps([Gutscheinkonto.__dict__ for Gutscheinkonto in gutscheinkonto])

    return json_string


def define_bestellte_artikel(session_key, c):
    bestellte_artikel = []

    class Bestellte_Artikel(object):
        def __init__(self, bestellnummer, style, bhgroesse, slipgroesse, anzahl):
            self.bestellnummer = bestellnummer
            self.style = style
            self.bhgroesse = bhgroesse
            self.slipgroesse = slipgroesse
            self.anzahl = anzahl

    c.execute("""select * from bestellt where gutscheincode=%s ORDER BY idforsorting DESC""", (session_key,))
    bestellt_data = c.fetchall()
    for row_2 in bestellt_data:
        c.execute("""select * from cart_details where gutscheincode=%s""", (row_2[0], session_key,))
        for row in c:
            bestellte_artikel.append(Bestellte_Artikel(row_2[21], row[0], row[2], row[3], row[1], ))

    json_string = json.dumps([Bestellte_Artikel.__dict__ for Bestellte_Artikel in bestellte_artikel])
    return json_string


def define_rebates_for_ruecksendung(session_key, bestellnummer, c, erfolgte_ruecksendung):
    rebates = []

    class Rebates(object):
        def __init__(self, coupon, couponcode, braforfreevalue, braforfreecount, storecredit, credit, bestellung,
                     gesamtpreis, aenderung, aenderung_rechnungsbetrag, lieferkosten, bestellnummer, rabattname):
            self.coupon = coupon
            self.couponcode = couponcode
            self.braforfreevalue = braforfreevalue
            self.braforfreecount = braforfreecount
            self.storecredit = storecredit
            self.credit = credit
            self.bestellung = bestellung
            self.gesamtpreis = gesamtpreis
            self.aenderung = aenderung
            self.aenderung_rechnungsbetrag = aenderung_rechnungsbetrag
            self.lieferkosten = lieferkosten
            self.bestellnummer = bestellnummer
            self.rabattname = rabattname

    print "def define_rebates"
    print "hii"
    delta = 0
    aenderung_rechnungsbetrag = 0
    zwischensumme = 0

    c.execute("""select * from bestellt where gutscheincode=%s and bestellnummer=%s ORDER BY idforsorting DESC""",
              (session_key, bestellnummer))

    bestellt_data = c.fetchall()

    user = session_key

    for row_2 in bestellt_data:
        print "if row_2[21]==bestellnummer or bestellnummer=="
        print user
        print bestellnummer

        braforfreevalue = float(row_2[27])
        braforfreecount = float(row_2[26])

        versandkosten = float(row_2[16])

        credit = float(row_2[22])

        couponcode = row_2[18]
        coupon = float(-gutscheinwert_abrufen_fuer_ruecksendung_2(couponcode, c, session_key, bestellnummer,
                                                                  erfolgte_ruecksendung))
        gesamtanzahl = 0

        braforfreecount = float(row_2[26])
        storecredit = float(row_2[28])

        print "braforfreecount"
        print braforfreecount

        stylecodes_colorcodes = []
        bestellung = 0
        if erfolgte_ruecksendung == "nein":
            c.execute(
                """select * from cart_details where gutscheincode=%s and bestellt=%s and bestellnummer=%s and zurueckgesendet=%s""",
                (user, "ja", bestellnummer, "nein",))
            for row_3 in c:
                print "1"
                print "float(row_3[25])*row_3[8]"
                print row_3[8]
                print row_3[1]
                print row_3[25]
                bestellung = bestellung + (int(float(row_3[1]) - float(row_3[25]))) * row_3[8]




        else:
            c.execute(
                """select * from cart_details where gutscheincode=%s and bestellt=%s and zurueckgesendet=%s and bestellnummer=%s""",
                (user, "ja", "ja", bestellnummer,))
            for row_3 in c:
                print "1"
                bestellung = bestellung + float(row_3[24]) * row_3[8]

        if erfolgte_ruecksendung == "nein":
            c.execute(
                """select * from cart_details where gutscheincode=%s and bestellt=%s and productgroup=%s and  bestellnummer=%s and zurueckgesendet=%s""",
                (user, "ja", "lingerie", bestellnummer, "nein",))
            for row_3 in c:
                gesamtanzahl = gesamtanzahl + (int(float(row_3[1]) - float(row_3[25])))

        else:
            c.execute(
                """select * from cart_details where gutscheincode=%s and bestellt=%s and productgroup=%s and zurueckgesendet=%s and bestellnummer=%s""",
                (user, "ja", "lingerie", "ja", bestellnummer,))
            for row_3 in c:
                gesamtanzahl = gesamtanzahl + row_3[24]

        coupon_new = min(coupon, max(bestellung + versandkosten, 0))
        zwischensumme = bestellung - coupon_new + versandkosten

        credit_new = min(credit, max(zwischensumme, 0))
        zwischensumme = bestellung - coupon_new - credit_new + versandkosten

        braforfreevalue_new = 0
        braforfreecount_new = 0

        list = []
        if erfolgte_ruecksendung == "nein":
            c.execute(
                """select * from cart_details where gutscheincode=%s and bestellt=%s and bestellnummer=%s and zurueckgesendet=%s and bestellnummer=%s ORDER BY preis DESC""",
                (user, "ja", bestellnummer, "nein", "lingerie",))
            for row_3 in c:
                print row_3[8]
                list.append([row_3[8] + row_3[10], int(float(row_3[1]) - float(row_3[25]))])
        else:
            c.execute(
                """select * from cart_details where gutscheincode=%s and bestellt=%s and zurueckgesendet=%s and bestellnummer=%s and productgroup=%s  ORDER BY preis DESC""",
                (user, "ja", "ja", bestellnummer, "lingerie",))
            for row_3 in c:
                print row_3[8]
                list.append([row_3[8] + row_3[10], int(float(row_3[1]) - float(row_3[25]))])

        print list

        sorted_list = sorted(list, key=lambda tup: tup[0], reverse=True)
        print "sorted_list"
        print sorted_list
        j = 0
        while j <= len(sorted_list) - 1:
            i = 0
            while i <= int(sorted_list[j][1]) - 1:
                print "naechster"
                print str(bestellung)
                print str(coupon_new)
                print str(credit_new)
                print (sorted_list[j][0])
                print str(braforfreevalue_new)
                print str(braforfreecount_new)
                print str(braforfreecount)
                if bestellung - coupon_new - credit_new - braforfreevalue_new + versandkosten - float(
                        sorted_list[j][0]) >= 0 and braforfreecount_new < braforfreecount:
                    braforfreevalue_new = braforfreevalue_new + float(sorted_list[j][0])
                    braforfreecount_new = braforfreecount_new + 1
                i = i + 1
            j = j + 1

        zwischensumme = bestellung - coupon_new - credit_new - braforfreevalue_new + versandkosten

        storecredit_new = min(storecredit, max(zwischensumme, 0))

        zwischensumme = bestellung - coupon_new - credit_new - braforfreevalue_new - storecredit_new + versandkosten

        rebates.append(
            Rebates(coupon_new, couponcode, braforfreevalue_new, braforfreecount_new, storecredit_new, credit_new,
                    bestellung, zwischensumme, delta, aenderung_rechnungsbetrag, versandkosten, bestellnummer, "", ))

    json_string = json.dumps([Rebates.__dict__ for Rebates in rebates])
    return json_string


def define_rebates(session_key, bestellnummer, string_list_cart, length_string_list, aenderung, c, conn, land,
                   get_bestellewert, get_lieferkosten, get_rabatte):
    rebates = []

    class Rebates(object):
        def __init__(self, coupon, couponcode, braforfreevalue, braforfreecount, storecredit, credit, bestellung,
                     gesamtpreis, aenderung, aenderung_rechnungsbetrag, lieferkosten, bestellnummer, rabattname):
            self.coupon = coupon
            self.couponcode = couponcode
            self.braforfreevalue = braforfreevalue
            self.braforfreecount = braforfreecount
            self.storecredit = storecredit
            self.credit = credit
            self.bestellung = bestellung
            self.gesamtpreis = gesamtpreis
            self.aenderung = aenderung
            self.aenderung_rechnungsbetrag = aenderung_rechnungsbetrag
            self.lieferkosten = lieferkosten
            self.bestellnummer = bestellnummer
            self.rabattname = rabattname

    print "def define_rebates"
    delta = 0
    aenderung_rechnungsbetrag = 0
    zwischensumme = 0

    c.execute("""select * from userdaten where gutscheincode=%s """, (session_key,))

    userdaten = c.fetchall()

    for row in userdaten:

        gutscheincode = row[21]
        user = row[11]
        print user

        if bestellnummer != "":

            c.execute("""select * from bestellt where gutscheincode=%s ORDER BY idforsorting DESC""", (row[11],))

            bestellt_data = c.fetchall()

            for row_2 in bestellt_data:
                if row_2[21] == bestellnummer or bestellnummer == "All":
                    coupon = float(row_2[17])
                    coupon_new = coupon
                    couponcode = row_2[18]
                    storecredit = float(row_2[28])
                    braforfreevalue = float(row_2[27])
                    braforfreecount = float(row_2[26])
                    credit = float(row_2[22])
                    versandkosten = float(row_2[16])
                    bestellnummer = row_2[21]

                    if string_list_cart != "":
                        bestellung = 0
                        stylecodes_colorcodes = []
                        c.execute(
                            """select * from cart_details where gutscheincode=%s and bestellt=%s and bestellnummer=%s""",
                            (user, "ja", bestellnummer,))
                        for row_3 in c:
                            gesamtanzahl = gesamtanzahl + row_3[1]
                            stylecodes_colorcodes.append(row_3[7] + "_" + row_3[4])

                            j = 0
                            while j <= length_string_list:
                                style = string_list_cart[j * 7 + 0]
                                stylecode = string_list_cart[j * 7 + 1]
                                colorcode = string_list_cart[j * 7 + 2]
                                bh_groesse = string_list_cart[j * 7 + 3]
                                slip_groesse = string_list_cart[j * 7 + 4]
                                anzahl = int(string_list_cart[j * 7 + 5])
                                preis = float(string_list_cart[j * 7 + 6])

                                if row_3[7] == stylecode and row_3[4] == colorcode and row_3[2] == bh_groesse and row_3[
                                    3] == slip_groesse:
                                    bestellung = bestellung + row_3[8] * anzahl

                                j = j + 1
                        coupon_new = min(coupon, max(bestellung + versandkosten, 0))
                        zwischensumme = bestellung - coupon_new + versandkosten

                        credit_new = min(credit, max(zwischensumme, 0))
                        zwischensumme = bestellung - coupon_new - credit_new + versandkosten

                        braforfreevalue_new = 0
                        braforfreecount_new = 0
                        bestellung_alt = 0

                        c.execute(
                            """select * from cart_details where gutscheincode=%s and bestellt=%s and bestellnummer=%s ORDER BY preis DESC""",
                            (user, "ja", bestellnummer,))
                        for row_3 in c:

                            j = 0
                            while j <= length_string_list:
                                style = string_list_cart[j * 7 + 0]
                                stylecode = string_list_cart[j * 7 + 1]
                                colorcode = string_list_cart[j * 7 + 2]
                                bh_groesse = string_list_cart[j * 7 + 3]
                                slip_groesse = string_list_cart[j * 7 + 4]
                                anzahl = string_list_cart[j * 7 + 5]
                                preis = string_list_cart[j * 7 + 6]

                                if row_3[7] == stylecode and row_3[4] == colorcode and row_3[2] == bh_groesse and row_3[
                                    3] == slip_groesse:
                                    i = 0
                                    while i <= int(anzahl) - 1:

                                        if bestellung - coupon_new - credit_new - braforfreevalue_new - float(
                                                sorted_list[j][0]) >= 0 and braforfreecount_new < braforfreecount:
                                            braforfreevalue_new = braforfreevalue_new + float(preis)
                                            braforfreecount_new = braforfreecount_new + 1
                                        i = i + 1
                                j = j + 1

                            bestellung_alt = bestellung_alt + float(row_3[1]) * row_3[8]

                        zwischensumme = bestellung - coupon_new - credit_new - braforfreevalue_new + versandkosten

                        storecredit_new = min(storecredit, max(zwischensumme, 0))

                        if aenderung == "":

                            c.execute(
                                """update %s set rabatt=%%s, creditused=%%s,braforfreecount=%%s,braforfreevalue=%%s,storecredit=%%s where bestellnummer=%%s and gutscheincode=%%s and bestellt=%%s""" % (
                                "bestellt"), (
                                coupon_new, credit_new, braforfreecount_new, braforfreevalue_new, storecredit_new,
                                bestellnummer, row[11], "ja",))
                            c.execute(
                                """update userdaten set numberofbraforfree=%s, credit=%s,storecredit=%s where gutscheincode=%s""",
                                (int(row[25]) + braforfreecount - braforfreecount_new,
                                 int(row[10]) + credit - credit_new, int(row[24]) + storecredit - storecredit_new,
                                 session_key,))

                            conn.commit()
                        else:
                            delta = bestellung - bestellung_alt
                            aenderung_rechnungsbetrag = bestellung - bestellung_alt + (coupon - coupon_new) + (
                                    credit - credit_new) + (braforfreevalue - braforfreevalue_new) + (
                                                                storecredit - storecredit_new)

                            if delta != 0:
                                bestellung = bestellung_alt








                    else:

                        bestellung = 0

                        coupon_new = coupon
                        credit_new = credit
                        braforfreevalue_new = braforfreevalue
                        braforfreecount_new = braforfreecount
                        storecredit_new = storecredit
                        gesamtanzahl = 0

                        c.execute(
                            """select * from cart_details where gutscheincode=%s and bestellt=%s and bestellnummer=%s""",
                            (user, "ja", bestellnummer,))
                        for row_3 in c:
                            bestellung = bestellung + float(row_3[1]) * row_3[8]

                        c.execute(
                            """select * from cart_details where gutscheincode=%s and bestellt=%s and bestellnummer=%s and productgroup=%s""",
                            (user, "ja", bestellnummer, "lingerie",))
                        for row_3 in c:
                            gesamtanzahl = gesamtanzahl + row_3[1]

                        list = []
                        c.execute(
                            """select * from cart_details where gutscheincode=%s and bestellt=%s and bestellnummer=%s and productgroup=%s ORDER BY preis DESC""",
                            (user, "ja", bestellnummer, "lingerie",))
                        for row_3 in c:
                            list.append([row_3[8] + row_3[10], row_3[1]])

                        sorted_list = sorted(list, key=lambda tup: tup[0], reverse=True)
                        j = 0
                        while j <= len(sorted_list) - 1:
                            i = 0
                            while i <= int(sorted_list[j][1]) - 1:

                                if bestellung - coupon_new - credit_new - braforfreevalue_new + versandkosten - float(
                                        sorted_list[j][0]) >= 0 and braforfreecount_new < braforfreecount:
                                    braforfreevalue_new = braforfreevalue_new + float(sorted_list[j][0])
                                    braforfreecount_new = braforfreecount_new + 1
                                i = i + 1
                            j = j + 1
                    zwischensumme = bestellung - coupon_new - credit_new - braforfreevalue_new - storecredit_new + delta + versandkosten
                    print "gesamtanzahl_for_rabattname"

                    rebates.append(
                        Rebates(coupon_new, couponcode, braforfreevalue_new, braforfreecount_new, storecredit_new,
                                credit_new, bestellung, zwischensumme, delta, aenderung_rechnungsbetrag, versandkosten,
                                bestellnummer, get_rabattname(gutscheincode, gesamtanzahl, c, user), ))




        else:
            versandkosten = get_country_delivery_costs(land, c)
            credit = float(row[10])

            couponcode = row[21]
            coupon = float(-gutscheinwert_abrufen(couponcode, c, session_key, conn, "nein", user))
            gesamtanzahl = 0

            braforfreecount = get_bra_for_free_in_VIP_model(c, row[11])
            storecredit = get_existing_store_credit(c, row[11])

            stylecodes_colorcodes = []
            bestellung = 0
            c.execute("""select * from cart_details where gutscheincode=%s and bestellt=%s""", (user, "nein",))
            for row_3 in c:
                bestellung = bestellung + float(row_3[1]) * row_3[8]

            c.execute("""select * from cart_details where gutscheincode=%s and bestellt=%s and productgroup=%s""",
                      (user, "nein", "lingerie",))
            for row_3 in c:
                gesamtanzahl = gesamtanzahl + row_3[1]

            coupon_new = min(coupon, max(bestellung + versandkosten, 0))
            zwischensumme = bestellung - coupon_new + versandkosten

            credit_new = min(credit, max(zwischensumme, 0))
            zwischensumme = bestellung - coupon_new - credit_new + versandkosten

            braforfreevalue_new = 0
            braforfreecount_new = 0

            list = []
            c.execute(
                """select * from cart_details where gutscheincode=%s and bestellt=%s and productgroup=%s ORDER BY preis DESC""",
                (user, "nein", "lingerie",))
            for row_3 in c:
                print row_3[8]
                list.append([row_3[8] + row_3[10], row_3[1]])

            print list

            sorted_list = sorted(list, key=lambda tup: tup[0], reverse=True)
            print "sorted_list"
            print sorted_list
            j = 0
            while j <= len(sorted_list) - 1:
                i = 0
                while i <= int(sorted_list[j][1]) - 1:
                    print str(bestellung) + "-" + str(coupon_new - credit_new) + "-" + str(
                        sorted_list[j][0]) + "-" + str(braforfreevalue_new) + ">=0 and )+" + str(
                        braforfreecount_new) + "<" + str(braforfreecount)

                    if bestellung - coupon_new - credit_new - braforfreevalue_new + versandkosten - float(
                            sorted_list[j][0]) >= 0 and braforfreecount_new < braforfreecount:
                        braforfreevalue_new = braforfreevalue_new + float(sorted_list[j][0])
                        braforfreecount_new = braforfreecount_new + 1
                    i = i + 1
                j = j + 1

            zwischensumme = bestellung - coupon_new - credit_new - braforfreevalue_new + versandkosten

            storecredit_new = min(storecredit, max(zwischensumme, 0))

            zwischensumme = bestellung - coupon_new - credit_new - braforfreevalue_new - storecredit_new + versandkosten

            rebates.append(
                Rebates(coupon_new, couponcode, braforfreevalue_new, braforfreecount_new, storecredit_new, credit_new,
                        bestellung, zwischensumme, delta, aenderung_rechnungsbetrag, versandkosten, bestellnummer,
                        get_rabattname(gutscheincode, gesamtanzahl, c, user), ))

    json_string = json.dumps([Rebates.__dict__ for Rebates in rebates])
    if bestellnummer == "":
        c.execute(
            """update userdaten set definerebates=%s,definerebatesbestellwert=%s,definerebateslieferkosten=%s,definerebatesrabatte=%s,gesamtanzahlbestellung=%s where gutscheincode=%s""",
            (
            json_string, zwischensumme, versandkosten, zwischensumme - bestellung - versandkosten, gesamtanzahl, user,))
        conn.commit()

    if get_bestellewert == "no" and get_rabatte == "no" and get_lieferkosten == "no":
        return json_string
    else:
        if get_bestellewert == "yes":
            return zwischensumme
        else:
            if get_lieferkosten == "yes":
                return versandkosten
            else:
                if get_rabatte == "yes":
                    return zwischensumme - bestellung - versandkosten


def get_country_delivery_costs(land, c):
    c.execute("""select * from versandkosten """)
    versandkosten_table = c.fetchall()
    versandkosten = -1
    for row in versandkosten_table:
        if row[0] == land:
            versandkosten = row[1]

    if versandkosten == -1:
        versandkosten = 0

    return versandkosten


def get_ruecksendewert_von_bestellnummer(bestellnummer, c):
    c.execute("""select * from ruecksendungen """)

    ruecksendungen_table = c.fetchall()
    ruecksendewert = 0
    for row_4 in ruecksendungen_table:

        if row_4[2] == bestellnummer:
            ruecksendewert = ruecksendewert + row_4[11]

    c.execute("""select * from ruecksendungen_gesamt """)

    ruecksendungen_table = c.fetchall()
    verrechnungmitrabatt = 0
    for row_4 in ruecksendungen_table:

        if row_4[2] == bestellnummer:
            verrechnungmitrabatt = verrechnungmitrabatt + row_4[9]

    return ruecksendewert - verrechnungmitrabatt


def get_bestellwert_von_bestellnummer(bestellnummer, c, session_key):
    c.execute("""select * from userdaten where gutscheincode=%s """, (session_key,))

    userdaten = c.fetchall()
    for row in userdaten:

        c.execute("""select * from bestellt where gutscheincode=%s """, (row[11],))

        bestellt_daten = c.fetchall()

        for row_2 in bestellt_daten:
            if row_2[21] == bestellnummer:
                return float(row_2[15]) + float(row_2[16]) - float(row_2[17]) - float(row_2[27]) - float(
                    row_2[28]) - float(row_2[22])


def define_ruecksende_value(c, bestellnummer, stylecode, colorcode, bhgroesse, slipgroesse, anzahl, session_key, conn):
    ruecksendung = []

    class Ruecksendung(object):
        def __init__(self, neue_ruecksendung, alte_ruecksendung, gesamtbestellung):
            self.neue_ruecksendung = neue_ruecksendung
            self.alte_ruecksendung = alte_ruecksendung
            self.gesamtbestellung = gesamtbestellung

    aktueller_rucksendewert = get_ruecksendewert_von_bestellnummer(bestellnummer, c)
    aktueller_bestellwert = get_bestellwert_von_bestellnummer(bestellnummer, c, session_key)
    new_ruecksendung = 0

    new_ruecksendung = 0
    j = 0
    c.execute("""select * from userdaten where gutscheincode=%s """, (session_key,))
    userdaten = c.fetchall()

    for row in userdaten:

        c.execute("""select * from bestellt where gutscheincode=%s """, (row[11],))

        bestellt_data = c.fetchall()

        for row_2 in bestellt_data:
            if row_2[21] == bestellnummer:
                gutscheincode = row_2[18]

                land = row_2[4]
                while j <= len(stylecode) - 1:
                    c.execute("""select * from cart_details where gutscheincode=%s and bestellnummer=%s""",
                              (row[11], bestellnummer,))
                    data_table = c.fetchall()
                    for row_3 in data_table:
                        stylecode_ = stylecode[j]
                        colorcode_ = colorcode[j]
                        bh_groesse_ = bhgroesse[j]
                        slip_groesse_ = slipgroesse[j]
                        anzahl_ = anzahl[j]

                        if row_3[7] == stylecode_ and row_3[4] == colorcode_ and row_3[2] == bh_groesse_ and row_3[
                            3] == slip_groesse_ and row_3[9] == "lingerie":
                            print row_3[7] + "==" + stylecode_ + "and" + row_3[4] + "==" + colorcode_ + "and" + row_3[
                                2] + "==" + bh_groesse_ + "and" + row_3[3] + "==" + slip_groesse_ + "and" + row_3[
                                      9] + "==lingerie"

                            c.execute(
                                """update cart_details set imzuruecksendungsprozess=%s,anzahlimzuruecksendungsprozess=%s where stylecode=%s and color=%s and bhgroesse=%s and slipgroesse=%s and productgroup=%s and bestellnummer=%s and zurueckgesendet=%s""",
                                ("ja", anzahl_, stylecode_, colorcode_, bh_groesse_, slip_groesse_, "lingerie",
                                 bestellnummer, "nein",))

                            new_ruecksendung = new_ruecksendung + row_3[8] * int(anzahl_)
                        if row_3[4] == colorcode_ and row_3[3] == slip_groesse_ and row_3[9] == "panties":
                            c.execute(
                                """update cart_details set imzuruecksendungsprozess=%s,anzahlimzuruecksendungsprozess=%s where color=%s and slipgroesse=%s and productgroup=%s and bestellnummer=%s and zurueckgesendet=%s""",
                                ("ja", anzahl_, colorcode_, slip_groesse_, "panties", bestellnummer, "nein",))
                            new_ruecksendung = new_ruecksendung + row_3[8] * int(anzahl_)
                    j = j + 1

    conn.commit()
    behalten_1 = define_rebates_for_ruecksendung(session_key, bestellnummer, c, "nein")
    gesamtbestellung = define_rebates(session_key, bestellnummer, "", "", "", c, conn, "", "no", "no", "no")

    behalten_alt = define_ruecksendungen_gesamt(session_key, c, bestellnummer)
    print behalten_1
    print gesamtbestellung

    print "ich weiss"
    c.execute(
        """update cart_details set imzuruecksendungsprozess=%s,anzahlimzuruecksendungsprozess=%s where zurueckgesendet=%s and gutscheincode=%s and bestellnummer=%s""",
        ("nein", 0, "nein", session_key, bestellnummer,))
    conn.commit()

    ruecksendung.append(Ruecksendung(behalten_1, behalten_alt, gesamtbestellung))

    json_string = json.dumps([Ruecksendung.__dict__ for Ruecksendung in ruecksendung])

    return json_string


def define_ruecksendungen_gesamt(user, c, bestellnummer):
    ruecksendungen = []

    class Ruecksendungen(object):
        def __init__(self, warenwert, erstattung, storecredit, bra4free, credit):
            self.warenwert = warenwert
            self.erstattung = erstattung
            self.storecredit = storecredit
            self.bra4free = bra4free
            self.credit = credit

    c.execute("""select * from ruecksendungen_gesamt where bestellnummer=%s""", (bestellnummer,))
    ruecksendungen_gesamt = c.fetchall()

    warenwert = 0
    erstattung = 0
    storecredit = 0
    bra4free = 0
    credit = 0

    for row in ruecksendungen_gesamt:
        warenwert = warenwert + row[6]
        erstattung = erstattung + row[7]
        storecredit = storecredit + row[16]
        credit = credit + row[15]
        bra4free = bra4free + row[14]

    ruecksendungen.append(Ruecksendungen(warenwert, erstattung, storecredit, bra4free, credit))

    json_string = json.dumps([Ruecksendungen.__dict__ for Ruecksendungen in ruecksendungen])

    return json_string


def gutscheinwert_abrufen_fuer_ruecksendung(gutscheincode, c, user, bestellnummer, stylecode, colorcode, bhgroesse,
                                            slipgroesse, anzahl):
    print "gutscheinwert_abrufen_fuer_ruecksendung"

    print "jetut aber"

    fehlermeldung = ""
    gutscheinwert = 0
    c.execute("""select * from gutscheine """)
    gutscheine = c.fetchall()
    for row in gutscheine:
        if row[0] == gutscheincode:

            if row[4] == 1:
                gutscheinwert = float(row[6])

            if row[4] == 0:
                while j <= len(stylecode) - 1:
                    c.execute("""select * from cart_details where gutscheincode=%s and bestellnummer=%s""",
                              (user, bestellnummer,))
                    current_cart_database = c.fetchall()
                    for row_3 in current_cart_database:
                        stylecode_ = stylecode[j]
                        colorcode_ = colorcode[j]
                        bh_groesse_ = bhgroesse[j]
                        slip_groesse_ = slipgroesse[j]
                        anzahl_ = anzahl[j]

                        if row_3[7] == stylecode_ and row_3[4] == colorcode_ and row_3[2] == bh_groesse_ and row_3[
                            3] == slip_groesse_ and row_3[9] == "lingerie":
                            gutscheinwert = gutscheinwert + min(row[5] - row_3[8], 0) * row_3[1]

                        if row_3[4] == colorcode_ and row_3[3] == slip_groesse_ and row_3[9] == "panties":
                            gutscheinwert = gutscheinwert + min(row[5] - row_3[8], 0) * row_3[1]
                    j = j + 1

            if row[4] == 2:

                while j <= len(stylecode) - 1:
                    c.execute("""select * from cart_details where gutscheincode=%s and bestellnummer=%s""",
                              (user, bestellnummer,))
                    current_cart_database = c.fetchall()
                    for row_3 in current_cart_database:
                        stylecode_ = stylecode[j]
                        colorcode_ = colorcode[j]
                        bh_groesse_ = bhgroesse[j]
                        slip_groesse_ = slipgroesse[j]
                        anzahl_ = anzahl[j]

                        if row_3[7] == stylecode_ and row_3[4] == colorcode_ and row_3[2] == bh_groesse_ and row_3[
                            3] == slip_groesse_ and row_3[9] == "lingerie":
                            gutscheinwert = gutscheinwert + min(row[5] - row_3[8], 0) * int(anzahl_)

                        if row_3[4] == colorcode_ and row_3[3] == slip_groesse_ and row_3[9] == "panties":
                            gutscheinwert = gutscheinwert + min(row[5] - row_3[8], 0) * int(anzahl_)
                    j = j + 1

            if row[4] == 3:

                zaehler = 0
                erstes_set = row[8]
                zweites_set = row[9]
                drittes_set = row[10]
                viertes_set = row[11]
                mehralsvier_set = row[12]
                gutscheinwert = 0
                gutscheinwert_sub = 0

                sets_gekauft = 0
                summe_preis = 0
                c.execute(
                    """select * from cart_details where gutscheincode=%s and bestellnummer=%s and productgroup=%s""",
                    (user, bestellnummer, "lingerie"))
                current_cart_database = c.fetchall()
                for row_3 in current_cart_database:
                    sets_gekauft = sets_gekauft + row_3[1]
                    summe_preis = summe_preis + row_3[8]

                durchschnittspreis = summe_preis / sets_gekauft
                sets_zurueckgeschickt_alt = 0
                c.execute(
                    """select * from ruecksendungen where gutscheincode=%s and bestellnummer=%s and productgroup=%s""",
                    (user, bestellnummer, "lingerie"))
                current_cart_database = c.fetchall()
                for row_3 in current_cart_database:
                    sets_zurueckgeschickt_alt = sets_zurueckgeschickt_alt + row_3[9]

                j = 0
                sets_zurueckgeschickt_neu = 0
                while j <= len(stylecode) - 1:
                    if stylecode[j] != "" and colorcode[j] != "" and bhgroesse[j] != "" and slipgroesse[j] != "":
                        sets_zurueckgeschickt_neu = sets_zurueckgeschickt_neu + int(anzahl[j])
                    j = j + 1

                j = 0
                gutscheinwert_sub_sets_gekauft = 0
                gutscheinwert_sub_sets_zurueckgeschickt_alt = 0
                gutscheinwert_sub_sets_zurueckgeschickt_neu = 0
                while j <= 2:
                    print j

                    if j == 0:
                        zaehler = sets_gekauft - 1
                        max = 0
                    if j == 1:
                        zaehler = sets_gekauft - 1

                        max = sets_gekauft - sets_zurueckgeschickt_alt

                    if j == 2:
                        print sets_gekauft
                        print sets_zurueckgeschickt_alt
                        print sets_zurueckgeschickt_neu

                        zaehler = sets_gekauft - sets_zurueckgeschickt_alt - 1

                        max = sets_gekauft - sets_zurueckgeschickt_alt - sets_zurueckgeschickt_neu

                        print"sets_zurueckgeschickt_neu"
                        print zaehler
                        print max

                    while zaehler >= max:

                        if zaehler == 0 and erstes_set != 0:
                            if j == 0:
                                gutscheinwert_sub_sets_gekauft = gutscheinwert_sub_sets_gekauft + erstes_set
                            if j == 1:
                                gutscheinwert_sub_sets_zurueckgeschickt_alt = gutscheinwert_sub_sets_zurueckgeschickt_alt + erstes_set
                            if j == 2:
                                gutscheinwert_sub_sets_zurueckgeschickt_neu = gutscheinwert_sub_sets_zurueckgeschickt_neu + durchschnittspreis - erstes_set

                        if zaehler == 1 and zweites_set != 0:
                            if j == 0:
                                gutscheinwert_sub_sets_gekauft = gutscheinwert_sub_sets_gekauft + zweites_set
                            if j == 1:
                                gutscheinwert_sub_sets_zurueckgeschickt_alt = gutscheinwert_sub_sets_zurueckgeschickt_alt + zweites_set
                            if j == 2:
                                gutscheinwert_sub_sets_zurueckgeschickt_neu = gutscheinwert_sub_sets_zurueckgeschickt_neu + durchschnittspreis - zweites_set

                        if zaehler == 2 and drittes_set != 0:
                            if j == 0:
                                gutscheinwert_sub_sets_gekauft = gutscheinwert_sub_sets_gekauft + drittes_set
                            if j == 1:
                                gutscheinwert_sub_sets_zurueckgeschickt_alt = gutscheinwert_sub_sets_zurueckgeschickt_alt + drittes_set
                            if j == 2:
                                gutscheinwert_sub_sets_zurueckgeschickt_neu = gutscheinwert_sub_sets_zurueckgeschickt_neu + durchschnittspreis - drittes_set

                        if zaehler == 3 and viertes_set != 0:
                            if j == 0:
                                gutscheinwert_sub_sets_gekauft = gutscheinwert_sub_sets_gekauft + viertes_set
                            if j == 1:
                                gutscheinwert_sub_sets_zurueckgeschickt_alt = gutscheinwert_sub_sets_zurueckgeschickt_alt + viertes_set
                            if j == 2:
                                gutscheinwert_sub_sets_zurueckgeschickt_neu = gutscheinwert_sub_sets_zurueckgeschickt_neu + durchschnittspreis - viertes_set

                        if zaehler > 3 and mehralsvier_set != 0:
                            if j == 0:
                                gutscheinwert_sub_sets_gekauft = gutscheinwert_sub_sets_gekauft + mehralsvier_set
                            if j == 1:
                                gutscheinwert_sub_sets_zurueckgeschickt_alt = gutscheinwert_sub_sets_zurueckgeschickt_alt + mehralsvier_set
                            if j == 2:
                                gutscheinwert_sub_sets_zurueckgeschickt_neu = gutscheinwert_sub_sets_zurueckgeschickt_neu + durchschnittspreis - mehralsvier_set

                        zaehler = zaehler - 1
                    j = j + 1

                print gutscheinwert_sub_sets_zurueckgeschickt_neu
                gutscheinwert = gutscheinwert_sub_sets_zurueckgeschickt_neu
                print "gutscheinwert"
                print gutscheinwert

        print "gutscheinwert"
        print gutscheinwert

        return gutscheinwert


def define_warenkorb_object(user, modelAB, sub_picture, c, conn):
    warenkorb = []

    class Warenkorb(object):
        def __init__(self, style, anzahl, bhgroesse, slipgroesse, color, freiemenge, status, picture, priceregular,
                     pricesubscription, stylecode, colorcode, link1, productgroup, rabatt):
            self.style = style
            self.anzahl = anzahl
            self.bhgroesse = bhgroesse
            self.slipgroesse = slipgroesse
            self.color = color
            self.freiemenge = freiemenge
            self.status = status
            self.picture = picture
            self.priceregular = priceregular
            self.pricesubscription = pricesubscription
            self.stylecode = stylecode
            self.colorcode = colorcode
            self.link1 = link1
            self.productgroup = productgroup
            self.rabatt = rabatt

    print "define_warenkorb_object"

    c.execute("""select * from cart_details where gutscheincode=%s and bestellt=%s""", (user, "nein",))
    current_cart_database = c.fetchall()

    for row in current_cart_database:
        print "next"
        print row[0]
        c.execute("""select * from lingerieselection where colorcode=%s""", (row[4],))
        lingerieselection_data = c.fetchall()

        for row_2 in lingerieselection_data:
            print row_2[0]
            print row[2] + "!= and " + row_2[12] + "==" + row[7] + "and " + row[9] + "==" + row_2[8]
            if row[2] != "" and row_2[12] == row[7] and row[9] == row_2[8]:
                print "ja"

                warenkorb.append(Warenkorb(row[0], row[1], row[2], row[3], row[4], row[5], row[6],
                                           get_pictures_from_consolidated_table(c, row_2[12], row_2[13], modelAB,
                                                                                sub_picture, row_2[2], "first",
                                                                                "small"), row_2[3], row_2[4], row_2[12],
                                           row_2[13], link_name_bestimmen(row_2[8]), row[9], row[10]))
            else:
                print "if " + row[0] + "==" + row_2[0]
                if row[0] == row_2[0]:
                    warenkorb.append(Warenkorb(row[0], row[1], row[2], row[3], row[4], row[5], row[6],
                                               get_pictures_from_consolidated_table(c, row_2[12], row_2[13], modelAB,
                                                                                    sub_picture, row_2[2], "first",
                                                                                    "small"), row_2[3], row_2[4],
                                               row_2[12], row_2[13], link_name_bestimmen(row_2[8]), row[9], row[10]))

    json_string = json.dumps([Warenkorb.__dict__ for Warenkorb in warenkorb])

    if json_string != "[]":
        c.execute("""update userdaten set warenkorb=%s where gutscheincode=%s""", (json_string, user,))
        conn.commit()
    else:
        c.execute("""update userdaten set warenkorb=%s, messageshownwarenkorbleer=%s where gutscheincode=%s""",
                  (json_string, "yes", user,))
        conn.commit()

    return json_string


def check_whether_warenkorb_ist_leer(user, c):
    count_rows_userdaten = c.execute("""select * from cart_details where gutscheincode=%s and bestellt=%s""",
                                     (user, "nein",))
    c.execute(count_rows_userdaten)
    zaehler_cart_details = int(c.rowcount)

    return zaehler_cart_details


def define_warenkorb(user, modelAB, sub_picture, c, conn):
    warenkorb = []

    class Warenkorb(object):
        def __init__(self, style, anzahl, bhgroesse, slipgroesse, color, freiemenge, status, picture, priceregular,
                     pricesubscription, stylecode, colorcode, link1, productgroup, rabatt):
            self.style = style
            self.anzahl = anzahl
            self.bhgroesse = bhgroesse
            self.slipgroesse = slipgroesse
            self.color = color
            self.freiemenge = freiemenge
            self.status = status
            self.picture = picture
            self.priceregular = priceregular
            self.pricesubscription = pricesubscription
            self.stylecode = stylecode
            self.colorcode = colorcode
            self.link1 = link1
            self.productgroup = productgroup
            self.rabatt = rabatt

    c.execute("""select * from cart_details where gutscheincode=%s and bestellt=%s""", (user, "nein",))
    current_cart_database = c.fetchall()

    for row in current_cart_database:
        print "next"
        print row[0]
        c.execute("""select * from lingerieselection where colorcode=%s""", (row[4],))
        lingerieselection_data = c.fetchall()

        for row_2 in lingerieselection_data:
            print row_2[0]
            print row[2] + "!= and " + row_2[12] + "==" + row[7] + "and " + row[9] + "==" + row_2[8]
            if row[2] != "" and row_2[12] == row[7] and row[9] == row_2[8]:
                print "ja"
                warenkorb.append(Warenkorb(row[0], row[1], row[2], row[3], row[4], row[5], row[6],
                                           get_pictures_from_consolidated_table(c, row_2[12], row_2[13], modelAB,
                                                                                sub_picture, row_2[2], "first",
                                                                                "small"), row_2[3], row_2[4], row_2[12],
                                           row_2[13], link_name_bestimmen(row_2[8]), row[9], row[10]))
            else:
                print "if " + row[0] + "==" + row_2[0]
                if row[0] == row_2[0]:
                    warenkorb.append(Warenkorb(row[0], row[1], row[2], row[3], row[4], row[5], row[6],
                                               get_pictures_from_consolidated_table(c, row_2[12], row_2[13], modelAB,
                                                                                    sub_picture, row_2[2], "first",
                                                                                    "small"), row_2[3], row_2[4],
                                               row_2[12], row_2[13], link_name_bestimmen(row_2[8]), row[9], row[10]))

    #   warenkorb.sort(key = lambda x: x.position)
    json_string = json.dumps([Warenkorb.__dict__ for Warenkorb in warenkorb])

    if json_string != "[]":
        c.execute("""update userdaten set warenkorb=%s where gutscheincode=%s""", (json_string, user,))
        conn.commit()
    else:
        c.execute("""update userdaten set warenkorb=%s, messageshownwarenkorbleer=%s where gutscheincode=%s""",
                  (json_string, "yes", user,))
        conn.commit()
    return json_string


def get_pictures(c, stylecode, colorcode, productgroup, modelAB, sub_picture, pantytype, first_or_all, small_or_big):
    pictures_json = []

    class Pictures_JSON(object):
        def __init__(self, link, alt, title):
            self.link = link
            self.alt = alt
            self.title = title

    sys.setdefaultencoding("ISO-8859-1")

    pic1 = [[] for i in range(10)]
    pic2 = [[] for i in range(10)]
    pic3 = [[] for i in range(10)]
    pic4 = [[] for i in range(10)]

    c.execute("""select * from %s """ % ("picturelibrary"))
    picturelibrary_data = c.fetchall()
    group1 = productgroup
    pic_1 = ""
    pic_2 = ""
    pic_3 = ""
    pic_4 = ""
    zaehler = 0
    zaehler_1 = 0
    zaehler_2 = 0
    zaehler_3 = 0
    zaehler_4 = 0
    for row_7 in picturelibrary_data:
        if group1 != "panties" and stylecode != "":
            if stylecode == row_7[5] and colorcode == row_7[6]:
                if row_7[3] != "panties":
                    if ((row_7[0] == modelAB and row_7[1] == sub_picture) or (
                            row_7[0] == -1 and row_7[1] == sub_picture)):
                        if small_or_big == "big":
                            pic1[zaehler_1].append(row_7[2])
                            pic1[zaehler_1].append(row_7[8])
                            pic1[zaehler_1].append(row_7[9])
                            zaehler_1 = zaehler_1 + 1
                        else:
                            pic1[zaehler_1].append(row_7[7])
                            pic1[zaehler_1].append(row_7[8])
                            pic1[zaehler_1].append(row_7[9])
                            zaehler_1 = zaehler_1 + 1
                    if ((row_7[0] == modelAB and row_7[1] != sub_picture and sub_picture != -1 and row_7[1] != -1) or (
                            row_7[0] == -1 and row_7[1] != sub_picture and sub_picture != -1 and row_7[1] != -1)) or (
                            group1 == "panties" and group1 == row_7[3]):
                        if small_or_big == "big":
                            pic2[zaehler_2].append(row_7[2])
                            pic2[zaehler_2].append(row_7[8])
                            pic2[zaehler_2].append(row_7[9])
                            zaehler_2 = zaehler_2 + 1
                        else:
                            pic2[zaehler_2].append(row_7[7])
                            pic2[zaehler_2].append(row_7[8])
                            pic2[zaehler_2].append(row_7[9])
                            zaehler_2 = zaehler_2 + 1

                        zaehler = zaehler + 1

                    if row_7[1] == -1:
                        if row_7[10] == "modelpicture":
                            if row_7[0] == modelAB or row_7[0] == -1:
                                if small_or_big == "big":
                                    pic3[zaehler_3].append(row_7[2])
                                    pic3[zaehler_3].append(row_7[8])
                                    pic3[zaehler_3].append(row_7[9])
                                    zaehler_3 = zaehler_3 + 1
                                else:
                                    pic3[zaehler_3].append(row_7[7])
                                    pic3[zaehler_3].append(row_7[8])
                                    pic3[zaehler_3].append(row_7[9])
                                    zaehler_3 = zaehler_3 + 1
                        else:
                            if row_7[0] == modelAB or row_7[0] == -1:
                                if small_or_big == "big":
                                    pic4[zaehler_4].append(row_7[2])
                                    pic4[zaehler_4].append(row_7[8])
                                    pic4[zaehler_4].append(row_7[9])
                                    zaehler_4 = zaehler_4 + 1
                                else:
                                    pic4[zaehler_4].append(row_7[7])
                                    pic4[zaehler_4].append(row_7[8])
                                    pic4[zaehler_4].append(row_7[9])
                                    zaehler_4 = zaehler_4 + 1


        else:
            if colorcode == row_7[6]:
                if group1 == row_7[3] and (pantytype == row_7[4]):
                    if small_or_big == "big":
                        pic1[zaehler_1].append(row_7[2])
                        pic1[zaehler_1].append(row_7[8])
                        pic1[zaehler_1].append(row_7[9])
                        zaehler_1 = zaehler_1 + 1
                    else:
                        pic1[zaehler_1].append(row_7[7])
                        pic1[zaehler_1].append(row_7[8])
                        pic1[zaehler_1].append(row_7[9])
                        zaehler_1 = zaehler_1 + 1

    pictures = [[] for i in range(zaehler_1 + zaehler_2 + zaehler_3 + zaehler_4)]

    if first_or_all == "first":

        if len(pic1[0]) != 0:
            pictures_json.append(Pictures_JSON(pic1[0][0], pic1[0][1], pic1[0][2], ))
            pictures_json = json.dumps([Pictures_JSON.__dict__ for Pictures_JSON in pictures_json])
            return pictures_json
        else:
            if len(pic2[0]) != 0:
                pictures_json.append(Pictures_JSON(pic2[0][0], pic2[0][1], pic2[0][2], ))
                pictures_json = json.dumps([Pictures_JSON.__dict__ for Pictures_JSON in pictures_json])
                return pictures_json

            else:
                if len(pic3[0]) != 0:
                    pictures_json.append(Pictures_JSON(pic3[0][0], pic3[0][1], pic3[0][2], ))
                    pictures_json = json.dumps([Pictures_JSON.__dict__ for Pictures_JSON in pictures_json])
                    return pictures_json
    else:
        zaehler = 0
        i = 0
        while i <= zaehler_1 - 1:
            pictures_json.append(Pictures_JSON(pic1[i][0], pic1[i][1], pic1[i][2], ))

            i = i + 1
            zaehler = zaehler + 1

        i = 0
        while i <= zaehler_2 - 1:
            pictures_json.append(Pictures_JSON(pic2[i][0], pic2[i][1], pic2[i][2], ))

            i = i + 1
            zaehler = zaehler + 1

        i = 0
        while i <= zaehler_3 - 1:
            pictures_json.append(Pictures_JSON(pic3[i][0], pic3[i][1], pic3[i][2], ))

            i = i + 1
            zaehler = zaehler + 1

        i = 0
        while i <= zaehler_4 - 1:
            pictures_json.append(Pictures_JSON(pic4[i][0], pic4[i][1], pic4[i][2], ))

            i = i + 1
            zaehler = zaehler + 1

        pictures_json = json.dumps([Pictures_JSON.__dict__ for Pictures_JSON in pictures_json])
        return pictures_json


def get_stylecode_colorcode_from_order(session_key, bestellnummer, c, user):
    stylecodes_colorcodes = []
    if bestellnummer != "":
        c.execute("""select * from userdaten where gutscheincode=%s """, (session_key,))
        userdaten = c.fetchall()
        for row in userdaten:
            c.execute("""select * from bestellt where gutscheincode=%s """, (row[11],))
            bestellt_daten = c.fetchall()
            for row_2 in bestellt_daten:
                c.execute("""select * from cart_details where gutscheincode=%s""", (row[11],))

                session_table = c.fetchall()

                for row_3 in session_table:
                    if bestellnummer == row_2[21]:
                        stylecodes_colorcodes.append(row_3[7] + "_" + row_3[4])
    else:
        c.execute("""select * from cart_details where gutscheincode=%s""", (user,))
        current_cart_database = c.fetchall()
        for row in current_cart_database:
            stylecodes_colorcodes.append(row[7] + "_" + row[4])

    return stylecodes_colorcodes


def get_content_for_facebookpixel_from_order(session_key, bestellnummer, c, user):
    facebook = []

    class Facebook(object):
        def __init__(self, id, quantity, price):
            self.id = id
            self.quantity = quantity
            self.price = price

    google = []

    class Google(object):
        def __init__(self, id, quantity, price, name):
            self.id = id
            self.quantity = quantity
            self.price = price
            self.name = name

    data = []

    class Data(object):
        def __init__(self, facebook, google):
            self.facebook = facebook
            self.google = google

    if bestellnummer != "":

        c.execute("""select * from bestellt where gutscheincode=%s and bestellnummer=%s""",
                  (session_key, bestellnummer,))
        bestellt_daten = c.fetchall()
        for row_2 in bestellt_daten:
            c.execute("""select * from cart_details where gutscheincode=%s and bestellnummer=%s""",
                      (session_key, bestellnummer))

            session_table = c.fetchall()

            for row_3 in session_table:
                stylecodes_colorcodes.append(row_3[7] + "_" + row_3[4])
                facebook.append(Facebook(row_3[7] + "_" + row_3[4], row_3[1], row_3[8], ))
                google.append(Google(row_3[7] + "_" + row_3[4], row_3[1], row_3[8], row_3[0], ))

    else:
        c.execute("""select * from cart_details where gutscheincode=%s""", (user,))
        current_cart_database = c.fetchall()
        for row in current_cart_database:
            facebook.append(Facebook(row[7] + "_" + row[4], row[1], row[8], ))
            google.append(Google(row[7] + "_" + row[4], row[1], row[8], row[0], ))

    json_string_facebook = json.dumps([Facebook.__dict__ for Facebook in facebook])
    json_string_google = json.dumps([Google.__dict__ for Google in google])

    data.append(Data(json_string_facebook, json_string_google, ))

    json_string = json.dumps([Data.__dict__ for Data in data])
    return json_string


def define_bestelldetails(session_key, bestellnummer, gerichtname, bewertung, c, modelAB, sub_picture):
    bestelldetails = []
    style_names = []

    class Bestelldetails(object):
        def __init__(self, style, anzahl, datum, freiemenge, datumweekday, status, bestellnummer, bewertung,
                     bewertungstext, bewertungsdatum, picture_link_small, subtitle, preis, bhgroesse, slipgroesse,
                     color, stylecode, passform, bewertungsheadline):
            self.style = style
            self.anzahl = anzahl
            self.datum = datum
            self.freiemenge = freiemenge
            self.datumweekday = datumweekday
            self.status = status
            self.bestellnummer = bestellnummer
            self.bewertung = bewertung
            self.bewertungstext = bewertungstext
            self.bewertungsdatum = bewertungsdatum
            self.picture_link_small = picture_link_small
            self.subtitle = subtitle
            self.preis = preis
            self.bhgroesse = bhgroesse
            self.slipgroesse = slipgroesse
            self.color = color
            self.stylecode = stylecode
            self.passform = passform
            self.bewertungsheadline = bewertungsheadline

    if bestellnummer == "":

        c.execute("""select * from userdaten where gutscheincode=%s """, (session_key,))

        userdaten = c.fetchall()

        for row in userdaten:
            c.execute("""select * from bestellt where gutscheincode=%s""", (row[11],))

            bestellt_daten = c.fetchall()

            for row_2 in bestellt_daten:
                c.execute("""select * from cart_details where bestellnummer=%s and bestellt=%s""", (row_2[21], "ja",))

                session_table = c.fetchall()

                for row_3 in session_table:
                    c.execute("""select * from lingerieselection where name='%s'""" % (row_3[0],))
                    lingerieselection_name = c.fetchall()
                    for row_5 in lingerieselection_name:
                        if row_3[2] != "":
                            c.execute("""select * from %s where color='%s' and size='%s' and stylecode='%s'""" % (
                            "stylecode", row_3[4], row_3[2], row_5[12],))

                            stylecode_daten = c.fetchall()
                        else:
                            c.execute("""select * from %s where color='%s' and size='%s'""" % (
                            "stylecode", row_3[4], row_3[3],))

                            stylecode_daten = c.fetchall()

                        for row_6 in stylecode_daten:
                            freie_menge = min(int(row_6[4]) - int(row_6[5]), 10)
                            if row_2[23] == "VIP":
                                bestelldetails.append(
                                    Bestelldetails(row_3[0], row_3[1], row[18], freie_menge, row_3[4], row_3[6],
                                                   row_2[21], row_3[16], row_3[18], row_3[19],
                                                   get_pictures_from_consolidated_table(c, row_5[12], row_5[13],
                                                                                        modelAB, sub_picture, row_5[2],
                                                                                        "first", "small"), row_5[9],
                                                   row_5[4], row_3[2], row_3[3], row_6[2], row_5[12], row_3[20],
                                                   row_3[17], ))
                            else:
                                bestelldetails.append(
                                    Bestelldetails(row_3[0], row_3[1], row[18], freie_menge, row_3[4], row_3[6],
                                                   row_2[21], row_3[16], row_3[18], row_3[19],
                                                   get_pictures_from_consolidated_table(c, row_5[12], row_5[13],
                                                                                        modelAB, sub_picture, row_5[2],
                                                                                        "first", "small"), row_5[9],
                                                   row_5[3], row_3[2], row_3[3], row_6[2], row_5[12], row_3[20],
                                                   row_3[17], ))

    else:
        c.execute("""select * from userdaten where gutscheincode=%s """, (session_key,))

        userdaten = c.fetchall()
        for row in userdaten:

            c.execute("""select * from bestellt where gutscheincode=%s """, (row[11],))

            bestellt_daten = c.fetchall()

            for row_2 in bestellt_daten:
                c.execute("""select * from cart_details where bestellnummer=%s and bestellt=%s""", (row_2[21], "ja",))
                session_table = c.fetchall()

                for row_3 in session_table:
                    if bestellnummer == row_2[21]:

                        c.execute("""select * from lingerieselection """)

                        lingerieselection_daten = c.fetchall()

                        for row_5 in lingerieselection_daten:
                            if row_5[0] == row_3[0]:
                                print row_5[0]

                                c.execute("""select * from %s """ % ("stylecode"))
                                stylecode_daten = c.fetchall()

                                for row_6 in stylecode_daten:
                                    if row_5[12] == row_6[1]:

                                        print row_3[4] + "==" + row_6[2] + "and" + row_3[7] + "==" + row_6[1] + "and" + \
                                              row_3[2] + "==" + row_6[3] + "or " + row_3[2] + "== and " + row_6[
                                                  3] + "==" + row_3[3] + "and " + row_3[4] + "==" + row_6[2]
                                        if (row_3[4] == row_6[2] and row_3[7] == row_6[1] and row_3[2] == row_6[3]) or (
                                                row_3[2] == "" and row_6[3] == row_3[3] and row_3[4] == row_6[2]):

                                            if row_2[23] == "VIP":
                                                bestelldetails.append(
                                                    Bestelldetails(row_3[0], row_3[1], row[18], 10, row_3[4], row_3[6],
                                                                   row_2[21], row_3[16], row_3[18], row_3[19],
                                                                   get_pictures_from_consolidated_table(c, row_6[1],
                                                                                                        row_3[4],
                                                                                                        modelAB,
                                                                                                        sub_picture,
                                                                                                        row_5[2],
                                                                                                        "first",
                                                                                                        "small"),
                                                                   row_5[9], row_5[4], row_3[2], row_3[3], row_6[2],
                                                                   row_5[12], row_3[20], row_3[17], ))

                                            else:
                                                bestelldetails.append(
                                                    Bestelldetails(row_3[0], row_3[1], row[18], 10, row_3[4], row_3[6],
                                                                   row_2[21], row_3[16], row_3[18], row_3[19],
                                                                   get_pictures_from_consolidated_table(c, row_6[1],
                                                                                                        row_3[4],
                                                                                                        modelAB,
                                                                                                        sub_picture,
                                                                                                        row_5[2],
                                                                                                        "first",
                                                                                                        "small"),
                                                                   row_5[9], row_5[3], row_3[2], row_3[3], row_6[2],
                                                                   row_5[12], row_3[20], row_3[17], ))

    json_string = json.dumps([Bestelldetails.__dict__ for Bestelldetails in bestelldetails])

    return json_string


def define_ruecksendungen(session_key, c, modelAB, sub_picture):
    ruecksendungen = []

    class Ruecksendungen(object):
        def __init__(self, style, anzahl, bestellnummer, picture_link_small, subtitle, preis, bhgroesse, slipgroesse,
                     dateofproposal, dateofmaxreturn, deliverycode, grund, stylecode, colorcode, wareerhalten, status,
                     id, lieferkosten, verrechnungmitrabatt, versandlabel, geldzurueckueberwiesen, usercode, bra4free,
                     storecredit, credit):
            self.style = style
            self.anzahl = anzahl
            self.bestellnummer = bestellnummer
            self.picture_link_small = picture_link_small
            self.subtitle = subtitle
            self.preis = preis
            self.bhgroesse = bhgroesse
            self.slipgroesse = slipgroesse
            self.dateofproposal = dateofproposal
            self.dateofmaxreturn = dateofmaxreturn
            self.deliverycode = deliverycode
            self.grund = grund
            self.stylecode = stylecode
            self.colorcode = colorcode
            self.wareerhalten = wareerhalten
            self.status = status
            self.id = id
            self.lieferkosten = lieferkosten
            self.verrechnungmitrabatt = verrechnungmitrabatt
            self.versandlabel = versandlabel
            self.geldzurueckueberwiesen = geldzurueckueberwiesen
            self.geldzurueckueberwiesen = geldzurueckueberwiesen
            self.usercode = usercode
            self.bra4free = bra4free
            self.storecredit = storecredit
            self.credit = credit

    print "asdasdasd"

    print "def define_ruecksendungen(session_key,c,modelAB,sub_picture)"
    if session_key != "all":
        print "schritt 1"

        c.execute("""select * from ruecksendungen where gutscheincode=%s""", (session_key,))

        ruecksendungen_table = c.fetchall()
        for row_4 in ruecksendungen_table:
            print "schritt 2"

            print row_4[0]
            c.execute("""select * from lingerieselection """)

            lingerieselection = c.fetchall()
            for row_5 in lingerieselection:
                if row_4[17] == "lingerie":
                    if row_5[12] == row_4[7] and row_4[8] == row_5[13] and row_4[17] == row_5[8]:
                        c.execute("""select * from ruecksendungen_gesamt """)

                        ruecksendungen_gesamt = c.fetchall()

                        for row_6 in ruecksendungen_gesamt:
                            print "ruecksendungen_gesamtruecksendungen_gesamt"

                            print row_6[0] + "==" + row_4[0]
                            if row_6[0] == row_4[0]:
                                print row_5[0]
                                print row_6[6]
                                ruecksendungen.append(Ruecksendungen(row_5[0], row_4[9], row_4[2],
                                                                     get_pictures_from_consolidated_table(c, row_5[12],
                                                                                                          row_5[13],
                                                                                                          modelAB,
                                                                                                          sub_picture,
                                                                                                          row_5[2],
                                                                                                          "first",
                                                                                                          "small"),
                                                                     row_5[9], row_4[10], row_4[15], row_4[16],
                                                                     row_4[3], row_4[4], row_4[5], row_4[6], row_4[7],
                                                                     row_4[8], row_4[12], row_4[14], row_4[0], row_6[7],
                                                                     row_6[7], row_6[13], row_6[11], row_4[1],
                                                                     row_6[14], row_6[16], row_6[15], ))

                else:

                    panty_type = row_4[16].split(" ")
                    panty_type = panty_type[0]

                    if row_4[8] == row_5[13] and row_4[17] == row_5[8] and panty_type == row_5[2]:
                        print row_4[8] + "==" + row_5[13] + "and" + row_4[17] + "==" + row_5[8]
                        c.execute("""select * from ruecksendungen_gesamt """)

                        ruecksendungen_gesamt = c.fetchall()
                        print "ruecksendungen_gesamtruecksendungen_gesamt"
                        for row_6 in ruecksendungen_gesamt:

                            print row_6[0] + "==" + row_4[0]
                            if row_6[0] == row_4[0]:
                                print row_5[0]

                                ruecksendungen.append(Ruecksendungen(row_5[0], row_4[9], row_4[2],
                                                                     get_pictures_from_consolidated_table(c, row_5[12],
                                                                                                          row_5[13],
                                                                                                          modelAB,
                                                                                                          sub_picture,
                                                                                                          row_5[2],
                                                                                                          "first",
                                                                                                          "small"),
                                                                     row_5[9], row_4[10], "", row_4[16], row_4[3],
                                                                     row_4[4], row_4[5], row_4[6], row_4[7], row_4[8],
                                                                     row_4[12], row_4[14], row_4[0], row_6[7], row_6[7],
                                                                     row_6[13], row_6[11], row_4[1], row_6[14],
                                                                     row_6[16], row_6[15]))



    else:

        c.execute("""select * from cart_details where gutscheincode=%s  and zurueckgesendet=%s""", (session_key, "ja",))

        data_table = c.fetchall()

        for row_3 in data_table:
            print row_3[2] + "," + row_3[3]

            c.execute("""select * from lingerieselection """)

            lingerieselection = c.fetchall()

            for row_5 in lingerieselection:
                if row_3[9] == "lingerie":
                    if row_5[12] == row_4[7] and row_4[4] == row_5[13] and row_4[9] == row_5[8]:
                        c.execute("""select * from ruecksendungen_gesamt """)

                        ruecksendungen_gesamt = c.fetchall()
                        for row_6 in ruecksendungen_gesamt:
                            if row_6[0] == row_4[0]:
                                ruecksendungen.append(
                                    Ruecksendungen(row_3[0], row_4[9], row_4[2], "", row_5[9], row_4[10], row_3[2],
                                                   row_3[3], row_4[3], row_4[4], row_4[5], row_4[6], row_4[7], row_4[8],
                                                   row_4[12], row_4[14], row_4[0], row_6[9], row_6[9], row_6[13],
                                                   row_6[11], row_4[1], row_6[14], row_6[16], row_6[15]))


                else:
                    print row_4[4] + "==" + row_5[13] + "and" + row_4[9] + "==" + row_5[8] + "and" + panty_type + "==" + \
                          row_5[2]
                    if row_4[4] == row_5[13] and row_4[9] == row_5[8] and panty_type == row_5[2]:
                        c.execute("""select * from ruecksendungen_gesamt """)

                        ruecksendungen_gesamt = c.fetchall()
                        print "ruecksendungen_gesamtruecksendungen_gesamt"
                        for row_6 in ruecksendungen_gesamt:

                            print row_6[0] + "==" + row_4[0]
                            if row_6[0] == row_4[0]:
                                ruecksendungen.append(
                                    Ruecksendungen(row_3[0], row_4[9], row_4[2], "", row_5[9], row_4[10], "", row_3[3],
                                                   row_4[3], row_4[4], row_4[5], "", row_4[7], row_4[8], row_4[12],
                                                   row_4[14], row_4[0], row_6[9], row_6[9], row_6[13], row_6[11],
                                                   row_4[1], row_6[14], row_6[16], row_6[15]))

    json_string = json.dumps([Ruecksendungen.__dict__ for Ruecksendungen in ruecksendungen])

    return json_string


def get_sendungsverfolgung(tracking_code, session_id_table):
    easypost.api_key = 'OZVgLVsYx7ik768m3wApeQ'

    trackers = easypost.Tracker.all(tracking_code="LM984883917US")

    i = 0

    while i <= len(trackers['trackers'][0]['tracking_details']) - 1:
        i = i + 1


# {#012  "carrier": "USPS", #012  "carrier_detail":
#    {#012    "alternate_identifier": null, #012    "container_type": null, #012    "destination_location": "CHARLESTON SC, 29401", #012    "destination_tracking_location":
#        {#012      "city": "CHARLESTON", #012      "country": null, #012      "object": "TrackingLocation", #012      "state": "SC", #012      "zip": "29407"#012    }
#        ,#012    "est_delivery_date_local": null, #012    "est_delivery_time_local": null, #012    "guaranteed_delivery_date": null, #012    "initial_delivery_attempt": "2017-09-11T05:32:00Z", #012    "object": "CarrierDetail", #012    "origin_location": "HOUSTON TX, 77001",#012    "origin_tracking_location":
#        {#012      "city": "NORTH HOUSTON", #012      "country": null, #012      "object": "TrackingLocation", #012      "state": "TX", #012      "zip": "77315"#012    }
#        , #012    "service": "First-Class Package Service"#012  }
#    , #012  "created_at": "2017-10-08T15:38:00Z", #012  "est_delivery_date": "2017-10-08T15:41:00Z", #012  "fees": [], #012  "finalized": true, #012  "id": "trk_72004a9a19a44f96a62f85b25abd5786", #012  "is_return": false, #012  "mode": "test", #012  "object": "Tracker", #012  "public_url": "https://track.easypost.com/djE6dHJrXzcyMDA0YTlhMTlhNDRmOTZhNjJmODViMjVhYmQ1Nzg2", #012  "shipment_id": "shp_8471f100957242c3ae0e82de0377dd4b", #012  "signed_by": "John Tester", #012  "status": "delivered", #012  "status_detail": "arrived_at_destination", #012  "tracking_code": "LM984883917US", #012  "tracking_details": [#012    {#012      "carrier_code": null, #012      "datetime": "2017-09-08T15:41:00Z", #012      "message": "Pre-Shipment Info Sent to USPS", #012      "object": "TrackingDetail", #012      "source": "USPS", #012      "status": "pre_transit", #012      "status_detail": "status_update", #012      "tracking_location": {#012        "city": null, #012        "country": null, #012        "object": "TrackingLocation", #012        "state": null, #012        "zip": null#012      }#012    }, #012    {#012      "carrier_code": null, #012      "datetime": "2017-09-09T04:18:00Z", #012      "message": "Shipping Label Created", #012      "object": "TrackingDetail", #012      "source": "USPS", #012      "status": "pre_transit", #012      "status_detail": "status_update", #012      "tracking_location": {#012        "city": "HOUSTON", #012        "country": null, #012        "object": "TrackingLocation", #012        "state": "TX", #012        "zip": "77063"#012      }#012    }, #012    {#012      "carrier_code": null, #012      "datetime": "2017-09-09T14:23:00Z", #012      "message": "Arrived at USPS Origin Facility", #012      "object": "TrackingDetail", #012      "source": "USPS", #012      "status": "in_transit", #012      "status_detail": "arrived_at_facility", #012      "tracking_location": {#012        "city": "NORTH HOUSTON", #012        "country": null, #012        "object": "TrackingLocation", #012        "state": "TX", #012        "zip": "77315"#012      }#012    }, #012    {#012      "carrier_code": null, #012      "datetime": "2017-09-10T15:59:00Z", #012      "message": "Arrived at USPS Facility", #012      "object": "TrackingDetail", #012      "source": "USPS", #012      "status": "in_transit", #012      "status_detail": "arrived_at_facility", #012      "tracking_location": {#012        "city": "COLUMBIA", #012        "country": null, #012        "object": "TrackingLocation", #012        "state": "SC", #012        "zip": "29201"#012      }#012    }, #012    {#012      "carrier_code": null, #012      "datetime": "2017-09-10T18:50:00Z", #012      "message": "Arrived at Post Office", #012      "object": "TrackingDetail", #012      "source": "USPS", #012      "status": "in_transit", #012      "status_detail": "arrived_at_facility", #012      "tracking_location": {#012        "city": "CHARLESTON", #012        "country": null, #012        "object": "TrackingLocation", #012        "state": "SC", #012        "zip": "29407"#012      }#012    }, #012    {#012      "carrier_code": null, #012      "datetime": "2017-09-11T00:30:00Z", #012      "message": "Sorting Complete", #012      "object": "TrackingDetail", #012      "source": "USPS", #012      "status": "in_transit", #012      "status_detail": "status_update", #012      "tracking_location": {#012        "city": "CHARLESTON", #012        "country": null, #012        "object": "TrackingLocation", #012        "state": "SC", #012        "zip": "29407"#012      }#012    }, #012    {#012      "carrier_code": null, #012      "datetime": "2017-09-11T00:40:00Z", #012      "message": "Out for Delivery", #012      "object": "TrackingDetail", #012      "source": "USPS", #012      "status": "out_for_delivery", #012      "status_detail": "out_for_delivery", #012      "tracking_location": {#012        "city": "CHARLESTON", #012        "country": null, #012        "object": "TrackingLocation", #012        "state": "SC", #012        "zip": "29407"#012      }#012    }, #012    {#012      "carrier_code": null, #012      "datetime": "2017-09-11T05:32:00Z", #012      "message": "Delivered", #012      "object": "TrackingDetail", #012      "source": "USPS", #012      "status": "delivered", #012      "status_detail": "arrived_at_destination", #012      "tracking_location": {#012        "city": "CHARLESTON", #012        "country": null, #012        "object": "TrackingLocation", #012        "state": "SC", #012        "zip": "29407"#012      }#012    }#012  ], #012  "updated_at": "2017-10-08T15:41:00Z", #012  "weight": null#012}


def define_sendungsverfolgung(tracking_code_):
    sendungsverfolgung = []

    class Sendungsverfolgung(object):
        def __init__(self, date, time, location, content, trackingcode, supplier):
            self.date = date
            self.time = time
            self.location = location
            self.content = content
            self.trackingcode = trackingcode
            self.supplier = supplier

    headers = {
        'Authorization': 'ShippoToken shippo_live_0a020559d875b3cecd5bbbe04c3399794fe0aaab',
        'Content-Type': 'application/json',
    }

    r = requests.get('https://api.goshippo.com/tracks/dhl_germany/' + tracking_code_, headers=headers)

    try:

        tracking_history = json.loads(r.text)

        i = 0

        while i <= len(tracking_history["tracking_history"]) - 1:
            print(tracking_history["tracking_history"][i])
            year = tracking_history["tracking_history"][i]['object_created'][:4]
            month = tracking_history["tracking_history"][i]['object_created'][5:7]
            day = tracking_history["tracking_history"][i]['object_created'][8:10]
            time = tracking_history["tracking_history"][i]['object_created'][12:16]

            Monat = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober",
                     "November", "Dezember"]
            now_date = str(day) + ". " + str(Monat[int(month) - 1]) + " " + str(year)
            location = tracking_history["tracking_history"][i]['location']
            content = tracking_history["tracking_history"][i]['status_details']
            supplier = "DHL"
            trackingcode = tracking_code_

            if i == 0:
                location = ""
            sendungsverfolgung.append(Sendungsverfolgung(now_date, time, location, content, trackingcode, supplier, ))

            i = i + 1


    except:

        sendungsverfolgung.append(Sendungsverfolgung("", "", "", "", "", "", ))

    json_string = json.dumps([Sendungsverfolgung.__dict__ for Sendungsverfolgung in sendungsverfolgung])

    return json_string


def define_bewertung(session_key, gutscheincode_id, c):
    bewertungen = []

    class Bewertung(object):
        def __init__(self, bestellnummer, style, bewertung, bewertungstext, bewertungsdatum, gutscheincode_id):
            self.bestellnummer = bestellnummer
            self.style = style
            self.bewertung = bewertung
            self.bewertungstext = bewertungstext
            self.bewertungsdatum = bewertungsdatum
            self.gutscheincode_id = gutscheincode_id

    c.execute("""select * from userdaten where gutscheincode=%s """, (session_key,))

    userdaten = c.fetchall()

    for row in userdaten:
        c.execute("""select * from bewertungen """)
        for row_2 in c:
            if row_2[5] == gutscheincode_id:
                bewertungen.append(Bewertungen(row_2[0], row_2[1], row_2[2], row_2[3], row_2[4], row_2[5], ))

    json_string = json.dumps([Bewertungen.__dict__ for Bewertungen in bewertungen])

    return json_string


def get_tracking_number(session_key, bestellnummer, c):
    c.execute("""select * from userdaten where gutscheincode=%s """, (session_key,))
    userdaten = c.fetchall()
    tracking_code = ""

    for row in userdaten:
        c.execute("""select * from bestellt where gutscheincode=%s ORDER BY idforsorting DESC""", (row[11],))
        for row_2 in c:
            if row_2[21] == bestellnummer:
                tracking_code = row_2[30]

    return tracking_code


@csrf_exempt
def cart_data_sent_to_google_analytics(request):
    if request.is_ajax() and request.GET:
        bestellnummer = request.GET.get('bestellnummer')
        usercode = request.GET.get('usercode')
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2', \
                                       password='okano1988', database='maxfischer2database')

        c = conn.cursor(buffered=True)
        c.execute("""update %s set datasenttogoogleanalytics=%%s where bestellnummer=%%s and gutscheincode=%%s""" % (
        "bestellt"), ("ja", bestellnummer, usercode,))
        conn.commit()

    conn.close()

    return HttpResponse(json.dumps(""), content_type='application/json')


def define_bestellung(session_key, bestellnummer, c, transaction_id_ja_oder_nein):
    bestellung = []

    class Bestellung(object):
        def __init__(self, sessionidtablename, strasserechnung, hausnummerrechnung, stadtrechnung, plzrechnung,
                     landrechnung, anrederechnung, vornamerechnung, nachnamerechnung, telefonnummerrechnung,
                     zahlungsoption, namekarteninhaber, kartennummer, ablaufdatum, pruefnummer, bestellungspreis,
                     lieferkosten, rabatt, rabattcode, datum, uhrzeit, bestellnummer, creditused, status,
                     braforfreevalue, storecredit, braforfreecount, liefertermin, usercode, datasenttogoogleanalytics,
                     unternehmensdetailsrechnung, strasselieferadresse, hausnummerlieferadresse, stadtlieferadresse,
                     plzlieferadresse, landlieferadresse, anredelieferadresse, vornamelieferadresse,
                     nachnamelieferadresse, telefonnummerlieferadresse, unternehmensdetailslieferadresse,
                     transactionid):
            self.sessionidtablename = sessionidtablename
            self.strasserechnung = strasserechnung
            self.hausnummerrechnung = hausnummerrechnung
            self.stadtrechnung = stadtrechnung
            self.plzrechnung = plzrechnung
            self.landrechnung = landrechnung
            self.anrederechnung = anrederechnung
            self.vornamerechnung = vornamerechnung
            self.nachnamerechnung = nachnamerechnung
            self.telefonnummerrechnung = telefonnummerrechnung
            self.zahlungsoption = zahlungsoption
            self.namekarteninhaber = namekarteninhaber
            self.kartennummer = kartennummer
            self.ablaufdatum = ablaufdatum
            self.pruefnummer = pruefnummer
            self.bestellungspreis = bestellungspreis
            self.lieferkosten = lieferkosten
            self.rabatt = rabatt
            self.rabattcode = rabattcode
            self.datum = datum
            self.uhrzeit = uhrzeit
            self.bestellnummer = bestellnummer
            self.creditused = creditused
            self.status = status
            self.braforfreevalue = braforfreevalue
            self.storecredit = storecredit
            self.braforfreecount = braforfreecount
            self.liefertermin = liefertermin
            self.usercode = usercode
            self.datasenttogoogleanalytics = datasenttogoogleanalytics
            self.unternehmensdetailsrechnung = unternehmensdetailsrechnung
            self.strasselieferadresse = strasselieferadresse
            self.hausnummerlieferadresse = hausnummerlieferadresse
            self.stadtlieferadresse = stadtlieferadresse
            self.plzlieferadresse = plzlieferadresse
            self.landlieferadresse = landlieferadresse
            self.anredelieferadresse = anredelieferadresse
            self.vornamelieferadresse = vornamelieferadresse
            self.nachnamelieferadresse = nachnamelieferadresse
            self.telefonnummerlieferadresse = telefonnummerlieferadresse
            self.unternehmensdetailslieferadresse = unternehmensdetailslieferadresse
            self.transactionid = transactionid

    if session_key != "all":
        c.execute("""select * from userdaten where gutscheincode=%s """, (session_key,))

        userdaten = c.fetchall()

        for row in userdaten:
            if row[11] == session_key:
                c.execute("""select * from bestellt where gutscheincode=%s ORDER BY idforsorting DESC""", (row[11],))
                for row_2 in c:

                    if row_2[21] == bestellnummer or bestellnummer == "all":
                        if row_2[10] == "2":
                            try:
                                kartennummer_kurz = row_2[12]
                                kartennummer_kurz = kartennummer_kurz[15:]
                            except:
                                kartennummer_kurz = ""
                        else:
                            kartennummer_kurz = row_2[12]
                        if transaction_id_ja_oder_nein == "ja":
                            transaction_id = row_2[38]
                        else:
                            transaction_id = ""
                        bestellung.append(
                            Bestellung(row_2[0], row_2[1], row_2[2], row_2[3], row_2[4], row_2[5], row_2[6], row_2[7],
                                       row_2[8], row_2[9], row_2[10], row_2[11], kartennummer_kurz, row_2[13],
                                       row_2[14], row_2[15], row_2[16], row_2[17], row_2[18], row_2[19], row_2[20],
                                       row_2[21], row_2[22], row_2[24], row_2[27], row_2[28], row_2[26], row_2[29],
                                       row[11], row_2[39], row_2[40], row_2[41], row_2[42], row_2[43], row_2[44],
                                       row_2[45], row_2[46], row_2[47], row_2[48], row_2[49], row_2[50],
                                       transaction_id, ))
    else:

        try:
            c.execute("""select * from bestellt ORDER BY idforsorting DESC""")
            for row_2 in c:
                if row_2[21] == bestellnummer or bestellnummer == "all":
                    if row_2[10] == "2":
                        try:
                            kartennummer_kurz = row_2[12]
                            kartennummer_kurz = kartennummer_kurz[15:]
                        except:
                            kartennummer_kurz = ""
                    else:
                        kartennummer_kurz = row_2[12]
                    if transaction_id_ja_oder_nein == "ja":
                        transaction_id = row_2[38]
                    else:
                        transaction_id = ""
                    bestellung.append(
                        Bestellung(row_2[0], row_2[1], row_2[2], row_2[3], row_2[4], row_2[5], row_2[6], row_2[7],
                                   row_2[8], row_2[9], row_2[10], row_2[11], kartennummer_kurz, row_2[13], row_2[14],
                                   row_2[15], row_2[16], row_2[17], row_2[18], row_2[19], row_2[20], row_2[21],
                                   row_2[22], row_2[24], row_2[27], row_2[28], row_2[26], row_2[29], row_2[52],
                                   row_2[39], row_2[40], row_2[41], row_2[42], row_2[43], row_2[44], row_2[45],
                                   row_2[46], row_2[47], row_2[48], row_2[49], row_2[50], transaction_id, ))

        except:
            print("error: no bestellt_table")

    json_string = json.dumps([Bestellung.__dict__ for Bestellung in bestellung])

    return json_string


def define_zahlungsmethoden(session_key, c):
    zahlungsmethoden = []

    class Zahlungsmethoden(object):
        def __init__(self, email, indexnummer, zahlungsoption, name, kreditkartennummer, ablaufmonat, ablaufjahr,
                     standard, cardtype, zahlungsart, iban, bic):
            self.email = email
            self.indexnummer = indexnummer
            self.zahlungsoption = zahlungsoption
            self.name = name
            self.kreditkartennummer = kreditkartennummer
            self.ablaufmonat = ablaufmonat
            self.ablaufjahr = ablaufjahr
            self.standard = standard
            self.cardtype = cardtype
            self.zahlungsart = zahlungsart
            self.iban = iban
            self.bic = bic

    c.execute("""select * from userdaten where gutscheincode=%s """, (session_key,))

    userdaten = c.fetchall()

    for row in userdaten:
        c.execute("""select * from zahlungsmethoden where gutscheincode=%s """, (row[11],))
        for row_2 in c:
            if row_2[13] == "true" or row_2[14] == session_key:

                kredikartennummer = row_2[4]
                Monat_kurz = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
                try:
                    monat = Monat_kurz[int(row_2[5]) - 1]
                except:
                    monat = ""
                zahlungsmethoden.append(
                    Zahlungsmethoden(row_2[0], row_2[1], row_2[2], row_2[3], kredikartennummer, monat, row_2[6],
                                     row_2[8], row_2[9], row_2[10], row_2[11], row_2[12], ))

    json_string = json.dumps([Zahlungsmethoden.__dict__ for Zahlungsmethoden in zahlungsmethoden])

    return json_string


def define_standard_lieferadresse(session_key, c):
    standard_land = "Deutschland"
    c.execute("""select * from adressbuch where gutscheincode=%s and standardlieferadresse=%s""", (session_key, "ja",))
    for row in c:
        standard_land = row[12]

    return standard_land


def define_adressbuch(session_key, c):
    adressbuch = []

    class Adressbuch(object):
        def __init__(self, email, indexnummer, vorname, nachname, telefonnummer, strasse, apt, unternehmensdetails,
                     stadt, plz, anrede, standard_rechnungsadresse, land, hausnummer, standard_lieferadresse):
            self.email = email
            self.indexnummer = indexnummer
            self.vorname = vorname
            self.nachname = nachname
            self.telefonnummer = telefonnummer
            self.strasse = strasse
            self.apt = apt
            self.unternehmensdetails = unternehmensdetails
            self.stadt = stadt
            self.plz = plz
            self.anrede = anrede
            self.standard_rechnungsadresse = standard_rechnungsadresse
            self.land = land
            self.hausnummer = hausnummer
            self.standard_lieferadresse = standard_lieferadresse

    c.execute("""select * from adressbuch where gutscheincode=%s ORDER BY standard ASC""", (session_key,))
    for row_2 in c:
        adressbuch.append(
            Adressbuch(row_2[0], row_2[1], row_2[2], row_2[3], row_2[4], row_2[5], row_2[6], row_2[7], row_2[8],
                       row_2[9], row_2[10], row_2[11], row_2[12], row_2[13], row_2[14]))

    json_string = json.dumps([Adressbuch.__dict__ for Adressbuch in adressbuch])

    return json_string


def define_profil(session_key, c):
    profil = []

    class Profil(object):
        def __init__(self, email, vorname, nachname, lastplz, telefon, lastsessionid, credit, gutscheincode, facebookid,
                     passwordcheck, persmsbenachrichtigtwerden, newsletter):
            self.email = email
            self.vorname = vorname
            self.nachname = nachname
            self.lastplz = lastplz
            self.telefon = telefon
            self.lastsessionid = lastsessionid
            self.credit = credit
            self.gutscheincode = gutscheincode
            self.facebookid = facebookid
            self.passwordcheck = passwordcheck
            self.persmsbenachrichtigtwerden = persmsbenachrichtigtwerden
            self.newsletter = newsletter

    c.execute("""select * from userdaten where gutscheincode=%s """, (session_key,))
    userdaten = c.fetchall()
    password = "ok"
    for row in userdaten:
        password = "ok"
        if row[1] == "":
            password = "not ok"

        profil.append(
            Profil(row[0], row[2], row[3], row[5], row[8], row[9], row[10], row[11], row[12], password, row[20],
                   row[49], ))

    json_string = json.dumps([Profil.__dict__ for Profil in profil])

    return json_string


@csrf_exempt
def kollektion_abrufen(request):
    if request.is_ajax() and request.GET:
        group = request.GET.get('group')
        link = request.GET.get('link')
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2', \
                                       password='okano1988', database='maxfischer2database')

        c = conn.cursor(buffered=True)
        if link == "Mein Showroom":
            page = link_name_bestimmen("no")
        else:
            page = link_name_bestimmen(group)

    conn.close()

    return HttpResponse(json.dumps(page), content_type='application/json')


class Me(object):
    def __init__(self):
        self.name = 1
        self.nachname = 2


def freunde_einladen(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2', \
                                   password='okano1988', database='maxfischer2database')
    c = conn.cursor(buffered=True)

    request.session.create()
    x = str(request.session.session_key)
    create_user(x, c, conn)

    gutscheincode = request.GET.get('gutscheincode')
    print(gutscheincode)
    VIP = "Regular"
    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        userdaten = c.fetchall()
        for row in userdaten:
            user = row[11]
            modelAB = row[47]
            sub_picture = row[48]
            neukunde = row[57]
            if row[22] == "VIP":
                VIP = row[22]

    gutschein_einloesen_do_it(user, gutscheincode, "einloesen", c, conn, neukunde, VIP, user)

    conn.close()

    return HttpResponseRedirect("/")


@csrf_exempt
def anmeldung_bestaetigen(request, offset):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2', \
                                   password='okano1988', database='maxfischer2database')
    c = conn.cursor(buffered=True)

    x = str(request.session.session_key)

    login = "false"
    status = 0
    modelAB = ""
    sub_picture = ""
    user = ""

    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        for row in c:
            status = 1
            wishlist = row[65]
            bereitsbestellt = row[75]
            bereitsversandt = row[76]
            warenkorb = row[66]
            email = row[0]
            user = row[11]
            vorname = row[2]
            nachname = row[3]
            default_bra_size = row[58]
            default_panty_size = row[59]
            facebookid = row[12]
            quiz = row[26]
            stadt = row[6]
            plz = row[4]
            modelAB = row[47]
            sub_picture = row[48]
            wishlist_quantity = row[16]
            cart_quantity = row[17]
            if (row[0] != "" and row[12] != "") or (row[0] != "" and row[1] != ""):
                login = "true"
            if row[22] == "VIP" and row[23] == "true":
                VIP = "VIP"
            else:
                VIP = "Regular"

    if status == 0:
        if x != "None":
            x = str(request.session.session_key)
            create_user(x, c, conn)
        else:
            print(request.path + ",create_new_request," + x)
            log_out_do_it(x, c, conn)
            request.session.create()
            x = str(request.session.session_key)
            create_user(x, c, conn)

        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            for row in c:
                wishlist = row[65]
                bereitsbestellt = row[75]
                bereitsversandt = row[76]
                warenkorb = row[66]
                email = row[0]
                user = row[11]
                vorname = row[2]
                nachname = row[3]
                default_bra_size = row[58]
                default_panty_size = row[59]
                facebookid = row[12]
                quiz = row[26]
                stadt = row[6]
                plz = row[4]
                modelAB = row[47]
                sub_picture = row[48]
                wishlist_quantity = row[16]
                cart_quantity = row[17]
                if row[22] == "VIP" and row[23] == "true":
                    VIP = "VIP"
                else:
                    VIP = "Regular"

    if user != "":
        bestellungen = define_bestellung(user, "all", c, "nein")

        url = get_link_positioining("")
        links = get_links(quiz)

        t = get_template('anmeldung_bestaetigen.html')
        title = ("Anmeldung bestätigen | Darling Lace").decode('windows-1252')

        description_header = (
        "BHs und BH Sets für jede Größe und Brustform. Wir bieten lingerie in einer großen Auswahl an Farben an. Hochwertige Unterwäsche für Frauen günstig kaufen. BHs in vielen Designs, basic, sexy und bequeme BHs. Auf Rechnung kaufen mit 30 Tage Rückgaberecht. Kostenloser Versand.").encode(
            'utf8')
        html = t.render({'description_header': description_header,
                         'user_id_google_analytics': get_google_analytics_user_id(login, user), 'email': email,
                         'bereitsbestellt': bereitsbestellt, 'bereitsversandt': bereitsversandt,
                         'fb_link': 'https://www.darlinglace.com',
                         'fb_title': ("Liebst du Lingerie? Erhalte Dein BH Set ab 29,95 EUR!").encode('utf8'),
                         'fb_description': (
                         "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                             'utf8'), 'fb_description': (
            "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                'utf8'), 'fb_image': 'https://www.darlinglace.com/static/overall_picture_bra.jpg', 'vorname': vorname,
                         'nachname': nachname, 'stadt': stadt, 'plz': plz, 'wishlist': wishlist, 'warenkorb': warenkorb,
                         'security_key': offset, 'favicon': get_favicon(), 'path': request.path,
                         'brand_name': 'Darling Lace', 'lingerie_offerings': '', 'title': title,
                         'bestellungen': bestellungen, 'wishlist': wishlist, 'warenkorb': warenkorb, 'login': login,
                         'url': url, 'links': links})
        conn.close()
        return HttpResponse(html)
    else:
        conn.close()
        return HttpResponseRedirect("/")


def newsletter_abmelden_page(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2', \
                                   password='okano1988', database='maxfischer2database')
    c = conn.cursor(buffered=True)

    x = str(request.session.session_key)

    login = "false"
    status = 0
    modelAB = ""
    sub_picture = ""
    user = ""

    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        for row in c:
            status = 1
            wishlist = row[65]
            bereitsbestellt = row[75]
            bereitsversandt = row[76]
            warenkorb = row[66]
            email = row[0]
            user = row[11]
            vorname = row[2]
            nachname = row[3]
            default_bra_size = row[58]
            default_panty_size = row[59]
            facebookid = row[12]
            quiz = row[26]
            stadt = row[6]
            plz = row[4]
            modelAB = row[47]
            sub_picture = row[48]
            wishlist_quantity = row[16]
            cart_quantity = row[17]
            if (row[0] != "" and row[12] != "") or (row[0] != "" and row[1] != ""):
                login = "true"
            if row[22] == "VIP" and row[23] == "true":
                VIP = "VIP"
            else:
                VIP = "Regular"

    if status == 0:
        if x != "None":
            x = str(request.session.session_key)
            create_user(x, c, conn)
        else:
            print(request.path + ",create_new_request," + x)
            log_out_do_it(x, c, conn)
            request.session.create()
            x = str(request.session.session_key)
            create_user(x, c, conn)

        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            for row in c:
                wishlist = row[65]
                bereitsbestellt = row[75]
                bereitsversandt = row[76]
                warenkorb = row[66]
                email = row[0]
                user = row[11]
                vorname = row[2]
                nachname = row[3]
                default_bra_size = row[58]
                default_panty_size = row[59]
                facebookid = row[12]
                quiz = row[26]
                stadt = row[6]
                plz = row[4]
                modelAB = row[47]
                sub_picture = row[48]
                wishlist_quantity = row[16]
                cart_quantity = row[17]
                if row[22] == "VIP" and row[23] == "true":
                    VIP = "VIP"
                else:
                    VIP = "Regular"

    security_key = request.GET.get('security_key')
    if user != "":
        bestellungen = define_bestellung(user, "all", c, "nein")

        url = get_link_positioining("")
        links = get_links(quiz)

        t = get_template('newsletter_abmelden.html')
        title = ("Newsletter abmelden | Darling Lace").decode('windows-1252')

        description_header = (
        "BHs und BH Sets für jede Größe und Brustform. Wir bieten lingerie in einer großen Auswahl an Farben an. Hochwertige Unterwäsche für Frauen günstig kaufen. BHs in vielen Designs, basic, sexy und bequeme BHs. Auf Rechnung kaufen mit 30 Tage Rückgaberecht. Kostenloser Versand.").encode(
            'utf8')
        html = t.render({'security_key': security_key, 'description_header': description_header,
                         'user_id_google_analytics': get_google_analytics_user_id(login, user), 'email': email,
                         'bereitsbestellt': bereitsbestellt, 'bereitsversandt': bereitsversandt,
                         'fb_link': 'https://www.darlinglace.com',
                         'fb_title': ("Liebst du Lingerie? Erhalte Dein BH Set ab 29,95 EUR!").encode('utf8'),
                         'fb_description': (
                         "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                             'utf8'), 'fb_description': (
            "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                'utf8'), 'fb_image': 'https://www.darlinglace.com/static/overall_picture_bra.jpg', 'vorname': vorname,
                         'nachname': nachname, 'stadt': stadt, 'plz': plz, 'wishlist': wishlist, 'warenkorb': warenkorb,
                         'favicon': get_favicon(), 'path': request.path, 'brand_name': 'Darling Lace',
                         'lingerie_offerings': '', 'title': title, 'bestellungen': bestellungen, 'wishlist': wishlist,
                         'warenkorb': warenkorb, 'login': login, 'url': url, 'links': links})
        conn.close()
        return HttpResponse(html)
    else:
        conn.close()
        return HttpResponseRedirect("/")


@csrf_exempt
def passwort_vergessen_bestaetigen(request, offset):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2', \
                                   password='okano1988', database='maxfischer2database')
    c = conn.cursor(buffered=True)

    x = str(request.session.session_key)

    login = "false"
    status = 0
    modelAB = ""
    sub_picture = ""
    user = ""

    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        for row in c:
            status = 1
            bereitsbestellt = row[75]
            bereitsversandt = row[76]
            wishlist = row[65]
            warenkorb = row[66]
            email = row[0]
            user = row[11]
            vorname = row[2]
            nachname = row[3]
            default_bra_size = row[58]
            default_panty_size = row[59]
            facebookid = row[12]
            quiz = row[26]
            stadt = row[6]
            plz = row[4]
            modelAB = row[47]
            sub_picture = row[48]
            wishlist_quantity = row[16]
            cart_quantity = row[17]
            if (row[0] != "" and row[12] != "") or (row[0] != "" and row[1] != ""):
                login = "true"
            if row[22] == "VIP" and row[23] == "true":
                VIP = "VIP"
            else:
                VIP = "Regular"

    if status == 0:
        if x != "None":
            x = str(request.session.session_key)
            create_user(x, c, conn)
        else:
            print(request.path + ",create_new_request," + x)
            log_out_do_it(x, c, conn)
            request.session.create()
            x = str(request.session.session_key)
            create_user(x, c, conn)

        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            for row in c:
                wishlist = row[65]
                bereitsbestellt = row[75]
                bereitsversandt = row[76]
                warenkorb = row[66]
                email = row[0]
                user = row[11]
                vorname = row[2]
                nachname = row[3]
                default_bra_size = row[58]
                default_panty_size = row[59]
                facebookid = row[12]
                quiz = row[26]
                stadt = row[6]
                plz = row[4]
                modelAB = row[47]
                sub_picture = row[48]
                wishlist_quantity = row[16]
                cart_quantity = row[17]
                if row[22] == "VIP" and row[23] == "true":
                    VIP = "VIP"
                else:
                    VIP = "Regular"

    if user != "":

        bestellungen = define_bestellung(user, "all", c, "nein")
        url = get_link_positioining("")
        links = get_links(quiz)

        t = get_template('passwort_vergessen.html')
        description_header = (
        "BHs und BH Sets für jede Größe und Brustform. Wir bieten lingerie in einer großen Auswahl an Farben an. Hochwertige Unterwäsche für Frauen günstig kaufen. BHs in vielen Designs, basic, sexy und bequeme BHs. Auf Rechnung kaufen mit 30 Tage Rückgaberecht. Kostenloser Versand.").encode(
            'utf8')

        html = t.render({'description_header': description_header,
                         'user_id_google_analytics': get_google_analytics_user_id(login, user), 'email': email,
                         'bereitsbestellt': bereitsbestellt, 'bereitsversandt': bereitsversandt,
                         'fb_link': 'https://www.darlinglace.com',
                         'fb_title': ("Liebst du Lingerie? Erhalte Dein BH Set ab 29,95 EUR!").encode('utf8'),
                         'fb_description': (
                         "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                             'utf8'), 'fb_description': (
            "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                'utf8'), 'fb_image': 'https://www.darlinglace.com/static/overall_picture_bra.jpg', 'vorname': vorname,
                         'nachname': nachname, 'stadt': stadt, 'plz': plz, 'wishlist': wishlist, 'warenkorb': warenkorb,
                         'security_key': offset, 'favicon': get_favicon(), 'path': request.path,
                         'brand_name': 'Darling Lace', 'lingerie_offerings': '', 'title': "Home | Darling Lace",
                         'bestellungen': bestellungen, 'wishlist': wishlist, 'warenkorb': warenkorb, 'login': login,
                         'url': url, 'links': links})
        conn.close()
        return HttpResponse(html)
    else:
        conn.close()
        return HttpResponseRedirect("/")


@csrf_exempt
def passwort_vergessen_page(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2', \
                                   password='okano1988', database='maxfischer2database')
    c = conn.cursor(buffered=True)

    x = str(request.session.session_key)

    login = "false"
    status = 0
    modelAB = ""
    sub_picture = ""
    user = ""

    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        for row in c:
            status = 1
            wishlist = row[65]
            bereitsbestellt = row[75]
            bereitsversandt = row[76]
            warenkorb = row[66]
            email = row[0]
            user = row[11]
            vorname = row[2]
            nachname = row[3]
            default_bra_size = row[58]
            default_panty_size = row[59]
            facebookid = row[12]
            quiz = row[26]
            stadt = row[6]
            plz = row[4]
            modelAB = row[47]
            sub_picture = row[48]
            wishlist_quantity = row[16]
            cart_quantity = row[17]
            if (row[0] != "" and row[12] != "") or (row[0] != "" and row[1] != ""):
                login = "true"
            if row[22] == "VIP" and row[23] == "true":
                VIP = "VIP"
            else:
                VIP = "Regular"

    if status == 0:
        if x != "None":
            x = str(request.session.session_key)
            create_user(x, c, conn)
        else:
            print(request.path + ",create_new_request," + x)
            log_out_do_it(x, c, conn)
            request.session.create()
            x = str(request.session.session_key)
            create_user(x, c, conn)

        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            for row in c:
                wishlist = row[65]
                bereitsbestellt = row[75]
                bereitsversandt = row[76]
                warenkorb = row[66]
                email = row[0]
                user = row[11]
                vorname = row[2]
                nachname = row[3]
                default_bra_size = row[58]
                default_panty_size = row[59]
                facebookid = row[12]
                quiz = row[26]
                stadt = row[6]
                plz = row[4]
                modelAB = row[47]
                sub_picture = row[48]
                wishlist_quantity = row[16]
                cart_quantity = row[17]
                if row[22] == "VIP" and row[23] == "true":
                    VIP = "VIP"
                else:
                    VIP = "Regular"

    if user != "":

        url = get_link_positioining("")
        links = get_links(quiz)

        t = get_template('passwort_vergessen_beantragen.html')

        description_header = (
        "BHs und BH Sets für jede Größe und Brustform. Wir bieten lingerie in einer großen Auswahl an Farben an. Hochwertige Unterwäsche für Frauen günstig kaufen. BHs in vielen Designs, basic, sexy und bequeme BHs. Auf Rechnung kaufen mit 30 Tage Rückgaberecht. Kostenloser Versand.").encode(
            'utf8')
        html = t.render({'description_header': description_header,
                         'user_id_google_analytics': get_google_analytics_user_id(login, user), 'email': email,
                         'bereitsbestellt': bereitsbestellt, 'bereitsversandt': bereitsversandt,
                         'fb_link': 'https://www.darlinglace.com',
                         'fb_title': ("Liebst du Lingerie? Erhalte Dein BH Set ab 29,95 EUR!").encode('utf8'),
                         'fb_description': (
                         "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                             'utf8'), 'fb_description': (
            "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                'utf8'), 'fb_image': 'https://www.darlinglace.com/static/overall_picture_bra.jpg', 'vorname': vorname,
                         'nachname': nachname, 'stadt': stadt, 'plz': plz, 'favicon': get_favicon(),
                         'path': request.path, 'brand_name': 'Darling Lace',
                         'title': "Passwort vergessen | Darling Lace", 'wishlist': wishlist, 'warenkorb': warenkorb,
                         'login': login, 'url': get_link_positioining(""), 'links': get_links(quiz)})
        conn.close()
        return HttpResponse(html)

    else:
        conn.close()
        return HttpResponseRedirect("/")


@csrf_exempt
def passwort_aendern_passwort_vergessen(request):
    if request.is_ajax() and request.POST:

        security_key = request.POST.get('security_key')
        neues_passwort = request.POST.get('neues_passwort')

        neues_passwort = hashlib.sha512(neues_passwort).hexdigest()

        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2', \
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)

        x = str(request.session.session_key)

        c.execute("""select * from security_keys """)
        feedback = "not ok"
        security_keys = c.fetchall()
        for row in security_keys:

            if row[0] == security_key:

                c.execute("""select * from userdaten where gutscheincode=%s """, (row[1],))
                userdaten = c.fetchall()
                for row_2 in userdaten:
                    if row_2[11] == row[1]:
                        c.execute("""update userdaten set passwort=%s where gutscheincode=%s""",
                                  (neues_passwort, row[1],))
                        c.execute("""delete from security_keys where securitykey=%s""", (security_key,))
                        conn.commit()
                        feedback = "ok"

        conn.close()
        return HttpResponse(json.dumps(feedback), content_type='application/json')
    else:
        raise Http404


def create_shippment_for_ruecksendung(bestellung, usercode, c, conn):
    easypost.api_key = 'OZVgLVsYx7ik768m3wApeQ'


def test_email(request):
    address_from = {}
    address_from['name'] = 'Maximilian Fischer'
    address_from['street1'] = 'Lindwurmstrasse 99'
    address_from['city'] = 'Munich'
    address_from['state'] = 'Munich'
    address_from['zip'] = '80337'
    address_from['country'] = 'DE'

    json_data_address_from = json.dumps(address_from)

    address_to = {}
    address_to['name'] = 'Maximilian Fischer'
    address_to['street1'] = 'Chausseestrasse 60'
    address_to['city'] = 'Berlin'
    address_to['state'] = 'Berlin'
    address_to['zip'] = '10115'
    address_to['country'] = 'DE'
    json_data_address_to = json.dumps(address_to)

    parcels = {}
    parcels['length'] = '30'
    parcels['width'] = '30'
    parcels['height'] = '30'
    parcels['distance_unit'] = 'cm'
    parcels['weight'] = '1'
    parcels['mass_unit'] = 'KG'

    json_data_parcels = json.dumps(parcels)

    #    myheaders = {'address_from':json_data_address_from,'address_to':json_data_address_to,'parcels':json_data_parcels,'Authorization': 'ShippoToken shippo_live_0a020559d875b3cecd5bbbe04c3399794fe0aaab','label_file_type':'PDF','async':'false'}
    #
    #    r =requests.get('https://api.goshippo.com/shipments/', headers=myheaders)
    #
    #
    #    print(json.loads(r.text))

    headers = {
        'Authorization': 'ShippoToken shippo_live_0a020559d875b3cecd5bbbe04c3399794fe0aaab',
        'Content-Type': 'application/json',
    }

    data = '{\n        "shipment": {\n            "address_from": {\n                "name": "Mr. Max Fischer",\n                "street1": "Chausseestrasse",\n                "street_no": "60",\n                "city": "Berlin",\n                "state": "Berlin",\n                "zip": "10115",\n                "country": "DE",\n                "phone": "+1 555 341 9393",\n                "email": "support@goshippo.com"\n            },\n            "address_to": {\n                "name": "Mr. Kai Fischer",\n                "street1": "Chausseestrasse",\n                "street_no": "100",\n                "city": "Berlin",\n                "state": "Berlin",\n                "zip": "10115",\n                "country": "DE",\n                "phone": "+1 555 341 9393",\n                "email": "support@goshippo.com"\n            },\n            "parcels": [{\n                "length": "30",\n                "width": "30",\n                "height": "30",\n                "distance_unit": "cm",\n                "weight": "1",\n                "mass_unit": "kg"\n            }]\n        },\n        "carrier_account": "cb1b1dc329f84031a71a385297f0a796",\n        "servicelevel_token": "dhl_germany_paket"\n        }'

    r = requests.post('https://api.goshippo.com/transactions/', headers=headers, data=data)

    t = get_template('impressum.html')

    html = t.render({'shippo_data': json.loads(r.text)})

    return HttpResponse(html)


#    headers = {
#        'Authorization': 'ShippoToken shippo_live_0a020559d875b3cecd5bbbe04c3399794fe0aaab',
#    }
#
#    data = [
#      ('label_file_type', 'PDF\n'),
#      ('async', 'false'),
#    ]
#
#    requests.post('https://api.goshippo.com/transactions', headers=headers, data=data)
#
#    json_data=json.loads(r.text)
#    print(json_data)
#    json_data_2=json_data["label_url"]
#    print(json_data_2)
#    print(json_data["ratesaa"])


def create_shippment_for_delivery(bestellung, usercode, c, conn):
    headers = {
        'Authorization': 'ShippoToken shippo_live_0a020559d875b3cecd5bbbe04c3399794fe0aaab',
        'Content-Type': 'application/json',
    }

    table_country_code = {'Deutschland': 'DE',
                          'deutschland': 'DE',
                          'Germany': 'DE',
                          'germany': 'DE',
                          'Oesterreich': 'AT',
                          'oesterreich': 'AT',
                          'Österreich': 'AT',
                          'österreich': 'AT',
                          'Schweiz': 'CH',
                          'schweiz': 'CH',
                          'Switzerland': 'CH',
                          'switzerland': 'CH',

                          }

    name_to = bestellung[0]['anredelieferadresse'] + " " + bestellung[0]['vornamelieferadresse'] + " " + bestellung[0][
        'nachnamelieferadresse']
    street1_to = bestellung[0]['strasselieferadresse']
    street_no_to = bestellung[0]['hausnummerlieferadresse']
    city_to = bestellung[0]['stadtlieferadresse']
    zip_to = bestellung[0]['plzlieferadresse']
    country_to = table_country_code[bestellung[0]['landlieferadresse']]
    phone_to = bestellung[0]['telefonnummerlieferadresse']
    email_to = ""

    name_from = "Darling Lace GmbH"
    street1_from = "Wilhelmine-Gemberg-Weg"
    street_no_from = "3"
    city_from = "Berlin"
    zip_from = "10179"
    country_from = "DE"
    phone_from = "015154707511"
    email_from = "service@darlinglace.com"

    address_from = {'name': 'Darling Lace GmbH', 'street1': 'Wilhelmine-Gemberg-Weg', 'street_no': '3',
                    'city': 'Berlin', 'zip': '10179', 'country': 'DE', 'phone': '015154707511',
                    'email': 'service@darlinglace.com'}
    address_to = {'name': name_to, 'street1': street1_to, 'street_no': street_no_to, 'city': city_to, 'zip': zip_to,
                  'country': country_to, 'phone': phone_to, 'email': ''}
    #    addresses_combined={'address_from':address_from,'address_to':address_to,'pacels':'['+pacels+']'}
    parcels = []
    parcels.append(
        {'length': '30', 'width': '23', 'height': '11', 'distance_unit': 'cm', 'weight': '1', 'mass_unit': 'kg'})
    addresses_combined = {'address_from': address_from, 'address_to': address_to, 'parcels': parcels}
    data = {'shipment': addresses_combined, 'carrier_account': 'cb1b1dc329f84031a71a385297f0a796',
            'servicelevel_token': 'dhl_germany_paket'}
    data = json.dumps(data)

    #   data = '{"shipment":{"address_from": {"name": "Mr. Max Fischer","street1": "Chausseestrasse","street_no": "60","city": "Berlin","zip": "10115","country": "DE","phone": "01607448195","email": "maximilian.fischer@whu.edu"},"address_to": {"name": "Mr. Kai Fischer","street1": "Chausseestrasse","street_no": "100","city": "Berlin","zip": "10115","country": "DE","phone": "+1 555 341 9393","email": "support@goshippo.com"},"parcels": [{"length": "30","width": "30","height": "30","distance_unit": "cm","weight": "1","mass_unit": "kg"}]},"carrier_account": "cb1b1dc329f84031a71a385297f0a796","servicelevel_token": "dhl_germany_paket"}'
    print(data)
    r = requests.post('https://api.goshippo.com/transactions/', headers=headers, data=data)

    #    data = """{\n        "shipment": {"address_from": {"name": """+name_from+""",\n                "street1": "Chausseestrasse",\n                "street_no": "60",\n                "city": "Berlin",\n                "state": "Berlin",\n                "zip": "10115",\n                "country": "DE",\n                "phone": "+1 555 341 9393",\n                "email": "support@goshippo.com"\n            },\n            "address_to": {\n                "name": "Mr. Kai Fischer",\n                "street1": "Chausseestrasse",\n                "street_no": "100",\n                "city": "Berlin",\n                "state": "Berlin",\n                "zip": "10115",\n                "country": "DE",\n                "phone": "+1 555 341 9393",\n                "email": "support@goshippo.com"\n            },\n            "parcels": [{\n                "length": "30",\n                "width": "30",\n                "height": "30",\n                "distance_unit": "cm",\n                "weight": "1",\n                "mass_unit": "kg"\n            }]\n        },\n        "carrier_account": "cb1b1dc329f84031a71a385297f0a796",\n        "servicelevel_token": "dhl_germany_paket"\n        }"""

    #    r=requests.post('https://api.goshippo.com/transactions/', headers=headers, data=data)
    #    print(r)

    feedback = json.loads(r.text)

    tracking_number = feedback["tracking_number"]
    sippo_object_id = feedback["object_id"]

    r = requests.get('https://api.goshippo.com/transactions/' + sippo_object_id, headers=headers)

    feedback2 = json.loads(r.text)

    print(feedback2)

    tracking_label = feedback2["label_url"]

    #    tracking_number="00340434195551200150"

    #    r=requests.get('https://api.goshippo.com/tracks/dhl_germany/'+tracking_number, headers=headers)

    #    tracking_history=json.loads(r.text)
    #    print(tracking_history["tracking_history"])
    #    print(tracking_history["tracking_history"][0])
    #    print(json.loads(r.text))

    c.execute(
        """update %s set trackingcodeversand=%%s,versandsupplier=%%s,versandlabellink=%%s,shippoobjectid=%%s where bestellnummer=%%s and gutscheincode=%%s""" % (
        "bestellt"),
        (tracking_number, "DHL", tracking_label, sippo_object_id, bestellung[0]['bestellnummer'], usercode,))
    conn.commit()


@csrf_exempt
def bestellung_versenden(request):
    if request.is_ajax() and request.POST:

        bestellnummer = request.POST.get('bestellnummer')
        usercode = request.POST.get('usercode')
        liefertermin = request.POST.get('liefertermin')

        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2', \
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)

        x = str(request.session.session_key)

        c.execute("""select * from userdaten """)
        userdaten = c.fetchall()
        for row in userdaten:
            if row[11] == usercode:

                bestellung = define_bestellung(row[11], bestellnummer, c, "ja")

                bestellung = json.loads(bestellung)

                print bestellung[0]
                print bestellung[0]["transactionid"]
                c.execute("""update %s set bestellungversandt=%%s where gutscheincode=%%s""" % ("userdaten"),
                          ("yes", row[11],))

                if bestellung[0]["zahlungsoption"] == "4":
                    feedback_klarna = activate_klarna_rechnung(bestellung[0]["transactionid"])
                    if feedback_klarna != "not ok":
                        c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s)""" % ("rechnungsnummer"), (
                        id_generator("rechnungsnummer", c, conn), bestellnummer, usercode, "", "", feedback_klarna,))
                        create_shippment_for_delivery(bestellung, row[11], c, conn)
                        change_lieferstatus(bestellnummer, usercode, "Versandt", liefertermin, c, conn, feedback_klarna)
                        c.execute("""insert into shipping_confirmation_emails values (%s,%s,%s,%s,%s,%s,%s)""", (
                        bestellnummer, row[11], row[0],
                        "Deine Darling Lace Bestellung wurde veschickt (#" + bestellnummer,
                        get_tracking_number(usercode, bestellnummer, c) + ")", "nein", "no",))
                        conn.commit()
                        status = "Versandt"
                    else:
                        status = "Bezahlung durch klarna abgelehnt"



                else:
                    c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s)""" % ("rechnungsnummer"),
                              (id_generator("rechnungsnummer", c, conn), bestellnummer, usercode, "", "", "",))
                    create_shippment_for_delivery(bestellung, row[11], c, conn)
                    change_lieferstatus(bestellnummer, usercode, "Versandt", liefertermin, c, conn, "")
                    c.execute("""insert into shipping_confirmation_emails values (%s,%s,%s,%s,%s,%s,%s)""", (
                    bestellnummer, row[11], row[0], "Deine Darling Lace Bestellung wurde veschickt (#" + bestellnummer,
                    get_tracking_number(usercode, bestellnummer, c) + ")", "nein", "no",))
                    conn.commit()
                    status = "Versandt"

        conn.close()

        return HttpResponse(json.dumps(status), content_type='application/json')
    else:
        raise Http404


def activate_klarna_rechnung(transaction_id_klarna):
    config = klarna.Config(
        eid=70492,
        secret='VzRcsRPkLIF4qrT',
        country='DE',
        language='DE',
        currency='EUR',
        mode='live',
        pcstorage='json',
        pcuri='/srv/pclasses.json',
        scheme='https',
        candice=True)

    k = klarna.Klarna(config)
    k.init()

    print("transaction_id_klarna")

    oder_activation = k.activate(transaction_id_klarna, flags=8)

    status = oder_activation[0]
    invoice_number = oder_activation[1]

    print status
    print invoice_number
    if status == "ok":
        return str(invoice_number)
    else:
        return "not ok"


def refund_klarna_rechnung(transaction_id_klarna, refund_amount, return_number, invoice_number):
    config = klarna.Config(
        eid=70492,
        secret='VzRcsRPkLIF4qrT',
        country='DE',
        language='DE',
        currency='EUR',
        mode='live',
        pcstorage='json',
        pcuri='/srv/pclasses.json',
        scheme='https',
        candice=True)

    k = klarna.Klarna(config)
    k.init()

    print(transaction_id_klarna)

    oder_activation = k.return_amount(
        invoice_number,
        amount=float(refund_amount),
        vat=19,
        description="Stornorechnung zu Ruecksendenummer: " + return_number)

    print(oder_activation)

    return oder_activation


def change_lieferstatus(bestellnummer, usercode, status, liefertermin, c, conn, klarna_invoicenumber):
    c.execute("""select * from bestellt where gutscheincode=%s """, (usercode,))
    bestellt_daten = c.fetchall()

    for row_2 in bestellt_daten:
        if row_2[21] == bestellnummer:
            c.execute("""update %s set status=%%s where bestellnummer=%%s""" % ("cart_details"),
                      ("Versandt", row_2[21],))

    conn.commit()

    print status
    print bestellnummer
    print usercode
    if liefertermin != "":
        c.execute(
            """update %s set status=%%s,lieferdatum=%%s, invoicenumberklarna=%%s where bestellnummer=%%s and gutscheincode=%%s""" % (
            "bestellt"), (status, liefertermin, klarna_invoicenumber, bestellnummer, usercode))
    else:
        c.execute("""update bestellt set status=%s where bestellnummer=%s and gutscheincode=%s""",
                  (status, bestellnummer, usercode,))
    conn.commit()


def get_versandettiket(usercode, bestellnummer, c):
    c.execute("""select * from userdaten """)

    userdaten = c.fetchall()

    versandettiket_link = ""
    for row in userdaten:
        if row[11] == usercode:

            c.execute("""select * from bestellt where gutscheincode=%s ORDER BY idforsorting DESC""", (row[11],))
            for row_2 in c:
                if row_2[21] == bestellnummer:
                    versandettiket_link = row_2[32]

    return versandettiket_link


@csrf_exempt
def versandettikett_drucken(request):
    if request.is_ajax() and request.POST:

        bestellnummer = request.POST.get('bestellnummer')
        usercode = request.POST.get('usercode')

        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2', \
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)

        x = str(request.session.session_key)

        c.execute("""select * from userdaten """)
        userdaten = c.fetchall()
        versandettiket = ""
        for row in userdaten:
            if row[11] == usercode:
                versandettiket = get_versandettiket(usercode, bestellnummer, c)
        conn.close()

        return HttpResponse(json.dumps(versandettiket), content_type='application/json')
    else:
        raise Http404


@csrf_exempt
def request_passwort_vergessen(request):
    if request.is_ajax() and request.POST:

        email = request.POST.get('email')

        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2', \
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)

        x = str(request.session.session_key)
        email = email.lower()
        c.execute("""select * from userdaten where email=%s """, (email,))
        userdaten = c.fetchall()
        for row_2 in userdaten:
            if row_2[0] == email:
                security_code = id_generator_long()

                current_time = datetime.datetime.now(pytz.timezone('Europe/Berlin')).time()
                now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
                date_ = str(now.year) + str((now.month) - 1) + str(now.day)
                time_ = str(current_time)
                time__ = time_.replace(":", "")
                time__ = time__.replace(".", "")

                c.execute("""insert into security_keys values (%s,%s,%s,%s)""",
                          (security_code, row_2[11], date_, time__))
                c.execute("""insert into email_passwort_zuruecksetzen values (%s,%s,%s,%s,%s)""",
                          (email, security_code, "nein", row_2[11], "no",))

                conn.commit()

        conn.close()
        return HttpResponse(json.dumps("ok"), content_type='application/json')
    else:
        raise Http404


def email_adresse_bestaetigen_versand_email(email, c, conn, ip_adresse, user):
    current_time = datetime.datetime.now(pytz.timezone('Europe/Berlin')).time()
    now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
    date_ = str(now.year) + str((now.month) - 1) + str(now.day)
    time_ = str(current_time)
    time__ = time_.replace(":", "")
    time__ = time__.replace(".", "")

    security_code = id_generator_long()

    count_rows_bestellt_table = c.execute("""select * from anmeldebestaetigungen where userid=%s """, (user,))
    c.execute(count_rows_bestellt_table)
    zaehler_anmeldungen = int(c.rowcount)

    if zaehler_anmeldungen == 0:
        c.execute("""insert into anmeldebestaetigungen values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                  (email, security_code, ip_adresse, "", date_, "", time__, "", 0, "", "false", user, "",))
        conn.commit()


@csrf_exempt
def email_adresse_zu_bestaetigen(request):
    if request.is_ajax() and request.POST:

        code = request.POST.get('code')

        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2', \
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)

        x = str(request.session.session_key)

        current_time = datetime.datetime.now(pytz.timezone('Europe/Berlin')).time()
        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        date_ = str(now.year) + str((now.month) - 1) + str(now.day)
        time_ = str(current_time)
        time__ = time_.replace(":", "")
        time__ = time__.replace(".", "")

        email = ""

        c.execute("""select * from anmeldebestaetigungen """)
        feedback = "not ok"
        anmeldebestaetigungen = c.fetchall()
        right_password = "false"
        for row in anmeldebestaetigungen:
            if row[1] == code and row[3] == "":
                if row[12] != "":
                    password_hash = hashlib.sha512(row[12]).hexdigest()
                    c.execute("""update userdaten set email=%s, passwort=%s where emailquiz=%s""",
                              (row[0], password_hash, row[0],))
                    conn.commit()

                c.execute("""select * from userdaten where email=%s """, (row[0],))
                userdaten = c.fetchall()
                for row_2 in userdaten:
                    if row_2[0] == row[0]:
                        right_password = "true"
                        email = row_2[0]
                        userid = row_2[11]

        if right_password == "true":
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip_adresse = x_forwarded_for.split(',')[0]
            else:
                ip_adresse = request.META.get('REMOTE_ADDR')
            c.execute(
                """update %s set IPadressesecondoptin=%%s,datesecondoptin=%%s,timesecondoptin=%%s where email=%%s and code=%%s""" % (
                "anmeldebestaetigungen"), (ip_adresse, date_, time__, email, code,))
            c.execute("""update userdaten set lastsessionid=%s where lastsessionid=%s""", ("", x,))

            c.execute(
                """update userdaten set newslettersignedup=%s, anmeldedatumnewslettersubscriber=%s,lastsessionid=%s where gutscheincode=%s""",
                ("true", date_, x, userid,))

            conn.commit()

        conn.close()

        return HttpResponse(json.dumps(""), content_type='application/json')
    else:
        raise Http404


@csrf_exempt
def facebook_login(request):
    if request.is_ajax() and request.POST:

        vorname = request.POST.get('vorname')
        id_ = request.POST.get('id')
        nachname = request.POST.get('nachname')
        email = request.POST.get('email')
        min_alter = request.POST.get('min_alter')
        max_alter = request.POST.get('max_alter')
        geschlecht = request.POST.get('geschlecht')

        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2', \
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)

        x = str(request.session.session_key)

        feedback = ""
        gutscheine = ""
        status = 1
        user_existiert = "nein"
        id_existiert = "nein"
        email = email.lower()
        c.execute("""select * from userdaten where email=%s """, (email,))

        userdaten = c.fetchall()
        for row in userdaten:

            if row[0] == str(email):
                modelAB = row[47]
                sub_picture = row[48]

                user_existiert = "ja"
                gutscheincode = row[11]

        c.execute("""select * from userdaten where lastsessionid=%s """, (x,))

        userdaten = c.fetchall()
        for row in userdaten:

            if row[9] == x and x != "None":
                gutscheincode_old = row[11]

        c.execute("""select * from userdaten where facebookid=%s """, (id_,))

        userdaten = c.fetchall()
        for row in userdaten:
            if row[12] == id_:
                modelAB = row[47]
                sub_picture = row[48]
                id_existiert = "ja"
                gutscheincode = row[11]

        if id_existiert == "ja" and user_existiert == "nein":

            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip_adresse = x_forwarded_for.split(',')[0]
            else:
                ip_adresse = request.META.get('REMOTE_ADDR')

            email_adresse_bestaetigen_versand_email(email, c, conn, ip_adresse)

            c.execute("""update userdaten set lastsessionid=%s where lastsessionid=%s""", ("", x,))
            c.execute(
                """update userdaten set lastsessionid=%s, vorname=%s,nachname=%s,email=%s,minalter=%s,maxalter=%s,geschlecht=%s where facebookid=%s""",
                (
                x, str(vorname), str(nachname), str(email), str(min_alter), str(max_alter), str(geschlecht), str(id_),))
            c.execute("""insert into session_id_match_userdaten values (%s,%s)""", (gutscheincode, x,))
            change = transfer_quiz_results_to_new_user(gutscheincode, gutscheincode_old, c, conn)

            conn.commit()

            feedback = "ok"
            merge_cart_details_from_old_to_new_session(gutscheincode, gutscheincode_old, c, conn)
            if test_whether_quantities_are_available_for_order(gutscheincode, c, conn) == "update warenkorb":
                feedback = "update warenkorb"
            define_wishlist_object(gutscheincode, modelAB, sub_picture, c, conn)
            define_warenkorb_object(gutscheincode, modelAB, sub_picture, c, conn)
            define_rebates(gutscheincode, "", "", "", "", c, conn, define_standard_lieferadresse(gutscheincode, c),
                           "no", "no", "no")
            status = 0
        else:
            if (id_existiert == "nein" and user_existiert == "ja") or (id_existiert == "ja" and user_existiert == "ja"):
                c.execute("""update userdaten set lastsessionid=%s where lastsessionid=%s""", ("", x,))
                c.execute(
                    """update userdaten set lastsessionid=%s, vorname=%s,nachname=%s,facebookid=%s,minalter=%s,maxalter=%s,geschlecht=%s where email=%s""",
                    (x, str(vorname), str(nachname), str(id_), str(min_alter), str(max_alter), str(geschlecht),
                     str(email),))
                c.execute("""insert into session_id_match_userdaten values (%s,%s)""", (gutscheincode, x,))
                change = transfer_quiz_results_to_new_user(gutscheincode, gutscheincode_old, c, conn)
                conn.commit()

                merge_cart_details_from_old_to_new_session(gutscheincode, gutscheincode_old, c, conn)
                test_whether_quantities_are_available_for_order(gutscheincode, c, conn)
                feedback = "ok"

                if test_whether_quantities_are_available_for_order(gutscheincode, c, conn) == "update warenkorb":
                    feedback = "update warenkorb"

                define_wishlist_object(gutscheincode, modelAB, sub_picture, c, conn)
                define_warenkorb_object(gutscheincode, modelAB, sub_picture, c, conn)
                define_rebates(gutscheincode, "", "", "", "", c, conn, define_standard_lieferadresse(gutscheincode, c),
                               "no", "no", "no")
                status = 0

        if status == 1:
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip_adresse = x_forwarded_for.split(',')[0]
            else:
                ip_adresse = request.META.get('REMOTE_ADDR')

            user = get_userid_from_session_id(c, x)
            email_adresse_bestaetigen_versand_email(email, c, conn, ip_adresse, user)
            c.execute(
                """update userdaten set vorname=%s,facebookid=%s,nachname=%s,email=%s,minalter=%s,maxalter=%s,geschlecht=%s where gutscheincode=%s""",
                (str(vorname), str(id_), str(nachname), str(email), str(min_alter), str(max_alter), str(geschlecht),
                 user,))
            conn.commit()
            feedback = "ok"
        conn.close()

        return HttpResponse(json.dumps(feedback), content_type='application/json')
    else:
        raise Http404


def gutscheinkonto(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2', \
                                   password='okano1988', database='maxfischer2database')
    c = conn.cursor(buffered=True)

    x = str(request.session.session_key)

    #    c.execute("""insert into gutscheinkonto values (%s,%s,%s,%s,%s)""" ,("service@darlinglace.com","20","Janet"," ","19. Oktober 2016",))
    #   conn.commit()

    # c.execute("""update userdaten set credit=%s where lastsessionid=%s""" ,("40.1",x,))
    # conn.commit()

    # q.execute ("""select * from gutscheinkonto """)
    gutscheine = define_gutscheinkonto(x)

    profildaten = define_profil(x, c)
    if profildaten != "":
        login = "true"
        status = 1
        try:
            c.execute("""select * from %s""" % (x))

            cart_gesamt = 0
            for row_2 in c:
                cart_gesamt = cart_gesamt + row_2[1]
        except:
            status = 0



    else:
        login = ""
        status = 0

    update_timestamp(x, c, conn)
    t = get_template('gutscheinkonto.html')
    html = t.render(
        {'user_id_google_analytics': get_google_analytics_user_id(login, user), 'email': get_userdata(user, c, 0),
         'vorname': get_userdata(user, c, 2), 'nachname': get_userdata(user, c, 3), 'stadt': get_userdata(user, c, 6),
         'plz': get_userdata(user, c, 5), 'favicon': get_favicon(), 'path': request.path, 'brand_name': 'Darling Lace',
         'title': "Gutscheinkonto | Darling Lace", 'bestellungen': define_bestellung(user, "all", c, "nein"),
         'wishlist': wishlist, 'warenkorb': warenkorb, 'gutscheine': gutscheine, 'login': 'true',
         'cart_gesamt': cart_gesamt})

    if status == 1:
        return HttpResponse(html)


def link_group_bestimmen(name):
    links = {"BH Sets": "lingerie",
             "Mein Showroom": "no",
             #           "VIP Box" : "no",
             "Push-Up_BH": "lingerie",
             "Balconette": "lingerie",
             #          "Geschenkkarten" : "geschenkkarten",
             "schwarze_BH": "lingerie",
             "kleine_groessen": "lingerie",
             "grosse_groessen": "lingerie",
             "Slips": "panties",
             "": 0,

             }

    return links[name]


def link_name_bestimmen(group):
    links = {"lingerie": "BH Sets",
             "panties": "Slips",
             "no": "Mein Showroom",
             #           "VIP Box" : "no",

             "Geschenkkarten": "Geschenkkarten",
             "BH_Box": "BH Box",

             0: "",
             }

    return links[group]


@csrf_exempt
def filter_abrufen(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2', \
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)

        group1 = request.GET.get('group1')
        filter_style = request.GET.get('filter_style')
        filter_color = request.GET.get('filter_color')
        filter_size = request.GET.get('filter_size')
        filter_padding = request.GET.get('filter_padding')
        link = request.GET.get('group1')

        x = str(request.session.session_key)
        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            userdaten = c.fetchall()
            for row in userdaten:
                user = row[11]
                day = row[43]
                month = row[44]
                year = row[45]
                filter = load_style_filter(filter_style, filter_color, filter_size, "", filter_padding, link, user, day,
                                           month, year, c)

        conn.close()
        return HttpResponse(filter, content_type='application/json')
    else:
        raise Http404


@csrf_exempt
def content_abrufen(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2', \
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)

        name = request.GET.get('name')
        group1 = request.GET.get('group1')
        group2 = request.GET.get('group2')
        group3 = request.GET.get('group3')
        link = request.GET.get('group1')

        print "content_abrufen"

        filter_style = request.GET.get('filter_style')
        filter_color = request.GET.get('filter_color')
        filter_size = request.GET.get('filter_size')
        filter_padding = request.GET.get('filter_padding')

        filter = filter_style + "_" + filter_color + "_" + filter_size + "_" + filter_padding

        windowwidth = request.GET.get('windowwidth')
        windowheight = request.GET.get('windowheight')

        color = request.GET.get('color')
        size = request.GET.get('size')

        if name != "":
            group1 = link_group_bestimmen(name)

        x = str(request.session.session_key)
        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            userdaten = c.fetchall()
            for row in userdaten:
                user = row[11]
                modelAB = row[47]
                sub_picture = row[48]
                day = row[43]
                month = row[44]
                year = row[45]
                facebookid = row[12]
        print "lingerie_selection abrufen"
        lingerie_selection = get_lingerie_selection_filter(group1, group2, group3, color, size, user, "", day, month,
                                                           year, filter_style, filter_color, filter_padding,
                                                           filter_size, modelAB, sub_picture, c)
        print "filter abrufen"
        filter = load_style_filter(filter_style, filter_color, filter_size, "", filter_padding, link, user, day, month,
                                   year, c)
        print "filter abrufen done"

        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        Monat = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober",
                 "November", "Dezember"]
        now_date = str(now.day) + ". " + str(Monat[now.month - 1]) + " " + str(now.year)
        Y = now.year
        M = now.month
        D = now.day
        H = now.hour
        Mi = now.minute
        time = datetime.datetime.strptime(str(Y) + "-" + str(M) + "-" + str(D) + " " + str(H) + ":" + str(Mi),
                                          "%Y-%m-%d %H:%M")
        c.execute("""insert into Big_data_click_on_main_page values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (
        user, facebookid, modelAB, sub_picture, now_date, time, windowwidth, windowheight, "", "", "", filter, "", "",))
        c.execute(
            """update userdaten set letztefilter=%s,letztelingeriebasisfilter=%s,letztecolorsbasisfilter=%s where gutscheincode=%s""",
            (filter, lingerie_selection, "", user,))

        conn.commit()

        filter_data = []

        class Filter_Data(object):
            def __init__(self, lingerieselection, filter):
                self.lingerieselection = lingerieselection
                self.filter = filter

        filter_data.append(Filter_Data(lingerie_selection, filter))

        json_string = json.dumps([Filter_Data.__dict__ for Filter_Data in filter_data])

        conn.close()
        return HttpResponse(json.dumps(json_string), content_type='application/json')
    else:
        raise Http404


@csrf_exempt
def bewertung_speichern(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2', \
                                   password='okano1988', database='maxfischer2database')
    c = conn.cursor(buffered=True)
    if request.is_ajax() and request.POST:

        passform = request.POST.get('passform')

        bewertung = request.POST.get('bewertung')

        bewertungsheadline = request.POST.get('bewertungsheadline')

        bewertungstext = request.POST.get('bewertungstext')

        style = request.POST.get('style')
        stylecode = request.POST.get('stylecode')
        color = request.POST.get('color')
        bestellnummer = request.POST.get('bestellnummer')
        gutscheincodeid = request.POST.get('gutscheincodeid')

        x = str(request.session.session_key)
        status = 0
        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            userdaten = c.fetchall()
            for row in userdaten:
                namebewerter = row[2][2:] + " " + row[3]
                gutscheincodeid = row[11]

        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))

        Monat = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober",
                 "November", "Dezember"]
        date = str(now.day) + ". " + Monat[(now.month) - 1] + " " + str(now.year)

        c.execute(
            """update %s set bewertungstext=%%s, bewertungsheadline=%%s, bewertung=%%s, passform=%%s, bewertungsdatum=%%s, bewertungapproved=%%s  where bestellnummer=%%s and gutscheincode=%%s and stylecode=%%s and color=%%s""" % (
            "cart_details"), (
            bewertungstext, bewertungsheadline, bewertung, passform, date, "nein", bestellnummer, gutscheincodeid,
            stylecode, color))
        conn.commit()

        conn.close()
        return HttpResponse(json.dumps(""), content_type='application/json')
    else:
        raise Http404


def get_modelAB(user, c):
    c.execute("""select * from userdaten where gutscheincode=%s """, (user,))
    for row in c:
        return row[47]


def get_subpicture(user, c):
    c.execute("""select * from userdaten where gutscheincode=%s """, (user,))
    for row in c:
        return row[48]


def bewertung_abgeben(request, offset, offset_2):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2', \
                                   password='okano1988', database='maxfischer2database')
    c = conn.cursor(buffered=True)

    x = str(request.session.session_key)

    login = "false"
    status = 0
    modelAB = ""
    sub_picture = ""
    user = ""

    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        for row in c:
            password = "ok"
            status = 1
            bereitsbestellt = row[75]
            bereitsversandt = row[76]
            wishlist = row[65]
            warenkorb = row[66]
            email = row[0]
            user = row[11]
            vorname = row[2]
            nachname = row[3]
            default_bra_size = row[58]
            default_panty_size = row[59]
            facebookid = row[12]
            quiz = row[26]
            stadt = row[6]
            plz = row[4]
            modelAB = row[47]
            sub_picture = row[48]
            wishlist_quantity = row[16]
            cart_quantity = row[17]
            if row[1] == "":
                password = "not ok"
            if (row[0] != "" and row[12] != "") or (row[0] != "" and row[1] != ""):
                login = "true"
            if row[22] == "VIP" and row[23] == "true":
                VIP = "VIP"
            else:
                VIP = "Regular"

    if status == 0:
        if x != "None":
            x = str(request.session.session_key)
            create_user(x, c, conn)
        else:
            print(request.path + ",create_new_request," + x)
            log_out_do_it(x, c, conn)
            request.session.create()
            x = str(request.session.session_key)
            create_user(x, c, conn)

        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            for row in c:
                email = row[0]
                bereitsbestellt = row[75]
                bereitsversandt = row[76]
                user = row[11]
                vorname = row[2]
                nachname = row[3]
                default_bra_size = row[58]
                default_panty_size = row[59]
                facebookid = row[12]
                quiz = row[26]
                stadt = row[6]
                plz = row[4]
                modelAB = row[47]
                sub_picture = row[48]
                wishlist_quantity = row[16]
                cart_quantity = row[17]
                if row[22] == "VIP" and row[23] == "true":
                    VIP = "VIP"
                else:
                    VIP = "Regular"

    if login != "false":

        bestellungen = define_bestellung(user, "all", c, "nein")
        bestelldetails = define_bestelldetails(user, offset, offset_2, c, get_modelAB(user, c), get_subpicture(user, c))

        t = get_template('bewertung_abgeben.html')
        html = t.render({'user_id_google_analytics': get_google_analytics_user_id(login, user), 'password': password,
                         'email': email, 'bereitsbestellt': bereitsbestellt, 'bereitsversandt': bereitsversandt,
                         'fb_link': 'https://www.darlinglace.com',
                         'fb_title': ("Liebst du Lingerie? Erhalte Dein BH Set ab 29,95 EUR!").encode('utf8'),
                         'fb_description': (
                         "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                             'utf8'), 'fb_description': (
            "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                'utf8'), 'fb_image': 'https://www.darlinglace.com/static/overall_picture_bra.jpg', 'vorname': vorname,
                         'nachname': nachname, 'stadt': stadt, 'plz': plz, 'wishlist': wishlist, 'warenkorb': warenkorb,
                         'favicon': get_favicon(), 'path': request.path, 'brand_name': 'Darling Lace',
                         'title': "Bewertung abgeben | Darling Lace", 'bestellungen': bestellungen,
                         'bestelldetails': bestelldetails, 'login': login})
        conn.close()
        return HttpResponse(html)
    else:
        path = request.path
        html = call_login_page(path, c, x)
        conn.close()
        return HttpResponse(html)


def bewertungen_bearbeiten(request, offset):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2', \
                                   password='okano1988', database='maxfischer2database')
    c = conn.cursor(buffered=True)

    x = str(request.session.session_key)

    login = "false"
    status = 0
    modelAB = ""
    sub_picture = ""
    user = ""

    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        for row in c:
            password = "ok"
            status = 1
            bereitsbestellt = row[75]
            bereitsversandt = row[76]
            wishlist = row[65]
            warenkorb = row[66]
            email = row[0]
            user = row[11]
            vorname = row[2]
            nachname = row[3]
            default_bra_size = row[58]
            default_panty_size = row[59]
            facebookid = row[12]
            quiz = row[26]
            stadt = row[6]
            plz = row[4]
            modelAB = row[47]
            sub_picture = row[48]
            wishlist_quantity = row[16]
            cart_quantity = row[17]
            if row[1] == "":
                password = "not ok"
            if (row[0] != "" and row[12] != "") or (row[0] != "" and row[1] != ""):
                login = "true"
            if row[22] == "VIP" and row[23] == "true":
                VIP = "VIP"
            else:
                VIP = "Regular"

    if status == 0:
        if x != "None":
            x = str(request.session.session_key)
            create_user(x, c, conn)
        else:
            print(request.path + ",create_new_request," + x)
            log_out_do_it(x, c, conn)
            request.session.create()
            x = str(request.session.session_key)
            create_user(x, c, conn)

        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            for row in c:
                email = row[0]
                bereitsbestellt = row[75]
                bereitsversandt = row[76]
                user = row[11]
                vorname = row[2]
                nachname = row[3]
                default_bra_size = row[58]
                default_panty_size = row[59]
                facebookid = row[12]
                quiz = row[26]
                stadt = row[6]
                plz = row[4]
                modelAB = row[47]
                sub_picture = row[48]
                wishlist_quantity = row[16]
                cart_quantity = row[17]
                if row[22] == "VIP" and row[23] == "true":
                    VIP = "VIP"
                else:
                    VIP = "Regular"

    if login != "false":
        bestellungen = define_bestellung(user, "all", c, "nein")
        bestelldetails = define_bestelldetails(user, offset, "", "yes", c, get_modelAB(user, c),
                                               get_subpicture(user, c))

        if bestelldetails == "[]":
            status = 0

        if status == 1:
            t = get_template('bewertungen_ansehen.html')
            html = t.render({'user_id_google_analytics': get_google_analytics_user_id(login, user), 'email': email,
                             'bereitsbestellt': bereitsbestellt, 'bereitsversandt': bereitsversandt,
                             'fb_link': 'https://www.darlinglace.com',
                             'fb_title': ("Liebst du Lingerie? Erhalte Dein BH Set ab 29,95 EUR!").encode('utf8'),
                             'fb_description': (
                             "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                                 'utf8'), 'fb_description': (
                "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                    'utf8'), 'fb_image': 'https://www.darlinglace.com/static/overall_picture_bra.jpg',
                             'vorname': vorname, 'nachname': nachname, 'stadt': stadt, 'plz': plz, 'wishlist': wishlist,
                             'warenkorb': warenkorb, 'favicon': get_favicon(), 'path': request.path,
                             'brand_name': 'Darling Lace', 'title': "Bewertungen | Darling Lace",
                             'links': get_links(quiz), 'wishlist': wishlist, 'warenkorb': warenkorb,
                             'bestellungen': bestellungen, 'bestelldetails': bestelldetails, 'login': login})
            conn.close()
            return HttpResponse(html)
        else:
            conn.close()
            return HttpResponseRedirect("/accout_page/")
    else:
        path = request.path
        html = call_login_page(path, c, x)
        conn.close()
        return HttpResponse(html)


def table_bestelldetails(session_key, bestellnummer, c):
    c.execute("""select * from userdaten where lastsessionid=%s """, (session_key,))

    userdaten = c.fetchall()

    for row_2 in userdaten:

        if row_2[9] == session_key:
            c.execute("""select * from bestellt where gutscheincode=%s """, (row_2[11],))
            for row in c:
                if row[21] == bestellnummer:
                    return row[0]


def table_bestelldetails_datum(table, c):
    c.execute("""select * from %s """ % (table))
    datum = []
    datum_ = ""
    for row_2 in c:
        if datum_ != row_2[2]:
            datum.append(row_2[2])
            datum_ = row_2[2]
    return datum


def table_bestelldetails_namen(bestellnummer, c):
    c.execute("""select * from cart_details where bestellnummer=%s """, (bestellnummer,))
    name = []
    name_ = ""
    for row_2 in c:
        if name_ != row_2[0]:
            name.append(row_2[0])
            name_ = row_2[0]
    return name


def bestellungen_details_ansehen(request, offset):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database')
    c = conn.cursor(buffered=True)

    x = str(request.session.session_key)

    login = "false"
    status = 0
    modelAB = ""
    sub_picture = ""
    user = ""

    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        for row in c:
            status = 1
            wishlist = row[65]
            bereitsbestellt = row[75]
            bereitsversandt = row[76]
            warenkorb = row[66]
            email = row[0]
            user = row[11]
            vorname = row[2]
            nachname = row[3]
            default_bra_size = row[58]
            default_panty_size = row[59]
            facebookid = row[12]
            quiz = row[26]
            stadt = row[6]
            plz = row[4]
            modelAB = row[47]
            sub_picture = row[48]
            wishlist_quantity = row[16]
            cart_quantity = row[17]
            if (row[0] != "" and row[12] != "") or (row[0] != "" and row[1] != ""):
                login = "true"
            if row[22] == "VIP" and row[23] == "true":
                VIP = "VIP"
            else:
                VIP = "Regular"

    if status == 0:
        if x != "None":
            x = str(request.session.session_key)
            create_user(x, c, conn)
        else:
            print(request.path + ",create_new_request," + x)
            log_out_do_it(x, c, conn)
            request.session.create()
            x = str(request.session.session_key)
            create_user(x, c, conn)

        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            for row in c:
                email = row[0]
                bereitsbestellt = row[75]
                bereitsversandt = row[76]
                user = row[11]
                vorname = row[2]
                nachname = row[3]
                default_bra_size = row[58]
                default_panty_size = row[59]
                facebookid = row[12]
                quiz = row[26]
                stadt = row[6]
                plz = row[4]
                modelAB = row[47]
                sub_picture = row[48]
                wishlist_quantity = row[16]
                cart_quantity = row[17]
                if row[22] == "VIP" and row[23] == "true":
                    VIP = "VIP"
                else:
                    VIP = "Regular"

    if login != "false":
        bestellung = define_bestellung(user, offset, c, "nein")
        if len(bestellung) == 2:
            status = 0
        else:
            bestelldetails = define_bestelldetails(user, offset, "", "", c, get_modelAB(user, c),
                                                   get_subpicture(user, c))
            namen = table_bestelldetails_namen(offset, c)
            lingerie = get_lingerie_sizes("", "", "", "", "", "", "", namen, c)
            stylecodes_colorcodes = get_stylecode_colorcode_from_order(x, offset, c, user)

            get_content_for_facebookpixel_from_order_ = get_content_for_facebookpixel_from_order(x, "", c, user)

        if status == 1:
            t = get_template('order_summary.html')

            html = t.render({'user_id_google_analytics': get_google_analytics_user_id(login, user),
                             'contents_list': get_content_for_facebookpixel_from_order_,
                             'url': get_link_positioining(""), 'email': email, 'bereitsbestellt': bereitsbestellt,
                             'bereitsversandt': bereitsversandt, 'fb_link': 'https://www.darlinglace.com',
                             'fb_title': ("Liebst du Lingerie? Erhalte Dein BH Set ab 29,95 EUR!").encode('utf8'),
                             'fb_description': (
                             "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                                 'utf8'), 'fb_description': (
                "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                    'utf8'), 'fb_image': 'https://www.darlinglace.com/static/overall_picture_bra.jpg',
                             'vorname': vorname, 'nachname': nachname, 'stadt': stadt, 'plz': plz, 'wishlist': wishlist,
                             'warenkorb': warenkorb, 'stylecodes_colorcodes': stylecodes_colorcodes,
                             'bestellung_gesamt': define_rebates(user, offset, "", "", "", c, conn, "", "yes", "no",
                                                                 "no"), 'favicon': get_favicon(), 'path': request.path,
                             'brand_name': 'Darling Lace', 'title': "Zusammenfassung Bestellung | Darling Lace",
                             'rebates': define_rebates(user, offset, "", "", "", c, conn, "", "no", "no", "no"),
                             'links': get_links(quiz), 'wishlist': wishlist, 'warenkorb': warenkorb,
                             'lingerieselection': lingerie, 'bestellung': bestellung, 'bestelldetails': bestelldetails,
                             'login': login})
            conn.close()
            return HttpResponse(html)
        else:
            conn.close()
            return HttpResponseRedirect("/account_page/")

    else:
        path = request.path
        html = call_login_page(path, c, x)
        conn.close()
        return HttpResponse(html)


@csrf_exempt
def datum_abrufen_array(x):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database')
    c = conn.cursor(buffered=True)

    c.execute("""select * from cart_details where gutscheincode=%s""", (user,))

    b = ""
    max_var_warenkorb = 7
    datum = []
    datum_ = ""
    h = 0
    for row in c:
        j = 0
        if (h != 0):
            b = b + ";"
        if row[2] != datum_:
            datum.append(row[2])
            datum_ = row[2]
        while (j <= max_var_warenkorb):
            if (j == max_var_warenkorb):
                b = b + str(row[j])
            else:
                b = b + str(row[j]) + ","
            j = j + 1
        h = h + 1
    return datum


@csrf_exempt
def groessentabelle_uebersicht(request):
    if request.is_ajax() and request.GET:
        # print("asd")

        list = [[] for i in range(55)]

        i = 0
        while (i <= 9):

            j = 0
            while (j <= 4):
                # print(i*5+j)
                list[i * 5 + j].append(i * 5 + j + 63)
                list[i * 5 + j].append(i * 5 + 75)
                list[i * 5 + j].append(i * 5 + 99)

                j = j + 1

            i = i + 1

        #        print(list)

        conn.close()
        return HttpResponse(json.dumps(list), content_type='application/json')
    else:
        raise Http404


@csrf_exempt
def groessentabelle_detailliert(request):
    if request.is_ajax() and request.GET:

        list = [[[] for i in range(49)] for j in range(49)]

        get_cup = {0: 'AA',
                   1: 'A',
                   2: 'B',
                   3: 'C',
                   4: 'D',
                   5: 'E',
                   6: 'F',
                   7: 'G',
                   8: 'H',
                   9: 'I',
                   10: 'J',
                   11: 'K',
                   12: 'K'

                   }

        get_bralette = {'65A': 'XS',
                        '65B': 'XS',
                        '65C': 'XS',
                        '70A': 'XS',
                        '70B': 'XS',
                        '65D': 'S',
                        '65E': 'S',

                        '70C': 'S',
                        '70D': 'S',
                        '75A': 'S',
                        '75B': 'S',

                        '75C': 'M',
                        '75D': 'M',
                        '80A': 'M',
                        '80B': 'M',
                        '80C': 'L',
                        '80D': 'L',

                        '85A': 'L',
                        '85B': 'L',
                        '85C': 'L',
                        '85D': 'L',

                        '90B': 'XL',
                        '90C': 'XL',
                        '90D': 'XL'

                        }
        i = 0
        zaehler_1 = 0
        zaehler_2 = 0

        unterbrust = 65

        while (i <= 48):
            if zaehler_1 > 4:
                unterbrust = unterbrust + 5
                zaehler_1 = 0

            zaehler_1 = zaehler_1 + 1

            j = 0
            cup = 0
            zaehler_2 = 0
            cup_detail = get_cup[cup]
            while (j <= 24):
                if zaehler_2 > 1:
                    cup = cup + 1
                    cup_detail = get_cup[cup]
                    zaehler_2 = 0

                zaehler_2 = zaehler_2 + 1

                #               print(str(unterbrust)+cup_detail)
                list[i][0].append(str(unterbrust) + cup_detail)
                try:
                    bralette_detail = get_bralette[str(unterbrust) + cup_detail]

                    list[i][1].append(bralette_detail)
                except:
                    list[i][1].append("")

                j = j + 1

            i = i + 1

        #        print(list)
        conn.close()
        return HttpResponse(json.dumps(list), content_type='application/json')
    else:
        raise Http404


@csrf_exempt
def ruecksendungen_abrufen(request):
    if request.is_ajax() and request.POST:
        session_key = request.POST.get('session_key')

        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)
        x = str(request.session.session_key)
        ruecksendungen = ""
        if session_key == "all":
            ruecksendungen = define_ruecksendungen(session_key, c, "", "")
        conn.close()
        return HttpResponse(json.dumps(ruecksendungen), content_type='application/json')
    else:
        raise Http404


@csrf_exempt
def bestellung_abrufen(request):
    if request.is_ajax() and request.POST:
        bestellnummer = request.POST.get('bestellnummer')
        session_key = request.POST.get('session_key')

        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)
        x = str(request.session.session_key)

        if session_key != "all":
            bestellung = define_bestellung(session_key, bestellnummer, c, "nein")

        else:
            bestellung = define_bestellung(session_key, bestellnummer, c, "nein")
        conn.close()
        return HttpResponse(json.dumps(bestellung), content_type='application/json')
    else:
        raise Http404


@csrf_exempt
def bestelldetails_abrufen(request):
    if request.is_ajax() and request.POST:
        bestellnummer = request.POST.get('bestellnummer')
        x = str(request.session.session_key)

        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)
        user = get_userid_from_session_id(c, x)
        bestelldetails = define_bestelldetails(user, bestellnummer, "", "", c, get_modelAB(user, c),
                                               get_subpicture(user, c))
        conn.close()
        return HttpResponse(json.dumps(bestelldetails), content_type='application/json')
    else:
        raise Http404


def bestellungen_ansehen(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database')
    c = conn.cursor(buffered=True)

    x = str(request.session.session_key)

    login = "false"
    status = 0
    modelAB = ""
    sub_picture = ""
    user = ""

    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        for row in c:
            password = "ok"
            status = 1
            wishlist = row[65]
            bereitsbestellt = row[75]
            bereitsversandt = row[76]
            warenkorb = row[66]
            email = row[0]
            user = row[11]
            vorname = row[2]
            nachname = row[3]
            default_bra_size = row[58]
            default_panty_size = row[59]
            facebookid = row[12]
            quiz = row[26]
            stadt = row[6]
            plz = row[4]
            modelAB = row[47]
            sub_picture = row[48]
            wishlist_quantity = row[16]
            cart_quantity = row[17]
            if row[1] == "":
                password = "not ok"
            if (row[0] != "" and row[12] != "") or (row[0] != "" and row[1] != ""):
                login = "true"
            if row[22] == "VIP" and row[23] == "true":
                VIP = "VIP"
            else:
                VIP = "Regular"

            bestellungen = define_bestellung(user, "all", c, "nein")
            bestelldetails = define_bestelldetails(user, "", "", "", c, get_modelAB(user, c), get_subpicture(user, c))

    if status == 0:
        if x != "None":
            x = str(request.session.session_key)
            create_user(x, c, conn)
        else:
            print(request.path + ",create_new_request," + x)
            log_out_do_it(x, c, conn)
            request.session.create()
            x = str(request.session.session_key)
            create_user(x, c, conn)

        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            for row in c:
                email = row[0]
                bereitsbestellt = row[75]
                bereitsversandt = row[76]
                user = row[11]
                vorname = row[2]
                nachname = row[3]
                default_bra_size = row[58]
                default_panty_size = row[59]
                facebookid = row[12]
                quiz = row[26]
                stadt = row[6]
                plz = row[4]
                modelAB = row[47]
                sub_picture = row[48]
                wishlist_quantity = row[16]
                cart_quantity = row[17]
                if row[22] == "VIP" and row[23] == "true":
                    VIP = "VIP"
                else:
                    VIP = "Regular"

    if login != "false":

        if len(bestellungen) == 2:
            status = 0

        if status == 1:
            t = get_template('bestellungen_ansehen.html')
            html = t.render(
                {'user_id_google_analytics': get_google_analytics_user_id(login, user), 'password': password,
                 'url': get_link_positioining(""), 'links': get_links(quiz), 'email': email,
                 'bereitsbestellt': bereitsbestellt, 'bereitsversandt': bereitsversandt,
                 'fb_link': 'https://www.darlinglace.com',
                 'fb_title': ("Liebst du Lingerie? Erhalte Dein BH Set ab 29,95 EUR!").encode('utf8'),
                 'fb_description': (
                 "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                     'utf8'), 'fb_description': (
                "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                    'utf8'), 'fb_image': 'https://www.darlinglace.com/static/overall_picture_bra.jpg',
                 'vorname': vorname, 'nachname': nachname, 'stadt': stadt, 'plz': plz, 'wishlist': wishlist,
                 'warenkorb': warenkorb, 'favicon': get_favicon(), 'path': request.path, 'brand_name': 'Darling Lace',
                 'title': "Bestellungen | Darling Lace", 'links': get_links(quiz), 'wishlist': wishlist,
                 'warenkorb': warenkorb, 'bestellungen': bestellungen, 'bestelldetails': bestelldetails,
                 'login': login})
            conn.close()
            return HttpResponse(html)
        else:
            conn.close()
            return HttpResponseRedirect("/account_page/")

    else:
        path = request.path
        html = call_login_page(path, c, x)
        conn.close()
        return HttpResponse(html)


def credit_card_add_new_payment(token_id, client_id_):
    paymill_context = paymill.PaymillContext('82239adeff57ef5d51ec2e5d11fd915d')
    payment_service = paymill_context.get_payment_service()
    payment_with_token_and_client = payment_service.create(
        token=token_id,
        client_id=client_id_
    )

    return "true"


@csrf_exempt
def zahlungsmethode_speichern_test(request):
    if request.is_ajax() and request.POST:

        hinzufuegen = request.POST.get('hinzufuegen')

        indexnummer = request.POST.get('indexnummer')
        standard = request.POST.get('standard')
        card_type = request.POST.get('card_type')
        token = request.POST.get('token')

        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)

        userdaten = c.fetchall()

        x = str(request.session.session_key)
        status = 0
        existiert = "nein"
        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            userdaten = c.fetchall()
            for row in userdaten:
                print(credit_card_add_new_payment_test(token, row[50]))

        conn.close()
        return HttpResponse(json.dumps("asd"), content_type='application/json')
    else:
        raise Http404


@csrf_exempt
def zahlungsmethode_speichern(request):
    if request.is_ajax() and request.POST:
        hinzufuegen = request.POST.get('hinzufuegen')

        indexnummer = request.POST.get('indexnummer')
        standard = request.POST.get('standard')
        card_type = request.POST.get('card_type')
        token = request.POST.get('token')
        zahlungsoption = request.POST.get('zahlungsoption')
        zahlungsart = request.POST.get('zahlungsart')
        speichern = request.POST.get('speichern')
        email = request.POST.get('email')

        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)

        x = str(request.session.session_key)

        status = 0
        existiert = "nein"

        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            userdaten = c.fetchall()
            for row in userdaten:
                user = row[11]
                if hinzufuegen == "1":
                    if row[50] == "":
                        clientidpaymill = credit_card_create_new_client(row[11] + "@test.de")
                        c.execute("""update %s set clientidpaymill=%%s where gutscheincode=%%s""" % ("userdaten"),
                                  (clientidpaymill, user,))
                    else:
                        clientidpaymill = row[50]

                    payment_with_token_and_client = credit_card_add_new_payment_test(token, clientidpaymill)

                    paymill_context = paymill.PaymillContext('82239adeff57ef5d51ec2e5d11fd915d')
                    payment_service = paymill_context.get_payment_service()
                    payments_list = payment_service.list()

                    now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
                    Y = now.year
                    M = now.month
                    D = now.day
                    H = now.hour
                    Mi = now.minute
                    S = now.second
                    d1 = datetime.datetime.strptime(
                        str(Y) + "-" + str(M) + "-" + str(D) + " " + str(H) + ":" + str(Mi) + ":" + str(S),
                        "%Y-%m-%d %H:%M:%S")
                    d2 = datetime.datetime.strptime("2016-09-25 12:03:01", "%Y-%m-%d %H:%M:%S")

                    diff = d2 - d1

                    c.execute("""select * from zahlungsmethoden where gutscheincode=%s """, (row[11],))
                    zahlungsmethoden = c.fetchall()
                    if clientidpaymill == payment_with_token_and_client["client"]["id"]:
                        existiert = "nein"
                        for row_2 in zahlungsmethoden:
                            if payment_with_token_and_client["id"] == row_2[0]:
                                existiert = "ja"
                    else:
                        existiert = ""
                    if existiert == "nein":

                        if zahlungsart == "kreditkarte":
                            c.execute("""update %s set standard=%%s where gutscheincode=%%s""" % ("zahlungsmethoden"),
                                      ("nein", row[11],))
                            c.execute(
                                """insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % (
                                "zahlungsmethoden"), (payment_with_token_and_client["id"], diff, zahlungsoption,
                                                      payment_with_token_and_client["card_holder"],
                                                      payment_with_token_and_client["last4"],
                                                      payment_with_token_and_client["expire_month"],
                                                      payment_with_token_and_client["expire_year"], "", "ja",
                                                      payment_with_token_and_client["card_type"], "kreditkarte", "", "",
                                                      str(speichern), x, row[11],))
                            c.execute(
                                """update %s set selectedzahlungsoption=%%s where gutscheincode=%%s""" % ("userdaten"),
                                ("0", row[11],))
                            conn.commit()
                        else:
                            c.execute("""update %s set standard=%%s where gutscheincode=%%s""" % ("zahlungsmethoden"),
                                      ("nein", row[11],))
                            c.execute(
                                """insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % (
                                "zahlungsmethoden"), (payment_with_token_and_client["id"], diff, zahlungsoption,
                                                      payment_with_token_and_client["holder"], "", "", "", "", "ja", "",
                                                      "lastschrift", payment_with_token_and_client["iban"],
                                                      payment_with_token_and_client["bic"], str(speichern), x,
                                                      row[11],))
                            c.execute(
                                """update %s set selectedzahlungsoption=%%s where gutscheincode=%%s""" % ("userdaten"),
                                ("3", row[11],))
                            conn.commit()
                    else:
                        zahlungsmethoden = "existiert"
                    status = 1

                if hinzufuegen == "0":

                    zaehler = 0
                    threshold = 1
                    c.execute("""select * from zahlungsmethoden where gutscheincode=%s """, (row[11],))
                    for row_2 in c:
                        if row_2[4] == kreditkartennummer:
                            zaehler = zaehler + 1
                        if row_2[1] == indexnummer:
                            if row_2[4] == kreditkartennummer:
                                threshold = 1
                            else:
                                threshold = 0

                    c.execute(
                        """update %s set zahlungsoption=%%s, name=%%s,kreditkartennummer=%%s,ablaufmonat=%%s,ablaufjahr=%%s,sicherheitscode=%%s where clientid=%%s and indexnummer=%%s and gutscheincode=%%s""" % (
                        "zahlungsmethoden"), (
                        zahlungsoption, name, kreditkartennummer, ablaufmonat, ablaufjahr, sicherheitscode, row[0],
                        indexnummer, row[11],))
                    c.execute("""insert into keyuserdaten values (%s,%s,%s,%s,%s,%s)""",
                              (row[0], "", kreditkartennummer, "", "", row[11],))
                    conn.commit()

                if hinzufuegen == "-1":
                    c.execute("""select * from zahlungsmethoden where gutscheincode=%s """, (row[11],))
                    data_table = c.fetchall()

                    for row_2 in data_table:
                        if row_2[1] == indexnummer:
                            client_id = row_2[0]
                    credit_card_delete_payment_test(client_id)
                    c.execute("""delete from %s where clientid=%%s and indexnummer=%%s and gutscheincode=%%s""" % (
                    "zahlungsmethoden"), (client_id, indexnummer, row[11],))
                    conn.commit()

                if hinzufuegen == "-2":

                    c.execute("""select * from zahlungsmethoden where gutscheincode=%s """, (row[11],))

                    data_table = c.fetchall()
                    for row_2 in data_table:
                        c.execute("""update %s set standard=%%s where indexnummer=%%s and gutscheincode=%%s""" % (
                        "zahlungsmethoden"), ("nein", row_2[1], row[11],))
                        conn.commit()
                    c.execute("""update %s set standard=%%s where indexnummer=%%s and gutscheincode=%%s""" % (
                    "zahlungsmethoden"), (standard, indexnummer, row[11]))
                    conn.commit()

        if existiert == "nein":
            zahlungsmethoden = define_zahlungsmethoden(user, c)
        conn.close()
        return HttpResponse(json.dumps(zahlungsmethoden), content_type='application/json')
    else:
        raise Http404


def zahlungsmethoden_bearbeiten(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database')
    c = conn.cursor(buffered=True)

    login = "false"
    status = 0
    modelAB = ""
    sub_picture = ""
    user = ""

    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        for row in c:
            password = "ok"
            status = 1
            bereitsbestellt = row[75]
            bereitsversandt = row[76]
            wishlist = row[65]
            warenkorb = row[66]
            email = row[0]
            user = row[11]
            vorname = row[2]
            nachname = row[3]
            default_bra_size = row[58]
            default_panty_size = row[59]
            facebookid = row[12]
            quiz = row[26]
            stadt = row[6]
            plz = row[4]
            modelAB = row[47]
            sub_picture = row[48]
            wishlist_quantity = row[16]
            cart_quantity = row[17]
            zahlungsmethoden = define_zahlungsmethoden(user, c)
            if row[1] == "":
                password = "not ok"
            if (row[0] != "" and row[12] != "") or (row[0] != "" and row[1] != ""):
                login = "true"
            if row[22] == "VIP" and row[23] == "true":
                VIP = "VIP"
            else:
                VIP = "Regular"

            zahlungsmethoden = define_zahlungsmethoden(user, c)

    if status == 0:
        if x != "None":
            x = str(request.session.session_key)
            create_user(x, c, conn)
        else:
            print(request.path + ",create_new_request," + x)
            log_out_do_it(x, c, conn)
            request.session.create()
            x = str(request.session.session_key)
            create_user(x, c, conn)

        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            for row in c:
                email = row[0]
                user = row[11]
                bereitsbestellt = row[75]
                bereitsversandt = row[76]
                vorname = row[2]
                nachname = row[3]
                default_bra_size = row[58]
                default_panty_size = row[59]
                facebookid = row[12]
                quiz = row[26]
                stadt = row[6]
                plz = row[4]
                modelAB = row[47]
                sub_picture = row[48]
                wishlist_quantity = row[16]
                cart_quantity = row[17]
                if row[22] == "VIP" and row[23] == "true":
                    VIP = "VIP"
                else:
                    VIP = "Regular"

    if login != "false":
        t = get_template('zahlungsmethoden_bearbeiten.html')
        html = t.render({'user_id_google_analytics': get_google_analytics_user_id(login, user), 'email': email,
                         'bereitsbestellt': bereitsbestellt, 'bereitsversandt': bereitsversandt,
                         'fb_link': 'https://www.darlinglace.com',
                         'fb_title': ("Liebst du Lingerie? Erhalte Dein BH Set ab 29,95 EUR!").encode('utf8'),
                         'fb_description': (
                         "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                             'utf8'), 'fb_description': (
            "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                'utf8'), 'fb_image': 'https://www.darlinglace.com/static/overall_picture_bra.jpg', 'vorname': vorname,
                         'nachname': nachname, 'stadt': stadt, 'plz': plz, 'wishlist': wishlist, 'warenkorb': warenkorb,
                         'favicon': get_favicon(), 'path': request.path, 'brand_name': 'Darling Lace',
                         'title': "Zahlungsmethoden | Darling Lace",
                         'bestellungen': define_bestellung(user, "all", c, "nein"), 'links': get_links(quiz),
                         'wishlist': wishlist, 'warenkorb': warenkorb, 'zahlungsmethoden': zahlungsmethoden,
                         'login': login})
        conn.close()
        return HttpResponse(html)
    else:
        path = request.path
        html = call_login_page(path, c, x)
        conn.close()
        return HttpResponse(html)


def adressbuch_bearbeiten(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database')
    c = conn.cursor(buffered=True)

    login = "false"
    status = 0
    modelAB = ""
    sub_picture = ""
    user = ""

    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        for row in c:
            password = "ok"
            status = 1
            bereitsbestellt = row[75]
            bereitsversandt = row[76]
            wishlist = row[65]
            warenkorb = row[66]
            email = row[0]
            user = row[11]
            vorname = row[2]
            nachname = row[3]
            default_bra_size = row[58]
            default_panty_size = row[59]
            facebookid = row[12]
            quiz = row[26]
            stadt = row[6]
            plz = row[4]
            modelAB = row[47]
            sub_picture = row[48]
            wishlist_quantity = row[16]
            cart_quantity = row[17]
            adressbuch = define_adressbuch(user, c)
            if row[1] == "":
                password = "not ok"
            if (row[0] != "" and row[12] != "") or (row[0] != "" and row[1] != ""):
                login = "true"
            if row[22] == "VIP" and row[23] == "true":
                VIP = "VIP"
            else:
                VIP = "Regular"

    if status == 0:
        if x != "None":
            x = str(request.session.session_key)
            create_user(x, c, conn)
        else:
            print(request.path + ",create_new_request," + x)
            log_out_do_it(x, c, conn)
            request.session.create()
            x = str(request.session.session_key)
            create_user(x, c, conn)

        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            for row in c:
                email = row[0]
                bereitsbestellt = row[75]
                bereitsversandt = row[76]
                user = row[11]
                vorname = row[2]
                nachname = row[3]
                default_bra_size = row[58]
                default_panty_size = row[59]
                facebookid = row[12]
                quiz = row[26]
                stadt = row[6]
                plz = row[4]
                modelAB = row[47]
                sub_picture = row[48]
                wishlist_quantity = row[16]
                cart_quantity = row[17]
                if row[22] == "VIP" and row[23] == "true":
                    VIP = "VIP"
                else:
                    VIP = "Regular"

    if login != "false":
        t = get_template('adressen_bearbeiten.html')
        html = t.render({'user_id_google_analytics': get_google_analytics_user_id(login, user), 'email': email,
                         'bereitsbestellt': bereitsbestellt, 'bereitsversandt': bereitsversandt,
                         'fb_link': 'https://www.darlinglace.com',
                         'fb_title': ("Liebst du Lingerie? Erhalte Dein BH Set ab 29,95 EUR!").encode('utf8'),
                         'fb_description': (
                         "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                             'utf8'), 'fb_description': (
            "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                'utf8'), 'fb_image': 'https://www.darlinglace.com/static/overall_picture_bra.jpg', 'vorname': vorname,
                         'nachname': nachname, 'stadt': stadt, 'plz': plz, 'wishlist': wishlist, 'warenkorb': warenkorb,
                         'favicon': get_favicon(), 'path': request.path, 'brand_name': 'Darling Lace',
                         'title': "Adressbuch | Darling Lace",
                         'bestellungen': define_bestellung(user, "all", c, "nein"), 'links': get_links(quiz),
                         'wishlist': wishlist, 'warenkorb': warenkorb, 'adressbuch': adressbuch, 'login': 'true',
                         'cart_gesamt': cart_gesamt})
        conn.close()
        return HttpResponse(html)
    else:
        path = request.path
        html = call_login_page(path, c, x)
        conn.close()
        return HttpResponse(html)


def adresse_hinzufuegen(hinzufuegen, vorname, nachname, telefonnummer, strasse, unternehmensdetails, stadt, plz,
                        indexnummer, standard, land, anrede, hausnummer, standard_lieferadresse, c, conn, user, email,
                        x):
    postion_data_entry = 0
    if standard_lieferadresse == "ja":
        c.execute("""update %s set standardlieferadresse=%%s where gutscheincode=%%s""" % ("adressbuch"),
                  ("nein", user,))
        conn.commit()
    if standard == "ja":
        c.execute("""update %s set standard=%%s where gutscheincode=%%s""" % ("adressbuch"), ("nein", user,))
        conn.commit()
    if hinzufuegen == "1":
        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        Y = now.year
        M = now.month
        D = now.day
        H = now.hour
        Mi = now.minute
        S = now.second
        d1 = datetime.datetime.strptime(
            str(Y) + "-" + str(M) + "-" + str(D) + " " + str(H) + ":" + str(Mi) + ":" + str(S), "%Y-%m-%d %H:%M:%S")
        d2 = datetime.datetime.strptime("2016-09-25 12:03:01", "%Y-%m-%d %H:%M:%S")

        diff = d2 - d1

        c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % (
        "adressbuch"), (
                  email, diff, vorname, nachname, telefonnummer, strasse, "", unternehmensdetails, stadt, plz, anrede,
                  standard, land, hausnummer, standard_lieferadresse, user,))
        c.execute("""insert into keyuserdaten values (%s,%s,%s,%s,%s,%s)""", (email, telefonnummer, "", "", "", user,))

        if standard == "ja":
            c.execute("""update userdaten set vorname=%s, nachname=%s, telefon=%s,lastplz=%s where gutscheincode=%s""",
                      (vorname, nachname, telefonnummer, plz, user,))

        conn.commit()
        count_rows = c.execute("""select * from adressbuch where gutscheincode=%s """, (user,))
        c.execute(count_rows)
        postion_data_entry = c.rowcount - 1
        status = 1
    print(hinzufuegen)
    if hinzufuegen == "0":

        c.execute(
            """update %s set vorname=%%s, nachname=%%s,telefonnummer=%%s,adresse=%%s,apt=%%s,unternehmensdetails=%%s,stadt=%%s,plz=%%s,anrede=%%s,land=%%s,hausnummer=%%s,standard=%%s,standardlieferadresse=%%s where email=%%s and indexnummer=%%s and gutscheincode=%%s""" % (
            "adressbuch"), (
            vorname, nachname, telefonnummer, strasse, "", unternehmensdetails, stadt, plz, anrede, land, hausnummer,
            standard, standard_lieferadresse, email, indexnummer, user,))
        c.execute("""insert into keyuserdaten values (%s,%s,%s,%s,%s,%s)""", (email, telefonnummer, "", "", "", user,))

        c.execute("""select * from adressbuch where gutscheincode=%s """, (user,))
        adressdaten = c.fetchall()
        zaehler = 0
        for row_2 in adressdaten:
            if row_2[1] == indexnummer:
                postion_data_entry = zaehler
            zaehler = zaehler + 1

        if standard == "ja":
            c.execute("""update userdaten set vorname=%s, nachname=%s, telefon=%s,lastplz=%s where gutscheincode=%s""",
                      (vorname, nachname, telefonnummer, plz, user,))
        conn.commit()

    if hinzufuegen == "-1":
        c.execute("""delete from %s where email=%%s and indexnummer=%%s and gutscheincode=%%s""" % ("adressbuch"),
                  (email, indexnummer, user,))
        conn.commit()

    if hinzufuegen == "-2":
        c.execute("""select * from adressbuch where gutscheincode=%s """, (user,))
        data_table = c.fetchall()

        for row_2 in data_table:
            c.execute("""update %s set standard=%%s where email=%%s and indexnummer=%%s and gutscheincode=%%s""" % (
            "adressbuch"), ("nein", email, row_2[1], user,))
            conn.commit()

        c.execute(
            """update %s set standard=%%s where email=%%s and indexnummer=%%s and gutscheincode=%%s""" % ("adressbuch"),
            (standard, email, indexnummer, user,))
        conn.commit()
        c.execute("""update userdaten set lastplz=%s where gutscheincode=%s""", (plz, user,))
        conn.commit()
    return postion_data_entry


@csrf_exempt
def adresse_speichern(request):
    if request.is_ajax() and request.POST:

        hinzufuegen = request.POST.get('hinzufuegen')
        vorname = request.POST.get('vorname')
        nachname = request.POST.get('nachname')
        telefonnummer = request.POST.get('telefonnummer')
        strasse = request.POST.get('strasse')
        unternehmensdetails = request.POST.get('unternehmensdetails')
        stadt = request.POST.get('stadt')
        plz = request.POST.get('plz')
        indexnummer = request.POST.get('indexnummer')
        standard = request.POST.get('standard')
        land = request.POST.get('land')
        anrede = request.POST.get('anrede')
        hausnummer = request.POST.get('hausnummer')

        hinzufuegen_lieferadresse = request.POST.get('hinzufuegen_lieferadresse')
        vorname_lieferadresse = request.POST.get('vorname_lieferadresse')
        nachname_lieferadresse = request.POST.get('nachname_lieferadresse')
        telefonnummer_lieferadresse = request.POST.get('telefonnummer_lieferadresse')
        strasse_lieferadresse = request.POST.get('strasse_lieferadresse')
        unternehmensdetails_lieferadresse = request.POST.get('unternehmensdetails_lieferadresse')
        stadt_lieferadresse = request.POST.get('stadt_lieferadresse')
        plz_lieferadresse = request.POST.get('plz_lieferadresse')
        indexnummer_lieferadresse = request.POST.get('indexnummer_lieferadresse')
        standard_2 = request.POST.get('standard_2')

        land_lieferadresse = request.POST.get('land_lieferadresse')
        anrede_lieferadresse = request.POST.get('anrede_lieferadresse')
        hausnummer_lieferadresse = request.POST.get('hausnummer_lieferadresse')

        standard_lieferadresse = request.POST.get('standard_lieferadresse')
        email = request.POST.get('email')

        wie_viele_adressen_checken = request.POST.get('wie_viele_adressen_checken')

        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)

        x = str(request.session.session_key)

        if email != "":
            gutscheincode = get_userid_from_session_id(c, x)

            email = email.lower()
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip_adresse = x_forwarded_for.split(',')[0]
            else:
                ip_adresse = request.META.get('REMOTE_ADDR')

            current_time = datetime.datetime.now(pytz.timezone('Europe/Berlin')).time()
            now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
            date_ = str(now.year) + str((now.month) - 1) + str(now.day)
            time_ = str(current_time)
            time__ = time_.replace(":", "")
            time__ = time__.replace(".", "")

            if x != "None":
                c.execute("""select * from userdaten where email=%s """, (email,))

                for row in c:
                    gutscheincode = row[11]
                    if row[0] == email:
                        if (row[26] == "yes" and row[1] != "") or (row[26] != "yes"):
                            status = 1

            status = 0

            security_code = id_generator_long()
            password_new = id_generator_short()

            count_rows_bestellt_table = c.execute("""select * from anmeldebestaetigungen where userid=%s """,
                                                  (gutscheincode,))
            c.execute(count_rows_bestellt_table)
            zaehler_anmeldungen = int(c.rowcount)

            if zaehler_anmeldungen == 0:
                c.execute("""insert into anmeldebestaetigungen values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (
                email, security_code, ip_adresse, "", date_, "", time__, "", 0, "", "false", gutscheincode,
                password_new,))

            password_hash = hashlib.sha512(password_new).hexdigest()

            c.execute("""update userdaten set email=%s, passwort=%s,emailquiz=%s where gutscheincode=%s""",
                      (email, password_hash, email, gutscheincode,))

            conn.commit()

        postion_data_entry = [[] for i in range(2)]
        postion_data_entry[0] = 0
        postion_data_entry[1] = 0
        print("ES geht los")
        i = 0
        status = 0
        postion_data_entry_1 = 0
        postion_data_entry_2 = 0
        json_string = ""
        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            userdaten = c.fetchall()
            for row in userdaten:
                user = row[11]
                print(wie_viele_adressen_checken)
                while i <= int(wie_viele_adressen_checken):
                    if i == 0:
                        print("postion_data_entry_1")
                        postion_data_entry_1 = adresse_hinzufuegen(hinzufuegen, vorname, nachname, telefonnummer,
                                                                   strasse, unternehmensdetails, stadt, plz,
                                                                   indexnummer, standard, land, anrede, hausnummer,
                                                                   standard_lieferadresse, c, conn, row[11], row[0], x)
                    else:
                        postion_data_entry_2 = adresse_hinzufuegen(hinzufuegen_lieferadresse, vorname_lieferadresse,
                                                                   nachname_lieferadresse, telefonnummer_lieferadresse,
                                                                   strasse_lieferadresse,
                                                                   unternehmensdetails_lieferadresse,
                                                                   stadt_lieferadresse, plz_lieferadresse,
                                                                   indexnummer_lieferadresse, standard_2,
                                                                   land_lieferadresse, anrede_lieferadresse,
                                                                   hausnummer_lieferadresse, standard_lieferadresse, c,
                                                                   conn, row[11], row[0], x)
                    i = i + 1

                rebates_details = define_rebates(user, "", "", "", "", c, conn, define_standard_lieferadresse(user, c),
                                                 "no", "no", "no")

                adressbuch_daten = []

                class Adressbuch_Daten(object):
                    def __init__(self, postion_data_entry_1, postion_data_entry_2, adressbuch, rebates):
                        self.postion_data_entry_1 = postion_data_entry_1
                        self.postion_data_entry_2 = postion_data_entry_2
                        self.adressbuch = adressbuch
                        self.rebates = rebates

                adressbuch_daten.append(
                    Adressbuch_Daten(postion_data_entry_1, postion_data_entry_2, define_adressbuch(user, c),
                                     rebates_details))

                json_string = json.dumps([Adressbuch_Daten.__dict__ for Adressbuch_Daten in adressbuch_daten])

        conn.close()

        return HttpResponse(json.dumps(json_string), content_type='application/json')
    else:
        raise Http404


@csrf_exempt
def get_adressbuch_daten(request):
    if request.is_ajax() and request.POST:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)
        x = str(request.session.session_key)
        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            userdaten = c.fetchall()
            for row in userdaten:
                user = row[11]
        conn.close()
        return HttpResponse(json.dumps(define_adressbuch(user, c)), content_type='application/json')
    else:
        raise Http404


def passwort_bearbeiten(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database')
    c = conn.cursor(buffered=True)

    x = str(request.session.session_key)
    login = "false"
    status = 0
    modelAB = ""
    sub_picture = ""
    user = ""

    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        for row in c:
            password = "ok"
            status = 1
            bereitsbestellt = row[75]
            bereitsversandt = row[76]
            wishlist = row[65]
            warenkorb = row[66]
            email = row[0]
            user = row[11]
            vorname = row[2]
            nachname = row[3]
            default_bra_size = row[58]
            default_panty_size = row[59]
            facebookid = row[12]
            quiz = row[26]
            stadt = row[6]
            plz = row[4]
            modelAB = row[47]
            sub_picture = row[48]
            wishlist_quantity = row[16]
            cart_quantity = row[17]
            if row[1] == "":
                password = "not ok"
            if (row[0] != "" and row[12] != "") or (row[0] != "" and row[1] != ""):
                login = "true"
            if row[22] == "VIP" and row[23] == "true":
                VIP = "VIP"
            else:
                VIP = "Regular"

    if status == 0:
        if x != "None":
            x = str(request.session.session_key)
            create_user(x, c, conn)
        else:
            print(request.path + ",create_new_request," + x)
            log_out_do_it(x, c, conn)
            request.session.create()
            x = str(request.session.session_key)
            create_user(x, c, conn)

        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            for row in c:
                email = row[0]
                bereitsbestellt = row[75]
                bereitsversandt = row[76]
                user = row[11]
                vorname = row[2]
                nachname = row[3]
                default_bra_size = row[58]
                default_panty_size = row[59]
                facebookid = row[12]
                quiz = row[26]
                stadt = row[6]
                plz = row[4]
                modelAB = row[47]
                sub_picture = row[48]
                wishlist_quantity = row[16]
                cart_quantity = row[17]
                if row[22] == "VIP" and row[23] == "true":
                    VIP = "VIP"
                else:
                    VIP = "Regular"

    if login != "false":
        t = get_template('passwort_aendern.html')
        html = t.render({'user_id_google_analytics': get_google_analytics_user_id(login, user), 'password': password,
                         'email': email, 'bereitsbestellt': bereitsbestellt, 'bereitsversandt': bereitsversandt,
                         'fb_link': 'https://www.darlinglace.com',
                         'fb_title': ("Liebst du Lingerie? Erhalte Dein BH Set ab 29,95 EUR!").encode('utf8'),
                         'fb_description': (
                         "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                             'utf8'), 'fb_description': (
            "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                'utf8'), 'fb_image': 'https://www.darlinglace.com/static/overall_picture_bra.jpg', 'vorname': vorname,
                         'nachname': nachname, 'stadt': stadt, 'plz': plz, 'wishlist': wishlist, 'warenkorb': warenkorb,
                         'favicon': get_favicon(), 'path': request.path, 'brand_name': 'Darling Lace',
                         'title': "Passwort bearbeien | Darling Lace",
                         'bestellungen': define_bestellung(user, "all", c, "nein"), 'links': get_links(quiz),
                         'wishlist': wishlist, 'warenkorb': warenkorb, "login": login})
        conn.close()
        return HttpResponse(html)
    else:
        path = request.path
        html = call_login_page(path, c, x)
        conn.close()
        return HttpResponse(html)


@csrf_exempt
def passwort_aktualisieren(request):
    if request.is_ajax() and request.POST:
        altes_passwort = request.POST.get('altes_passwort')
        neues_passwort = request.POST.get('neues_passwort')

        altes_passwort = hashlib.sha512(altes_passwort).hexdigest()
        neues_passwort = hashlib.sha512(neues_passwort).hexdigest()

        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)

        x = str(request.session.session_key)

        status = ""
        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            userdaten = c.fetchall()
            for row in userdaten:
                user = row[11]

                if row[1] == altes_passwort:
                    status = "ok"

        if status == "ok" or row[1] == "":
            status = "ok"
            c.execute("""update userdaten set passwort=%s where gutscheincode=%s""", (neues_passwort, user,))
            conn.commit()
        conn.close()
        return HttpResponse(json.dumps(status), content_type='application/json')
    else:
        raise Http404


@csrf_exempt
def check_mobilnummer(request):
    if request.is_ajax() and request.POST:
        telefonnummer = request.POST.get('telefonnummer')
        telefonnummer2 = request.POST.get('telefonnummer2')
        telefonnummer = validate_mobilnummer(telefonnummer)
        telefonnummer2 = validate_mobilnummer(telefonnummer2)

        telefonnummern = []

        class Telefonnummern(object):
            def __init__(self, telefonnummer, telefonnummer2):
                self.telefonnummer = telefonnummer
                self.telefonnummer2 = telefonnummer2

        telefonnummern.append(Telefonnummern(telefonnummer, telefonnummer2))

        json_string = json.dumps([Telefonnummern.__dict__ for Telefonnummern in telefonnummern])

        return HttpResponse(json.dumps(json_string), content_type='application/json')


def validate_mobilnummer(telefonnummer):
    try:
        nummer = ""
        for match in phonenumbers.PhoneNumberMatcher("+49" + telefonnummer, "DE"):
            nummer = phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164)
        type = phonenumbers.number_type(phonenumbers.parse(nummer, "DE"))
        valid = phonenumbers.is_valid_number(phonenumbers.parse(nummer, "DE"))

        formatter = phonenumbers.AsYouTypeFormatter("DE")
        i = 0
        while i <= len(nummer) - 1:
            nummer_formatted = formatter.input_digit(nummer[i])
            i = i + 1
        nummer_formatted = nummer_formatted[4:]

        if str(valid) == "True" and str(type) == "1":
            return nummer_formatted
        else:
            return ""

    except:
        return ""


@csrf_exempt
def profil_aktualisieren(request):
    if request.is_ajax() and request.POST:
        vorname = request.POST.get('vorname')
        nachname = request.POST.get('nachname')
        passwort = request.POST.get('passwort')
        email = request.POST.get('email')
        telefonnummer = request.POST.get('telefonnummer')
        benachrichtigung = request.POST.get('benachrichtigung')
        newsletter = request.POST.get('newsletter')

        passwort = hashlib.sha512(passwort).hexdigest()

        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)

        x = str(request.session.session_key)

        status = ""
        try:
            validate_email(email)

        except:

            status = "e-mail nicht ok"
        email = email.lower()
        user = get_userid_from_session_id(c, x)
        if telefonnummer != "":
            telefonnummer = validate_mobilnummer(telefonnummer)
            if telefonnummer == "":
                status = "mobilnummer nicht korrekt"

        if status == "":
            if status == "":
                c.execute("""select * from userdaten where email=%s """, (email,))

                userdaten = c.fetchall()
                for row in userdaten:
                    if row[0] == email and row[11] != user:
                        status = "exists already"

                if status == "":
                    if x != "None":
                        c.execute("""select * from userdaten where gutscheincode=%s """,
                                  (get_userid_from_session_id(c, x),))
                        userdaten = c.fetchall()
                        for row in userdaten:

                            if row[1] == passwort:
                                status = "ok"
                    if status == "ok":
                        if telefonnummer == "":
                            benachrichtigung = "false"

                        c.execute(
                            """update userdaten set vorname=%s, nachname=%s,email=%s,telefon=%s,persmsbenachrichtigtwerden=%s, newslettersignedup=%s where gutscheincode=%s""",
                            (vorname, nachname, email, telefonnummer, benachrichtigung, newsletter, user,))
                        c.execute("""insert into keyuserdaten values (%s,%s,%s,%s,%s,%s)""",
                                  (row[0], telefonnummer, "", "", "", row[11],))
                        conn.commit()
        conn.close()
        return HttpResponse(json.dumps(status), content_type='application/json')
    else:
        raise Http404


def verschicke_gutscheine_send_email(request):
    if request.is_ajax() and request.GET:
        empfaenger = request.GET.get('empfaenger')
        betreff = request.GET.get('betreff')
        message = request.GET.get('message')

        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)

        print "verschicke_gutscheine_send_email"
        feedback = "ok"
        if empfaenger != "":
            empfaenger = empfaenger.split(";")

            j = 0

            while j <= len(empfaenger) - 1:
                empfaenger[j] = empfaenger[j].replace(" ", "")
                print empfaenger[j]
                try:
                    validate_email(empfaenger[j])
                except:
                    feedback = "email falsch"

                j = j + 1
        else:
            feedback = "keine email"

        if feedback == "ok":

            x = str(request.session.session_key)
            status = 0
            if x != "None":
                c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
                userdaten = c.fetchall()
                for row in userdaten:
                    code = row[11]
                    von = row[0]

            j = 0
            while j <= len(empfaenger) - 1:
                print empfaenger[j]
                c.execute("""insert into gutscheincodes_sent values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (
                code, get_date_stamp_now(), get_time_stamp_now(), empfaenger[j], "no", "", "", message, betreff, von,
                "no",))

                j = j + 1
            conn.commit()

        conn.close()
        return HttpResponse(json.dumps(feedback), content_type='application/json')
    else:
        raise Http404


def verschicke_gutscheine(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database')
    c = conn.cursor(buffered=True)

    x = str(request.session.session_key)

    login = "false"
    status = 0
    modelAB = ""
    sub_picture = ""
    user = ""

    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        for row in c:
            password = "ok"
            status = 1
            bereitsbestellt = row[75]
            bereitsversandt = row[76]
            wishlist = row[65]
            warenkorb = row[66]
            email = row[0]
            user = row[11]
            vorname = row[2]
            nachname = row[3]
            default_bra_size = row[58]
            default_panty_size = row[59]
            facebookid = row[12]
            quiz = row[26]
            stadt = row[6]
            plz = row[4]
            modelAB = row[47]
            sub_picture = row[48]
            wishlist_quantity = row[16]
            cart_quantity = row[17]
            if row[1] == "":
                password = "not ok"
            if (row[0] != "" and row[12] != "") or (row[0] != "" and row[1] != ""):
                login = "true"
            if row[22] == "VIP" and row[23] == "true":
                VIP = "VIP"
            else:
                VIP = "Regular"

    if status == 0:
        if x != "None":
            x = str(request.session.session_key)
            create_user(x, c, conn)
        else:
            print(request.path + ",create_new_request," + x)
            log_out_do_it(x, c, conn)
            request.session.create()
            x = str(request.session.session_key)
            create_user(x, c, conn)

        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            for row in c:
                email = row[0]
                bereitsbestellt = row[75]
                bereitsversandt = row[76]
                user = row[11]
                vorname = row[2]
                nachname = row[3]
                default_bra_size = row[58]
                default_panty_size = row[59]
                facebookid = row[12]
                quiz = row[26]
                stadt = row[6]
                plz = row[4]
                modelAB = row[47]
                sub_picture = row[48]
                wishlist_quantity = row[16]
                cart_quantity = row[17]
                if row[22] == "VIP" and row[23] == "true":
                    VIP = "VIP"
                else:
                    VIP = "Regular"

    if login != "false":
        t = get_template('verschicke_gutscheine.html')
        html = t.render(
            {'user_id_google_analytics': get_google_analytics_user_id(login, user), 'url': get_link_positioining(""),
             'email': email, 'bereitsbestellt': bereitsbestellt, 'bereitsversandt': bereitsversandt,
             'fb_link': 'https://www.darlinglace.com',
             'fb_title': ("Liebst du Lingerie? Erhalte Dein BH Set ab 29,95 EUR!").encode('utf8'), 'fb_description': (
                "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                'utf8'), 'fb_description': (
            "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                'utf8'), 'fb_image': 'https://www.darlinglace.com/static/overall_picture_bra.jpg', 'vorname': vorname,
             'nachname': nachname, 'stadt': stadt, 'plz': plz, 'wishlist': wishlist, 'warenkorb': warenkorb,
             'favicon': get_favicon(), 'path': request.path, 'brand_name': 'Darling Lace', 'email_from': row[0],
             'title': "Freunde einladen | Darling Lace", 'links': get_links(quiz), 'wishlist': wishlist,
             'warenkorb': warenkorb, "login": login, 'gutscheincode': user})
        conn.close()
        return HttpResponse(html)
    else:
        path = request.path
        html = call_login_page(path, c, x)
        conn.close()
        return HttpResponse(html)


def profil_bearbeiten(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database')
    c = conn.cursor(buffered=True)

    x = str(request.session.session_key)

    login = "false"
    status = 0
    modelAB = ""
    sub_picture = ""
    user = ""

    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        for row in c:
            password = "ok"
            status = 1
            bereitsbestellt = row[75]
            bereitsversandt = row[76]
            wishlist = row[65]
            warenkorb = row[66]
            email = row[0]
            user = row[11]
            vorname = row[2]
            nachname = row[3]
            default_bra_size = row[58]
            default_panty_size = row[59]
            facebookid = row[12]
            quiz = row[26]
            stadt = row[6]
            plz = row[4]
            modelAB = row[47]
            sub_picture = row[48]
            wishlist_quantity = row[16]
            cart_quantity = row[17]
            if row[1] == "":
                password = "not ok"
            if (row[0] != "" and row[12] != "") or (row[0] != "" and row[1] != ""):
                login = "true"
            if row[22] == "VIP" and row[23] == "true":
                VIP = "VIP"
            else:
                VIP = "Regular"

    if status == 0:
        if x != "None":
            x = str(request.session.session_key)
            create_user(x, c, conn)
        else:
            print(request.path + ",create_new_request," + x)
            log_out_do_it(x, c, conn)
            request.session.create()
            x = str(request.session.session_key)
            create_user(x, c, conn)

        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            for row in c:
                email = row[0]
                bereitsbestellt = row[75]
                bereitsversandt = row[76]
                user = row[11]
                vorname = row[2]
                nachname = row[3]
                default_bra_size = row[58]
                default_panty_size = row[59]
                facebookid = row[12]
                quiz = row[26]
                stadt = row[6]
                plz = row[4]
                modelAB = row[47]
                sub_picture = row[48]
                wishlist_quantity = row[16]
                cart_quantity = row[17]
                if row[22] == "VIP" and row[23] == "true":
                    VIP = "VIP"
                else:
                    VIP = "Regular"

    if login != "false":
        profildaten = define_profil(user, c)
        t = get_template('profil_bearbeiten.html')
        html = t.render(
            {'user_id_google_analytics': get_google_analytics_user_id(login, user), 'url': get_link_positioining(""),
             'password': password, 'default_bra_size': default_bra_size, 'default_panty_size': default_panty_size,
             'email': email, 'bereitsbestellt': bereitsbestellt, 'bereitsversandt': bereitsversandt,
             'fb_link': 'https://www.darlinglace.com',
             'fb_title': ("Liebst du Lingerie? Erhalte Dein BH Set ab 29,95 EUR!").encode('utf8'), 'fb_description': (
            "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                'utf8'), 'fb_description': (
            "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                'utf8'), 'fb_image': 'https://www.darlinglace.com/static/overall_picture_bra.jpg', 'vorname': vorname,
             'nachname': nachname, 'stadt': stadt, 'plz': plz, 'wishlist': wishlist, 'warenkorb': warenkorb,
             'favicon': get_favicon(), 'path': request.path, 'brand_name': 'Darling Lace',
             'title': "Profil bearbeiten | Darling Lace", 'links': get_links(quiz), 'wishlist': wishlist,
             'warenkorb': warenkorb, 'profildaten': profildaten, "login": login})
        conn.close()
        return HttpResponse(html)
    else:
        path = request.path
        html = call_login_page(path, c, x)
        conn.close()
        return HttpResponse(html)


def VIP_bearbeiten(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database')
    c = conn.cursor(buffered=True)

    x = str(request.session.session_key)

    login = "false"
    status = 0
    modelAB = ""
    sub_picture = ""
    user = ""

    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        for row in c:
            password = "ok"
            status = 1
            bereitsbestellt = row[75]
            bereitsversandt = row[76]
            wishlist = row[65]
            warenkorb = row[66]
            email = row[0]
            user = row[11]
            vorname = row[2]
            nachname = row[3]
            default_bra_size = row[58]
            default_panty_size = row[59]
            facebookid = row[12]
            quiz = row[26]
            stadt = row[6]
            plz = row[4]
            modelAB = row[47]
            sub_picture = row[48]
            wishlist_quantity = row[16]
            cart_quantity = row[17]
            VIP_member_since = row[24]
            if row[1] == "":
                password = "not ok"
            if (row[0] != "" and row[12] != "") or (row[0] != "" and row[1] != ""):
                login = "true"
            if row[22] == "VIP" and row[23] == "true":
                VIP = "VIP"
            else:
                VIP = "Regular"

    if status == 0:
        if x != "None":
            x = str(request.session.session_key)
            create_user(x, c, conn)
        else:
            print(request.path + ",create_new_request," + x)
            log_out_do_it(x, c, conn)
            request.session.create()
            x = str(request.session.session_key)
            create_user(x, c, conn)

        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            for row in c:
                email = row[0]
                bereitsbestellt = row[75]
                bereitsversandt = row[76]
                user = row[11]
                vorname = row[2]
                nachname = row[3]
                default_bra_size = row[58]
                default_panty_size = row[59]
                facebookid = row[12]
                quiz = row[26]
                stadt = row[6]
                plz = row[4]
                modelAB = row[47]
                sub_picture = row[48]
                wishlist_quantity = row[16]
                cart_quantity = row[17]
                if row[22] == "VIP" and row[23] == "true":
                    VIP = "VIP"
                else:
                    VIP = "Regular"

    if login != "false":
        if VIP == "VIP":
            skip = "false"
            skip_rueckerstattung = "false"

            store_credit = get_existing_store_credit(c, user)
            skip = check_month_VIP(user, c, VIP_member_since)
            skip_rueckerstattung = check_rueckerstattung_month_VIP(c, user)
            bra_for_free = get_bra_for_free_in_VIP_model(c, user)
            bra_ordered = get_sets_purchased_in_VIP_model(c, user)

            t = get_template('VIP_Mitgliedschaft.html')
            html = t.render({'user_id_google_analytics': get_google_analytics_user_id(login, user), 'email': email,
                             'bereitsbestellt': bereitsbestellt, 'bereitsversandt': bereitsversandt,
                             'fb_link': 'https://www.darlinglace.com',
                             'fb_title': ("Liebst du Lingerie? Erhalte Dein BH Set ab 29,95 EUR!").encode('utf8'),
                             'fb_description': (
                             "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                                 'utf8'), 'fb_description': (
                "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                    'utf8'), 'fb_image': 'https://www.darlinglace.com/static/overall_picture_bra.jpg',
                             'vorname': vorname, 'nachname': nachname, 'stadt': stadt, 'plz': plz, 'wishlist': wishlist,
                             'warenkorb': warenkorb, 'help_center': get_help_center_link(), 'favicon': get_favicon(),
                             'path': request.path, 'brand_name': 'Darling Lace',
                             'title': "VIP bearbeien | Darling Lace", 'login': login,
                             'skip_rueckerstattung': skip_rueckerstattung, 'links': get_links(quiz),
                             'wishlist': wishlist, 'warenkorb': warenkorb, 'skip': skip,
                             'guthaben': ('%.2f' % store_credit).replace('.', ','), 'bra_ordered': bra_ordered,
                             'bra_for_free': bra_for_free})
            conn.close()
            return HttpResponse(html)
        else:
            conn.close()
            return HttpResponseRedirect("/account_page/")

    else:
        path = request.path
        html = call_login_page(path, c, x)
        conn.close()
        return HttpResponse(html)


def get_existing_store_credit(c, user_id):
    c.execute("""select * from VIP_model_store_credit where gutscheincode=%s """, (user_id,))
    VIP_model_store_credit = c.fetchall()
    used_storecredit = 0
    granted_storecredit = 0
    for row_2 in VIP_model_store_credit:
        if row_2[3] > 0:
            granted_storecredit = granted_storecredit + row_2[3]
        if row_2[3] < 0:
            used_storecredit = used_storecredit + row_2[3]

    return granted_storecredit + used_storecredit


def get_bra_for_free_in_VIP_model(c, user_id):
    setspurchasedformoney = 0
    setspurchasedforfree = 0
    c.execute("""select * from VIP_model_store_credit where gutscheincode=%s """, (user_id,))
    VIP_model_store_credit = c.fetchall()
    for row in VIP_model_store_credit:
        setspurchasedformoney = setspurchasedformoney + row[8]
        setspurchasedforfree = setspurchasedforfree + row[7]

    if setspurchasedformoney > 0:
        bra_for_free = int(setspurchasedformoney / 5) - setspurchasedforfree
    else:
        bra_for_free = 0

    return bra_for_free


def get_sets_purchased_in_VIP_model(c, user_id):
    setspurchasedformoney = 0
    c.execute("""select * from VIP_model_store_credit where gutscheincode=%s """, (user_id,))
    VIP_model_store_credit = c.fetchall()
    for row in VIP_model_store_credit:
        setspurchasedformoney = setspurchasedformoney + row[8]

    if setspurchasedformoney > 0:
        bra_calc = setspurchasedformoney % 5
    else:
        bra_calc = 0

    return bra_calc


def VIP_mitgliedschaft_kuendigen(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database')
    c = conn.cursor(buffered=True)

    x = str(request.session.session_key)

    login = "false"
    status = 0
    modelAB = ""
    sub_picture = ""
    user = ""

    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        for row in c:
            password = "ok"
            status = 1
            bereitsbestellt = row[75]
            bereitsversandt = row[76]
            wishlist = row[65]
            warenkorb = row[66]
            email = row[0]
            user = row[11]
            vorname = row[2]
            nachname = row[3]
            default_bra_size = row[58]
            default_panty_size = row[59]
            facebookid = row[12]
            quiz = row[26]
            stadt = row[6]
            plz = row[4]
            modelAB = row[47]
            sub_picture = row[48]
            wishlist_quantity = row[16]
            cart_quantity = row[17]
            VIP_member_since = row[24]
            if row[1] == "":
                password = "not ok"
            if (row[0] != "" and row[12] != "") or (row[0] != "" and row[1] != ""):
                login = "true"
            if row[22] == "VIP" and row[23] == "true":
                VIP = "VIP"
            else:
                VIP = "Regular"

    if status == 0:
        if x != "None":
            x = str(request.session.session_key)
            create_user(x, c, conn)
        else:
            print(request.path + ",create_new_request," + x)
            log_out_do_it(x, c, conn)
            request.session.create()
            x = str(request.session.session_key)
            create_user(x, c, conn)

        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            for row in c:
                email = row[0]
                bereitsbestellt = row[75]
                bereitsversandt = row[76]
                user = row[11]
                vorname = row[2]
                nachname = row[3]
                default_bra_size = row[58]
                default_panty_size = row[59]
                facebookid = row[12]
                quiz = row[26]
                stadt = row[6]
                plz = row[4]
                modelAB = row[47]
                sub_picture = row[48]
                wishlist_quantity = row[16]
                cart_quantity = row[17]
                if row[22] == "VIP" and row[23] == "true":
                    VIP = "VIP"
                else:
                    VIP = "Regular"

    if login != "false":
        if VIP == "VIP":
            skip = "false"
            skip_rueckerstattung = "false"
            store_credit = get_existing_store_credit(c, user)

            skip = check_month_VIP(user, c, VIP_member_since)
            skip_rueckerstattung = check_rueckerstattung_month_VIP(c, user)

            bra_for_free = get_bra_for_free_in_VIP_model(c, user)
            bra_ordered = get_sets_purchased_in_VIP_model(c, user)

            t = get_template('VIP_Mitgliedschaft_kuendigen.html')
            html = t.render(
                {'user_id_google_analytics': get_google_analytics_user_id(login, user), 'password': password,
                 'email': email, 'bereitsbestellt': bereitsbestellt, 'bereitsversandt': bereitsversandt,
                 'fb_link': 'https://www.darlinglace.com',
                 'fb_title': ("Liebst du Lingerie? Erhalte Dein BH Set ab 29,95 EUR!").encode('utf8'),
                 'fb_description': (
                 "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                     'utf8'), 'fb_description': (
                "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                    'utf8'), 'fb_image': 'https://www.darlinglace.com/static/overall_picture_bra.jpg',
                 'vorname': vorname, 'nachname': nachname, 'stadt': stadt, 'plz': plz, 'wishlist': wishlist,
                 'warenkorb': warenkorb, 'help_center': get_help_center_link(), 'favicon': get_favicon(),
                 'path': request.path, 'brand_name': 'Darling Lace', 'title': "VIP bearbeien | Darling Lace",
                 'login': login, 'skip_rueckerstattung': skip_rueckerstattung, 'links': get_links(quiz),
                 'wishlist': wishlist, 'warenkorb': warenkorb, 'skip': skip,
                 'guthaben': ('%.2f' % store_credit).replace('.', ','), 'bra_ordered': bra_ordered,
                 'bra_for_free': bra_for_free})
            conn.close()
            return HttpResponse(html)
        else:
            conn.close()
            return HttpResponseRedirect("/account_page/")
    else:
        path = request.path
        html = call_login_page(path, c, x)
        conn.close()
        return HttpResponse(html)


def bestellung_zuruecksenden(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database')
    c = conn.cursor(buffered=True)

    x = str(request.session.session_key)

    login = "false"
    status = 0
    modelAB = ""
    sub_picture = ""
    user = ""

    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        for row in c:
            password = "ok"
            status = 1
            bereitsbestellt = row[75]
            bereitsversandt = row[76]
            wishlist = row[65]
            warenkorb = row[66]
            email = row[0]
            user = row[11]
            vorname = row[2]
            nachname = row[3]
            default_bra_size = row[58]
            default_panty_size = row[59]
            facebookid = row[12]
            quiz = row[26]
            stadt = row[6]
            plz = row[4]
            modelAB = row[47]
            sub_picture = row[48]
            wishlist_quantity = row[16]
            cart_quantity = row[17]
            VIP_member_since = row[24]
            if row[1] == "":
                password = "not ok"
            if (row[0] != "" and row[12] != "") or (row[0] != "" and row[1] != ""):
                login = "true"
            if row[22] == "VIP" and row[23] == "true":
                VIP = "VIP"
            else:
                VIP = "Regular"

    if status == 0:
        if x != "None":
            x = str(request.session.session_key)
            create_user(x, c, conn)
        else:
            print(request.path + ",create_new_request," + x)
            log_out_do_it(x, c, conn)
            request.session.create()
            x = str(request.session.session_key)
            create_user(x, c, conn)

        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            for row in c:
                email = row[0]
                bereitsbestellt = row[75]
                bereitsversandt = row[76]
                user = row[11]
                vorname = row[2]
                nachname = row[3]
                default_bra_size = row[58]
                default_panty_size = row[59]
                facebookid = row[12]
                quiz = row[26]
                stadt = row[6]
                plz = row[4]
                modelAB = row[47]
                sub_picture = row[48]
                wishlist_quantity = row[16]
                cart_quantity = row[17]
                if row[22] == "VIP" and row[23] == "true":
                    VIP = "VIP"
                else:
                    VIP = "Regular"

    if login != "false":
        bestellungen = define_bestellung(user, "all", c, "nein")
        ruecksendungen = define_ruecksendungen(user, c, modelAB, sub_picture)

        if len(bestellungen) == 2:
            status = 0

        if status == 1:
            t = get_template('Bestellung_zuruecksenden.html')
            html = t.render({'url': get_link_positioining(""),
                             'user_id_google_analytics': get_google_analytics_user_id(login, user),
                             'password': password, 'email': email, 'bereitsbestellt': bereitsbestellt,
                             'bereitsversandt': bereitsversandt, 'fb_link': 'https://www.darlinglace.com',
                             'fb_title': ("Liebst du Lingerie? Erhalte Dein BH Set ab 29,95 EUR!").encode('utf8'),
                             'fb_description': (
                             "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                                 'utf8'), 'fb_description': (
                "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                    'utf8'), 'fb_image': 'https://www.darlinglace.com/static/overall_picture_bra.jpg',
                             'vorname': vorname, 'nachname': nachname, 'stadt': stadt, 'plz': plz, 'wishlist': wishlist,
                             'warenkorb': warenkorb, 'favicon': get_favicon(), 'path': request.path,
                             'brand_name': 'Darling Lace', 'title': "Zuruecksenden | Darling Lace",
                             'links': get_links(quiz), 'wishlist': wishlist, 'warenkorb': warenkorb,
                             'bestellungen': bestellungen, 'ruecksendungen': ruecksendungen, 'login': login})
            conn.close()
            return HttpResponse(html)
        else:
            conn.close()
            return HttpResponseRedirect("/account_page/")

    else:
        path = request.path
        html = call_login_page(path, c, x)
        conn.close()
        return HttpResponse(html)


@csrf_exempt
def cancel_VIP(request):
    if request.is_ajax() and request.POST:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)

        x = str(request.session.session_key)
        gutscheincode = ""
        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            userdaten = c.fetchall()
            for row in userdaten:
                gutscheincode = row[11]

        if gutscheincode != "":
            c.execute(
                """update userdaten set shoppingtype=%s, shoppingtypeentschieden=%s,paymentidforsubscription=%s where gutscheincode=%s""",
                ("Regular", "false", "", gutscheincode,))
            conn.commit()

        conn.close()
        return HttpResponse(json.dumps(""), content_type='application/json')
    else:
        raise Http404


@csrf_exempt
def skip_VIP(request):
    if request.is_ajax() and request.POST:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)

        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        current_time = datetime.datetime.now(pytz.timezone('Europe/Berlin')).time()

        time_ = str(current_time)

        time__ = time_.replace(":", "")
        time__ = time__.replace(".", "")

        date_ = str(now.year) + "." + str((now.month) - 1) + "." + str(now.day)
        if now.day >= 1 and now.day <= 10:
            x = str(request.session.session_key)
            if x != "None":
                c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
                userdaten = c.fetchall()
                for row in userdaten:
                    c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % (
                    "VIP_model_store_credit"), (
                              date_, date_, time__, 0, "", "false", "true", 0, 0, "", date_.replace(".", ""), row[11],))
                    conn.commit()

            data = get_data_for_VIP_model(x, c, conn)
        else:
            datat = "not ok"

        conn.close()
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404


@csrf_exempt
def get_money_back_VIP(request):
    if request.is_ajax() and request.POST:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)

        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        current_time = datetime.datetime.now(pytz.timezone('Europe/Berlin')).time()

        time_ = str(current_time)

        time__ = time_.replace(":", "")
        time__ = time__.replace(".", "")
        date_now = str(now.year) + "." + str(now.month - 1) + "." + str(now.day)

        x = str(request.session.session_key)
        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            userdaten = c.fetchall()
            for row in userdaten:

                payback = check_rueckerstattung_month_VIP(c, row[11])

                payback_in_progress = payback

                c.execute(
                    """select * from VIP_model_store_credit where gutscheincode=%s ORDER BY VIPdatumforsortingpurposes DESC""",
                    (row[11],))
                VIP_model_store_credit = c.fetchall()

                for row_2 in VIP_model_store_credit:
                    if row_2[3] > 0 and row_2[5] == "no":
                        to_be_paid_back = min(row_2[3], payback_in_progress)
                        to_be_paid_back_rounded = round(to_be_paid_back, 2)
                        if to_be_paid_back > 0:
                            if to_be_paid_back_rounded == 0:
                                c.execute(
                                    """insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % (
                                    "VIP_model_store_credit"), (
                                    date_now, date_now, time__, -to_be_paid_back, "", "yes", "", 0, 0, row_2[9],
                                    date_now, row[11]))
                                conn.commit()
                            else:
                                payback_in_progress = payback_in_progress - to_be_paid_back
                                if row[56] != "klarna" and row[56] != "paypal" and row[56] != "sofort":

                                    payment_credit_card_paypal_refund(row_2[9], to_be_paid_back)
                                    c.execute(
                                        """insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % (
                                        "VIP_model_store_credit"), (
                                        date_now, date_now, time__, -to_be_paid_back, "", "yes", "", 0, 0, row_2[9],
                                        date_now, row[11]))
                                    c.execute(
                                        """update %s set rueckerstattet=%%s where paymilltransactionid=%%s and gutscheincode=%%s""" % (
                                        "VIP_model_store_credit"), ("yes", row_2[9], row[11],))
                                    conn.commit()
                                else:
                                    c.execute(
                                        """insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % (
                                        "VIP_model_store_credit"), (
                                        date_now, date_now, time__, -to_be_paid_back, "", "yes", "", 0, 0, row_2[9],
                                        date_now, row[11]))
                                    c.execute("""insert into %s values (%%s,%%s,%%s,%%s)""" % (
                                    "offenen_eigene_rechnungen_VIP"),
                                              (date_, date_, row[11], "yes", -payback_in_progress))
                                    conn.commit()
                                    von = "Internes To Do: VIP Model Abbuchung pending"
                                    email = "service@darlinglace.com"
                                    betreff = "Abbuchung VIP Model " + str(now.month) + "/" + str(
                                        now.year) + " pending: Kundennummer #" + row[11]

                                    message = """Rueckbuchnung von """ + str(
                                        payback_in_progress) + """ EUR fuer VIP Model durchzufuehren. Email-Adresse des Kunden ist """ + \
                                              row[0] + """. Zahlungsmittel ist """ + row[56]

                                    zenpy_client.tickets.create(
                                        Ticket(description=message, subject=betreff,
                                               requester=User(name=von, email=email))
                                    )

            data = get_data_for_VIP_model(x, c, conn)

        conn.close()

        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404


def get_data_for_VIP_model(x, c, conn):
    vip_model = []

    class VIP_Model(object):
        def __init__(self, guthaben, check_skip_button, check_rueckerstattung_button):
            self.guthaben = guthaben
            self.check_skip_button = check_skip_button
            self.check_rueckerstattung_button = check_rueckerstattung_button

    skip_rueckerstattung = "false"
    skip = "false"
    guthaben = 0
    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        userdaten = c.fetchall()
        for row in userdaten:
            skip = check_month_VIP(row[11], c, row[24])

            guthaben = get_existing_store_credit(c, row[11])
            skip_rueckerstattung = check_rueckerstattung_month_VIP(c, row[11])

    vip_model.append(VIP_Model(guthaben, skip, skip_rueckerstattung, ))

    json_string = json.dumps([VIP_Model.__dict__ for VIP_Model in vip_model])

    return json_string


def sendungsverfolgung_tracken(request, offset):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database')

    c = conn.cursor(buffered=True)
    x = str(request.session.session_key)

    login = "false"
    status = 0
    modelAB = ""
    sub_picture = ""
    user = ""

    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        for row in c:
            password = "ok"
            status = 1
            bereitsbestellt = row[75]
            bereitsversandt = row[76]
            wishlist = row[65]
            warenkorb = row[66]
            email = row[0]
            user = row[11]
            vorname = row[2]
            nachname = row[3]
            default_bra_size = row[58]
            default_panty_size = row[59]
            facebookid = row[12]
            quiz = row[26]
            stadt = row[6]
            plz = row[4]
            modelAB = row[47]
            sub_picture = row[48]
            wishlist_quantity = row[16]
            cart_quantity = row[17]
            VIP_member_since = row[24]
            if row[1] == "":
                password = "not ok"
            if (row[0] != "" and row[12] != "") or (row[0] != "" and row[1] != ""):
                login = "true"
            if row[22] == "VIP" and row[23] == "true":
                VIP = "VIP"
            else:
                VIP = "Regular"

    if status == 0:
        if x != "None":
            x = str(request.session.session_key)
            create_user(x, c, conn)
        else:
            print(request.path + ",create_new_request," + x)
            log_out_do_it(x, c, conn)
            request.session.create()
            x = str(request.session.session_key)
            create_user(x, c, conn)

        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            for row in c:
                email = row[0]
                bereitsbestellt = row[75]
                bereitsversandt = row[76]
                user = row[11]
                vorname = row[2]
                nachname = row[3]
                default_bra_size = row[58]
                default_panty_size = row[59]
                facebookid = row[12]
                quiz = row[26]
                stadt = row[6]
                plz = row[4]
                modelAB = row[47]
                sub_picture = row[48]
                wishlist_quantity = row[16]
                cart_quantity = row[17]
                if row[22] == "VIP" and row[23] == "true":
                    VIP = "VIP"
                else:
                    VIP = "Regular"

    if login != "false":
        bestellungen = define_bestellung(user, offset, c, "nein")
        tracking_number = get_tracking_number(user, offset, c)
        sendungsverfolgung = define_sendungsverfolgung(tracking_number)

        if len(bestellungen) == 2:
            status = 0

        if status == 1:
            t = get_template('Sendung_verfolgen.html')
            html = t.render(
                {'user_id_google_analytics': get_google_analytics_user_id(login, user), 'password': password,
                 'bestellungen': bestellungen, 'login': 'true', 'email': email, 'bereitsbestellt': bereitsbestellt,
                 'bereitsversandt': bereitsversandt, 'fb_link': 'https://www.darlinglace.com',
                 'fb_title': ("Liebst du Lingerie? Erhalte Dein BH Set ab 29,95 EUR!").encode('utf8'),
                 'fb_description': (
                 "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                     'utf8'), 'fb_description': (
                "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                    'utf8'), 'fb_image': 'https://www.darlinglace.com/static/overall_picture_bra.jpg',
                 'vorname': vorname, 'nachname': nachname, 'stadt': stadt, 'plz': plz, 'wishlist': wishlist,
                 'warenkorb': warenkorb, 'favicon': get_favicon(), 'path': request.path, 'brand_name': 'Darling Lace',
                 'title': "Sendung verfolgen | Darling Lace", 'links': get_links(quiz), 'wishlist': wishlist,
                 'warenkorb': warenkorb, 'sendungsverfolgung': sendungsverfolgung, 'tracking_number': tracking_number})
            conn.close()
            return HttpResponse(html)
        else:
            conn.close()
            return HttpResponseRedirect("/account_page/")

    else:
        path = request.path
        html = call_login_page(path, c, x)
        conn.close()
        return HttpResponse(html)


def check_whether_logged_in(x, c):
    data = "no"
    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        userdaten = c.fetchall()
        for row in userdaten:
            print row[0] + "!= and " + row[1] + "!=) or " + row[12] + "=="
            if (row[0] != "" and row[1] != "") or row[12] != "":
                data = "yes"

    return data


@csrf_exempt
def check_log_in(request):
    #print("adfadsfadsf")
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')

        c = conn.cursor(buffered=True)
        x = str(request.session.session_key)
        data = check_whether_logged_in(x, c)
        #print(data)
        conn.close()
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404


@csrf_exempt
def ruecksendung_calcualte_wert(request):
    if request.is_ajax() and request.POST:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)
        bestellnummer = request.POST.get('bestellnummer')
        stylecode = request.POST.get('stylecode')
        colorcode = request.POST.get('colorcode')
        anzahl = request.POST.get('anzahl')
        grund = request.POST.get('grund')
        gesamt = request.POST.get('gesamt')
        bhgroesse = request.POST.get('bhgroesse')
        slipgroesse = request.POST.get('slipgroesse')

        h = int(request.POST.get('item-length'))

        x = str(request.session.session_key)

        user = get_userid_from_session_id(c, x)
        stylecode = stylecode.split(";")
        colorcode = colorcode.split(";")
        bhgroesse = bhgroesse.split(";")
        slipgroesse = slipgroesse.split(";")
        anzahl = anzahl.split(";")

        return HttpResponse(json.dumps(
            define_ruecksende_value(c, bestellnummer, stylecode, colorcode, bhgroesse, slipgroesse, anzahl, user,
                                    conn)), content_type='application/json')
        conn.close()
    else:
        raise Http404


@csrf_exempt
def rueckerstattung_veranlassen(request):
    if request.is_ajax() and request.POST:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)
        id = request.POST.get('id')
        amount = request.POST.get('amount')

        c.execute("""select * from %s """ % ("ruecksendungen_gesamt"))
        ruecksendungen_gesamt = c.fetchall()
        zahlungsmethode = ""
        for row in ruecksendungen_gesamt:
            if row[0] == id:
                c.execute("""select * from bestellt where gutscheincode=%s """, (row[1],))
                bestellt_daten = c.fetchall()
                for row_2 in bestellt_daten:
                    if row_2[21] == row[2]:
                        zahlungsmethode = row_2[10]
                        transaction_id = row_2[38]
                        bestellnummer = row_2[21]
                        klarna_invoice_number = row_2[54]

        feedback = "error"
        if zahlungsmethode == "0" or zahlungsmethode == "3":  # kreditkarte+sepa
            payment_credit_card_paypal_refund(transaction_id, amount)
            feedback = "Rueckerstattung ueber Paymill erfolgt"
            c.execute("""update %s set geldzurueckueberwiesen=%%s where id=%%s""" % ("ruecksendungen_gesamt"),
                      ("true", id,))
            c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s)""" % ("rechnungsnummer"),
                      (id_generator("rechnungsnummer", c, conn), "", usercode, "", id, "",))
            conn.commit()

        if zahlungsmethode == "1":  # paypal
            send_email_reminder_sofortueberweisung("service@darlinglace.com", bestellnummer, amount, "paypal")
            feedback = "Ueberweisung fuer Paypal noch durchzufuehren. Reminder per an Support Tool Zendesk versandt."
            c.execute("""update %s set geldzurueckueberwiesen=%%s where id=%%s""" % ("ruecksendungen_gesamt"),
                      ("true", id,))
            c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s)""" % ("rechnungsnummer"),
                      (id_generator("rechnungsnummer", c, conn), "", usercode, "", id, "",))
            conn.commit()

        if zahlungsmethode == "2":  # sofortueberweisung
            send_email_reminder_sofortueberweisung("service@darlinglace.com", bestellnummer, amount,
                                                   "sofortueberweisung")
            feedback = "Ueberweisung fuer sofortueberweisung noch durchzufuehren. Reminder per an Support Tool Zendesk versandt."
            c.execute("""update %s set geldzurueckueberwiesen=%%s where id=%%s""" % ("ruecksendungen_gesamt"),
                      ("true", id,))
            c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s)""" % ("rechnungsnummer"),
                      (id_generator("rechnungsnummer", c, conn), "", usercode, "", id, "",))
            conn.commit()

        if zahlungsmethode == "4":  # klarna
            feedback_klarna = refund_klarna_rechnung(transaction_id, amount, id, klarna_invoice_number)
            #            send_email_reminder_sofortueberweisung("service@darlinglace.com",bestellnummer,amount,"sofortueberweisung")
            feedback = "Rueckerstattung ueber Klarna beantragt"
            c.execute("""update %s set geldzurueckueberwiesen=%%s where id=%%s""" % ("ruecksendungen_gesamt"),
                      ("true", id,))
            c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s)""" % ("rechnungsnummer"),
                      (id_generator("rechnungsnummer", c, conn), "", usercode, "", id, feedback_klarna,))
            conn.commit()

        conn.close()
        return HttpResponse(json.dumps(feedback), content_type='application/json')
    else:
        raise Http404


def send_email_reminder_sofortueberweisung(to, bestellnummer, amount, zahlungsmittel):
    # me == my email address
    # you == recipient's email address

    von = "Internes To Do"
    email = "service@darlinglace.com"
    betreff = "Erstattung Ruecksendung ueber " + zahlungsmittel

    message = """Erstattung von """ + str(
        amount) + """ EUR noch durchzufuehren. Bestellnummer ist""" + bestellnummer + """. Zahlungsmittel ist """ + zahlungsmittel

    creds = {
        'email': 'service@darlinglace.com',
        'token': 'oY8q9R9T4io7ZwQ1KdDktKwXgF3sWhMneMECjpL0',
        'subdomain': 'darlinglace'
    }
    zenpy_client = Zenpy(**creds)

    zenpy_client.tickets.create(
        Ticket(description=message, subject=betreff,
               requester=User(name=von, email=email))
    )


@csrf_exempt
def rueckversand_erhalten(request):
    if request.is_ajax() and request.POST:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)
        status = request.POST.get('status')
        id = request.POST.get('id')
        bhgroesse = request.POST.get('bhgroesse')
        slipgroesse = request.POST.get('slipgroesse')
        anzahl = request.POST.get('anzahl')
        stylecode = request.POST.get('stylecode')
        colorcode = request.POST.get('colorcode')
        usercode = request.POST.get('usercode')

        c.execute(
            """update %s set status=%%s where id=%%s and bhgroesse=%%s and slipgroesse=%%s""" % ("ruecksendungen"),
            (status, id, bhgroesse, slipgroesse,))

        conn.commit()

        current_time = datetime.datetime.now(pytz.timezone('Europe/Berlin')).time()
        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))

        Wochentag = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
        Monat = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober",
                 "November", "Dezember"]
        date = str(now.day) + ". " + Monat[(now.month) - 1] + " " + str(now.year)
        date_short = str(now.day) + ". " + Monat[(now.month) - 1] + " " + str(now.year)
        date_ = str(now.year) + str((now.month) - 1) + str(now.day)
        time_ = str(current_time)

        time__ = time_.replace(":", "")
        time__ = time__.replace(".", "")

        c.execute("""select * from %s """ % ("stylecode"))
        stylecode_ = c.fetchall()
        for row_12 in stylecode_:
            if row_12[1] == stylecode:
                if (colorcode == str(row_12[2])) and (bhgroesse == str(row_12[3])):
                    bestelltemengebestellt = row_12[5] + int(anzahl)
                    c.execute(
                        """update %s set bestelltemengebestellt=%%s where size=%%s and color=%%s and stylecode=%%s""" % (
                        "stylecode"), (bestelltemengebestellt, row_12[3], colorcode, stylecode,))
                    c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % ("supply_order_log"),
                              (usercode, date, time__, stylecode, colorcode, bhgroesse, slipgroesse, anzahl,))
                    conn.commit()
                if (colorcode == str(row_12[2])) and slipgroesse == str(row_12[3]):
                    bestelltemengebestellt = row_12[5] + int(anzahl)
                    c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % ("supply_order_log"),
                              (usercode, date, time__, stylecode, colorcode, bhgroesse, slipgroesse, anzahl,))
                    c.execute(
                        """update %s set bestelltemengebestellt=%%s where size=%%s and color=%%s and stylecode=%%s""" % (
                        "stylecode"), (bestelltemengebestellt, row_12[3], colorcode, stylecode,))
                    conn.commit()

        conn.close()
        return HttpResponse(json.dumps(""), content_type='application/json')
    else:
        raise Http404


@csrf_exempt
def ruecksendung_beauftragen(request):
    if request.is_ajax() and request.POST:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')

        c = conn.cursor(buffered=True)
        bestellnummer = request.POST.get('bestellnummer')
        stylecode = request.POST.get('stylecode')
        colorcode = request.POST.get('colorcode')
        anzahl = request.POST.get('anzahl')
        grund = request.POST.get('grund')
        gesamt = request.POST.get('gesamt')
        bhgroesse = request.POST.get('bhgroesse')
        slipgroesse = request.POST.get('slipgroesse')

        h = int(request.POST.get('item-length'))

        x = str(request.session.session_key)

        user = get_userid_from_session_id(c, x)
        stylecode = stylecode.split(";")
        colorcode = colorcode.split(";")
        bhgroesse = bhgroesse.split(";")
        slipgroesse = slipgroesse.split(";")
        anzahl = anzahl.split(";")
        grund = grund.split(";")

        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        Monat = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober",
                 "November", "Dezember"]
        now_date = str(now.day) + ". " + str(Monat[now.month - 1]) + " " + str(now.year)
        future = now + datetime.timedelta(days=35)
        future_date = str(future.day) + ". " + str(Monat[future.month - 1]) + " " + str(future.year)

        x = str(request.session.session_key)
        session_key = get_userid_from_session_id(c, x)
        gutscheincode = session_key

        new_ruecksendung = 0
        j = 0
        c.execute("""select * from userdaten where gutscheincode=%s """, (session_key,))
        userdaten = c.fetchall()

        for row in userdaten:
            modelAB = row[47]
            sub_picture = row[48]
            email = row[0]

            credit = float(row[10])
            braforfreecount = get_bra_for_free_in_VIP_model(c, row[11])

            storecredit = get_existing_store_credit(c, row[11])

            c.execute("""select * from bestellt where gutscheincode=%s """, (row[11],))

            bestellt_data = c.fetchall()

            for row_2 in bestellt_data:
                if row_2[21] == bestellnummer:
                    gutscheincode = row_2[18]
                    land = row_2[45]

                    land = row_2[4]
                    j = 0
                    while j <= len(stylecode) - 1:
                        c.execute("""select * from cart_details where gutscheincode=%s and bestellnummer=%s""",
                                  (row[11], bestellnummer,))
                        data_table = c.fetchall()
                        for row_3 in data_table:
                            stylecode_ = stylecode[j]
                            colorcode_ = colorcode[j]
                            bh_groesse_ = bhgroesse[j]
                            slip_groesse_ = slipgroesse[j]
                            anzahl_ = anzahl[j]

                            print row_3[7] + "==" + stylecode_ + "and" + row_3[4] + "==" + colorcode_ + "and" + row_3[
                                2] + "==" + bh_groesse_ + "and" + row_3[3] + "==" + slip_groesse_ + "and" + row_3[
                                      9] + "==lingerie"
                            if row_3[7] == stylecode_ and row_3[4] == colorcode_ and row_3[2] == bh_groesse_ and row_3[
                                3] == slip_groesse_ and row_3[9] == "lingerie":
                                c.execute(
                                    """update cart_details set imzuruecksendungsprozess=%s,anzahlimzuruecksendungsprozess=%s where stylecode=%s and color=%s and bhgroesse=%s and slipgroesse=%s and productgroup=%s and bestellnummer=%s""",
                                    ("ja", anzahl_, stylecode_, colorcode_, bh_groesse_, slip_groesse_, "lingerie",
                                     bestellnummer,))

                                new_ruecksendung = new_ruecksendung + row_3[8] * int(anzahl_)
                            if row_3[4] == colorcode_ and row_3[3] == slip_groesse_ and row_3[9] == "panties":
                                c.execute(
                                    """update cart_details set imzuruecksendungsprozess=%s,anzahlimzuruecksendungsprozess=%s where color=%s and slipgroesse=%s and productgroup=%s and bestellnummer=%s""",
                                    ("ja", anzahl_, colorcode_, slip_groesse_, "panties", bestellnummer))
                                new_ruecksendung = new_ruecksendung + row_3[8] * int(anzahl_)
                        j = j + 1

        conn.commit()
        print "haaaaaaaaaaalllooo"
        behalten_1 = define_rebates_for_ruecksendung(session_key, bestellnummer, c, "nein")
        gesamtbestellung = define_rebates(session_key, bestellnummer, "", "", "", c, conn, "", "no", "no", "no")
        behalten_alt = define_ruecksendungen_gesamt(session_key, c, bestellnummer)

        print behalten_1

        print gesamtbestellung
        print behalten_alt

        code = id_generator("userid", c, conn)

        behalten_1 = json.loads(behalten_1)
        gesamtbestellung = json.loads(gesamtbestellung)
        behalten_alt = json.loads(behalten_alt)

        setspurchasedformoney = 0
        setspurchasedforfree = 0
        c.execute("""select * from VIP_model_store_credit where gutscheincode=%s and bestellnummer=%s """,
                  (session_key, bestellnummer,))
        VIP_model_store_credit = c.fetchall()
        for row in VIP_model_store_credit:
            setspurchasedformoney = setspurchasedformoney + row[8]

        print "braforfreecount=setspurchasedformoney+(int(gesamtbestellung[0]['braforfreecount'])-int(behalten_1[0]['braforfreecount'])+int(behalten_alt[0]['bra4free']))"

        print str(setspurchasedformoney) + "+" + str(gesamtbestellung[0]['braforfreecount']) + "-" + str(
            behalten_1[0]['braforfreecount']) + "+" + str(behalten_alt[0]['bra4free'])

        if int(behalten_alt[0]['bra4free']) != 0:
            braforfreecount = setspurchasedformoney + (
                    -int(behalten_1[0]['braforfreecount']) + int(behalten_alt[0]['bra4free']))
        else:
            braforfreecount = setspurchasedformoney + (
                    -int(behalten_1[0]['braforfreecount']) + int(gesamtbestellung[0]['braforfreecount']))

        print "storecredit=storecredit+(-float(behalten_1[0]['storecredit'])+float(behalten_alt[0]['storecredit']))"
        print str(storecredit) + "+" + "(-" + str(behalten_1[0]['storecredit']) + "+" + str(
            behalten_alt[0]['storecredit'])

        if float(behalten_alt[0]['storecredit']) != 0:
            storecredit = storecredit + (-float(behalten_1[0]['storecredit']) + float(behalten_alt[0]['storecredit']))
        else:
            storecredit = storecredit + (
                    -float(behalten_1[0]['storecredit']) + float(gesamtbestellung[0]['storecredit']))

        print "credit=credit+(-float(behalten_1[0]['credit'])+float(behalten_alt[0]['credit']))+"
        print str(credit) + "+(-" + str(behalten_1[0]['credit']) + "+" + str(behalten_alt[0]['credit'])
        if float(behalten_alt[0]['credit']) != 0:
            credit = credit + (-float(behalten_1[0]['credit']) + float(behalten_alt[0]['credit']))
        else:
            credit = credit + (-float(behalten_1[0]['credit']) + float(gesamtbestellung[0]['credit']))

        coupon = behalten_1[0]['coupon']

        warenwert = float(gesamtbestellung[0]['bestellung']) - float(behalten_1[0]['bestellung']) - float(
            behalten_alt[0]['warenwert'])
        erstattung = float(gesamtbestellung[0]['gesamtpreis']) - float(behalten_1[0]['gesamtpreis']) - float(
            behalten_alt[0]['erstattung'])

        print "erstattung=float(gesamtbestellung[0]['gesamtpreis'])-float(behalten_1[0]['gesamtpreis'])+float(behalten_alt[0]['erstattung'])"
        print gesamtbestellung[0]['gesamtpreis']
        print behalten_1[0]['gesamtpreis']
        print behalten_alt[0]['erstattung']

        j = 0
        while j <= len(stylecode) - 1:
            c.execute("""select * from cart_details where gutscheincode=%s and bestellnummer=%s""",
                      (row[11], bestellnummer,))
            data_table = c.fetchall()
            for row_3 in data_table:
                stylecode_ = stylecode[j]
                colorcode_ = colorcode[j]
                bh_groesse_ = bhgroesse[j]
                slip_groesse_ = slipgroesse[j]
                anzahl_ = anzahl[j]
                print "grund_=grund[j]"
                print grund[j]
                grund_ = grund[j]

                print row_3[7] + "==" + stylecode_ + "and" + row_3[4] + "==" + colorcode_ + "and" + row_3[
                    2] + "==" + bh_groesse_ + "and" + row_3[3] + "==" + slip_groesse_ + "and" + row_3[9] + "==lingerie"
                if row_3[7] == stylecode_ and row_3[4] == colorcode_ and row_3[2] == bh_groesse_ and row_3[
                    3] == slip_groesse_ and row_3[9] == "lingerie":
                    c.execute(
                        """update cart_details set zurueckgesendet=%s,anzahlzurueckgesendet=%s where stylecode=%s and color=%s and bhgroesse=%s and slipgroesse=%s and productgroup=%s and bestellnummer=%s""",
                        ("ja", anzahl_, stylecode_, colorcode_, bh_groesse_, slip_groesse_, "lingerie", bestellnummer,))

                    c.execute(
                        """insert into ruecksendungen values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                        (code, session_key, bestellnummer, now_date, future_date, "dhl", grund_, stylecode_, colorcode_,
                         int(anzahl_), row_3[8], 0, "false", "false", "Auf Ruecksendung wartend", bh_groesse_,
                         slip_groesse_, "lingerie",))

                    new_ruecksendung = new_ruecksendung + row_3[8] * int(anzahl_)
                if row_3[4] == colorcode_ and row_3[3] == slip_groesse_ and row_3[9] == "panties":
                    c.execute(
                        """update cart_details set zurueckgesendet=%s,anzahlzurueckgesendet=%s where color=%s and slipgroesse=%s and productgroup=%s and bestellnummer=%s""",
                        ("ja", anzahl_, colorcode_, slip_groesse_, "panties", bestellnummer))
                    new_ruecksendung = new_ruecksendung + row_3[8] * int(anzahl_)
                    c.execute(
                        """insert into ruecksendungen values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                        (code, session_key, bestellnummer, now_date, future_date, "dhl", grund_, "", colorcode_,
                         int(anzahl_), row_3[8], 0, "false", "false", "Auf Ruecksendung wartend", "", slip_groesse_,
                         "panties",))
            j = j + 1

        ########grund[j]###############

        c.execute(
            """update VIP_model_store_credit set setspurchasedformoney=%s, storecredit=%s where bestellnummer=%s""",
            (braforfreecount, storecredit, bestellnummer,))
        c.execute("""update userdaten set credit=%s where gutscheincode=%s""", (credit, session_key,))

        conn.commit()

        j = 0
        feedback = "ok"

        bestellung = define_bestellung(session_key, bestellnummer, c, "nein")

        bestellung = json.loads(bestellung)
        c.execute("""insert into ruecksendungen_gesamt values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (
        code, session_key, bestellnummer, now_date, future_date, "dhl", warenwert, erstattung, 0, coupon, "false",
        "false", "Auf Ruecksendung wartend", "", (
                int(gesamtbestellung[0]['braforfreecount']) - int(behalten_1[0]['braforfreecount']) + int(
            behalten_alt[0]['bra4free'])),
        float(gesamtbestellung[0]['credit']) - float(behalten_1[0]['credit']) + float(behalten_alt[0]['credit']),
        float(gesamtbestellung[0]['storecredit']) - float(behalten_1[0]['storecredit']) + float(
            behalten_alt[0]['storecredit'])))
        conn.commit()
        change_lieferstatus(bestellnummer, gutscheincode, "Auf Ruecksendung wartend", "", c, conn, "")
        dhl_fill_out_form(bestellung[0]["vornamerechnung"], bestellung[0]["nachnamerechnung"],
                          bestellung[0]["strasserechnung"], bestellung[0]["hausnummerrechnung"],
                          bestellung[0]["plzrechnung"], bestellung[0]["stadtrechnung"], email, code)

        return HttpResponse(json.dumps(define_ruecksendungen(session_key, c, modelAB, sub_picture)),
                            content_type='application/json')
        conn.close()
    else:
        raise Http404


def load_account_page(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database')
    c = conn.cursor(buffered=True)

    x = str(request.session.session_key)

    login = "false"
    status = 0
    modelAB = ""
    sub_picture = ""
    user = ""

    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        for row in c:
            password = "ok"
            status = 1
            bereitsbestellt = row[75]
            bereitsversandt = row[76]
            wishlist = row[65]
            warenkorb = row[66]
            email = row[0]
            user = row[11]
            vorname = row[2]
            nachname = row[3]
            default_bra_size = row[58]
            default_panty_size = row[59]
            facebookid = row[12]
            quiz = row[26]
            stadt = row[6]
            plz = row[4]
            modelAB = row[47]
            sub_picture = row[48]
            wishlist_quantity = row[16]
            cart_quantity = row[17]
            VIP_member_since = row[24]
            vorname_nachname = row[2] + " " + row[3]
            if row[1] == "":
                password = "not ok"
            if (row[0] != "" and row[12] != "") or (row[0] != "" and row[1] != ""):
                login = "true"
            if row[22] == "VIP" and row[23] == "true":
                VIP = "VIP"
            else:
                VIP = "Regular"

    if status == 0:
        if x != "None":
            x = str(request.session.session_key)
            create_user(x, c, conn)
        else:
            print(request.path + ",create_new_request," + x)

            log_out_do_it(x, c, conn)
            request.session.create()
            x = str(request.session.session_key)
            create_user(x, c, conn)

        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            for row in c:
                email = row[0]
                bereitsbestellt = row[75]
                bereitsversandt = row[76]
                user = row[11]
                vorname = row[2]
                nachname = row[3]
                default_bra_size = row[58]
                default_panty_size = row[59]
                facebookid = row[12]
                quiz = row[26]
                stadt = row[6]
                plz = row[4]
                modelAB = row[47]
                sub_picture = row[48]
                wishlist_quantity = row[16]
                cart_quantity = row[17]
                if row[22] == "VIP" and row[23] == "true":
                    VIP = "VIP"
                else:
                    VIP = "Regular"

    if login != "false":

        t = get_template('account_page.html')

        html = t.render({'user_id_google_analytics': get_google_analytics_user_id(login, user), 'password': password,
                         'url': get_link_positioining(""), 'email': email, 'bereitsbestellt': bereitsbestellt,
                         'bereitsversandt': bereitsversandt, 'fb_link': 'https://www.darlinglace.com',
                         'fb_title': ("Liebst du Lingerie? Erhalte Dein BH Set ab 29,95 EUR!").encode('utf8'),
                         'fb_description': (
                         "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                             'utf8'), 'fb_description': (
            "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                'utf8'), 'fb_image': 'https://www.darlinglace.com/static/overall_picture_bra.jpg', 'vorname': vorname,
                         'nachname': nachname, 'stadt': stadt, 'plz': plz, 'wishlist': wishlist, 'warenkorb': warenkorb,
                         'favicon': get_favicon(), 'path': request.path, 'brand_name': 'Darling Lace',
                         'title': "Account | Darling Lace", 'links': get_links(quiz), 'gutscheincode': user,
                         'login': login, 'name': vorname_nachname, 'VIP': VIP})
        conn.close()
        return HttpResponse(html)
    else:
        path = request.path
        html = call_login_page(path, c, x)
        conn.close()
        return HttpResponse(html)


@csrf_exempt
def save_preliminary_quiz_results(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)
        x = str(request.session.session_key)

        userid = get_userid_from_session_id(c, x)

        band_click_first_id = request.GET.get('band_click_first_id')
        cup_click_first_id = request.GET.get('cup_click_first_id')
        brand_click_first_id = request.GET.get('brand_click_first_id')
        band_click_second_id = request.GET.get('band_click_second_id')
        cup_click_second_id = request.GET.get('cup_click_second_id')
        brand_click_second_id = request.GET.get('brand_click_second_id')
        question_2 = request.GET.get('question_2')
        question_3 = request.GET.get('question_3')
        question_4 = request.GET.get('question_4')
        question_5 = request.GET.get('question_5')
        question_6 = request.GET.get('question_6')
        question_6a = request.GET.get('question_6a')
        question_8 = request.GET.get('question_8')
        question_9 = request.GET.get('question_9')
        panty_id = request.GET.get('panty_id')

        if band_click_first_id != None and cup_click_first_id != None and brand_click_first_id != None:
            c.execute(
                """update userdaten set bandclickfirstid=%s,cupclickfirstid=%s,brandclickfirstid=%s where gutscheincode=%s""",
                (band_click_first_id, cup_click_first_id, brand_click_first_id, userid,))
        if band_click_second_id != None and cup_click_second_id != None and brand_click_second_id != None:
            c.execute(
                """update userdaten set bandclicksecondid=%s,cupclicksecondid=%s,brandclicksecondid=%s where gutscheincode=%s""",
                (band_click_second_id, cup_click_second_id, brand_click_second_id, userid,))

        if question_2 != None:
            c.execute("""update userdaten set question2=%s where gutscheincode=%s""", (question_2, userid,))

        if question_3 != None:
            c.execute("""update userdaten set question3=%s where gutscheincode=%s""", (question_3, userid,))
        if question_4 != None:
            c.execute("""update userdaten set question4=%s where gutscheincode=%s""", (question_4, userid,))
        if question_5 != None:
            c.execute("""update userdaten set question5=%s where gutscheincode=%s""", (question_5, userid,))
        if question_6 != None:
            c.execute("""update userdaten set question6=%s where gutscheincode=%s""", (question_6, userid,))
        if question_6a != None:
            c.execute("""update userdaten set question6a=%s where gutscheincode=%s""", (question_6a, userid,))
        if question_8 != None:
            c.execute("""update userdaten set question8=%s where gutscheincode=%s""", (question_8, userid,))

        if question_9 != None:
            c.execute("""update userdaten set question9=%s where gutscheincode=%s""", (question_9, userid,))
        if panty_id != None:
            c.execute("""update userdaten set pantyid=%s where gutscheincode=%s""", (panty_id, userid,))
        conn.commit()
        print("saved")
        conn.close()
        return HttpResponse(json.dumps(""), content_type='application/json')


    else:
        raise Http404


@csrf_exempt
def submit_quiz_results(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)
        x = str(request.session.session_key)

        userid = get_userid_from_session_id(c, x)

        band_click_first_id = request.GET.get('band_click_first_id')
        cup_click_first_id = request.GET.get('cup_click_first_id')
        brand_click_first_id = request.GET.get('brand_click_first_id').encode('utf8')
        band_click_second_id = request.GET.get('band_click_second_id')
        cup_click_second_id = request.GET.get('cup_click_second_id')
        brand_click_second_id = request.GET.get('brand_click_second_id').encode('utf8')
        question_2 = request.GET.get('question_2')
        question_3 = request.GET.get('question_3')
        question_4 = request.GET.get('question_4')
        question_5 = request.GET.get('question_5')
        question_6 = request.GET.get('question_6')
        question_6a = request.GET.get('question_6a')
        question_8 = request.GET.get('question_8')
        question_9 = request.GET.get('question_9')
        panty_id = request.GET.get('panty_id')
        email = request.GET.get('email')

        feedback = ""

        print check_whether_logged_in(x, c)
        email = email.lower()
        if check_whether_logged_in(x, c) == "no":
            try:
                validate_email(email)
            except:
                feedback = "email falsch"

            if feedback == "":
                x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
                if x_forwarded_for:
                    ip_adresse = x_forwarded_for.split(',')[0]
                else:
                    ip_adresse = request.META.get('REMOTE_ADDR')

                current_time = datetime.datetime.now(pytz.timezone('Europe/Berlin')).time()
                now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
                date_ = str(now.year) + str((now.month) - 1) + str(now.day)
                time_ = str(current_time)
                time__ = time_.replace(":", "")
                time__ = time__.replace(".", "")

                c.execute("""insert into quiz_anmeldungen values (%s,%s,%s,%s)""", (email, ip_adresse, date_, time__))
                if x != "None":
                    c.execute("""select * from userdaten where email=%s """, (email,))

                    for row in c:
                        gutscheincode = row[11]
                        if row[0] == email:
                            if (row[26] == "yes" and row[1] != "") or (row[26] != "yes"):
                                status = 1

                status = 0

                security_code = id_generator_long()
                password_new = id_generator_short()

                count_rows_bestellt_table = c.execute("""select * from anmeldebestaetigungen where userid=%s """,
                                                      (userid,))
                c.execute(count_rows_bestellt_table)
                zaehler_anmeldungen = int(c.rowcount)

                if zaehler_anmeldungen == 0:
                    c.execute("""insert into anmeldebestaetigungen values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (
                    email, security_code, ip_adresse, "", date_, "", time__, "", 0, "", "false", userid, password_new,))

                password_hash = hashlib.sha512(password_new).hexdigest()

                c.execute("""update userdaten set email=%s, passwort=%s,emailquiz=%s where gutscheincode=%s""",
                          (email, password_hash, email, userid,))
                c.execute(
                    """update userdaten set bandclickfirstid=%s,cupclickfirstid=%s,brandclickfirstid=%s,bandclicksecondid=%s,cupclicksecondid=%s,brandclicksecondid=%s,question2=%s,question3=%s,question4=%s,question5=%s,question6=%s,question6a=%s,question8=%s,question9=%s,pantyid=%s,quiztaken=%s where gutscheincode=%s""",
                    (band_click_first_id, cup_click_first_id, brand_click_first_id, band_click_second_id,
                     cup_click_second_id, brand_click_second_id, question_2, question_3, question_4, question_5,
                     question_6, question_6a, question_8, question_9, panty_id, "yes", userid,))

                conn.commit()

                generate_showroom(c, conn, band_click_first_id, cup_click_first_id, brand_click_first_id,
                                  band_click_second_id, cup_click_second_id, brand_click_second_id, question_2,
                                  question_3, question_4, question_5, question_6, question_6a, question_8, question_9,
                                  panty_id, userid)

        else:
            c.execute(
                """update userdaten set bandclickfirstid=%s,cupclickfirstid=%s,brandclickfirstid=%s,bandclicksecondid=%s,cupclicksecondid=%s,brandclicksecondid=%s,question2=%s,question3=%s,question4=%s,question5=%s,question6=%s,question6a=%s,question8=%s,question9=%s,pantyid=%s,quiztaken=%s where gutscheincode=%s""",
                (band_click_first_id, cup_click_first_id, brand_click_first_id, band_click_second_id,
                 cup_click_second_id, brand_click_second_id, question_2, question_3, question_4, question_5, question_6,
                 question_6a, question_8, question_9, panty_id, "yes", userid,))
            generate_showroom(c, conn, band_click_first_id, cup_click_first_id, brand_click_first_id,
                              band_click_second_id, cup_click_second_id, brand_click_second_id, question_2, question_3,
                              question_4, question_5, question_6, question_6a, question_8, question_9, panty_id, userid)
            conn.commit()

        conn.close()
        return HttpResponse(json.dumps(feedback), content_type='application/json')


@csrf_exempt
def referral_message_shown(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)
        x = str(request.session.session_key)

        userid = get_userid_from_session_id(c, x)

        c.execute("""update userdaten set messageshownfreundeeingeladen=%s where gutscheincode=%s""", ("yes", userid,))
        conn.commit()

        conn.close()
        return HttpResponse(json.dumps(""), content_type='application/json')


@csrf_exempt
def wishlist_abrufen(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database')
    c = conn.cursor(buffered=True)

    x = str(request.session.session_key)
    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        userdaten = c.fetchall()
        for row in userdaten:
            modelAB = row[47]
            sub_picture = row[48]
            gutscheincode = row[21]
    conn.close()
    return HttpResponse(json.dumps(define_wishlist(user, modelAB, sub_picture, c)), content_type='application/json')


def get_link_positioining(offset):
    links = {"BH Sets": 0,
             "Slips": 7,
             "Mein Showroom": 1,
             #          "Geschenkkarten" : 3,
             "": "None",
             "Wunschliste": "None",
             "schwarze_BH": 4,
             "Push-Up_BH": 2,
             "Balconette": 3,
             "kleine_groessen": 5,
             "grosse_groessen": 6,
             }

    return links[offset]


def create_user(x, q, conn_2):
    code = id_generator("userid", q, conn_2)

    now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
    Monat = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November",
             "Dezember"]
    date_short = str(now.day) + ". " + Monat[(now.month) - 1] + " " + str(now.year)

    modelAB = random.randint(0, 1)
    subpicture = random.randint(0, 2)

    clientidpaymill = ""

    newsletterabbestellencode = id_generator_long() + id_generator_long()

    q.execute(
        """insert into userdaten values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
        ("", "", "", "", "", "", "", "", "", x, 0, code, "", "", "", "", "", "", "nein", date_short, "false",
         "WILLKOMMEN", "Regular", "false", "", 0, "no", -1, -1, "", -1, -1, "", -1, -1, -1, -1, "", -1, -1, -1, -1, -1,
         "", "", "", "", modelAB, subpicture, "no", clientidpaymill, 0, 0, -1, "false", "0", "", "true", "", "", "", "",
         "", "", newsletterabbestellencode, "", "", "", "", "", "", "", "", "", "", "no", "no", "", "", "", "", "", "",
         "", "", "", "", "", "",))

    q.execute("""insert into session_id_match_userdaten values (%s,%s)""", (code, x,))

    conn_2.commit()


def create_matching_table_stammdaten_stylecodes():
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database', charset='utf8')
    c = conn.cursor(buffered=True)

    c.execute("""drop table if exists matching_table_stammdaten_stylecodes""")
    conn.commit()

    c.execute("""create table %s (
     stylecode text,
     colorcode text,
     productgroup text,
     pantytype text,
    65AA text,
    65A text,
    65B text,
    65C text,
    65D text,
    65E text,
    65F text,
    65G text,
    70AA text,
    70A text,
    70B text,
    70C text,
    70D text,
    70E text,
    70F text,
    70G text,
    75AA text,
    75A text,
    75B text,
    75C text,
    75D text,
    75E text,
    75F text,
    75G text,
    80AA text,
    80A text,
    80B text,
    80C text,
    80D text,
    80E text,
    80F text,
    80G text,
    85AA text,
    85A text,
    85B text,
    85C text,
    85D text,
    85E text,
    85F text,
    85G text,
    90AA text,
    90A text,
    90B text,
    90C text,
    90D text,
    90E text,
    90F text,
    90G text,
    95AA text,
    95A text,
    95B text,
    95C text,
    95D text,
    95E text,
    95F text,
    95G text,
    BraletteS text,
    BraletteM text,
    BraletteL text,
    BraletteXL text,
    BikiniXXS text,
    BikiniXS text,
    BikiniS text,
    BikiniM text,
    BikiniL text,
    BikiniXl text,
    BikiniXXL text,
    HipsterXXS text,
    HipsterXS text,
    HipsterS text,
    HipsterM text,
    HipsterL text,
    HipsterXl text,
    HipsterXXL text,
    BoyshortXXS text,
    BoyshortXS text,
    BoyshortS text,
    BoyshortM text,
    BoyshortL text,
    BoyshortXl text,
    BoyshortXXL text,
    ThongXXS text,
    ThongXS text,
    ThongS text,
    ThongM text,
    ThongL text,
    ThongXl text,
    ThongXXL text)""" % ("matching_table_stammdaten_stylecodes"))

    cup_table = {'AA': 0,
                 'A': 1,
                 'B': 2,
                 'C': 3,
                 'D': 4,
                 'E': 5,
                 'F': 6,
                 'G': 7,

                 }

    band_table = {'65': 0,
                  '70': 1,
                  '75': 2,
                  '80': 3,
                  '85': 4,
                  '90': 5,
                  '95': 6,

                  }

    style_table_panty = {'Bikini': 0,
                         'Hipster': 1,
                         'Boyshort': 2,
                         'Thong': 3,

                         }

    size_table_panty = {
        'XXS': 0,
        'XS': 1,
        'S': 2,
        'M': 3,
        'L': 4,
        'XL': 5,
        'XXL': 6,

    }

    c.execute("""select * from lingerieselection ORDER BY position ASC""")
    lingerieselection = c.fetchall()
    for row in lingerieselection:
        if row[7] == "yes":
            list = []
            i = 0
            while i <= 87:
                list.append("")
                i = i + 1
            c.execute("""select * from stylecode where stylecode=%s and color=%s""", (row[12], row[13],))
            stylecode_data = c.fetchall()
            for row_2 in stylecode_data:

                menge = int(row_2[4]) - int(row_2[5])
                if menge > 0:
                    if row[8] == "lingerie":
                        if row_2[0] == "BH":
                            if row_2[3] == "Bralette S":
                                list[56] = "1"
                            else:
                                if row_2[3] == "Bralette M":
                                    list[57] = "1"
                                else:
                                    if row_2[3] == "Bralette L":
                                        list[58] = "1"
                                    else:
                                        if row_2[3] == "Bralette XL":
                                            list[59] = "1"
                                        else:

                                            band = row_2[3][:2]
                                            cup = row_2[3][2:]

                                            cup_number = cup_table[cup]
                                            band_number = band_table[band]

                                            list[band_number * 8 + cup_number] = "1"

                    else:
                        if row_2[0] == "panties":
                            panty_type = row_2[3].split(" ")
                            type_number = style_table_panty[panty_type[0]]
                            size_number = size_table_panty[panty_type[1]]

                            print panty_type
                            print type_number
                            print size_number

                            list[type_number * 7 + size_number + 60] = "1"

            print "0"

            c.execute(
                """insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % (
                "matching_table_stammdaten_stylecodes"), (
                row[12], row[13], row[8], row[2], list[0], list[1], list[2], list[3], list[4], list[5], list[6],
                list[7], list[8], list[9], list[10], list[11], list[12], list[13], list[14], list[15], list[16],
                list[17], list[18], list[19], list[20], list[21], list[22], list[23], list[24], list[25], list[26],
                list[27], list[28], list[29], list[30], list[31], list[32], list[33], list[34], list[35], list[36],
                list[37], list[38], list[39], list[40], list[41], list[42], list[43], list[44], list[45], list[46],
                list[47], list[48], list[49], list[50], list[51], list[52], list[53], list[54], list[55], list[56],
                list[57], list[58], list[59], list[60], list[61], list[62], list[63], list[64], list[65], list[66],
                list[67], list[68], list[69], list[70], list[71], list[72], list[73], list[74], list[75], list[76],
                list[77], list[78], list[79], list[80], list[81], list[82], list[83], list[84], list[85], list[86],
                list[87],))

    conn.commit()


def create_total_picturelibrary_tables():
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database', charset='utf8')
    c = conn.cursor(buffered=True)

    c.execute("""drop table if exists consolidated_picturelibrary""")
    conn.commit()

    c.execute("""create table %s (
     modelAB text,
     subpicture text,
    stylecode text,
    colorcode text,
    firtorall text,
    bigorsmall text,
    picturelibrary text)""" % ("consolidated_picturelibrary"))

    conn.commit()

    i = 0
    while i <= 1:
        j = 0
        while j <= 2:
            k = 0
            while k <= 1:
                if k == 0:
                    firstorall = "first"
                else:
                    firstorall = "all"
                p = 0
                while p <= 1:
                    if p == 0:
                        bigorsmall = "small"
                    else:
                        bigorsmall = "big"

                    c.execute("""select * from lingerieselection ORDER BY position ASC""")
                    lingerieselection = c.fetchall()
                    for row in lingerieselection:
                        if row[7] == "yes":
                            picture = get_pictures(c, row[12], row[13], row[8], i, j, row[2], firstorall, bigorsmall)
                            if picture != None:
                                c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % (
                                "consolidated_picturelibrary"),
                                          (i, j, row[12], row[13], firstorall, bigorsmall, picture,))
                            print "weiter"
                    p = p + 1
                k = k + 1
            j = j + 1
        i = i + 1

    conn.commit()


def generate_standard_product_library():
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database', charset='utf8')
    c = conn.cursor(buffered=True)

    c.execute("""drop table if exists standard_product_library""")
    conn.commit()

    c.execute("""create table %s (
     lingerieselection text,
     colors text,
     filter text,
     productgroup text,
     modelAB int,
     subpicture int)""" % ("standard_product_library"))

    conn.commit()

    lingerie_offerings_0_0_lingerie = get_lingerie_selection_filter("lingerie", "", "", "", "", "", "", "", "", "", "",
                                                                    "", "", "", 0, 0, c)
    lingerie_offerings_0_1_lingerie = get_lingerie_selection_filter("lingerie", "", "", "", "", "", "", "", "", "", "",
                                                                    "", "", "", 0, 1, c)
    lingerie_offerings_0_2_lingerie = get_lingerie_selection_filter("lingerie", "", "", "", "", "", "", "", "", "", "",
                                                                    "", "", "", 0, 2, c)

    lingerie_offerings_1_0_lingerie = get_lingerie_selection_filter("lingerie", "", "", "", "", "", "", "", "", "", "",
                                                                    "", "", "", 1, 0, c)
    lingerie_offerings_1_1_lingerie = get_lingerie_selection_filter("lingerie", "", "", "", "", "", "", "", "", "", "",
                                                                    "", "", "", 1, 1, c)
    lingerie_offerings_1_2_lingerie = get_lingerie_selection_filter("lingerie", "", "", "", "", "", "", "", "", "", "",
                                                                    "", "", "", 1, 2, c)

    colors_lingerie = get_other_colors("", "", "lingerie", c)
    filter_lingerie = load_style_filter("", "", "", "", "", "BH Sets", "", "", "", "", c)

    lingerie_offerings_0_0_panties = get_lingerie_selection_filter("panties", "", "", "", "", "", "", "", "", "", "",
                                                                   "", "", "", 0, 0, c)
    lingerie_offerings_0_1_panties = get_lingerie_selection_filter("panties", "", "", "", "", "", "", "", "", "", "",
                                                                   "", "", "", 0, 1, c)
    lingerie_offerings_0_2_panties = get_lingerie_selection_filter("panties", "", "", "", "", "", "", "", "", "", "",
                                                                   "", "", "", 0, 2, c)

    lingerie_offerings_1_0_panties = get_lingerie_selection_filter("panties", "", "", "", "", "", "", "", "", "", "",
                                                                   "", "", "", 1, 0, c)
    lingerie_offerings_1_1_panties = get_lingerie_selection_filter("panties", "", "", "", "", "", "", "", "", "", "",
                                                                   "", "", "", 1, 1, c)
    lingerie_offerings_1_2_panties = get_lingerie_selection_filter("panties", "", "", "", "", "", "", "", "", "", "",
                                                                   "", "", "", 1, 2, c)

    colors_panties = get_other_colors("", "", "panties", c)

    filter_panties = load_style_filter("", "", "", "", "", "Slips", "", "", "", "", c)

    c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s)""" % ("standard_product_library"),
              (lingerie_offerings_0_0_lingerie, colors_lingerie, filter_lingerie, "lingerie", 0, 0,))
    c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s)""" % ("standard_product_library"),
              (lingerie_offerings_0_1_lingerie, colors_lingerie, filter_lingerie, "lingerie", 0, 1,))
    c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s)""" % ("standard_product_library"),
              (lingerie_offerings_0_2_lingerie, colors_lingerie, filter_lingerie, "lingerie", 0, 2,))
    c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s)""" % ("standard_product_library"),
              (lingerie_offerings_1_0_lingerie, colors_lingerie, filter_lingerie, "lingerie", 1, 0,))
    c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s)""" % ("standard_product_library"),
              (lingerie_offerings_1_1_lingerie, colors_lingerie, filter_lingerie, "lingerie", 1, 1,))
    c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s)""" % ("standard_product_library"),
              (lingerie_offerings_1_2_lingerie, colors_lingerie, filter_lingerie, "lingerie", 1, 2,))

    c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s)""" % ("standard_product_library"),
              (lingerie_offerings_0_0_panties, colors_panties, filter_panties, "panties", 0, 0,))
    c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s)""" % ("standard_product_library"),
              (lingerie_offerings_0_1_panties, colors_panties, filter_panties, "panties", 0, 1,))
    c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s)""" % ("standard_product_library"),
              (lingerie_offerings_0_2_panties, colors_panties, filter_panties, "panties", 0, 2,))
    c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s)""" % ("standard_product_library"),
              (lingerie_offerings_1_0_panties, colors_panties, filter_panties, "panties", 1, 0,))
    c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s)""" % ("standard_product_library"),
              (lingerie_offerings_1_1_panties, colors_panties, filter_panties, "panties", 1, 1,))
    c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s)""" % ("standard_product_library"),
              (lingerie_offerings_1_2_panties, colors_panties, filter_panties, "panties", 1, 2,))

    conn.commit()


def get_userid_from_session_id(c, x):
    userid = ""
    c.execute("""select * from session_id_match_userdaten where lastsessionid=%s """, (x,))
    for row in c:
        userid = row[0]

    return userid


def decipher_marketing_email_click(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database', charset='utf8')
    c = conn.cursor(buffered=True)

    hash_code = request.GET.get('link')
    print hash_code
    user_id = ""
    email_name = ""
    x = str(request.session.session_key)
    link = ""
    c.execute("""select * from email_marketing_links where hashcode=%s """, (hash_code,))
    email_marketing_links = c.fetchall()
    for row_4 in email_marketing_links:
        link = row_4[1]
        anzahl_clicked = row_4[4]
        user_id = row_4[2]
        email_name = row_4[3]
        c.execute("""update email_marketing_links set clicked=%s where hashcode=%s""", (anzahl_clicked + 1, hash_code,))
        conn.commit()
        print "https://www.darlinglace.com/cart/"
        print link
        if link == "https://www.darlinglace.com/cart/":
            c.execute("""select * from userdaten where gutscheincode=%s """, (row_4[2],))
            userdaten = c.fetchall()
            print row_4[2]
            for row in userdaten:
                print row[0] + "== and " + row[12] + "=="
                if row[0] == "" and row[12] == "":

                    current_time = datetime.datetime.now(pytz.timezone('Europe/Berlin')).time()
                    now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
                    date_ = str(now.year) + str((now.month) - 1) + str(now.day)
                    time_ = str(current_time)
                    time__ = time_.replace(":", "")
                    time__ = time__.replace(".", "")

                    email = ""

                    c.execute("""select * from anmeldebestaetigungen """)
                    feedback = "not ok"
                    anmeldebestaetigungen = c.fetchall()
                    right_password = "false"
                    for row_2 in anmeldebestaetigungen:
                        if row_2[11] == row_4[2] and row_2[3] == "":
                            if row_2[12] != "":
                                password_hash = hashlib.sha512(row_2[12]).hexdigest()
                                c.execute("""update userdaten set email=%s, passwort=%s where emailquiz=%s""",
                                          (row_2[0], password_hash, row_2[0],))
                                conn.commit()

                            c.execute("""select * from userdaten where email=%s """, (row_2[0],))
                            userdaten = c.fetchall()
                            for row_3 in userdaten:
                                print row_2[0] + "==" + row_3[0]
                                if row_2[0] == row_3[0]:
                                    right_password = "true"
                                    email = row_3[0]
                                    userid = row_3[11]

                    print right_password
                    if right_password == "true":
                        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
                        if x_forwarded_for:
                            ip_adresse = x_forwarded_for.split(',')[0]
                        else:
                            ip_adresse = request.META.get('REMOTE_ADDR')
                        c.execute(
                            """update %s set IPadressesecondoptin=%%s,datesecondoptin=%%s,timesecondoptin=%%s where email=%%s and code=%%s""" % (
                            "anmeldebestaetigungen"), (ip_adresse, date_, time__, email, row_4[2],))
                        c.execute("""update userdaten set lastsessionid=%s where lastsessionid=%s""", ("", x,))

                        c.execute(
                            """update userdaten set newslettersignedup=%s, anmeldedatumnewslettersubscriber=%s,lastsessionid=%s where gutscheincode=%s""",
                            ("true", date_, x, userid,))

                        conn.commit()
                        link = "https://www.darlinglace.com/cart/?login=true"
                else:
                    link = "https://www.darlinglace.com/cart/?login=true"

    t = get_template('redirect_page.html')
    html = t.render({'link': link, 'user_id': user_id, 'email': email_name})

    conn.close()

    return HttpResponse(html)


def generate_lingerie(request, offset):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database', charset='utf8')
    c = conn.cursor(buffered=True)

    x = str(request.session.session_key)

    login = "false"
    status = 0
    modelAB = ""
    sub_picture = ""
    user = ""

    cup_table_1 = {0: 'AAA',
                   1: 'AA',
                   2: 'A',
                   3: 'B',
                   4: 'C',
                   5: 'D',
                   6: 'E',
                   7: 'F',
                   8: 'G',
                   9: 'H',
                   10: 'I',
                   11: 'J',
                   12: 'K',
                   13: 'L'

                   }

    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        for row in c:
            status = 1
            bereitsbestellt = row[75]
            bereitsversandt = row[76]
            email = row[0]
            user = row[11]
            vorname = row[2]
            nachname = row[3]
            default_bra_size = row[58]
            default_panty_size = row[59]
            facebookid = row[12]
            quiz = row[26]
            stadt = row[6]
            plz = row[4]
            modelAB = row[47]
            sub_picture = row[48]
            wishlist_quantity = row[16]
            cart_quantity = row[17]
            VIP_member_since = row[24]
            day = row[43]
            month = row[44]
            year = row[45]
            wishlist = row[65]
            warenkorb = row[66]
            brustform = row[41]
            recommendedsizetext = row[36]
            recommendedband = row[51]
            recommendedcup = row[52]
            cupproblem = row[34]
            bandproblem = row[35]
            strapproblem = row[39]
            letztefilter = row[81]
            letztelingeriebasisfilter = row[82]
            letztecolorsbasisfilter = row[83]
            recommendedbandsize = row[60]
            recommendedcupsize = row[61]

            if row[26] == "yes":
                quiz_footer = "true"
            else:
                quiz_footer = row[54]

            currentbandsize = 60 + int(row[27]) * 5
            currentcupsize = ""
            if row[28] >= 0 and row[28] <= 11:
                currentcupsize = cup_table_1[int(row[28])]

            if row[1] == "":
                password = "not ok"
            if (row[0] != "" and row[12] != "") or (row[0] != "" and row[1] != ""):
                login = "true"
            if row[22] == "VIP" and row[23] == "true":
                VIP = "VIP"
            else:
                VIP = "Regular"

    if status == 0:
        if x != "None":
            x = str(request.session.session_key)
            create_user(x, c, conn)
        else:
            print(request.path + ",create_new_request," + x)
            log_out_do_it(x, c, conn)
            request.session.create()
            x = str(request.session.session_key)
            create_user(x, c, conn)

        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            for row in c:
                brustform = row[41]
                email = row[0]
                bereitsbestellt = row[75]
                bereitsversandt = row[76]
                user = row[11]
                vorname = row[2]
                nachname = row[3]
                default_bra_size = row[58]
                default_panty_size = row[59]
                facebookid = row[12]
                quiz = row[26]
                stadt = row[6]
                plz = row[4]
                modelAB = row[47]
                sub_picture = row[48]
                wishlist = row[65]
                wishlist_quantity = row[16]
                cart_quantity = row[17]
                wishlist = row[65]
                warenkorb = row[66]
                day = row[43]
                month = row[44]
                year = row[45]
                recommendedsizetext = row[36]
                recommendedband = row[51]
                recommendedcup = row[52]
                cupproblem = row[34]
                bandproblem = row[35]
                strapproblem = row[39]
                letztefilter = row[81]
                letztelingeriebasisfilter = row[82]
                letztecolorsbasisfilter = row[83]
                currentbandsize = 60 + int(row[27]) * 5
                currentcupsize = ""

                if row[26] == "yes":
                    quiz_footer = "true"
                else:
                    quiz_footer = row[54]

                if row[28] >= 0 and row[28] <= 11:
                    currentcupsize = cup_table_1[int(row[28])]

                recommendedbandsize = row[60]
                recommendedcupsize = row[61]
                if row[22] == "VIP" and row[23] == "true":
                    VIP = "VIP"
                else:
                    VIP = "Regular"

    if user != "":

        description_header = ""
        size = ""
        style = ""
        color = ""
        padding = ""
        if offset == "Mein Showroom" and quiz == "no":
            lingerie_offerings = "Quiz"
            colors = ""
        else:
            if offset != "Mein Showroom":
                if offset != "Wunschliste":
                    if offset == "BH Sets" or offset == "Slips":
                        clientfilter = request.GET.get('clientfilter')
                        size = request.GET.get('size')
                        style = request.GET.get('style')
                        color = request.GET.get('color')
                        padding = request.GET.get('padding')

                        if offset == "BH Sets":
                            description_header = (
                            "BHs & BH Sets günstig kaufen in hoher Qualität &#10004; BH Sets mit Passform Garantie für jede Brustform &#10004; BH Sets für kleine Cups und große Cups &#10004; BHs und BH Sets als Push-Up BH, Balconette, Bralette oder Full Cup &#10004; BH Sets kaufen mit 30 Tage Rückgaberecht &#10004; Kostenloser Versand und Retoure. &#10004;").encode(
                                'utf8')
                            title = ("BH Sets, aktuelle Styles und viele Größen und Farben | Darling Lace").encode(
                                'utf8')
                        if offset == "Slips":
                            description_header = (
                            "Slips & Panties günstig kaufen in hoher Qualität &#10004; Slips kaufen als Hipster, Bikini, Tanga, Boyshort & Thong &#10004; Slips kaufen mit 30 Tage Rückgaberecht &#10004; Kostenloser Versand und Retoure. &#10004; Damen Slip kaufen auf Rechnung &#10004;").encode(
                                'utf8')
                            title = (
                            "Viele unterschidliche Slips und Panties: Thong, Tanga, Bikini und Boyshort | Darling Lace").encode(
                                'utf8')
                        if size == "All" or size == None:
                            size = ""

                        if style == "All" or style == None:
                            style = ""

                        if color == "All" or color == None:
                            color = ""

                        if padding == "All" or padding == None:
                            padding = ""

                        if clientfilter == None:
                            clientfilter = ""
                        if clientfilter == "yes":
                            lingerie_offerings = letztelingeriebasisfilter
                            colors = letztecolorsbasisfilter
                            filter = letztefilter
                        else:
                            if (size == "" and style == "" and color == "" and padding == "") or (
                                    size == None and style == None and color == None and padding == None):
                                c.execute(
                                    """select * from standard_product_library where modelAB=%s and subpicture=%s and productgroup=%s """,
                                    (modelAB, sub_picture, link_group_bestimmen(offset),))
                                standard_product_library = c.fetchall()
                                for row in standard_product_library:
                                    lingerie_offerings = row[0]
                                    colors = row[1]
                                    filter = row[2]
                                if letztelingeriebasisfilter != "":
                                    c.execute(
                                        """update userdaten set letztefilter=%s,letztelingeriebasisfilter=%s,letztecolorsbasisfilter=%s where gutscheincode=%s""",
                                        ("", "", "", user,))
                            else:
                                lingerie_offerings = get_lingerie_selection_filter(link_group_bestimmen(offset), "", "",
                                                                                   "", "", user, "", "", "", style,
                                                                                   color, "", padding, size, modelAB,
                                                                                   sub_picture, c)
                                colors = get_other_colors("", "", link_group_bestimmen(offset), c)
                                filter = load_style_filter("", "", "", "", "", offset, user, day, month, year, c)
                                if letztelingeriebasisfilter != "":
                                    c.execute(
                                        """update userdaten set letztefilter=%s,letztelingeriebasisfilter=%s,letztecolorsbasisfilter=%s where gutscheincode=%s""",
                                        (filter, lingerie_offerings, colors, user,))





                    else:
                        print "lingerie_filter_schwarz"
                        if offset == "schwarze_BH":
                            lingerie_offerings = get_lingerie_selection_filter("lingerie", "", "", "", "", user, "", "",
                                                                               "", "", "", "Schwarz", "", "", modelAB,
                                                                               sub_picture, c)
                            colors = get_other_colors("", "", "lingerie", c)
                            filter = load_style_filter("", "", "", "", "", "lingerie", user, day, month, year, c)
                            description_header = (
                            "Schwarze BHs in allen Formen: Push-Up, Balconette oder andere Styles &#10004; Schwarze BH kaufen in großer Größenauswahl &#1000; Schwarze BHs auf Rechnung kaufen &#10004; Schwarze BH kaufen mit 30 Tage Rückgaberecht &#10004; Kostenloser Versand und Retoure.").encode(
                                'utf8')
                            title = "Schwarze BH Sets in vielen unterschiedlichen BH Styles | Darling Lace"
                        if offset == "Push-Up_BH":
                            lingerie_offerings = get_lingerie_selection_filter("lingerie", "", "", "", "", user, "", "",
                                                                               "", "", "Push-Up BH", "", "", "",
                                                                               modelAB, sub_picture, c)
                            colors = get_other_colors("", "", "lingerie", c)
                            filter = load_style_filter("", "", "", "", "", "lingerie", user, day, month, year, c)
                            description_header = (
                            "Push-Up-BHs mit romantischer Spitzer und in schwarz oder anderen Farben &#10004; Push Up BH kaufen mit Passform Garantie &#10004; Push-Up BH auf Rechnung kaufen &#10004; Push-Up BH-BHs kaufen mit 30 Tage Rückgaberecht &#10004; Kostenloser Versand und Retoure.").encode(
                                'utf8')
                            title = "Push-Up BHs und Plunge BHs verpassen Dir einen tollen Ausschnitt | Darling Lace"
                        if offset == "Balconette":
                            lingerie_offerings = get_lingerie_selection_filter("lingerie", "", "", "", "", user, "", "",
                                                                               "", "", "Balconette", "", "", "",
                                                                               modelAB, sub_picture, c)
                            colors = get_other_colors("", "", "lingerie", c)
                            filter = load_style_filter("", "", "", "", "", "lingerie", user, day, month, year, c)
                            description_header = (
                            "Balconette-BHs: sexy und schlicht &#10004; Balconette-BHs für jede Brustform eine Passform Garantie &#10004; Balconette-BHs auf Rechnung kaufen &#10004; Balconette-BHs kaufen mit 30 Tage Rückgaberecht &#10004; Kostenloser Versand und Retoure.").encode(
                                'utf8')
                            title = "Balconette BHs geben Dir Halt und einen tollen Ausschnitt | Darling Lace"

                        if offset == "kleine_groessen":
                            list = []
                            list.append("65AA")
                            list.append("70AA")
                            list.append("75AA")
                            list.append("80AA")
                            list.append("65A")
                            list.append("70A")
                            lingerie_offerings = get_lingerie_selection_filter("lingerie", "", "", "", "", user, "", "",
                                                                               "", "", "", "", "", list, modelAB,
                                                                               sub_picture, c)
                            colors = get_other_colors("", "", "lingerie", c)
                            filter = load_style_filter("", "", "", "", "", "lingerie", user, day, month, year, c)
                            description_header = (
                            "Kleine Cups und kleine Größen kaufen  &#10004; Kleine Cups für jede Brustform eine Passform Garantie &#10004; Kleine Cups auf Rechnung kaufen &#10004; Kleine BHs kaufen mit 30 Tage Rückgaberecht &#10004; Kostenloser Versand und Retoure.").encode(
                                'utf8')
                            title = ("Kleine Cups mit Größen AA und A - viele Farben und Styles | Darling Lace").encode(
                                'utf8')

                        if offset == "grosse_groessen":
                            list = []
                            list.append("75E")
                            list.append("75F")
                            list.append("75G")

                            list.append("80E")
                            list.append("80F")
                            list.append("80G")

                            list.append("85B")
                            list.append("85C")
                            list.append("85D")
                            list.append("85E")
                            list.append("85F")
                            list.append("85G")

                            list.append("90C")
                            list.append("90D")
                            list.append("90E")
                            list.append("90F")
                            list.append("90G")

                            list.append("95C")
                            list.append("95D")
                            list.append("95E")
                            list.append("95F")

                            lingerie_offerings = get_lingerie_selection_filter("lingerie", "", "", "", "", user, "", "",
                                                                               "", "", "", "", "", list, modelAB,
                                                                               sub_picture, c)
                            colors = get_other_colors("", "", "lingerie", c)
                            filter = load_style_filter("", "", "", "", "", "lingerie", user, day, month, year, c)
                            description_header = (
                            "Große Cups und große Größen kaufen  &#10004; Große Cups für jede Brustform eine Passform Garantie &#10004; Große Cups auf Rechnung kaufen &#10004; Große BHs kaufen mit 30 Tage Rückgaberecht &#10004; Kostenloser Versand und Retoure.").encode(
                                'utf8')
                            title = (
                            "BH große Größen: Körbchengrößen bis Cup E, F und G - viele Styles | Darling Lace").encode(
                                'utf8')

                else:
                    if offset == "Wunschliste":
                        lingerie_offerings = get_lingerie_selection_filter("Wunschliste", "", "", "", "", user, "", "",
                                                                           "", "", "", "", "", "", modelAB, sub_picture,
                                                                           c)
                        colors = get_other_colors("", "", "Wunschliste", c)
                        filter = load_style_filter("", "", "", "", "", offset, user, day, month, year, c)
                        description_header = (
                        "Deine persönliche Wunschliste entdecken. Jetzt bei Darling Lace Dein BH Sets günstig kaufen in hoher Qualität mit Passform Garantie. Mach jetzt unser Passform Quiz.").encode(
                            'utf8')
                        title = offset + " | Darling Lace"
            else:

                lingerie_offerings = get_lingerie_selection_filter("Mein Showroom", "", "", "", "", user, "", day,
                                                                   month, year, "", "", "", "", modelAB, sub_picture, c)
                description_header = (
                "Passform Probleme? Falsche BH Größe? Mach unser Passform Quiz und erhalte Deine Passform Empfehlung. Wir empfehlen Dir den BH Typ, der am besten zu Dir passt. Egal ob Push-Up BH, Balconette, Bralette, Demi oder Full Cup: wir haben alle BH Typen in jeder Farbe.").encode(
                    'utf8')
                colors = ""
                filter = ""
                title = offset + " | Darling Lace"

        if (len(lingerie_offerings) != 2 or offset == "Mein Showroom") and lingerie_offerings != "Quiz":
            path = request.path
            print "pathpathpath"
            print path

            c.execute("""update userdaten set letzteshoppingsicht=%s where gutscheincode=%s""", (path, user,))
            conn.commit()
            t = get_template('test2.html')
            html = t.render({'quiz_footer': quiz_footer, 'description_header': description_header,
                             'user_id_google_analytics': get_google_analytics_user_id(login, user),
                             'currentbandsize': currentbandsize, 'currentcupsize': currentcupsize,
                             'recommendedcupsize': recommendedcupsize, 'recommendedbandsize': recommendedbandsize,
                             'cupproblem': cupproblem, 'bandproblem': bandproblem, 'strapproblem': strapproblem,
                             'brustform': brustform, 'recommendedsizetext': recommendedsizetext,
                             'recommendedband': recommendedband, 'recommendedcup': recommendedcup, 'filter_size': size,
                             'filter_style': style, 'filter_color': color, 'filter_padding': padding, 'email': email,
                             'bereitsbestellt': bereitsbestellt, 'bereitsversandt': bereitsversandt,
                             'fb_link': 'https://www.darlinglace.com',
                             'fb_title': ("Liebst du Lingerie? Erhalte Dein BH Set ab 29,95 EUR!").encode('utf8'),
                             'fb_description': (
                             "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                                 'utf8'), 'fb_description': (
                "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                    'utf8'), 'fb_image': 'https://www.darlinglace.com/static/overall_picture_bra.jpg',
                             'vorname': vorname, 'nachname': nachname, 'stadt': stadt, 'plz': plz, 'wishlist': wishlist,
                             'warenkorb': warenkorb, 'favicon': get_favicon(), 'path': request.path,
                             'brand_name': 'Darling Lace', 'VIP': VIP, 'title': title, 'filter': filter,
                             'lingerie_offerings': lingerie_offerings, 'login': login,
                             'url': get_link_positioining(offset), 'links': get_links(quiz), 'colors': colors})

            conn.close()
            return HttpResponse(html)
        else:
            if lingerie_offerings == "Quiz":
                conn.close()
                return HttpResponseRedirect("/quiz_fitting/")
            else:
                conn.close()
                return HttpResponseRedirect("/")
    else:
        conn.close()
        return HttpResponseRedirect("/")


def passform_quiz(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database')
    c = conn.cursor(buffered=True)

    x = str(request.session.session_key)

    login = "false"
    status = 0
    modelAB = ""
    sub_picture = ""
    user = ""

    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        for row in c:
            status = 1
            bereitsbestellt = row[75]
            bereitsversandt = row[76]
            messageshownfreundeeingeladen = row[77]
            wishlist = row[65]
            warenkorb = row[66]
            email = row[0]
            user = row[11]
            vorname = row[2]
            nachname = row[3]
            default_bra_size = row[58]
            default_panty_size = row[59]
            facebookid = row[12]
            quiz = row[26]
            stadt = row[6]
            plz = row[4]
            modelAB = row[47]
            sub_picture = row[48]
            wishlist_quantity = row[16]
            cart_quantity = row[17]
            VIP_member_since = row[24]
            day = row[43]

            if row[26] == "yes":
                quiz_footer = "true"
            else:
                quiz_footer = row[54]

            month = row[44]
            year = row[45]
            if row[1] == "":
                password = "not ok"
            if (row[0] != "" and row[12] != "") or (row[0] != "" and row[1] != ""):
                login = "true"
            if row[22] == "VIP" and row[23] == "true":
                VIP = "VIP"
            else:
                VIP = "Regular"

    if status == 0:
        if x != "None":
            x = str(request.session.session_key)
            create_user(x, c, conn)
        else:
            print(request.path + ",create_new_request," + x)
            log_out_do_it(x, c, conn)
            request.session.create()
            x = str(request.session.session_key)
            create_user(x, c, conn)

        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            for row in c:
                wishlist = row[65]
                bereitsbestellt = row[75]
                messageshownfreundeeingeladen = row[77]
                bereitsversandt = row[76]
                warenkorb = row[66]

                if row[26] == "yes":
                    quiz_footer = "true"
                else:
                    quiz_footer = row[54]

                email = row[0]
                user = row[11]
                vorname = row[2]
                nachname = row[3]
                default_bra_size = row[58]
                default_panty_size = row[59]
                facebookid = row[12]
                quiz = row[26]
                stadt = row[6]
                plz = row[4]
                modelAB = row[47]
                sub_picture = row[48]
                wishlist_quantity = row[16]
                cart_quantity = row[17]
                if row[22] == "VIP" and row[23] == "true":
                    VIP = "VIP"
                else:
                    VIP = "Regular"

    if user != "":
        url = get_link_positioining("")
        links = get_links(quiz)
        t = get_template('landing_page_passform_1.html')

        html = t.render(
            {'quiz_footer': quiz_footer, 'user_id_google_analytics': get_google_analytics_user_id(login, user),
             'messageshownfreundeeingeladen': messageshownfreundeeingeladen, 'email': email,
             'bereitsbestellt': bereitsbestellt, 'bereitsversandt': bereitsversandt,
             'fb_link': 'https://www.darlinglace.com',
             'fb_title': ("Liebst du Lingerie? Erhalte Dein BH Set ab 29,95 EUR!").encode('utf8'), 'fb_description': (
            "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                'utf8'), 'fb_description': (
            "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                'utf8'), 'fb_image': 'https://www.darlinglace.com/static/overall_picture_bra.jpg', 'vorname': vorname,
             'nachname': nachname, 'stadt': stadt, 'plz': plz, 'wishlist': wishlist, 'warenkorb': warenkorb,
             'favicon': get_favicon(), 'path': request.path, 'brand_name': 'Darling Lace', 'lingerie_offerings': '',
             'title': "Deine perfekte Passform bei Darling Lace | Darling Lace", 'login': login, 'url': url,
             'links': links})
        conn.close()
        return HttpResponse(html)
    else:
        conn.close()
        return HttpResponseRedirect("/")


def start_page_real(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database')
    c = conn.cursor(buffered=True)
    #c.execute("""insert into test_table value (7,'test6')""")
    x = str(request.session.session_key)
    #print("fsdfasdfdsafsdafds")
    login = "false"
    status = 0
    modelAB = ""
    sub_picture = ""
    user = ""

    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        for row in c:
            status = 1
            bereitsbestellt = row[75]
            bereitsversandt = row[76]
            if row[26] == "yes":
                quiz_footer = "true"
            else:
                quiz_footer = row[54]
            messageshownfreundeeingeladen = row[77]
            wishlist = row[65]
            warenkorb = row[66]
            email = row[0]
            user = row[11]
            vorname = row[2]
            nachname = row[3]
            default_bra_size = row[58]
            default_panty_size = row[59]
            facebookid = row[12]
            quiz = row[26]
            stadt = row[6]
            plz = row[4]
            modelAB = row[47]
            sub_picture = row[48]
            wishlist_quantity = row[16]
            cart_quantity = row[17]
            VIP_member_since = row[24]
            day = row[43]
            month = row[44]
            year = row[45]
            if row[1] == "":
                password = "not ok"
            if (row[0] != "" and row[12] != "") or (row[0] != "" and row[1] != ""):
                login = "true"
            if row[22] == "VIP" and row[23] == "true":
                VIP = "VIP"
            else:
                VIP = "Regular"

    if status == 0:
        if x != "None":
            x = str(request.session.session_key)
            create_user(x, c, conn)
        else:
            print(request.path + ",create_new_request," + x)
            log_out_do_it(x, c, conn)
            request.session.create()
            x = str(request.session.session_key)
            create_user(x, c, conn)

        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            for row in c:
                wishlist = row[65]
                bereitsbestellt = row[75]
                messageshownfreundeeingeladen = row[77]
                bereitsversandt = row[76]
                warenkorb = row[66]
                if row[26] == "yes":
                    quiz_footer = "true"
                else:
                    quiz_footer = row[54]

                email = row[0]
                user = row[11]
                vorname = row[2]
                nachname = row[3]
                default_bra_size = row[58]
                default_panty_size = row[59]
                facebookid = row[12]
                quiz = row[26]
                stadt = row[6]
                plz = row[4]
                modelAB = row[47]
                sub_picture = row[48]
                wishlist_quantity = row[16]
                cart_quantity = row[17]
                if row[22] == "VIP" and row[23] == "true":
                    VIP = "VIP"
                else:
                    VIP = "Regular"

    if user != "":
        url = get_link_positioining("")
        links = get_links(quiz)
        t = get_template('start_page_real.html')
        description_header = (
        "Finde bei Darling Lace die BHs und BH Sets für jede Größe und Brustform. Darling Lace bietet lingerie in einer großen Auswahl an Farben an. Hochwertige Unterwäsche für Frauen günstig kaufen bei Darling Lace. BHs in vielen Designs, basic, sexy und bequeme BHs. Auf Rechnung kaufen mit 30 Tage Rückgaberecht. Kostenloser Versand bei Darling Lace.").encode(
            'utf8')

        html = t.render({'quiz_footer': quiz_footer, 'description_header': description_header,
                         'user_id_google_analytics': get_google_analytics_user_id(login, user),
                         'messageshownfreundeeingeladen': messageshownfreundeeingeladen, 'email': email,
                         'bereitsbestellt': bereitsbestellt, 'bereitsversandt': bereitsversandt,
                         'fb_link': 'https://www.darlinglace.com',
                         'fb_title': ("Liebst du Lingerie? Erhalte Dein BH Set ab 29,95 EUR!").encode('utf8'),
                         'fb_description': (
                         "Es ist ganz einfach - Entdecke Deine persönliche Passform durch unser innovatives Quiz und erhalte ein BH Set für 19,95 EUR. Versand & Retoure sind umsonst!").encode(
                             'utf8'), 'fb_description': (
            "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                'utf8'), 'fb_image': 'https://www.darlinglace.com/static/overall_picture_bra.jpg', 'vorname': vorname,
                         'nachname': nachname, 'stadt': stadt, 'plz': plz, 'wishlist': wishlist, 'warenkorb': warenkorb,
                         'favicon': get_favicon(), 'path': request.path, 'brand_name': 'Darling Lace',
                         'lingerie_offerings': '', 'title': (
            "Lingerie, Dessous und Unterwäsche bei Darling Lace - Jetzt online bestellen! | Darling Lace").encode(
                'utf8'), 'login': login, 'url': url, 'links': links})
        conn.close()
        return HttpResponse(html)
    else:
        conn.close()
        return HttpResponseRedirect("/")


@csrf_exempt
def kein_quiz(request):
    if request.is_ajax() and request.GET:

        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)

        x = str(request.session.session_key)
        user = get_userid_from_session_id(c, x)

        c.execute("""update userdaten set VIPtermsandconditions=%s where gutscheincode=%s""", ("true", user,))

        conn.commit()

        conn.close()
        return HttpResponse(json.dumps(""), content_type='application/json')
    else:
        raise Http404


def impressum(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database')
    c = conn.cursor(buffered=True)

    x = str(request.session.session_key)

    login = "false"
    status = 0
    modelAB = ""
    sub_picture = ""
    user = ""

    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        for row in c:
            status = 1
            bereitsbestellt = row[75]
            bereitsversandt = row[76]
            wishlist = row[65]
            warenkorb = row[66]
            email = row[0]
            user = row[11]
            vorname = row[2]
            nachname = row[3]
            default_bra_size = row[58]
            default_panty_size = row[59]
            facebookid = row[12]
            quiz = row[26]
            stadt = row[6]
            plz = row[4]
            modelAB = row[47]
            sub_picture = row[48]
            wishlist_quantity = row[16]
            cart_quantity = row[17]
            VIP_member_since = row[24]
            day = row[43]
            month = row[44]
            year = row[45]
            if row[1] == "":
                password = "not ok"
            if (row[0] != "" and row[12] != "") or (row[0] != "" and row[1] != ""):
                login = "true"
            if row[22] == "VIP" and row[23] == "true":
                VIP = "VIP"
            else:
                VIP = "Regular"

    if status == 0:
        if x != "None":
            x = str(request.session.session_key)
            create_user(x, c, conn)
        else:
            print(request.path + ",create_new_request," + x)
            log_out_do_it(x, c, conn)
            request.session.create()
            x = str(request.session.session_key)
            create_user(x, c, conn)

        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            for row in c:
                wishlist = row[65]
                bereitsbestellt = row[75]
                bereitsversandt = row[76]
                warenkorb = row[66]
                email = row[0]
                user = row[11]
                vorname = row[2]
                nachname = row[3]
                default_bra_size = row[58]
                default_panty_size = row[59]
                facebookid = row[12]
                quiz = row[26]
                stadt = row[6]
                plz = row[4]
                modelAB = row[47]
                sub_picture = row[48]
                wishlist_quantity = row[16]
                cart_quantity = row[17]
                if row[22] == "VIP" and row[23] == "true":
                    VIP = "VIP"
                else:
                    VIP = "Regular"

    if user != "":
        t = get_template('impressum.html')
        description_header = (
        "BHs und BH Sets für jede Größe und Brustform. Wir bieten lingerie in einer großen Auswahl an Farben an. Hochwertige Unterwäsche für Frauen günstig kaufen. BHs in vielen Designs, basic, sexy und bequeme BHs. Auf Rechnung kaufen mit 30 Tage Rückgaberecht. Kostenloser Versand.").encode(
            'utf8')
        html = t.render({'description_header': description_header,
                         'user_id_google_analytics': get_google_analytics_user_id(login, user), 'email': email,
                         'bereitsbestellt': bereitsbestellt, 'bereitsversandt': bereitsversandt,
                         'fb_link': 'https://www.darlinglace.com',
                         'fb_title': ("Liebst du Lingerie? Erhalte Dein BH Set ab 29,95 EUR!").encode('utf8'),
                         'fb_description': (
                         "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                             'utf8'), 'fb_description': (
            "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                'utf8'), 'fb_image': 'https://www.darlinglace.com/static/overall_picture_bra.jpg', 'vorname': vorname,
                         'nachname': nachname, 'stadt': stadt, 'plz': plz, 'favicon': get_favicon(),
                         'path': request.path, 'brand_name': 'Darling Lace', 'title': "Impressum | Darling Lace",
                         'wishlist': wishlist, 'warenkorb': warenkorb, 'login': login, 'url': get_link_positioining(""),
                         'links': get_links(quiz)})
        conn.close()
        return HttpResponse(html)
    else:
        conn.close()
        return HttpResponseRedirect("/")


def versand_rueckversand(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database')
    c = conn.cursor(buffered=True)

    x = str(request.session.session_key)

    login = "false"
    status = 0
    modelAB = ""
    sub_picture = ""
    user = ""

    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        for row in c:
            status = 1
            bereitsbestellt = row[75]
            bereitsversandt = row[76]
            wishlist = row[65]
            warenkorb = row[66]
            email = row[0]
            user = row[11]
            vorname = row[2]
            nachname = row[3]
            default_bra_size = row[58]
            default_panty_size = row[59]
            facebookid = row[12]
            quiz = row[26]
            stadt = row[6]
            plz = row[4]
            modelAB = row[47]
            sub_picture = row[48]
            wishlist_quantity = row[16]
            cart_quantity = row[17]
            VIP_member_since = row[24]
            day = row[43]
            month = row[44]
            year = row[45]
            if row[1] == "":
                password = "not ok"
            if (row[0] != "" and row[12] != "") or (row[0] != "" and row[1] != ""):
                login = "true"
            if row[22] == "VIP" and row[23] == "true":
                VIP = "VIP"
            else:
                VIP = "Regular"

    if status == 0:
        if x != "None":
            x = str(request.session.session_key)
            create_user(x, c, conn)
        else:
            print(request.path + ",create_new_request," + x)
            log_out_do_it(x, c, conn)
            request.session.create()
            x = str(request.session.session_key)
            create_user(x, c, conn)

        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            for row in c:
                wishlist = row[65]
                bereitsbestellt = row[75]
                bereitsversandt = row[76]
                warenkorb = row[66]
                email = row[0]
                user = row[11]
                vorname = row[2]
                nachname = row[3]
                default_bra_size = row[58]
                default_panty_size = row[59]
                facebookid = row[12]
                quiz = row[26]
                stadt = row[6]
                plz = row[4]
                modelAB = row[47]
                sub_picture = row[48]
                wishlist_quantity = row[16]
                cart_quantity = row[17]
                if row[22] == "VIP" and row[23] == "true":
                    VIP = "VIP"
                else:
                    VIP = "Regular"

    if user != "":
        t = get_template('versand_rueckversand.html')
        description_header = (
        "BHs und BH Sets günstig kaufen. Der Versand ist kostenlos, schnell, ohne Risiko und einfach. Du kannst 30 Tage auf Probe bestellen Jedes sechste BH Set umsonst.Styles, Farben und Größen jeden Monat neu. Demi, Racerback, T-Shirt BH, Sexy BHs, Triangle BHs und vieles mehr. Wir bieten Dir aktuell Bandweiten von 65 bis 95 und Cupgrößen von AA bis G. Auf Rechnung kaufen mit 30 Tage Rückgaberecht. Kostenloser Versand und kostenloser Rückversand.").encode(
            'utf8')
        html = t.render({'description_header': description_header,
                         'user_id_google_analytics': get_google_analytics_user_id(login, user), 'email': email,
                         'bereitsbestellt': bereitsbestellt, 'bereitsversandt': bereitsversandt,
                         'fb_link': 'https://www.darlinglace.com',
                         'fb_title': ("Liebst du Lingerie? Erhalte Dein BH Set ab 29,95 EUR!").encode('utf8'),
                         'fb_description': (
                         "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                             'utf8'), 'fb_description': (
            "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                'utf8'), 'fb_image': 'https://www.darlinglace.com/static/overall_picture_bra.jpg', 'vorname': vorname,
                         'nachname': nachname, 'stadt': stadt, 'plz': plz, 'wishlist': wishlist, 'warenkorb': warenkorb,
                         'favicon': get_favicon(), 'path': request.path, 'brand_name': 'Darling Lace',
                         'lingerie_offerings': '', 'title': "Versandbedingungen | Darling Lace",
                         'bestellungen': define_bestellung(user, "all", c, "nein"), 'wishlist': wishlist,
                         'warenkorb': warenkorb, 'login': login, 'url': get_link_positioining(""),
                         'links': get_links(quiz)})
        conn.close()
        return HttpResponse(html)
    else:
        conn.close()
        return HttpResponseRedirect("/")


def ueber_uns(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database')
    c = conn.cursor(buffered=True)

    x = str(request.session.session_key)

    login = "false"
    status = 0
    modelAB = ""
    sub_picture = ""
    user = ""

    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        for row in c:
            status = 1
            wishlist = row[65]
            warenkorb = row[66]
            bereitsbestellt = row[75]
            bereitsversandt = row[76]
            email = row[0]
            user = row[11]
            vorname = row[2]
            nachname = row[3]
            default_bra_size = row[58]
            default_panty_size = row[59]
            facebookid = row[12]
            quiz = row[26]
            stadt = row[6]
            plz = row[4]
            modelAB = row[47]
            sub_picture = row[48]
            wishlist_quantity = row[16]
            cart_quantity = row[17]
            VIP_member_since = row[24]
            day = row[43]
            month = row[44]
            year = row[45]
            if row[1] == "":
                password = "not ok"
            if (row[0] != "" and row[12] != "") or (row[0] != "" and row[1] != ""):
                login = "true"
            if row[22] == "VIP" and row[23] == "true":
                VIP = "VIP"
            else:
                VIP = "Regular"

    if status == 0:
        if x != "None":
            x = str(request.session.session_key)
            create_user(x, c, conn)
        else:
            print(request.path + ",create_new_request," + x)
            log_out_do_it(x, c, conn)
            request.session.create()
            x = str(request.session.session_key)
            create_user(x, c, conn)

        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            for row in c:
                wishlist = row[65]
                warenkorb = row[66]
                bereitsbestellt = row[75]
                bereitsversandt = row[76]
                email = row[0]
                user = row[11]
                vorname = row[2]
                nachname = row[3]
                default_bra_size = row[58]
                default_panty_size = row[59]
                facebookid = row[12]
                quiz = row[26]
                stadt = row[6]
                plz = row[4]
                modelAB = row[47]
                sub_picture = row[48]
                wishlist_quantity = row[16]
                cart_quantity = row[17]
                if row[22] == "VIP" and row[23] == "true":
                    VIP = "VIP"
                else:
                    VIP = "Regular"

    if user != "":
        t = get_template('ueber_uns.html')

        description_header = (
        "BHs und BH Sets für jede Größe und Brustform. Unser Quiz hilft Dir, passende BHs zu finden. Wir bieten Dir aktuell Bandweiten von 65 bis 95 und Cupgrößen von AA bis G. Auf Rechnung kaufen mit 30 Tage Rückgaberecht. Kostenloser Versand und kostenloser Rückversand.").encode(
            'utf8')
        html = t.render({'description_header': description_header,
                         'user_id_google_analytics': get_google_analytics_user_id(login, user), 'email': email,
                         'bereitsbestellt': bereitsbestellt, 'bereitsversandt': bereitsversandt,
                         'fb_link': 'https://www.darlinglace.com',
                         'fb_title': ("Liebst du Lingerie? Erhalte Dein BH Set ab 29,95 EUR!").encode('utf8'),
                         'fb_description': (
                         "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                             'utf8'), 'fb_description': (
            "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                'utf8'), 'fb_image': 'https://www.darlinglace.com/static/overall_picture_bra.jpg', 'vorname': vorname,
                         'nachname': nachname, 'stadt': stadt, 'plz': plz, 'wishlist': wishlist, 'warenkorb': warenkorb,
                         'favicon': get_favicon(), 'path': request.path, 'brand_name': 'Darling Lace',
                         'lingerie_offerings': '', 'title': ("Über Uns | Darling Lace").encode('utf8')
                            , 'bestellungen': define_bestellung(user, "all", c, "nein"), 'wishlist': wishlist,
                         'warenkorb': warenkorb, 'login': login, 'url': get_link_positioining(""),
                         'links': get_links(quiz)})
        conn.close()
        return HttpResponse(html)
    else:
        conn.close()
        return HttpResponseRedirect("/")


def ueber_uns_2(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database')
    c = conn.cursor(buffered=True)

    x = str(request.session.session_key)

    login = "false"
    status = 0
    modelAB = ""
    sub_picture = ""
    user = ""

    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        for row in c:
            status = 1
            wishlist = row[65]
            warenkorb = row[66]
            bereitsbestellt = row[75]
            bereitsversandt = row[76]
            email = row[0]
            user = row[11]
            vorname = row[2]
            nachname = row[3]
            default_bra_size = row[58]
            default_panty_size = row[59]
            facebookid = row[12]
            quiz = row[26]
            stadt = row[6]
            plz = row[4]
            modelAB = row[47]
            sub_picture = row[48]
            wishlist_quantity = row[16]
            cart_quantity = row[17]
            VIP_member_since = row[24]
            day = row[43]
            month = row[44]
            year = row[45]
            if row[1] == "":
                password = "not ok"
            if (row[0] != "" and row[12] != "") or (row[0] != "" and row[1] != ""):
                login = "true"
            if row[22] == "VIP" and row[23] == "true":
                VIP = "VIP"
            else:
                VIP = "Regular"

    if status == 0:
        if x != "None":
            x = str(request.session.session_key)
            create_user(x, c, conn)
        else:
            print(request.path + ",create_new_request," + x)
            log_out_do_it(x, c, conn)
            request.session.create()
            x = str(request.session.session_key)
            create_user(x, c, conn)

        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            for row in c:
                wishlist = row[65]
                warenkorb = row[66]
                bereitsbestellt = row[75]
                bereitsversandt = row[76]
                email = row[0]
                user = row[11]
                vorname = row[2]
                nachname = row[3]
                default_bra_size = row[58]
                default_panty_size = row[59]
                facebookid = row[12]
                quiz = row[26]
                stadt = row[6]
                plz = row[4]
                modelAB = row[47]
                sub_picture = row[48]
                wishlist_quantity = row[16]
                cart_quantity = row[17]
                if row[22] == "VIP" and row[23] == "true":
                    VIP = "VIP"
                else:
                    VIP = "Regular"

    if user != "":
        t = get_template('ueber_uns_2.html')

        description_header = (
        "BHs und BH Sets für jede Größe und Brustform. Unser Quiz hilft Dir, passende BHs zu finden. Wir bieten Dir aktuell Bandweiten von 65 bis 95 und Cupgrößen von AA bis G. Auf Rechnung kaufen mit 30 Tage Rückgaberecht. Kostenloser Versand und kostenloser Rückversand.").encode(
            'utf8')
        html = t.render({'description_header': description_header,
                         'user_id_google_analytics': get_google_analytics_user_id(login, user), 'email': email,
                         'bereitsbestellt': bereitsbestellt, 'bereitsversandt': bereitsversandt,
                         'fb_link': 'https://www.darlinglace.com',
                         'fb_title': ("Liebst du Lingerie? Erhalte Dein BH Set ab 29,95 EUR!").encode('utf8'),
                         'fb_description': (
                         "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                             'utf8'), 'fb_description': (
            "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                'utf8'), 'fb_image': 'https://www.darlinglace.com/static/overall_picture_bra.jpg', 'vorname': vorname,
                         'nachname': nachname, 'stadt': stadt, 'plz': plz, 'wishlist': wishlist, 'warenkorb': warenkorb,
                         'favicon': get_favicon(), 'path': request.path, 'brand_name': 'Darling Lace',
                         'lingerie_offerings': '', 'title': ("Über Uns | Darling Lace").encode('utf8')
                            , 'bestellungen': define_bestellung(user, "all", c, "nein"), 'wishlist': wishlist,
                         'warenkorb': warenkorb, 'login': login, 'url': get_link_positioining(""),
                         'links': get_links(quiz)})
        conn.close()
        return HttpResponse(html)
    else:
        conn.close()
        return HttpResponseRedirect("/")


def quiz_fitting(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database')
    c = conn.cursor(buffered=True)

    x = str(request.session.session_key)

    login = "false"
    status = 0
    modelAB = ""
    sub_picture = ""
    user = ""

    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        for row in c:
            status = 1
            wishlist = row[65]
            warenkorb = row[66]
            bereitsbestellt = row[75]
            bereitsversandt = row[76]
            email = row[0]
            user = row[11]
            vorname = row[2]
            nachname = row[3]
            default_bra_size = row[58]
            default_panty_size = row[59]
            facebookid = row[12]
            quiz = row[26]
            stadt = row[6]
            plz = row[4]
            modelAB = row[47]
            sub_picture = row[48]
            wishlist_quantity = row[16]
            cart_quantity = row[17]
            VIP_member_since = row[24]
            day = row[43]
            month = row[44]
            year = row[45]
            emailquiz = row[85]
            print "get_quiz_fitting_data"
            print user
            quiz_data = get_quiz_fitting_data(c, row[27], row[28], row[29], row[30], row[31], row[32], row[33], row[34],
                                              row[35], row[38], row[39], row[40], row[41], row[42], row[53], )
            if row[1] == "":
                password = "not ok"
            if (row[0] != "" and row[12] != "") or (row[0] != "" and row[1] != ""):
                login = "true"
            if row[22] == "VIP" and row[23] == "true":
                VIP = "VIP"
            else:
                VIP = "Regular"

    if status == 0:
        if x != "None":
            x = str(request.session.session_key)
            create_user(x, c, conn)
        else:
            print(request.path + ",create_new_request," + x)
            log_out_do_it(x, c, conn)
            request.session.create()
            x = str(request.session.session_key)
            create_user(x, c, conn)

        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            for row in c:
                wishlist = row[65]
                warenkorb = row[66]
                bereitsbestellt = row[75]
                bereitsversandt = row[76]
                quiz_data = get_quiz_fitting_data(c, row[27], row[28], row[29], row[30], row[31], row[32], row[33],
                                                  row[34], row[35], row[38], row[39], row[40], row[41], row[42],
                                                  row[53], )
                email = row[0]
                user = row[11]
                vorname = row[2]
                nachname = row[3]
                default_bra_size = row[58]
                default_panty_size = row[59]
                facebookid = row[12]
                quiz = row[26]
                stadt = row[6]
                plz = row[4]
                modelAB = row[47]
                sub_picture = row[48]
                wishlist_quantity = row[16]
                cart_quantity = row[17]
                emailquiz = row[85]
                if row[22] == "VIP" and row[23] == "true":
                    VIP = "VIP"
                else:
                    VIP = "Regular"

    if user != "":

        t = get_template('quiz_fitting.html')

        description_header = (
        "Passform Probleme bei BHs? Wir können Dir eine ganz persönliche Passform-Empfehlung für Deine Brustform anbieten auf Basis eines Quiz. Wir bieten Cup von AA bis G an in vielen Styles wie Balconette, Push-Up oder Bralette an. Der Versand ist kostenlos, schnell, ohne Risiko und einfach. Du kannst 30 Tage auf Probe bestellen. Kostenloser Versand und kostenloser Rückversand.").encode(
            'utf8')

        html = t.render(
            {'user_id_google_analytics': get_google_analytics_user_id(login, user), 'email_provided_quiz': email,
             'quiz_data': quiz_data, 'email': email, 'bereitsbestellt': bereitsbestellt,
             'bereitsversandt': bereitsversandt, 'fb_link': 'https://www.darlinglace.com',
             'fb_title': ("Liebst du Lingerie? Erhalte Dein BH Set ab 29,95 EUR!").encode('utf8'), 'fb_description': (
            "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                'utf8'), 'fb_description': (
            "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                'utf8'), 'fb_image': 'https://www.darlinglace.com/static/overall_picture_bra.jpg', 'vorname': vorname,
             'nachname': nachname, 'stadt': stadt, 'plz': plz, 'wishlist': wishlist, 'warenkorb': warenkorb,
             'favicon': get_favicon(), 'path': request.path, 'brand_name': 'Darling Lace', 'lingerie_offerings': '',
             'title': ("Perfekte Passform | Darling Lace").encode('utf8')
                , 'wishlist': wishlist, 'warenkorb': warenkorb, 'login': login, 'url': get_link_positioining(""),
             'links': get_links(quiz)})
        conn.close()
        return HttpResponse(html)
    else:
        conn.close()
        return HttpResponseRedirect("/")


def get_quiz_fitting_data(c, band_click_first_id, cup_click_first_id, brand_click_first_id, band_click_second_id,
                          cup_click_second_id, brand_click_second_id, question_2, question_3, question_4, question_5,
                          question_6, question_6a, question_8, question_9, panty_id):
    quiz_fitting_data = []

    class Quiz_Fitting_Data(object):
        def __init__(self, band_click_first_id, cup_click_first_id, brand_click_first_id, band_click_second_id,
                     cup_click_second_id, brand_click_second_id, question_2, question_3, question_4, question_5,
                     question_6, question_6a, question_8, question_9, panty_id):
            self.band_click_first_id = band_click_first_id
            self.cup_click_first_id = cup_click_first_id
            self.brand_click_first_id = brand_click_first_id
            self.band_click_second_id = band_click_second_id
            self.cup_click_second_id = cup_click_second_id
            self.brand_click_second_id = brand_click_second_id
            self.question_2 = question_2
            self.question_3 = question_3
            self.question_4 = question_4
            self.question_5 = question_5
            self.question_6 = question_6
            self.question_6a = question_6a
            self.question_8 = question_8
            self.question_9 = question_9
            self.panty_id = panty_id

    quiz_fitting_data.append(
        Quiz_Fitting_Data(band_click_first_id, cup_click_first_id, brand_click_first_id, band_click_second_id,
                          cup_click_second_id, brand_click_second_id, question_2, question_3, question_4, question_5,
                          question_6, question_6a, question_8, question_9, panty_id))

    json_string = json.dumps([Quiz_Fitting_Data.__dict__ for Quiz_Fitting_Data in quiz_fitting_data])

    return json_string


def support(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database')
    c = conn.cursor(buffered=True)
    x = str(request.session.session_key)
    login = "false"
    status = 0
    modelAB = ""
    sub_picture = ""
    user = ""

    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        for row in c:
            status = 1
            bereitsbestellt = row[75]
            bereitsversandt = row[76]
            wishlist = row[65]
            warenkorb = row[66]
            email = row[0]
            user = row[11]
            vorname = row[2]
            nachname = row[3]
            default_bra_size = row[58]
            default_panty_size = row[59]
            facebookid = row[12]
            quiz = row[26]
            stadt = row[6]
            plz = row[4]
            modelAB = row[47]
            sub_picture = row[48]
            wishlist_quantity = row[16]
            cart_quantity = row[17]
            VIP_member_since = row[24]
            vorname_nachname = row[2] + row[3]
            day = row[43]
            month = row[44]
            year = row[45]
            if row[1] == "":
                password = "not ok"
            if (row[0] != "" and row[12] != "") or (row[0] != "" and row[1] != ""):
                login = "true"
            if row[22] == "VIP" and row[23] == "true":
                VIP = "VIP"
            else:
                VIP = "Regular"

    if status == 0:
        if x != "None":
            x = str(request.session.session_key)
            create_user(x, c, conn)
        else:
            print(request.path + ",create_new_request," + x)
            log_out_do_it(x, c, conn)
            request.session.create()
            x = str(request.session.session_key)
            create_user(x, c, conn)

        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            for row in c:
                wishlist = row[65]
                bereitsbestellt = row[75]
                bereitsversandt = row[76]
                warenkorb = row[66]
                email = row[0]
                user = row[11]
                vorname = row[2]
                nachname = row[3]
                default_bra_size = row[58]
                default_panty_size = row[59]
                facebookid = row[12]
                quiz = row[26]
                stadt = row[6]
                plz = row[4]
                modelAB = row[47]
                sub_picture = row[48]
                wishlist_quantity = row[16]
                cart_quantity = row[17]
                vorname_nachname = row[2] + row[3]
                if row[22] == "VIP" and row[23] == "true":
                    VIP = "VIP"
                else:
                    VIP = "Regular"

    if user != "":

        description_header = (
        "BHs und BH Sets günstig kaufen. Der Versand ist kostenlos, schnell, ohne Risiko und einfach. Du kannst 30 Tage auf Probe bestellen Jedes sechste BH Set umsonst. Styles, Farben und Größen jeden Monat neu. Demi, Racerback, T-Shirt BH, Sexy BHs, Triangle BHs und vieles mehr. Wir bieten Dir aktuell Bandweiten von 65 bis 95 und Cupgrößen von AA bis G. Auf Rechnung kaufen mit 30 Tage Rückgaberecht. Kostenloser Versand und kostenloser Rückversand.").encode(
            'utf8')
        t = get_template('hilfe.html')
        html = t.render({'description_header': description_header,
                         'user_id_google_analytics': get_google_analytics_user_id(login, user), 'email': email,
                         'bereitsbestellt': bereitsbestellt, 'bereitsversandt': bereitsversandt,
                         'fb_link': 'https://www.darlinglace.com',
                         'fb_title': ("Liebst du Lingerie? Erhalte Dein BH Set ab 29,95 EUR!").encode('utf8'),
                         'fb_description': (
                         "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                             'utf8'), 'fb_description': (
            "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                'utf8'), 'fb_image': 'https://www.darlinglace.com/static/overall_picture_bra.jpg', 'vorname': vorname,
                         'nachname': nachname, 'stadt': stadt, 'plz': plz, 'wishlist': wishlist, 'warenkorb': warenkorb,
                         'help_center': get_help_center_link(), 'telefonnummer': get_support_telefonnummer(),
                         'vorname_nachname': vorname_nachname, 'email_from': email, 'favicon': get_favicon(),
                         'path': request.path, 'brand_name': 'Darling Lace', 'lingerie_offerings': '',
                         'title': "Kontakt | Darling Lace", 'bestellungen': define_bestellung(user, "all", c, "nein"),
                         'wishlist': wishlist, 'warenkorb': warenkorb, 'login': login, 'url': get_link_positioining(""),
                         'links': get_links(quiz)})
        conn.close()
        return HttpResponse(html)
    else:
        conn.close()
        return HttpResponseRedirect("/")


def get_help_center_link():
    return "https://darlinglace.zendesk.com/hc/de"


def get_support_telefonnummer():
    return "012341234"


def datenschutz(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2', \
                                   password='okano1988', database='maxfischer2database')
    c = conn.cursor(buffered=True)

    x = str(request.session.session_key)

    login = "false"
    status = 0
    modelAB = ""
    sub_picture = ""
    user = ""

    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        for row in c:
            status = 1
            bereitsbestellt = row[75]
            bereitsversandt = row[76]
            wishlist = row[65]
            warenkorb = row[66]
            email = row[0]
            user = row[11]
            vorname = row[2]
            nachname = row[3]
            stadt = row[6]
            plz = row[4]
            quiz = row[26]
            modelAB = row[47]
            sub_picture = row[48]
            wishlist_quantity = row[16]
            cart_quantity = row[17]
            if (row[0] != "" and row[12] != "") or (row[0] != "" and row[1] != ""):
                login = "true"

    if status == 0:
        if x != "None":
            x = str(request.session.session_key)
            create_user(x, c, conn)
        else:
            print(request.path + ",create_new_request," + x)
            log_out_do_it(x, c, conn)
            request.session.create()
            x = str(request.session.session_key)
            create_user(x, c, conn)

        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            for row in c:
                wishlist = row[65]
                bereitsbestellt = row[75]
                bereitsversandt = row[76]
                warenkorb = row[66]
                email = row[0]
                user = row[11]
                vorname = row[2]
                nachname = row[3]
                quiz = row[26]
                stadt = row[6]
                plz = row[4]
                modelAB = row[47]
                sub_picture = row[48]
                wishlist_quantity = row[16]
                cart_quantity = row[17]

    if user != "":
        t = get_template('datenschutz.html')
        description_header = (
        "BHs und BH Sets für jede Größe und Brustform. Wir bieten lingerie in einer großen Auswahl an Farben an. Hochwertige Unterwäsche für Frauen günstig kaufen. BHs in vielen Designs, basic, sexy und bequeme BHs. Auf Rechnung kaufen mit 30 Tage Rückgaberecht. Kostenloser Versand.").encode(
            'utf8')

        html = t.render({'description_header': description_header,
                         'user_id_google_analytics': get_google_analytics_user_id(login, user), 'email': email,
                         'bereitsbestellt': bereitsbestellt, 'bereitsversandt': bereitsversandt,
                         'fb_link': 'https://www.darlinglace.com',
                         'fb_title': ("Liebst du Lingerie? Erhalte Dein BH Set ab 29,95 EUR!").encode('utf8'),
                         'fb_description': (
                         "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                             'utf8'), 'fb_description': (
            "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                'utf8'), 'fb_image': 'https://www.darlinglace.com/static/overall_picture_bra.jpg', 'vorname': vorname,
                         'nachname': nachname, 'stadt': stadt, 'plz': plz, 'wishlist': wishlist, 'warenkorb': warenkorb,
                         'favicon': get_favicon(), 'path': request.path, 'brand_name': 'Darling Lace',
                         'lingerie_offerings': '', 'title': "Datenschutz | Darling Lace",
                         'bestellungen': define_bestellung(user, "all", c, "nein"), 'wishlist': wishlist,
                         'warenkorb': warenkorb, 'login': login, 'url': get_link_positioining(""),
                         'links': get_links(quiz)})
        conn.close()
        return HttpResponse(html)
    else:
        conn.close()
        return HttpResponseRedirect("/")


def widerrufsbelehrung(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database')
    c = conn.cursor(buffered=True)

    x = str(request.session.session_key)

    login = "false"
    status = 0
    modelAB = ""
    sub_picture = ""
    user = ""

    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        for row in c:
            status = 1
            bereitsbestellt = row[75]
            bereitsversandt = row[76]
            wishlist = row[65]
            warenkorb = row[66]
            email = row[0]
            user = row[11]
            vorname = row[2]
            nachname = row[3]
            stadt = row[6]
            quiz = row[26]
            plz = row[4]
            modelAB = row[47]
            sub_picture = row[48]
            wishlist_quantity = row[16]
            cart_quantity = row[17]
            if (row[0] != "" and row[12] != "") or (row[0] != "" and row[1] != ""):
                login = "true"

    if status == 0:
        if x != "None":
            x = str(request.session.session_key)
            create_user(x, c, conn)
        else:
            print(request.path + ",create_new_request," + x)
            log_out_do_it(x, c, conn)
            request.session.create()
            x = str(request.session.session_key)
            create_user(x, c, conn)

        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            for row in c:
                wishlist = row[65]
                bereitsbestellt = row[75]
                bereitsversandt = row[76]
                warenkorb = row[66]
                email = row[0]
                user = row[11]
                vorname = row[2]
                nachname = row[3]
                stadt = row[6]
                quiz = row[26]
                plz = row[4]
                modelAB = row[47]
                sub_picture = row[48]
                wishlist_quantity = row[16]
                cart_quantity = row[17]

    if user != "":
        t = get_template('widerrufsbelehrung.html')
        description_header = (
        "BHs und BH Sets für jede Größe und Brustform. Wir bieten lingerie in einer großen Auswahl an Farben an. Hochwertige Unterwäsche für Frauen günstig kaufen. BHs in vielen Designs, basic, sexy und bequeme BHs. Auf Rechnung kaufen mit 30 Tage Rückgaberecht. Kostenloser Versand.").encode(
            'utf8')

        html = t.render({'description_header': description_header,
                         'user_id_google_analytics': get_google_analytics_user_id(login, user), 'email': email,
                         'bereitsbestellt': bereitsbestellt, 'bereitsversandt': bereitsversandt,
                         'fb_link': 'https://www.darlinglace.com',
                         'fb_title': ("Liebst du Lingerie? Erhalte Dein BH Set ab 29,95 EUR!").encode('utf8'),
                         'fb_description': (
                         "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                             'utf8'), 'fb_description': (
            "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                'utf8'), 'fb_image': 'https://www.darlinglace.com/static/overall_picture_bra.jpg', 'vorname': vorname,
                         'nachname': nachname, 'stadt': stadt, 'plz': plz, 'wishlist': wishlist, 'warenkorb': warenkorb,
                         'favicon': get_favicon(), 'path': request.path, 'brand_name': 'Darling Lace',
                         'lingerie_offerings': '', 'title': "Widerrufsbelehrung | Darling Lace",
                         'bestellungen': define_bestellung(user, "all", c, "nein"), 'wishlist': wishlist,
                         'warenkorb': warenkorb, 'login': login, 'url': get_link_positioining(""),
                         'links': get_links(quiz)})
        conn.close()
        return HttpResponse(html)
    else:
        conn.close()
        return HttpResponseRedirect("/")


def agb(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database')
    c = conn.cursor(buffered=True)

    x = str(request.session.session_key)

    login = "false"
    status = 0
    modelAB = ""
    sub_picture = ""
    user = ""

    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        for row in c:
            status = 1
            bereitsbestellt = row[75]
            bereitsversandt = row[76]
            wishlist = row[65]
            warenkorb = row[66]
            email = row[0]
            user = row[11]
            vorname = row[2]
            nachname = row[3]
            stadt = row[6]
            plz = row[4]
            quiz = row[26]

            modelAB = row[47]
            sub_picture = row[48]
            wishlist_quantity = row[16]
            cart_quantity = row[17]
            if (row[0] != "" and row[12] != "") or (row[0] != "" and row[1] != ""):
                login = "true"

    if status == 0:
        if x != "None":
            x = str(request.session.session_key)
            create_user(x, c, conn)
        else:
            print(request.path + ",create_new_request," + x)
            log_out_do_it(x, c, conn)
            request.session.create()
            x = str(request.session.session_key)
            create_user(x, c, conn)

        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            for row in c:
                wishlist = row[65]
                bereitsbestellt = row[75]
                bereitsversandt = row[76]
                warenkorb = row[66]
                email = row[0]
                user = row[11]
                vorname = row[2]
                nachname = row[3]
                stadt = row[6]
                plz = row[4]
                modelAB = row[47]
                sub_picture = row[48]
                wishlist_quantity = row[16]
                cart_quantity = row[17]
                quiz = row[26]
    if user != "":
        t = get_template('agb.html')
        description_header = (
        "BHs und BH Sets für jede Größe und Brustform. Wir bieten lingerie in einer großen Auswahl an Farben an. Hochwertige Unterwäsche für Frauen günstig kaufen. BHs in vielen Designs, basic, sexy und bequeme BHs. Auf Rechnung kaufen mit 30 Tage Rückgaberecht. Kostenloser Versand.").encode(
            'utf8')

        html = t.render({'description_header': description_header,
                         'user_id_google_analytics': get_google_analytics_user_id(login, user), 'email': email,
                         'bereitsbestellt': bereitsbestellt, 'bereitsversandt': bereitsversandt,
                         'fb_link': 'https://www.darlinglace.com',
                         'fb_title': ("Liebst du Lingerie? Erhalte Dein BH Set ab 29,95 EUR!").encode('utf8'),
                         'fb_description': (
                         "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                             'utf8'), 'fb_description': (
            "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                'utf8'), 'fb_image': 'https://www.darlinglace.com/static/overall_picture_bra.jpg', 'vorname': vorname,
                         'nachname': nachname, 'stadt': stadt, 'plz': plz, 'wishlist': wishlist, 'warenkorb': warenkorb,
                         'favicon': get_favicon(), 'path': request.path, 'brand_name': 'Darling Lace',
                         'lingerie_offerings': '', 'title': "AGB | Darling Lace",
                         'bestellungen': define_bestellung(user, "all", c, "nein"), 'wishlist': wishlist,
                         'warenkorb': warenkorb, 'login': login, 'url': get_link_positioining(""),
                         'links': get_links(quiz)})
        conn.close()
        return HttpResponse(html)
    else:
        conn.close()
        return HttpResponseRedirect("/")


def wie_funktioniert_VIP(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database')
    c = conn.cursor(buffered=True)

    x = str(request.session.session_key)

    login = "false"
    status = 0
    modelAB = ""
    sub_picture = ""
    user = ""

    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        for row in c:
            status = 1
            bereitsbestellt = row[75]
            bereitsversandt = row[76]
            wishlist = row[65]
            warenkorb = row[66]
            quiz = row[26]
            email = row[0]
            user = row[11]
            vorname = row[2]
            nachname = row[3]
            stadt = row[6]
            plz = row[4]
            modelAB = row[47]
            sub_picture = row[48]
            wishlist_quantity = row[16]
            cart_quantity = row[17]
            if (row[0] != "" and row[12] != "") or (row[0] != "" and row[1] != ""):
                login = "true"

    if status == 0:
        if x != "None":
            x = str(request.session.session_key)
            create_user(x, c, conn)
        else:
            print(request.path + ",create_new_request," + x)
            log_out_do_it(x, c, conn)
            request.session.create()
            x = str(request.session.session_key)
            create_user(x, c, conn)

        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            for row in c:
                wishlist = row[65]
                bereitsbestellt = row[75]
                bereitsversandt = row[76]
                warenkorb = row[66]
                email = row[0]
                user = row[11]
                quiz = row[26]
                vorname = row[2]
                nachname = row[3]
                stadt = row[6]
                plz = row[4]
                modelAB = row[47]
                sub_picture = row[48]
                wishlist_quantity = row[16]
                cart_quantity = row[17]

    if user != "":
        description_header = (
        "BHs und BH Sets in top Qualität noch günstiger für 29,95 EUR pro Set. Jedes sechste BH Set umsonst.Styles, Farben und Größen jeden Monat neu. Demi, Racerback, T-Shirt BH, Sexy BHs, Triangle BHs und vieles mehr. Wir bieten Dir aktuell Bandweiten von 65 bis 95 und Cupgrößen von AA bis G. Auf Rechnung kaufen mit 30 Tage Rückgaberecht. Kostenloser Versand und kostenloser Rückversand.").encode(
            'utf8')
        t = get_template('wie_funktioniert_VIP.html')
        html = t.render({'description_header': description_header,
                         'user_id_google_analytics': get_google_analytics_user_id(login, user), 'email': email,
                         'bereitsbestellt': bereitsbestellt, 'bereitsversandt': bereitsversandt,
                         'fb_link': 'https://www.darlinglace.com',
                         'fb_title': ("Liebst du Lingerie? Erhalte Dein BH Set ab 29,95 EUR!").encode('utf8'),
                         'fb_description': (
                         "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                             'utf8'), 'fb_description': (
            "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                'utf8'), 'fb_image': 'https://www.darlinglace.com/static/overall_picture_bra.jpg', 'vorname': vorname,
                         'nachname': nachname, 'stadt': stadt, 'plz': plz, 'wishlist': wishlist, 'warenkorb': warenkorb,
                         'favicon': get_favicon(), 'path': request.path, 'brand_name': 'Darling Lace',
                         'lingerie_offerings': '', 'title': "Wie funktioniert VIP? | Darling Lace",
                         'wishlist': wishlist, 'warenkorb': warenkorb, 'login': login, 'url': get_link_positioining(""),
                         'links': get_links(quiz)})
        conn.close()
        return HttpResponse(html)
    else:
        conn.close()
        return HttpResponseRedirect("/")


@csrf_exempt
def newsletter_abmelden(request):
    if request.is_ajax() and request.POST:
        security_key = request.POST.get('security_key')

        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)

        x = str(request.session.session_key)

        c.execute("""select * from userdaten where newsletterabbestellencode=%s """, (security_key,))
        for row in c:
            userid = row[11]

            now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
            date_now = day = str(now.year) + str(now.month - 1) + str(now.day)
            c.execute(
                """update userdaten set newslettersignedup=%s, abmeldedatumnewslettersubscriber=%s where gutscheincode=%s""",
                ("false", date_now, userid,))
            conn.commit()

            conn.close()
        return HttpResponse(json.dumps(""), content_type='application/json')
    else:
        raise Http404


@csrf_exempt
def login_user(request):
    if request.is_ajax() and request.POST:
        n = request.POST.get('item')
        m = n.split(",")

        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)

        x = str(request.session.session_key)
        m[0] = m[0].lower()
        print "login_user"
        data = "yes"
        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            userdaten = c.fetchall()
            for row in userdaten:
                if row[0] == "" and row[12] == "":
                    data = "no"

        print data
        if data != "yes":
            gutscheincode_old = ""
            if x != "None":
                c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
                for row in c:
                    gutscheincode_old = row[11]

            if gutscheincode_old == "":
                if x != "None":
                    create_user(x, c, conn)
                else:
                    print(request.path + ",create_new_request," + x)
                    request.session.create()
                    x = str(request.session.session_key)
                    create_user(x, c, conn)

                if x != "None":
                    c.execute("""select * from userdaten where gutscheincode=%s """,
                              (get_userid_from_session_id(c, x),))
                    for row in c:
                        gutscheincode_old = row[11]

            userdaten = c.fetchall()
            status = 0
            status_ = 0
            abc = ""
            plz = ""
            m[1] = hashlib.sha512(m[1]).hexdigest()
            print "," + m[0] + ","
            c.execute("""select * from userdaten where email=%s""", (m[0],))
            userdaten = c.fetchall()
            for row in userdaten:
                print row[0] + "==" + m[0] + "and" + row[1] + "==" + m[1] + " and" + row[1] + "!="
                if row[0] == m[0] and row[1] == m[1] and row[1] != "":
                    status = 1
                    feedback = "ok"
                    plz = row[5]
                    gutscheincode = row[11]
                    modelAB = row[47]
                    sub_picture = row[48]
                    print row[41]
                    print row[41]
                    print row[27]
                    print row[28]
                    print row[42]
                    change = transfer_quiz_results_to_new_user(gutscheincode, gutscheincode_old, c, conn)

                    c.execute("""insert into session_id_match_userdaten values (%s,%s)""", (gutscheincode, x,))
                    c.execute("""update userdaten set lastsessionid=%s, userbildlink=%s where lastsessionid=%s""",
                              ("", "true", x,))
                    merge_cart_details_from_old_to_new_session(gutscheincode, gutscheincode_old, c, conn)
                    if test_whether_quantities_are_available_for_order(gutscheincode, c, conn) == "update warenkorb":
                        feedback = "update warenkorb"

                    define_wishlist_object(gutscheincode, modelAB, sub_picture, c, conn)
                    define_warenkorb_object(gutscheincode, modelAB, sub_picture, c, conn)
                    define_rebates(gutscheincode, "", "", "", "", c, conn,
                                   define_standard_lieferadresse(gutscheincode, c), "no", "no", "no")

            if status == 0:
                feedback = "wrong data"
            else:
                if feedback != "update warenkorb":
                    feedback = "Produktauswahl/BH Sets"
        else:
            feedback = data
        conn.close()
        return HttpResponse(json.dumps(feedback), content_type='application/json')
    else:
        raise Http404


def merge_cart_details_from_old_to_new_session(gutscheincode, gutscheincode_old, c, conn):
    c.execute("""select * from cart_details where gutscheincode=%s and bestellt=%s""", (gutscheincode, "nein",))
    cart_details_new = c.fetchall()
    for row in cart_details_new:
        c.execute("""select * from cart_details where gutscheincode=%s and bestellt=%s""", (gutscheincode_old, "nein",))
        cart_details_old = c.fetchall()
        existiert = "nein"
        neue_menge = 0
        for row_2 in cart_details_old:
            if row[9] == "lingerie":
                if row[2] == row_2[2] and row[3] == row_2[3] and row[4] == row_2[4] and row[7] == row_2[7] and row[9] == \
                        row_2[9]:
                    neue_menge = row[1] + row_2[1]
                    existiert = "ja"
            if row[9] == "panties":
                if row[3] == row_2[3] and row[4] == row_2[4] and row[9] == row_2[9]:
                    neue_menge = row[1] + row_2[1]
                    existiert = "ja"
        if existiert == "ja":
            if row[9] == "lingerie":
                c.execute(
                    """update cart_details set anzahl=%s where bhgroesse=%s and slipgroesse=%s and stylecode=%s and color=%s and gutscheincode=%s and bestellt=%s and productgroup=%s""",
                    (neue_menge, row[2], row[3], row[7], row[4], gutscheincode, "nein", row[9],))
                c.execute(
                    """delete from cart_details where bhgroesse=%s and slipgroesse=%s and stylecode=%s and color=%s and gutscheincode=%s and bestellt=%s and productgroup=%s""",
                    (row[2], row[3], row[7], row[4], gutscheincode_old, "nein", row[9],))
            if row[9] == "panties":
                c.execute(
                    """update cart_details set anzahl=%s where slipgroesse=%s and color=%s and gutscheincode=%s and bestellt=%s and productgroup=%s""",
                    (neue_menge, row[3], row[4], gutscheincode, "nein", row[9],))
                c.execute(
                    """delete from cart_details where slipgroesse=%s and color=%s and gutscheincode=%s and bestellt=%s and productgroup=%s""",
                    (row[3], row[4], gutscheincode_old, "nein", row[9],))

    conn.commit()
    c.execute("""update cart_details set gutscheincode=%s where gutscheincode=%s""",
              (gutscheincode, gutscheincode_old,))
    conn.commit()


def transfer_quiz_results_to_new_user(gutscheincode, gutscheincode_old, c, conn):
    c.execute("""select * from userdaten where gutscheincode=%s """, (gutscheincode_old,))
    change = "no"
    for row in c:
        print row[27]
        if row[27] != -1 and row[28] != -1 and row[29] != "" and row[27] != None and row[28] != None and row[
            29] != None:
            c.execute(
                """update userdaten set bandclickfirstid=%s, cupclickfirstid=%s, brandclickfirstid=%s where gutscheincode=%s""",
                (row[27], row[28], row[29], gutscheincode,))
            change = "yes"
        if row[30] != -1 and row[31] != -1 and row[32] != "" and row[30] != None and row[31] != None and row[
            32] != None:
            c.execute(
                """update userdaten set bandclicksecondid=%s, cupclicksecondid=%s, brandclicksecondid=%s where gutscheincode=%s""",
                (row[30], row[31], row[32], gutscheincode,))
            change = "yes"
        if row[33] != -1 and row[33] != None:
            c.execute("""update userdaten set question2=%s where gutscheincode=%s""", (row[33], gutscheincode,))
            change = "yes"
        if row[34] != -1 and row[34] != None:
            c.execute("""update userdaten set question3=%s where gutscheincode=%s""", (row[34], gutscheincode,))
            change = "yes"
        if row[35] != -1 and row[35] != None:
            c.execute("""update userdaten set question4=%s where gutscheincode=%s""", (row[35], gutscheincode,))
            change = "yes"

        if row[38] != -1 and row[38] != None:
            c.execute("""update userdaten set question5=%s where gutscheincode=%s""", (row[38], gutscheincode,))
            change = "yes"
        if row[39] != -1 and row[39] != None:
            c.execute("""update userdaten set question6=%s where gutscheincode=%s""", (row[39], gutscheincode,))
            change = "yes"
        if row[40] != -1 and row[40] != None:
            c.execute("""update userdaten set question6a=%s where gutscheincode=%s""", (row[40], gutscheincode,))
            change = "yes"

        print "transfer_quiz_results_to_new_user"
        print row[41]
        print row[42]
        if row[41] != -1 and row[41] != None:
            c.execute("""update userdaten set question8=%s where gutscheincode=%s""", (row[41], gutscheincode,))
            change = "yes"

        if row[42] != -1 and row[42] != None:
            c.execute("""update userdaten set question9=%s where gutscheincode=%s""", (row[42], gutscheincode,))
            change = "yes"

        if row[53] != -1 and row[53] != None:
            c.execute("""update userdaten set pantyid=%s where gutscheincode=%s""", (row[53], gutscheincode,))
            change = "yes"
        if row[26] == "yes":
            c.execute("""update userdaten set quiztaken=%s where gutscheincode=%s""", (row[26], gutscheincode,))
    conn.commit()
    print "change"
    print change

    if change == "yes":
        c.execute("""select * from userdaten where gutscheincode=%s """, (gutscheincode,))
        for row in c:
            if row[26] == "yes":
                print row[27]
                print row[28]
                print "aendere showroom"
                generate_showroom(c, conn, row[27], row[28], row[29], row[30], row[31], row[32], row[33], row[34],
                                  row[35], row[38], row[39], row[40], row[41], row[42], row[53], gutscheincode)


@csrf_exempt
def gast_anmeldung(request):
    if request.is_ajax() and request.GET:
        n = request.GET.get('item')

        m = n.split(",")
        print "gast_anmeldung(request):"

        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)

        feedback = ""

        x = str(request.session.session_key)
        m[0] = m[0].lower()
        try:
            validate_email(m[0])
        except:
            feedback = "email falsch"
        print m[0]

        if feedback == "":
            password_new = id_generator_short()
            password_new_hash = hashlib.sha512(password_new).hexdigest()

            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip_adresse = x_forwarded_for.split(',')[0]
            else:
                ip_adresse = request.META.get('REMOTE_ADDR')
            user = get_userid_from_session_id(c, x)
            if x != "None":
                c.execute("""select * from userdaten where email=%s """, (m[0],))
                for row in c:
                    gutscheincode = row[11]
                    if row[0] == m[0] and row[7] != "":
                        status = 1
                        feedback = "exists already"

            if feedback != "exists already":
                status = 0

                current_time = datetime.datetime.now(pytz.timezone('Europe/Berlin')).time()
                now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
                date_ = str(now.year) + str((now.month) - 1) + str(now.day)
                time_ = str(current_time)
                time__ = time_.replace(":", "")
                time__ = time__.replace(".", "")

                security_code = id_generator_long()

                count_rows_bestellt_table = c.execute("""select * from anmeldebestaetigungen where userid=%s """,
                                                      (user,))
                c.execute(count_rows_bestellt_table)
                zaehler_anmeldungen = int(c.rowcount)

                if zaehler_anmeldungen == 0:
                    c.execute("""insert into anmeldebestaetigungen values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (
                    m[0], security_code, ip_adresse, "", date_, "", time__, "", 0, "", "false", user, password_new,))

                c.execute("""update userdaten set email=%s, passwort=%s,emailquiz=%s where gutscheincode=%s""",
                          (m[0], password_new_hash, m[0], user,))

                conn.commit()
                feedback = "Produktauwahl/Panties"

        conn.close()
        return HttpResponse(json.dumps(feedback), content_type='application/json')
    else:
        raise Http404


@csrf_exempt
def updater_user_registration(request):
    if request.is_ajax() and request.POST:
        n = request.POST.get('item')

        m = n.split(",")

        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)

        feedback = ""

        x = str(request.session.session_key)
        m[0] = m[0].lower()
        try:
            validate_email(m[0])
        except:
            feedback = "email falsch"
        print m[0]

        if feedback == "":
            m[1] = hashlib.sha512(m[1]).hexdigest()

            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip_adresse = x_forwarded_for.split(',')[0]
            else:
                ip_adresse = request.META.get('REMOTE_ADDR')
            user = get_userid_from_session_id(c, x)
            if x != "None":
                c.execute("""select * from userdaten where email=%s """, (m[0],))
                for row in c:
                    gutscheincode = row[11]
                    if row[0] == m[0]:
                        status = 1
                        feedback = "exists already"

            if feedback != "exists already":
                status = 0
                email_adresse_bestaetigen_versand_email(m[0], c, conn, ip_adresse, user)

                if len(m) == 2:
                    c.execute(
                        """update userdaten set email=%s, passwort=%s,emailquiz=%s,userbildlink=%s where gutscheincode=%s""",
                        (m[0], m[1], m[0], "true", user,))
                else:
                    c.execute("""update userdaten set email=%s,emailquiz=%s where gutscheincode=%s""",
                              (m[0], m[0], user,))

                conn.commit()
                feedback = "Produktauwahl/Panties"

        conn.close()
        return HttpResponse(json.dumps(feedback), content_type='application/json')


@csrf_exempt
def zur_kasse(request):
    if request.is_ajax() and request.POST:
        VIP = request.POST.get('VIP')

        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)

        x = str(request.session.session_key)

        if VIP == "VIP":
            feedback = "successful"
            c.execute("""update userdaten set shoppingtype=%s where gutscheincode=%s""",
                      (VIP, get_userid_from_session_id(c, x),))
            conn.commit()
        else:
            if VIP != "VIP":
                c.execute("""update userdaten set shoppingtype=%s where gutscheincode=%s""",
                          (VIP, get_userid_from_session_id(c, x),))
                conn.commit()
                feedback = "successful"
            else:
                feedback = "not successful"

        conn.close()
        return HttpResponse(json.dumps(feedback), content_type='application/json')


@csrf_exempt
def register_user(request):
    if request.is_ajax() and request.POST:
        n = request.POST.get('item')
        gutscheincode = request.POST.get('gutscheincode')
        m = n.split(",")

        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)

        validate_email(m[0])
        c.execute("""select * from userdaten where email=%s """, (m[0],))
        for row in c:
            if row[0] == m[0]:
                status = 1
                feedback = "exists already"

        if feedback != "exists already":
            status = 0
            #            if not request.session.exists(request.session.session_key):
            #                request.session.create()
            x = str(request.session.session_key)

            email_adresse_bestaetigen_versand_email(m[0], c, conn, gutscheincode)

            credit = 0

            geworben = "nein"
            genutztergutscheincode = ""

            if status == 0:
                now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
                Monat = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober",
                         "November", "Dezember"]
                date_short = str(now.day) + ". " + Monat[(now.month) - 1] + " " + str(now.year)

                c.execute("""select * from userdaten where gutscheincode=%s """, (gutscheincode,))

                userdaten = c.fetchall()

                for row in userdaten:
                    if row[11] == gutscheincode:
                        c.execute("""select * from bestellt where gutscheincode=%s """, (gutscheincode,))
                        bestellt_daten = c.fetchall()

                        zaehler_4 = 0
                        for row_3 in bestellt_daten:
                            zaehler_4 = zaehler_4 + 1

                        if zaehler_4 != 0:
                            geworben = "ja"
                            credit = 10

                            genutztergutscheincode = gutscheincode
                            c.execute("""insert into %s values (%%s,%%s,%%s,%%s)""" % (gutscheincode),
                                      (date_short, 0, "", row[11],))
                            conn.commit()

                conn.commit()
                feedback = "Produktauswahl/Panties"
        conn.close()
        return HttpResponse(json.dumps(feedback), content_type='application/json')
    else:
        raise Http404


def genuegend_warenmenge_vorhanden(panty_type, shopping_type, user, anzahl_lingerie, anzahl_panties, add_or_erase,
                                   stylecode_lingerie, colorcode_lingerie, colorcode_panties, bh_groesse,
                                   slip_groesse_lingerie, slip_groesse_panties, c, conn):
    print "ASDASDASD"
    alter_bestellwert_lingerie = 0
    neuer_bestellwert_lingerie = 0
    alter_bestellwert_panties_1 = 0
    neuer_bestellwert_panties_1 = 0
    alter_bestellwert_panties_2 = 0
    neuer_bestellwert_panties_2 = 0

    if bh_groesse != "":
        c.execute(
            """select * from cart_details where gutscheincode=%s and bestellt=%s and stylecode=%s and color=%s and bhgroesse=%s and slipgroesse=%s and productgroup=%s """,
            (user, "nein", stylecode_lingerie, colorcode_lingerie, bh_groesse, slip_groesse_lingerie, "lingerie"))
        for row in c:
            alter_bestellwert_lingerie = row[1] + alter_bestellwert_lingerie
            alter_bestellwert_panties_1 = row[1] + alter_bestellwert_panties_1

        if add_or_erase == "":
            neuer_bestellwert_lingerie = int(anzahl_lingerie)
            neuer_bestellwert_panties_1 = int(anzahl_lingerie)
        else:
            if add_or_erase == "add":
                neuer_bestellwert_lingerie = alter_bestellwert_lingerie + 1
                neuer_bestellwert_panties_1 = alter_bestellwert_panties_1 + 1
            else:
                if add_or_erase == "erase":
                    neuer_bestellwert_lingerie = alter_bestellwert_lingerie - 1
                    neuer_bestellwert_panties_1 = alter_bestellwert_panties_1 - 1
                else:
                    if add_or_erase == "change":
                        neuer_bestellwert_lingerie = int(anzahl_lingerie)
                        neuer_bestellwert_panties_1 = int(anzahl_lingerie)

    if slip_groesse_panties != "":

        print "slip_groesse_panties"
        c.execute(
            """select * from cart_details where gutscheincode=%s and bestellt=%s and color=%s and slipgroesse=%s""",
            (user, "nein", colorcode_panties, slip_groesse_panties,))
        for row in c:
            if row[9] == "panties":
                alter_bestellwert_panties_2 = row[1] + alter_bestellwert_panties_2
        if add_or_erase == "":
            neuer_bestellwert_panties_2 = int(anzahl_panties)
        else:
            if add_or_erase == "add":
                neuer_bestellwert_panties_2 = alter_bestellwert_panties_2 + 1
            else:
                if add_or_erase == "erase":
                    neuer_bestellwert_panties_2 = alter_bestellwert_panties_2 - 1
                else:
                    if add_or_erase == "change":
                        neuer_bestellwert_panties_2 = int(anzahl_panties)

    gesamt_bestellwert_panties_1 = neuer_bestellwert_panties_1 - alter_bestellwert_panties_1
    gesamt_bestellwert_panties_2 = neuer_bestellwert_panties_2 - alter_bestellwert_panties_2
    gesamt_bestellwert_lingerie = neuer_bestellwert_lingerie - alter_bestellwert_lingerie
    print gesamt_bestellwert_lingerie
    if colorcode_panties == colorcode_lingerie and slip_groesse_panties == slip_groesse_lingerie:
        gesamt_bestellwert_panties_1 = gesamt_bestellwert_panties_1 + gesamt_bestellwert_panties_2
        c.execute(
            """select * from cart_details where gutscheincode=%s and bestellt=%s and color=%s and slipgroesse=%s""",
            (user, "nein", colorcode_panties, slip_groesse_panties,))
        for row in c:
            print row[1]
            gesamt_bestellwert_panties_1 = gesamt_bestellwert_panties_1 + row[1]
    else:
        c.execute(
            """select * from cart_details where gutscheincode=%s and bestellt=%s and color=%s and slipgroesse=%s""",
            (user, "nein", colorcode_panties, slip_groesse_panties,))
        for row in c:
            gesamt_bestellwert_panties_2 = gesamt_bestellwert_panties_2 + row[1]
        c.execute(
            """select * from cart_details where gutscheincode=%s and bestellt=%s and color=%s and slipgroesse=%s""",
            (user, "nein", colorcode_lingerie, slip_groesse_lingerie,))
        for row in c:
            gesamt_bestellwert_panties_1 = gesamt_bestellwert_panties_1 + row[1]

    if bh_groesse != "":
        print "jeeeetzt"

        c.execute(
            """select * from cart_details where gutscheincode=%s and bestellt=%s and color=%s and bhgroesse=%s and stylecode=%s and productgroup=%s""",
            (user, "nein", colorcode_lingerie, bh_groesse, stylecode_lingerie, "lingerie",))
        for row in c:
            print row[1]
            print gesamt_bestellwert_lingerie
            gesamt_bestellwert_lingerie = gesamt_bestellwert_lingerie + row[1]

    print "gesamt_bestellwert_panties_1"
    print gesamt_bestellwert_panties_1
    print "gesamt_bestellwert_panties_2"
    print gesamt_bestellwert_panties_2
    print "gesamt_bestellwert_lingerie"
    print gesamt_bestellwert_lingerie
    feedback_panties = ""
    feedback_lingerie = ""
    feedback_lingerie_slip = ""

    print str(neuer_bestellwert_lingerie) + "==0 and " + str(alter_bestellwert_lingerie) + "!=0) or (" + str(
        neuer_bestellwert_panties_1) + "==0 and " + str(alter_bestellwert_panties_1) + "!=0) or (" + str(
        neuer_bestellwert_panties_2) + "==0 and " + str(alter_bestellwert_panties_2) + "!=0)"
    if (neuer_bestellwert_lingerie == 0 and alter_bestellwert_lingerie != 0) or (
            neuer_bestellwert_panties_1 == 0 and alter_bestellwert_panties_1 != 0) or (
            neuer_bestellwert_panties_2 == 0 and alter_bestellwert_panties_2 != 0):
        feedback = "ok"
    else:

        feedback = "not ok"
        feedback_lingerie = "lingerie not available"
        if bh_groesse != "":
            c.execute("""select * from stylecode where type=%s and stylecode=%s and color=%s and size=%s""",
                      ("BH", stylecode_lingerie, colorcode_lingerie, bh_groesse,))
            for row_2 in c:
                print "gesamt_bestellwert_lingerie"
                print row_2[4]
                print row_2[5]
                print gesamt_bestellwert_lingerie
                if row_2[4] >= row_2[5] + gesamt_bestellwert_lingerie:
                    feedback = "ok"
                    feedback_lingerie = ""
        else:
            feedback = "ok"
            feedback_lingerie = ""

        if feedback == "ok":

            if slip_groesse_lingerie != "":

                feedback = "not ok"
                feedback_lingerie_slip = "lingerie_panty not available"
                c.execute("""select * from stylecode where type=%s and color=%s and size=%s""",
                          ("panties", colorcode_lingerie, slip_groesse_lingerie,))
                for row_2 in c:
                    print "neuer_bestellwert_panties_1"
                    print row_2[4]
                    print row_2[5]
                    print gesamt_bestellwert_panties_1
                    if row_2[4] >= row_2[5] + gesamt_bestellwert_panties_1:
                        feedback = "ok"
                        feedback_lingerie_slip = ""

            if feedback == "ok":
                if slip_groesse_panties != "":

                    feedback_panties = "panty not available"
                    feedback = "not ok"
                    c.execute("""select * from stylecode where type=%s and color=%s and size=%s""",
                              ("panties", colorcode_panties, slip_groesse_panties,))
                    for row_2 in c:
                        print "neuer_bestellwert_panties_2_alter_bestellwert_panties_1"
                        print row_2[4]
                        print row_2[5]
                        print gesamt_bestellwert_panties_2

                        if row_2[4] >= row_2[5] + gesamt_bestellwert_panties_2:
                            feedback = "ok"
                            feedback_panties = ""

        print "neuer_bestellwert_lingerie"
        print neuer_bestellwert_lingerie
        print alter_bestellwert_lingerie
    if feedback == "ok":

        if neuer_bestellwert_lingerie - alter_bestellwert_lingerie != 0:

            if neuer_bestellwert_lingerie > 0 and alter_bestellwert_lingerie == 0:
                preis_lingerie = get_price(stylecode_lingerie, colorcode_lingerie, shopping_type, c, "lingerie")
                lingerie_name = get_lingerie_name(stylecode_lingerie, colorcode_lingerie, c)
                c.execute(
                    """insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % (
                    "cart_details"), (
                    lingerie_name, 1, bh_groesse, slip_groesse_lingerie, colorcode_lingerie, "", "Bestellt",
                    stylecode_lingerie, preis_lingerie, "lingerie", 0, "", "nein", user, "", "", "", "", "", "", "", "",
                    "nein", "nein", 0, 0,))
            else:
                if neuer_bestellwert_lingerie == 0 and alter_bestellwert_lingerie != 0:
                    c.execute(
                        """delete from %s where stylecode=%%s and color=%%s and bhgroesse=%%s and slipgroesse=%%s and gutscheincode=%%s and bestellt=%%s and productgroup=%%s""" % (
                        "cart_details"), (
                        stylecode_lingerie, colorcode_lingerie, bh_groesse, slip_groesse_lingerie, user, "nein",
                        "lingerie",))
                else:
                    if neuer_bestellwert_lingerie != alter_bestellwert_lingerie:
                        c.execute(
                            """update %s set anzahl=%%s where stylecode=%%s and color=%%s and bhgroesse=%%s and slipgroesse=%%s and gutscheincode=%%s and bestellt=%%s and productgroup=%%s""" % (
                            "cart_details"), (
                            int(neuer_bestellwert_lingerie), stylecode_lingerie, colorcode_lingerie, bh_groesse,
                            slip_groesse_lingerie, user, "nein", "lingerie"))

        if slip_groesse_panties != "":
            if neuer_bestellwert_panties_2 - alter_bestellwert_panties_2 != 0:
                if neuer_bestellwert_panties_2 > 0 and alter_bestellwert_panties_2 == 0:
                    preis_panties = get_price("", colorcode_panties, shopping_type, c, "panties")
                    panty_name = get_panty_name(panty_type, colorcode_panties, c)
                    c.execute(
                        """insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % (
                        "cart_details"), (
                        panty_name, 1, "", slip_groesse_panties, colorcode_panties, "", "Bestellt", "", preis_panties,
                        "panties", 0, "", "nein", user, "", "", "", "", "", "", "", "", "nein", "nein", 0, 0,))
                else:
                    if neuer_bestellwert_panties_2 == 0 and alter_bestellwert_panties_2 != 0:
                        c.execute(
                            """delete from %s where color=%%s and slipgroesse=%%s and gutscheincode=%%s and bestellt=%%s and productgroup=%%s""" % (
                            "cart_details"), (colorcode_panties, slip_groesse_panties, user, "nein", "panties"))
                    else:
                        if neuer_bestellwert_panties_2 != alter_bestellwert_panties_2:
                            c.execute(
                                """update %s set anzahl=%%s where color=%%s and slipgroesse=%%s and gutscheincode=%%s and bestellt=%%s and productgroup=%%s""" % (
                                "cart_details"), (
                                int(neuer_bestellwert_panties_2), colorcode_panties, slip_groesse_panties, user, "nein",
                                "panties"))

        conn.commit()

        return "true"
    else:
        print "feedback_lingerie"
        print feedback_lingerie
        print feedback_lingerie_slip
        print feedback_panties

        if feedback_lingerie != "":
            return feedback_lingerie
        else:
            if feedback_lingerie_slip != "":
                return feedback_lingerie_slip
            else:
                if feedback_panties != "":
                    return feedback_panties
                else:
                    return "true"


def update_bestellt_table(x, bestellnummer, bestellungspreis, lieferdetails, adresse, plz, stadt, unternehmensdetails,
                          vorname, nachname, c, conn):
    c.execute("""select * from userdaten """)

    userdaten = c.fetchall()

    for row_2 in userdaten:
        if row_2[9] == x:
            c.execute("""select * from bestellt where gutscheincode=%s """, (row_2[11],))
            bestellt_table = c.fetchall()

            for row in bestellt_table:
                if (row[21] == bestellnummer):
                    j = 0
                    output = ""
                    o = row[0]
                    c.execute(
                        """update %s set bestellungspreis=%%s,lieferdetails=%%s,adresse=%%s,plz=%%s,stadt=%%s,unternehmensdetails=%%s,vorname=%%s,nachname=%%s where bestellnummer=%%s and gutscheincode=%%s""" % (
                        "bestellt"), (
                        bestellungspreis, lieferdetails, adresse, plz, stadt, unternehmensdetails, vorname, nachname,
                        bestellnummer, row_2[11]))
                    conn.commit()


@csrf_exempt
def select_shopping_type(request):
    if request.is_ajax() and request.GET:

        shopping_type = request.GET.get('shopping_type')
        land = request.GET.get('land')

        x = str(request.session.session_key)

        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)

        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            for row in c:
                user = row[11]
                modelAB = row[47]
                sub_picture = row[48]
                if shopping_type == "VIP":
                    rabattcode = "willkommen"
                else:
                    rabattcode = "willkommen"
        if land == "" or land == None:
            land = define_standard_lieferadresse(user, c)
        update_cart_details_based_on_shopping_type(shopping_type, user, c, conn)
        if shopping_type == "VIP":
            c.execute("""update userdaten set shoppingtype=%s where gutscheincode=%s""", (shopping_type, user,))
            c.execute("""update userdaten set genutztergutscheincode=%s where gutscheincode=%s""",
                      (rabattcode.upper(), user,))
        else:
            c.execute("""update userdaten set shoppingtype=%s where gutscheincode=%s""", (shopping_type, user,))
            c.execute("""update userdaten set genutztergutscheincode=%s where gutscheincode=%s""",
                      (rabattcode.upper(), user,))
        conn.commit()
        feedback_recheck_gutschein_wert = recheck_gutschein_wert(c, user, conn)

        if feedback_recheck_gutschein_wert != "error" and feedback_recheck_gutschein_wert != "nur Non-VIP" and feedback_recheck_gutschein_wert != "VIP" and feedback_recheck_gutschein_wert != "nur Neukunde" and feedback_recheck_gutschein_wert != "nur Kunde":

            feedback = get_warenkorb_and_rebates(define_warenkorb(user, modelAB, sub_picture, c, conn),
                                                 define_rebates(user, "", "", "", "", c, conn, land, "no", "no", "no"))
            feedback = get_warenkorb_and_rebates_and_error_message(feedback, "no")
            define_warenkorb_object(user, modelAB, sub_picture, c, conn)
        else:
            gutscheinwert_abrufen("", c, user, conn, "nein", user)
            feedback = get_warenkorb_and_rebates(define_warenkorb(user, modelAB, sub_picture, c, conn),
                                                 define_rebates(user, "", "", "", "", c, conn, land, "no", "no", "no"))
            define_warenkorb_object(user, modelAB, sub_picture, c, conn)

            feedback = get_warenkorb_and_rebates_and_error_message(feedback, feedback_recheck_gutschein_wert)
        conn.close()
        return HttpResponse(json.dumps(feedback), content_type='application/json')
    else:
        raise Http404


def update_cart_details_based_on_shopping_type(shopping_type, user, c, conn):
    c.execute("""select * from cart_details where gutscheincode=%s""", (user,))
    cart_daten = c.fetchall()
    for row in cart_daten:
        c.execute("""select * from lingerieselection """)
        lingerieselection = c.fetchall()
        for row_2 in lingerieselection:
            if row[7] == row_2[12] and row[4] == row_2[13] and row[0] == row_2[0]:
                if shopping_type == "Regular":  # pay as you go
                    c.execute(
                        """update %s set preis=%%s where stylecode=%%s and color=%%s and style=%%s and gutscheincode=%%s""" % (
                        "cart_details"), (row_2[3], row[7], row[4], row[0], user,))
                else:
                    c.execute(
                        """update %s set preis=%%s where stylecode=%%s and color=%%s and style=%%s and gutscheincode=%%s""" % (
                        "cart_details"), (row_2[4], row[7], row[4], row[0], user,))
    conn.commit()


def update_detail_bestellung_table(userid, anzahl, bestellnummer, freiemenge, status, existiert_set, add_or_erase,
                                   anzahl_new, stylecode, colorcode, bh_groesse, slip_groesse, regular_price,
                                   subscription_price, c, conn, productgroup, stylename, x, slip_groesse_2,
                                   existiert_slip, priceforaddlpanty, panty_type):
    c.execute("""select * from userdaten where gutscheincode=%s""", (userid,))
    for row_2 in c:
        shopping_type = row_2[22]
        cart_quantity = row_2[17]

    c.execute("""select * from cart_details where gutscheincode=%s and bestellt=%s""", (userid, "nein",))
    for row in c:
        print(row[7] + "==" + stylecode + "and" + row[2] + "==" + bh_groesse + "and" + row[
            3] + "==" + slip_groesse + "and" + row[4] + "==" + colorcode)
        if row[7] == stylecode and row[2] == bh_groesse and row[3] == slip_groesse and row[4] == colorcode:
            anzahl = row[1]
        if row[3] == slip_groesse_2 and row[4] == colorcode:
            anzahl_2 = row[1]

    print "update_detail_bestellung_table"
    print(add_or_erase)
    print existiert_set
    print existiert_slip
    print slip_groesse
    print slip_groesse_2
    #    print anzahl_2

    preis_lingerie = get_price(stylecode, colorcode, shopping_type, c, "lingerie")
    preis_panties = get_price(stylecode, colorcode, shopping_type, c, "panties")

    print preis_lingerie
    print preis_panties

    if existiert_set == "ja" and slip_groesse != "":
        if add_or_erase == "":
            c.execute(
                """update %s set anzahl=%%s,preis=%%s where stylecode=%%s and color=%%s and bhgroesse=%%s and slipgroesse=%%s and gutscheincode=%%s and bestellt=%%s""" % (
                "cart_details"),
                (int(anzahl), preis_lingerie, stylecode, colorcode, bh_groesse, slip_groesse, userid, "nein"))
            conn.commit()
        else:
            if add_or_erase == "add":
                c.execute(
                    """update %s set anzahl=%%s,preis=%%s where stylecode=%%s and color=%%s and bhgroesse=%%s and slipgroesse=%%s and gutscheincode=%%s and bestellt=%%s""" % (
                    "cart_details"),
                    (int(anzahl) + 1, preis_lingerie, stylecode, colorcode, bh_groesse, slip_groesse, userid, "nein"))
                conn.commit()
            else:
                if add_or_erase == "erase":
                    if anzahl != 1 and anzahl != 0:
                        c.execute(
                            """update %s set anzahl=%%s,preis=%%s where stylecode=%%s and color=%%s and bhgroesse=%%s and slipgroesse=%%s and gutscheincode=%%s and bestellt=%%s""" % (
                            "cart_details"), (
                            int(anzahl) - 1, preis_lingerie, stylecode, colorcode, bh_groesse, slip_groesse, userid,
                            "nein"))
                        conn.commit()
                    else:
                        c.execute(
                            """delete from %s where stylecode = %%s and color=%%s and bhgroesse=%%s and slipgroesse=%%s and gutscheincode=%%s and bestellt=%%s""" % (
                            "cart_details"), (stylecode, colorcode, bh_groesse, slip_groesse, userid, "nein"))
                        conn.commit()

                else:
                    if add_or_erase == "change":
                        if int(anzahl_new) > 0:
                            c.execute(
                                """update %s set anzahl=%%s,preis=%%s where stylecode=%%s and color=%%s and bhgroesse=%%s and slipgroesse=%%s and gutscheincode=%%s and bestellt=%%s""" % (
                                "cart_details"), (
                                int(anzahl_new), preis_lingerie, stylecode, colorcode, bh_groesse, slip_groesse, userid,
                                "nein"))
                            conn.commit()
                        else:
                            c.execute(
                                """delete from %s where stylecode = %%s and color=%%s and bhgroesse=%%s and slipgroesse=%%s and gutscheincode=%%s and bestellt=%%s""" % (
                                "cart_details"), (stylecode, colorcode, bh_groesse, slip_groesse, userid, "nein"))
                            conn.commit()


    else:
        if slip_groesse != "":
            if add_or_erase == "add":
                print(userid)
                print(x)
                c.execute(
                    """insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % (
                    "cart_details"), (
                    stylename, 1, bh_groesse, slip_groesse, colorcode, "", status, stylecode, preis_lingerie,
                    productgroup, 0, x, "nein", userid, "", "", "", "", "", "", "", "", "nein",))

                conn.commit()
                print("ASD")

    if existiert_slip == "ja":
        if add_or_erase == "":
            if slip_groesse_2 != "":
                c.execute(
                    """update %s set anzahl=%%s,preis=%%s where color=%%s and bhgroesse=%%s and slipgroesse=%%s and gutscheincode=%%s and bestellt=%%s""" % (
                    "cart_details"), (int(anzahl_2), preis_lingerie, colorcode, "", slip_groesse_2, userid, "nein"))
            conn.commit()
        else:
            if add_or_erase == "add":
                if slip_groesse_2 != "":
                    c.execute(
                        """update %s set anzahl=%%s,preis=%%s where color=%%s and bhgroesse=%%s and slipgroesse=%%s and gutscheincode=%%s and bestellt=%%s""" % (
                        "cart_details"),
                        (int(anzahl_2) + 1, preis_lingerie, colorcode, "", slip_groesse_2, userid, "nein"))
                conn.commit()
            else:
                if add_or_erase == "erase":
                    if anzahl_2 != 1 and anzahl_2 != 0:
                        c.execute(
                            """update %s set anzahl=%%s,preis=%%s where color=%%s and bhgroesse=%%s and slipgroesse=%%s and gutscheincode=%%s and bestellt=%%s""" % (
                            "cart_details"),
                            (int(anzahl_2) - 1, preis_lingerie, colorcode, "", slip_groesse_2, userid, "nein"))
                        conn.commit()
                    else:
                        c.execute(
                            """delete from %s where color=%%s and bhgroesse=%%s and slipgroesse=%%s and gutscheincode=%%s and bestellt=%%s""" % (
                            "cart_details"), (colorcode, "", slip_groesse_2, userid, "nein"))
                        conn.commit()


                else:
                    if add_or_erase == "change":
                        if int(anzahl_new) > 0:
                            c.execute(
                                """update %s set anzahl=%%s,preis=%%s where color=%%s and bhgroesse=%%s and slipgroesse=%%s and gutscheincode=%%s and bestellt=%%s""" % (
                                "cart_details"),
                                (int(anzahl_new), preis_lingerie, colorcode, "", slip_groesse, userid, "nein"))
                            conn.commit()
                        else:
                            c.execute(
                                """delete from %s where color=%%s and bhgroesse=%%s and slipgroesse=%%s and gutscheincode=%%s and bestellt=%%s""" % (
                                "cart_details"), (colorcode, "", slip_groesse, userid, "nein"))
                            conn.commit()


    else:
        if add_or_erase == "add":
            print(userid)
            print(x)
            print("priceforaddlpanty")
            print priceforaddlpanty

            if slip_groesse_2 != "":
                panty_name = get_panty_name(panty_type, colorcode, c)
                c.execute(
                    """insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % (
                    "cart_details"), (
                    panty_name, 1, "", slip_groesse_2, colorcode, "", status, "", preis_panties, "panties", 0, x,
                    "nein", userid, "", "", "", "", "", "", "", "", "nein",))

            conn.commit()
            print("ASD")


def get_panty_name(panty_type, colorcode, c):
    c.execute("""select * from lingerieselection""")
    lingerieselection = c.fetchall()
    get_panty_name_ = ""
    for row in lingerieselection:
        if row[13] == colorcode and row[2] == panty_type:
            get_panty_name_ = row[0]

    print "get_panty_name_"
    print get_panty_name_
    return get_panty_name_


def get_lingerie_name(stylecode, colorcode, c):
    c.execute("""select * from lingerieselection""")
    lingerieselection = c.fetchall()
    get_lingerie_name_ = ""
    for row in lingerieselection:
        if row[13] == colorcode and row[12] == stylecode and row[8] == "lingerie":
            get_lingerie_name_ = row[0]

    print "get_lingerie_name_"
    print get_lingerie_name_
    return get_lingerie_name_


def gutschein_einloesen_do_it(user, gutscheincode, art, c, conn, neukunde, VIP, userid):
    now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
    Monat = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November",
             "Dezember"]
    now_date = str(now.day) + ". " + str(Monat[now.month - 1]) + " " + str(now.year)

    someday = datetime.date(now.year, now.month, now.day)

    print("einloesen")
    print(art)
    output = ""
    #    try:
    if art == "einloesen":

        c.execute("""select * from gutscheine """)

        gutscheine_daten = c.fetchall()

        for row in gutscheine_daten:
            print(gutscheincode + "==" + str(row[0]) + "and" + row[2] + "==aktiv")
            if gutscheincode == str(row[0]) and row[2] == "aktiv":
                year = row[1][-4:]
                end = row[1].find(".") + 1
                day = row[1][:end - 1]
                month = monthToNum(row[1][end + 1:len(row[1]) - 5])
                date_gericht = datetime.date(int(year), int(month), int(day))
                diff = date_gericht - someday
                print(diff.days)
                if diff.days >= 0:

                    print("ASD")
                    print(row[15] + "==No and false==" + neukunde + ") or " + row[15] + "==All or (" + row[
                        15] + "==Yes and true==" + neukunde)
                    if (row[15] == "No" and "false" == neukunde) or row[15] == "All" or (
                            row[15] == "Yes" and "true" == neukunde):
                        print "erster schritt"
                        if row[14] == "All" or (VIP == "Regular" and row[14] == "Non-VIP") or (
                                VIP == "VIP" and row[14] == "VIP"):
                            print "zweiter schritt"
                            if row[16] == "Mehrmals":
                                print "dritter schritt"
                                c.execute("""update userdaten set genutztergutscheincode=%s where gutscheincode=%s""",
                                          (gutscheincode, user,))
                                conn.commit()
                                output = "gutschein aufgenommen"
                                print output
                                print gutscheincode
                                gutscheinwert_abrufen(gutscheincode, c, user, conn, "nein", userid)
                            else:
                                c.execute("""select * from benutztegutscheincodes where gutscheincode=%%s""", (userid))
                                benutztegutscheincodes = c.fetchall()
                                existiert = "nein"
                                for row_2 in benutztegutscheincodes:
                                    if row_2[1] == gutscheincode:
                                        existiert = "ja"

                                if existiert == "nein":
                                    c.execute(
                                        """update userdaten set genutztergutscheincode=%s where gutscheincode=%s""",
                                        (gutscheincode, user,))
                                    conn.commit()
                                    output = "gutschein aufgenommen"
                                    print output
                                    print gutscheincode
                                    gutscheinwert_abrufen(gutscheincode, c, user, conn, "nein", userid)
                                else:
                                    output = "error"
                        else:
                            if row[14] == "Non-VIP":
                                output = "nur Non-VIP"
                            else:
                                output = "VIP"
                    else:
                        if row[15] == "No":
                            output = "nur Neukunde"
                        else:
                            output = "nur Kunde"




    else:
        c.execute("""select * from gutscheine """)
        print("gutscheine")
        gutscheine_daten = c.fetchall()
        for row in gutscheine_daten:
            if gutscheincode == str(row[0]):
                c.execute("""update gutscheine set status=%s where gutscheincode=%s""", ("aktiv", row[0],))
                c.execute("""update userdaten set genutztergutscheincode=%s where gutscheincode=%s""", ("", user,))
                conn.commit()
                output = "gutschein geloescht"
                print(output)

                c.execute("""select * from cart_details where gutscheincode=%s""", (userid,))
                current_cart_database = c.fetchall()
                for row_2 in current_cart_database:
                    print("ja")
                    c.execute(
                        """update cart_details set gutscheinwert=%s where bhgroesse=%s and slipgroesse=%s and stylecode=%s and color=%s and gutscheincode=%s and bestellt=%s""",
                        ("", row_2[2], row_2[3], row_2[7], row_2[4], userid, "nein",))
                    conn.commit()

        if output == "":
            c.execute("""update userdaten set genutztergutscheincode=%s where gutscheincode=%s""", ("", user,))
            conn.commit()

    print "output"
    print output

    if output == "":
        if art == "einloesen":
            c.execute("""select * from userdaten where gutscheincode=%s """, (user,))
            userdaten = c.fetchall()
            for row in userdaten:
                if row[18] == "nein":
                    #                        count_rows_bestellt_table=c.execute ("""select * from bestellt where gutscheincode=%s """,(row[11],))
                    #                        c.execute(count_rows_bestellt_table)
                    #                       zaehler_geworbene=int(c.rowcount)

                    #                       if zaehler_geworbene==0:

                    count_rows_userdaten = c.execute("""select * from userdaten where gutscheincode=%s """,
                                                     (gutscheincode,))
                    c.execute(count_rows_userdaten)
                    zaehler_userdaten = int(c.rowcount)
                    print "zaehler_userdaten"
                    print zaehler_userdaten
                    if zaehler_userdaten == 1:
                        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
                        Monat = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", "Juli", "August", "September",
                                 "Oktober", "November", "Dezember"]
                        date_short = str(now.day) + ". " + Monat[(now.month) - 1] + " " + str(now.year)
                        c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s)""" % ("gutscheine_werben"),
                                  (date_short, 15, "", gutscheincode, row[11],))
                        c.execute(
                            """update userdaten set credit=%s, geworben=%s,messageshownfreundeeingeladen=%s where gutscheincode=%s""",
                            (15, "ja", "no", user,))
                        conn.commit()

    if output == "":
        output = "error"

    return output


@csrf_exempt
def get_gutschein_value(request):
    if request.is_ajax() and request.GET:
        gutscheincode = request.GET.get('gutscheincode')

        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)
        gutscheinwert = 0

        c.execute("""select * from gutscheine """)
        for row in c:
            if row[0] == gutscheincode:
                gutscheinwert = row[1]
        conn.close()
        return HttpResponse(json.dumps(gutscheinwert), content_type='application/json')


@csrf_exempt
def gutschein_einloesen(request):
    if request.is_ajax() and request.GET:
        gutscheincode = request.GET.get('gutscheincode').encode('utf-8')

        art = request.GET.get('art')
        land = request.GET.get('land')

        x = str(request.session.session_key)

        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')

        c = conn.cursor(buffered=True)

        VIP = "Regular"
        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            userdaten = c.fetchall()
            for row in userdaten:
                user = row[11]
                modelAB = row[47]
                sub_picture = row[48]
                neukunde = row[57]
                if row[22] == "VIP":
                    VIP = row[22]
        if land == "" or land == None:
            land = define_standard_lieferadresse(user, c)

        feedback_recheck_gutschein_wert = gutschein_einloesen_do_it(user, gutscheincode, art, c, conn, neukunde, VIP,
                                                                    user)

        if feedback_recheck_gutschein_wert != "error" and feedback_recheck_gutschein_wert != "nur Non-VIP" and feedback_recheck_gutschein_wert != "VIP" and feedback_recheck_gutschein_wert != "nur Neukunde" and feedback_recheck_gutschein_wert != "nur Kunde":
            feedback = get_warenkorb_and_rebates(define_warenkorb(user, modelAB, sub_picture, c, conn),
                                                 define_rebates(user, "", "", "", "", c, conn, land, "no", "no", "no"))
            feedback = get_warenkorb_and_rebates_and_error_message(feedback, "no")
        else:
            feedback = get_warenkorb_and_rebates(define_warenkorb(user, modelAB, sub_picture, c, conn),
                                                 define_rebates(user, "", "", "", "", c, conn, land, "no", "no", "no"))
            feedback = get_warenkorb_and_rebates_and_error_message(feedback, feedback_recheck_gutschein_wert)

    conn.close()
    return HttpResponse(json.dumps(feedback), content_type='application/json')


def recheck_gutschein_wert(c, user, conn):
    VIP = "Regular"
    c.execute("""select * from userdaten where gutscheincode=%s """, (user,))
    userdaten = c.fetchall()
    for row in userdaten:
        user = row[11]
        modelAB = row[47]
        sub_picture = row[48]
        neukunde = row[57]
        gutscheincode = row[21]
        art = "einloesen"
        if row[22] == "VIP":
            VIP = row[22]

    if gutscheincode != "":
        output = gutschein_einloesen_do_it(user, gutscheincode, art, c, conn, neukunde, VIP, user)

        if output == "error":
            c.execute("""update userdaten set genutztergutscheincode=%s where gutscheincode=%s""", ("", user,))
            conn.commit()

        print "recheck_gutschein_wert"
        return output
    else:
        return ""


def id_generator_long(size=24, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def id_generator_short(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def id_generator(issue, c, conn):
    Buchstabe = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]

    c.execute("""select * from laufendenummern """)
    laufendenummern = c.fetchall()
    for row in laufendenummern:
        if issue == "rechnungsnummer":
            nummer = row[0]
        if issue == "bestellnummer":
            nummer = row[1]
        if issue == "userid":
            nummer = row[2]
        if issue == "transaktionsnummersofortueberweisung":
            nummer = row[3]

    new_nummer = nummer + 1

    if issue == "rechnungsnummer":
        c.execute("""update laufendenummern set rechnungsnummer=%s""", (new_nummer,))
        conn.commit()
    if issue == "bestellnummer":
        c.execute("""update laufendenummern set bestellnummer=%s""", (new_nummer,))
        conn.commit()
    if issue == "userid":
        c.execute("""update laufendenummern set userid=%s""", (new_nummer,))
        conn.commit()
    if issue == "transaktionsnummersofortueberweisung":
        c.execute("""update laufendenummern set transaktionsnummersofortueberweisung=%s""", (new_nummer,))
        conn.commit()

    new_nummer_string = str(new_nummer)

    i = 0
    buchstaben = ""
    while i <= len(new_nummer_string) - 2:
        buchstaben = buchstaben + Buchstabe[int(new_nummer_string[i + 1:i + 2])]
        i = i + 1

    return buchstaben


def kreditkarte_clientid(gutscheincode_id, selected_zahlungsoption, c):
    c.execute("""select * from zahlungsmethoden where gutscheincode=%s """, (gutscheincode_id,))
    zaehler = 0
    for row in c:
        if zaehler == int(selected_zahlungsoption):
            return row[0]
        zaehler = zaehler + 1


def kreditkartennummer(gutscheincode_id, selected_zahlungsoption, c):
    if selected_zahlungsoption != "":
        c.execute("""select * from zahlungsmethoden where gutscheincode=%s """, (gutscheincode_id,))
        zaehler = 0
        for row in c:
            if row[10] == "kreditkarte":
                if zaehler == int(selected_zahlungsoption):
                    return row[4]
            else:
                if zaehler == int(selected_zahlungsoption):
                    return row[11]
            zaehler = zaehler + 1
    else:
        return ""


def pruefziffer(gutscheincode_id, selected_zahlungsoption, c):
    if selected_zahlungsoption != "":
        c.execute("""select * from zahlungsmethoden where gutscheincode=%s """, (gutscheincode_id,))
        zaehler = 0
        pruefziffer = ""
        for row in c:
            if zaehler == int(selected_zahlungsoption):
                pruefziffer = row[7]
            zaehler = zaehler + 1

        return pruefziffer
    else:
        return ""


def name_kreditkarte(gutscheincode_id, selected_zahlungsoption, c):
    if selected_zahlungsoption != "":
        c.execute("""select * from zahlungsmethoden where gutscheincode=%s """, (gutscheincode_id,))
        zaehler = 0
        for row in c:
            if zaehler == int(selected_zahlungsoption):
                return row[3]
            zaehler = zaehler + 1
    else:
        return ""


def ablaufdatum(gutscheincode_id, selected_zahlungsoption, c):
    if selected_zahlungsoption != "":
        c.execute("""select * from zahlungsmethoden where gutscheincode=%s """, (gutscheincode_id,))
        zaehler = 0
        for row in c:
            if zaehler == int(selected_zahlungsoption):
                return row[5] + " " + row[6]
            zaehler = zaehler + 1
    else:
        return ""


def ist_gutscheincode(gutscheincode, c):
    feedback = "nein"
    gutscheinwert = 0
    c.execute("""select * from gutscheine """)
    gutscheine = c.fetchall()
    for row in gutscheine:
        if row[0] == gutscheincode:
            feedback = "ja"

    return feedback


def check_haushalt_wurde_von_geworben(rabattcode, gutscheincode, adresse, plz, telefonnummer, kreditkartennummer, c,
                                      conn, user):
    print "check_haushalt_wurde_von_geworben"
    output = "false"
    print rabattcode + "!= and " + ist_gutscheincode(rabattcode, c) + "==nein and " + rabattcode + "!="
    if rabattcode != "" and ist_gutscheincode(rabattcode, c) == "nein" and rabattcode != " ":
        c.execute("""select * from keyuserdaten""")

        for row in c:
            print row[5] + "!=" + gutscheincode
            if row[5] != gutscheincode:

                print telefonnummer + "==" + row[1]
                if telefonnummer == row[1]:
                    output = "true"
                    break
    #                if kreditkartennummer==row[2] and row[2]!="" and row[2]!=" ":
    #                    output="true"
    #                    break

    # print(rabattcode+"!="" and "+gutscheinwert_abrufen(rabattcode)+"==0 and "+rabattcode+"!=")
    return output


@csrf_exempt
def paypal_test(request):
    if request.is_ajax() and request.POST:
        checksum_code = request_paymill_paypal_code("1300", "EUR", "https://www.darlinglace.com/paypal_verficiation/",
                                                    "https://www.darlinglace.com/checkout/")
        return HttpResponse(json.dumps(checksum_code), content_type='application/json')


def get_available_amount_panty(colorcode, slipgroesse, c):
    available = 0
    c.execute("""select * from stylecode where type=%s and color=%s and size=%s""",
              ("panties", colorcode, slipgroesse,))
    for row_2 in c:
        available = row_2[4] - row_2[5]

    return available


def get_available_amount_lingerie(stylecode, colorcode, bhgroesse, c):
    available = 0
    c.execute("""select * from stylecode where type=%s and stylecode=%s and color=%s and size=%s""",
              ("BH", stylecode, colorcode, bhgroesse,))
    for row_2 in c:
        available = row_2[4] - row_2[5]

    return available


def test_whether_quantities_are_available_for_order(session_id, c, conn):
    done = "yes"
    schleife_beenden = "no"
    feedback = "ok"

    liste_bh = []
    liste_slip = []

    angepasst = ""

    bh_menge = 0
    slip_menge = 0
    c.execute("""select * from cart_details where gutscheincode=%s and bestellt=%s""", (session_id, "nein",))
    sessionid_table_detail = c.fetchall()
    for row in sessionid_table_detail:
        i = 0
        existiert = "nein"
        while i <= len(liste_bh) - 1:
            if liste_bh[i][0] == row[4] and liste_bh[i][1] == row[7] and liste_bh[i][2] == row[2] and liste_bh[i][3] == \
                    row[9]:
                liste_bh[i][4] = liste_bh[i][4] + row[1]
                existiert = "ja"
            i = i + 1
        if existiert == "nein":
            liste_bh.append([row[4], row[7], row[2], row[9], row[1]])

        i = 0
        existiert = "nein"
        while i <= len(liste_slip) - 1:
            if liste_slip[i][0] == row[4] and liste_slip[i][1] == row[3]:
                liste_slip[i][2] = liste_slip[i][2] + row[1]
                existiert = "ja"
            i = i + 1
        if existiert == "nein":
            liste_slip.append([row[4], row[3], row[1]])

    print liste_bh
    print liste_slip

    while schleife_beenden == "no":
        c.execute("""select * from cart_details where gutscheincode=%s and bestellt=%s""", (session_id, "nein",))
        sessionid_table = c.fetchall()
        feedback = "ok"
        done = "yes"
        print "test_whether_quantities_are_available_for_order"
        for row in sessionid_table:
            print row[9]

            if row[9] == "panties":

                i = 0
                while i <= len(liste_slip) - 1:
                    if liste_slip[i][0] == row[4] and liste_slip[i][1] == row[3]:
                        slip_menge = liste_slip[i][2]
                        slip_index = i
                    i = i + 1

                print "max_menge_1"
                print bh_menge
                print slip_menge
                max_menge_1 = -1
                max_menge_2 = -1
                c.execute("""select * from stylecode where color=%s""", (row[4],))
                stylecode = c.fetchall()
                for row_2 in stylecode:

                    print row_2[0] + "==panties"
                    if row_2[0] == "panties":
                        print row_2[3] + "==" + row[3]
                        if row_2[3] == row[3]:
                            print str(row_2[4]) + "<" + str(slip_menge)
                            if row_2[4] - row_2[5] < slip_menge:
                                max_menge_2 = row_2[4] - row_2[5]
                                print max_menge_2
                print "max_menge_2-slip_menge+row[1]"
                print str(max_menge_2) + "-" + str(slip_menge) + "+" + str(row[1])

                if max_menge_2 != -1:
                    neue_menge_panties = max(max_menge_2 - slip_menge + row[1], 0)
                else:
                    neue_menge_panties = -1

                print neue_menge_panties

                if neue_menge_panties != -1:
                    neue_menge = neue_menge_panties
                else:
                    neue_menge = -1

                print "neue_menge"
                print neue_menge
                if neue_menge != -1:
                    if neue_menge != 0:
                        print "liste_bh[bh_index][4]"
                        liste_slip[slip_index][2] = liste_slip[slip_index][2] - (row[1] - neue_menge)
                        c.execute(
                            """update cart_details set anzahl=%s where color=%s and productgroup=%s and slipgroesse=%s and bestellt=%s""",
                            (neue_menge, row[4], "panties", row[3], "nein",))
                        conn.commit()
                        done = "no"
                        feedback = "not ok"
                        angepasst = "yes"
                    else:
                        print "liste_slip[slip_index][2]"
                        liste_slip[slip_index][2] = liste_slip[slip_index][2] - (row[1] - neue_menge)
                        print liste_slip[slip_index][2]
                        c.execute(
                            """delete from cart_details where color=%s and productgroup=%s and slipgroesse=%s and bestellt=%s""",
                            (row[4], "panties", row[3], "nein",))
                        conn.commit()
                        done = "no"
                        feedback = "not ok"
                        angepasst = "yes"





            else:

                if row[9] == "lingerie":

                    i = 0
                    while i <= len(liste_bh) - 1:
                        if liste_bh[i][0] == row[4] and liste_bh[i][1] == row[7] and liste_bh[i][2] == row[2] and \
                                liste_bh[i][3] == row[9]:
                            bh_menge = liste_bh[i][4]
                            bh_index = i
                        i = i + 1

                    i = 0
                    while i <= len(liste_slip) - 1:
                        if liste_slip[i][0] == row[4] and liste_slip[i][1] == row[3]:
                            slip_menge = liste_slip[i][2]
                            slip_index = i
                        i = i + 1

                    print "max_menge_1"
                    print bh_menge
                    print slip_menge
                    max_menge_1 = -1
                    max_menge_2 = -1
                    c.execute("""select * from stylecode where color=%s""", (row[4],))
                    stylecode = c.fetchall()
                    for row_2 in stylecode:
                        print row_2[0] + "==BH"
                        if row_2[0] == "BH":
                            print row_2[3] + "==" + row[2]
                            if row_2[3] == row[2] and row_2[1] == row[7]:
                                print str(row_2[4] - row_2[5]) + "<" + str(bh_menge)
                                if row_2[4] - row_2[5] < bh_menge:
                                    print row_2[4] - row_2[5]
                                    max_menge_1 = row_2[4]
                        print row_2[0] + "==panties"
                        if row_2[0] == "panties":
                            print row_2[3] + "==" + row[3]
                            if row_2[3] == row[3]:
                                print str(row_2[4]) + "<" + str(slip_menge)
                                if row_2[4] - row_2[5] < slip_menge:
                                    max_menge_2 = row_2[4] - row_2[5]
                                    print max_menge_2
                    print "max_menge_1-bh_menge+row[1]"
                    print str(max_menge_1) + "-" + str(bh_menge) + "+" + str(row[1])
                    if max_menge_1 != -1:
                        neue_menge_bh = max(max_menge_1 - bh_menge + row[1], 0)
                    else:
                        neue_menge_bh = -1

                    print "max(max_menge_2-slip_menge+row[1],0)"
                    print str(max_menge_2) + "-" + str(slip_menge) + "+" + str(row[1])
                    if max_menge_2 != -1:
                        neue_menge_panties = max(max_menge_2 - slip_menge + row[1], 0)
                    else:
                        neue_menge_panties = -1

                    print neue_menge_bh
                    print neue_menge_panties

                    if neue_menge_bh != -1 and neue_menge_panties != -1:
                        neue_menge = min(neue_menge_bh, neue_menge_panties)
                    else:
                        if neue_menge_bh != -1 and neue_menge_panties == -1:
                            neue_menge = neue_menge_bh
                        else:
                            if neue_menge_bh == -1 and neue_menge_panties != -1:
                                neue_menge = neue_menge_panties
                            else:
                                neue_menge = -1

                    print "neue_menge"
                    print neue_menge
                    if neue_menge != -1:
                        if neue_menge != 0:
                            print "liste_bh[bh_index][4]"
                            print liste_bh[bh_index][4]
                            liste_bh[bh_index][4] = liste_bh[bh_index][4] - (row[1] - neue_menge)
                            liste_slip[slip_index][2] = liste_slip[slip_index][2] - (row[1] - neue_menge)
                            print liste_bh[bh_index][4]
                            c.execute(
                                """update cart_details set anzahl=%s where stylecode=%s and color=%s and productgroup=%s and bhgroesse=%s and slipgroesse=%s and bestellt=%s""",
                                (neue_menge, row[7], row[4], "lingerie", row[2], row[3], "nein",))
                            conn.commit()
                            done = "no"
                            feedback = "not ok"
                            angepasst = "yes"
                        else:
                            print "liste_slip[slip_index][2]"
                            liste_bh[bh_index][4] = liste_bh[bh_index][4] - (row[1] - neue_menge)
                            liste_slip[slip_index][2] = liste_slip[slip_index][2] - (row[1] - neue_menge)
                            print liste_slip[slip_index][2]
                            c.execute(
                                """delete from cart_details where stylecode=%s and color=%s and productgroup=%s and bhgroesse=%s and slipgroesse=%s and bestellt=%s""",
                                (row[7], row[4], "lingerie", row[2], row[3], "nein",))
                            conn.commit()
                            done = "no"
                            feedback = "not ok"
                            angepasst = "yes"

        if done == "yes":
            schleife_beenden = "yes"

    if angepasst == "yes":
        return "update warenkorb"
    else:
        return feedback


@csrf_exempt
def bestellen_pre_test(request):
    if request.is_ajax() and request.POST:
        strasse_rechnung = request.POST.get('strasse_rechnung')
        hausnummer_rechnung = request.POST.get('hausnummer_rechnung')
        stadt_rechnung = request.POST.get('stadt_rechnung')
        plz_rechnung = request.POST.get('plz_rechnung')
        land_rechnung = request.POST.get('land_rechnung')
        anrede_rechnung = request.POST.get('anrede_rechnung')
        vorname_rechnung = request.POST.get('vorname_rechnung')
        nachname_rechnung = request.POST.get('nachname_rechnung')
        telefonnummer_rechnung = request.POST.get('telefonnummer_rechnung')
        unternehmensdetails_rechnung = request.POST.get('unternehmensdetails_rechnung')

        strasse_lieferadresse = request.POST.get('strasse_lieferadresse')
        hausnummer_lieferadresse = request.POST.get('hausnummer_lieferadresse')
        stadt_lieferadresse = request.POST.get('stadt_lieferadresse')
        plz_lieferadresse = request.POST.get('plz_lieferadresse')
        land_lieferadresse = request.POST.get('land_lieferadresse')
        anrede_lieferadresse = request.POST.get('anrede_lieferadresse')
        vorname_lieferadresse = request.POST.get('vorname_lieferadresse')
        nachname_lieferadresse = request.POST.get('nachname_lieferadresse')
        telefonnummer_lieferadresse = request.POST.get('telefonnummer_lieferadresse')
        unternehmensdetails_lieferadresse = request.POST.get('unternehmensdetails_lieferadresse')

        zahlungsoption = request.POST.get('zahlungsoption')
        preis = request.POST.get('preis')
        lieferkosten = request.POST.get('lieferkosten')
        rabatt = request.POST.get('rabatt')
        rabattcode = request.POST.get('rabattcode')
        warenkorb_gerichte = request.POST.get('warenkorb_gerichte')
        warenkorb_anzahl = request.POST.get('warenkorb_anzahl')
        warenkorb_groesse = request.POST.get('warenkorb_groesse')

        selected_zahlungsoption = request.POST.get('selected_zahlungsoption')
        selected_credit_card = request.POST.get('selected_credit_card')
        shopping_type = request.POST.get('shopping_type')

        braforfreecount = request.POST.get('braforfreecount')

        braforfreevalue = request.POST.get('braforfreevalue')
        storecredit_to_be_used = request.POST.get('storecredit_to_be_used')

        geburtsdatum_tag = request.POST.get('geburtsdatum_tag')

        geburtsdatum_monat = request.POST.get('geburtsdatum_monat')
        geburtsdatum_jahr = request.POST.get('geburtsdatum_jahr')

        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))

        Monat = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober",
                 "November", "Dezember"]
        date = str(now.day) + ". " + Monat[(now.month) - 1] + " " + str(now.year)
        date_short = str(now.day) + ". " + Monat[(now.month) - 1] + " " + str(now.year)

        gerichte = warenkorb_gerichte.split(",")
        groesse = warenkorb_groesse.split(",")
        anzahl = warenkorb_anzahl.split(",")
        gesamtanzahl = 0

        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')

        c = conn.cursor(buffered=True)

        x = str(request.session.session_key)

        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            userdaten = c.fetchall()
            for row in userdaten:
                user = row[11]
                quiz = row[26]
                email = row[0]

                modelAB = row[47]
                sub_picture = row[48]

                storecredit_existing = get_existing_store_credit(c, row[11])
                bra_for_free_existing = get_bra_for_free_in_VIP_model(c, row[11])

                credit = row[10]
                gutscheincode = row[11]
                billing_amount = float(preis) + float(lieferkosten)

                if credit > billing_amount:
                    credit_used = billing_amount
                else:
                    credit_used = credit

                rabattcode_geworben = ""

                if row[10] > 0:

                    c.execute("""select * from gutscheine_werben where userid=%s """, (user,))
                    gutscheincode_data = c.fetchall()
                    gutscheincode_werbender = ""
                    credit_ = 0
                    for row_2 in gutscheincode_data:
                        credit_ = credit_ + row_2[1]
                        gutscheincode_werbender = row_2[4]
                    print credit_
                    print gutscheincode_werbender
                    if credit_ == 15:
                        rabattcode_geworben = gutscheincode_werbender

                namebewerter = row[2][:1] + ". " + row[3]
                if check_haushalt_wurde_von_geworben(rabattcode_geworben, row[11],
                                                     strasse_rechnung + " " + hausnummer_rechnung, plz_rechnung,
                                                     telefonnummer_rechnung,
                                                     kreditkartennummer(row[11], selected_credit_card, c), c, conn,
                                                     user) == "false":
                    feedback_warenkorb = test_whether_quantities_are_available_for_order(user, c, conn)
                    print "feedback_warenkorb"
                    print feedback_warenkorb
                    if feedback_warenkorb != "ok":
                        status_ = "not enough quantities"

                        define_warenkorb_object(user, modelAB, sub_picture, c, conn)
                        define_rebates(user, "", "", "", "", c, conn, define_standard_lieferadresse(gutscheincode, c),
                                       "no", "no", "no")
                    else:
                        status_ = "ok"
                        c.execute("""select * from cart_details where gutscheincode=%s and bestellt=%s""",
                                  (user, "nein"))
                        index = 0
                        status_ = "not ok"
                        for row_2 in c:
                            index = index + 1
                            i = 0
                            status_ = ""

                            while i <= len(gerichte) - 1:
                                if str(row_2[0]) == str(gerichte[i]) and str(row_2[2]) == str(groesse[i]):
                                    if str(row_2[1]) == str(anzahl[i]):
                                        gesamtanzahl = gesamtanzahl + int(anzahl[i])
                                        status_ = "ok"

                                i = i + 1
                            if status_ == "not ok" or status_ == "":
                                status_ = "not ok"
                                define_warenkorb_object(user, modelAB, sub_picture, c, conn)
                                define_rebates(user, "", "", "", "", c, conn,
                                               define_standard_lieferadresse(gutscheincode, c), "no", "no", "no")
                                break

                    if status_ == "ok":
                        bestellnummer = id_generator("bestellnummer", c, conn)

                        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
                        if x_forwarded_for:
                            ip_adresse = x_forwarded_for.split(',')[0]
                        else:
                            ip_adresse = request.META.get('REMOTE_ADDR')

                        if selected_zahlungsoption == "0" or selected_zahlungsoption == "3":

                            # if row[22]!="VIP" and shopping_type=="VIP":

                            price_paymill = int(float((float(preis) + float(lieferkosten) - float(rabatt) - float(
                                braforfreevalue) - float(storecredit_to_be_used) - float(credit_used))) * 100)

                            print "paymillforpresident"
                            if price_paymill > 0:
                                transaction_id = credit_card_add_new_transaction(
                                    kreditkarte_clientid(row[11], selected_credit_card, c), price_paymill, "EUR",
                                    "Bestellung mit Bestellnummer: " + bestellnummer, row[50])
                                print transaction_id
                                bezahlt = ""

                                while bezahlt == "":
                                    print "bezahlt"
                                    print bezahlt
                                    bezahlt = "true"
                                    #                                feedback_from_transaction=check_transaction(kreditkarte_clientid(row[11],selected_credit_card,c),price_paymill,"EUR","Bestellung mit Bestellnummer: "+bestellnummer,row[50])
                                    #                                print("bezahlt2")
                                    try:
                                        feedback_from_transaction = check_transaction(transaction_id)
                                        feedback_from_transaction = "true"
                                    except:
                                        feedback_from_transaction = "true"

                                    if feedback_from_transaction == "":
                                        timer.sleep(2)
                                        feedback_from_transaction = check_transaction(transaction_id)
                                        if feedback_from_transaction == "":
                                            feedback_from_transaction = "true"

                                    if feedback_from_transaction == "true":
                                        bezahlt = "true"
                                        if row[56] == "" and shopping_type == "VIP":
                                            subscription_id = kreditkarte_clientid(row[11], selected_credit_card, c)
                                        else:
                                            subscription_id = ""

                                        c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s)""" % (
                                        "order_confirmation_emails"), (
                                                  bestellnummer, get_userdata(user, c, 11), get_userdata(user, c, 0),
                                                  "Deine Bestellung bei Darling Lace", "nein", "no",))

                                        c.execute(
                                            """insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % (
                                            "pending_payments"), (
                                            user, "true", bestellnummer, strasse_rechnung, hausnummer_rechnung,
                                            stadt_rechnung, plz_rechnung, land_rechnung, anrede_rechnung,
                                            vorname_rechnung, nachname_rechnung, telefonnummer_rechnung,
                                            unternehmensdetails_rechnung, strasse_lieferadresse,
                                            hausnummer_lieferadresse, stadt_lieferadresse, plz_lieferadresse,
                                            land_lieferadresse, anrede_lieferadresse, vorname_lieferadresse,
                                            nachname_lieferadresse, telefonnummer_lieferadresse,
                                            unternehmensdetails_lieferadresse, zahlungsoption, preis, lieferkosten,
                                            rabatt, rabattcode, warenkorb_gerichte, warenkorb_anzahl, warenkorb_groesse,
                                            selected_zahlungsoption, shopping_type, braforfreecount, braforfreevalue,
                                            storecredit_to_be_used, transaction_id.id, selected_credit_card,
                                            subscription_id, ip_adresse, geburtsdatum_tag, geburtsdatum_monat,
                                            geburtsdatum_jahr,))
                                        conn.commit()

                                        bestellen(user, c, conn, bestellnummer)

                                    if feedback_from_transaction == "false":
                                        bezahlt = "false"
                                        c.execute(
                                            """insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % (
                                            "pending_payments"), (
                                            user, "false", bestellnummer, strasse_rechnung, hausnummer_rechnung,
                                            stadt_rechnung, plz_rechnung, land_rechnung, anrede_rechnung,
                                            vorname_rechnung, nachname_rechnung, telefonnummer_rechnung,
                                            unternehmensdetails_rechnung, strasse_lieferadresse,
                                            hausnummer_lieferadresse, stadt_lieferadresse, plz_lieferadresse,
                                            land_lieferadresse, anrede_lieferadresse, vorname_lieferadresse,
                                            nachname_lieferadresse, telefonnummer_lieferadresse,
                                            unternehmensdetails_lieferadresse, zahlungsoption, preis, lieferkosten,
                                            rabatt, rabattcode, warenkorb_gerichte, warenkorb_anzahl, warenkorb_groesse,
                                            selected_zahlungsoption, shopping_type, braforfreecount, braforfreevalue,
                                            storecredit_to_be_used, transaction_id.id, selected_credit_card, "",
                                            ip_adresse, geburtsdatum_tag, geburtsdatum_monat, geburtsdatum_jahr,))
                                        conn.commit()



                            else:
                                bezahlt = "true"
                                if row[56] == "" and shopping_type == "VIP":
                                    subscription_id = kreditkarte_clientid(row[11], selected_credit_card, c)
                                else:
                                    subscription_id = ""

                                c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s)""" % (
                                "order_confirmation_emails"), (
                                          bestellnummer, get_userdata(user, c, 11), get_userdata(user, c, 0),
                                          "Deine Bestellung bei Darling Lace", "nein", "no",))

                                c.execute(
                                    """insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % (
                                    "pending_payments"), (
                                    user, "true", bestellnummer, strasse_rechnung, hausnummer_rechnung, stadt_rechnung,
                                    plz_rechnung, land_rechnung, anrede_rechnung, vorname_rechnung, nachname_rechnung,
                                    telefonnummer_rechnung, unternehmensdetails_rechnung, strasse_lieferadresse,
                                    hausnummer_lieferadresse, stadt_lieferadresse, plz_lieferadresse,
                                    land_lieferadresse, anrede_lieferadresse, vorname_lieferadresse,
                                    nachname_lieferadresse, telefonnummer_lieferadresse,
                                    unternehmensdetails_lieferadresse, zahlungsoption, preis, lieferkosten, rabatt,
                                    rabattcode, warenkorb_gerichte, warenkorb_anzahl, warenkorb_groesse,
                                    selected_zahlungsoption, shopping_type, braforfreecount, braforfreevalue,
                                    storecredit_to_be_used, "", selected_credit_card, subscription_id, ip_adresse,
                                    geburtsdatum_tag, geburtsdatum_monat, geburtsdatum_jahr,))
                                conn.commit()

                                bestellen(user, c, conn, bestellnummer)

                            if bezahlt == "true":
                                conn.close()
                                return HttpResponse(json.dumps(str(bestellnummer)), content_type='application/json')

                            else:
                                conn.close()
                                return HttpResponse(json.dumps(bezahlt), content_type='application/json')

                        if selected_zahlungsoption == "1":
                            price_paymill = int(float((float(preis) + float(lieferkosten) - float(rabatt) - float(
                                braforfreevalue) - float(storecredit_to_be_used) - float(credit_used))) * 100)

                            if price_paymill > 0:

                                checksum_code = request_paymill_paypal_code(price_paymill, "EUR",
                                                                            "https://www.darlinglace.com/paypal_verficiation/",
                                                                            "https://www.darlinglace.com/checkout/",
                                                                            "Bestellung mit Bestellnummer: " + bestellnummer)

                                c.execute(
                                    """insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % (
                                    "pending_payments"), (
                                    user, "false", bestellnummer, strasse_rechnung, hausnummer_rechnung, stadt_rechnung,
                                    plz_rechnung, land_rechnung, anrede_rechnung, vorname_rechnung, nachname_rechnung,
                                    telefonnummer_rechnung, unternehmensdetails_rechnung, strasse_lieferadresse,
                                    hausnummer_lieferadresse, stadt_lieferadresse, plz_lieferadresse,
                                    land_lieferadresse, anrede_lieferadresse, vorname_lieferadresse,
                                    nachname_lieferadresse, telefonnummer_lieferadresse,
                                    unternehmensdetails_lieferadresse, zahlungsoption, preis, lieferkosten, rabatt,
                                    rabattcode, warenkorb_gerichte, warenkorb_anzahl, warenkorb_groesse,
                                    selected_zahlungsoption, shopping_type, braforfreecount, braforfreevalue,
                                    storecredit_to_be_used, checksum_code.id, "", "paypal", ip_adresse,
                                    geburtsdatum_tag, geburtsdatum_monat, geburtsdatum_jahr,))
                                conn.commit()
                                conn.close()

                                return HttpResponse(json.dumps(checksum_code.id), content_type='application/json')
                            else:
                                c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s)""" % (
                                "order_confirmation_emails"), (
                                          bestellnummer, get_userdata(user, c, 11), get_userdata(user, c, 0),
                                          "Deine Bestellung bei Darling Lace", "nein", "no",))

                                c.execute(
                                    """insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % (
                                    "pending_payments"), (
                                    user, "true", bestellnummer, strasse_rechnung, hausnummer_rechnung, stadt_rechnung,
                                    plz_rechnung, land_rechnung, anrede_rechnung, vorname_rechnung, nachname_rechnung,
                                    telefonnummer_rechnung, unternehmensdetails_rechnung, strasse_lieferadresse,
                                    hausnummer_lieferadresse, stadt_lieferadresse, plz_lieferadresse,
                                    land_lieferadresse, anrede_lieferadresse, vorname_lieferadresse,
                                    nachname_lieferadresse, telefonnummer_lieferadresse,
                                    unternehmensdetails_lieferadresse, zahlungsoption, preis, lieferkosten, rabatt,
                                    rabattcode, warenkorb_gerichte, warenkorb_anzahl, warenkorb_groesse,
                                    selected_zahlungsoption, shopping_type, braforfreecount, braforfreevalue,
                                    storecredit_to_be_used, "", "", "paypal", ip_adresse, geburtsdatum_tag,
                                    geburtsdatum_monat, geburtsdatum_jahr,))
                                conn.commit()
                                bestellen(user, c, conn, bestellnummer)
                                conn.close()
                                return HttpResponse(json.dumps(str(bestellnummer)), content_type='application/json')

                        if selected_zahlungsoption == "2":
                            transaktionsnummer = id_generator("transaktionsnummersofortueberweisung", c, conn)
                            price_paymill = int(float((float(preis) + float(lieferkosten) - float(rabatt) - float(
                                braforfreevalue) - float(storecredit_to_be_used) - float(credit_used))) * 100)

                            if price_paymill > 0:
                                c.execute(
                                    """insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % (
                                    "pending_payments"), (
                                    user, "false", bestellnummer, strasse_rechnung, hausnummer_rechnung, stadt_rechnung,
                                    plz_rechnung, land_rechnung, anrede_rechnung, vorname_rechnung, nachname_rechnung,
                                    telefonnummer_rechnung, unternehmensdetails_rechnung, strasse_lieferadresse,
                                    hausnummer_lieferadresse, stadt_lieferadresse, plz_lieferadresse,
                                    land_lieferadresse, anrede_lieferadresse, vorname_lieferadresse,
                                    nachname_lieferadresse, telefonnummer_lieferadresse,
                                    unternehmensdetails_lieferadresse, zahlungsoption, preis, lieferkosten, rabatt,
                                    rabattcode, warenkorb_gerichte, warenkorb_anzahl, warenkorb_groesse,
                                    selected_zahlungsoption, shopping_type, braforfreecount, braforfreevalue,
                                    storecredit_to_be_used, transaktionsnummer, "", "sofort", ip_adresse,
                                    geburtsdatum_tag, geburtsdatum_monat, geburtsdatum_jahr,))
                                conn.commit()

                                sofortueberweisung = []

                                class Sofortueberweisung(object):
                                    def __init__(self, name, value):
                                        self.name = name
                                        self.value = value

                                sofortueberweisung.append(Sofortueberweisung("user_id", "155319"))
                                sofortueberweisung.append(Sofortueberweisung("project_id", 376786))
                                sofortueberweisung.append(
                                    Sofortueberweisung("reason_1", "Bestellnummer: " + bestellnummer, ))

                                sofortueberweisung.append(Sofortueberweisung("reason_2", transaktionsnummer, ))
                                sofortueberweisung.append(Sofortueberweisung("amount",
                                                                             float(preis) + float(lieferkosten) - float(
                                                                                 rabatt) - float(
                                                                                 braforfreevalue) - float(
                                                                                 storecredit_to_be_used) - float(
                                                                                 credit_used)))

                                json_string = json.dumps(
                                    [Sofortueberweisung.__dict__ for Sofortueberweisung in sofortueberweisung])

                                conn.close()
                                return HttpResponse(json_string, content_type='application/json')
                            else:
                                c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s)""" % (
                                "order_confirmation_emails"), (
                                          bestellnummer, get_userdata(user, c, 11), get_userdata(user, c, 0),
                                          "Deine Bestellung bei Darling Lace", "nein", "no",))
                                c.execute(
                                    """insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % (
                                    "pending_payments"), (
                                    user, "true", bestellnummer, strasse_rechnung, hausnummer_rechnung, stadt_rechnung,
                                    plz_rechnung, land_rechnung, anrede_rechnung, vorname_rechnung, nachname_rechnung,
                                    telefonnummer_rechnung, unternehmensdetails_rechnung, strasse_lieferadresse,
                                    hausnummer_lieferadresse, stadt_lieferadresse, plz_lieferadresse,
                                    land_lieferadresse, anrede_lieferadresse, vorname_lieferadresse,
                                    nachname_lieferadresse, telefonnummer_lieferadresse,
                                    unternehmensdetails_lieferadresse, zahlungsoption, preis, lieferkosten, rabatt,
                                    rabattcode, warenkorb_gerichte, warenkorb_anzahl, warenkorb_groesse,
                                    selected_zahlungsoption, shopping_type, braforfreecount, braforfreevalue,
                                    storecredit_to_be_used, transaktionsnummer, "", "sofort", ip_adresse,
                                    geburtsdatum_tag, geburtsdatum_monat, geburtsdatum_jahr,))
                                conn.commit()
                                bestellen(user, c, conn, bestellnummer)
                                conn.close()
                                return HttpResponse(json.dumps(str(bestellnummer)), content_type='application/json')

                        if selected_zahlungsoption == "4":
                            price_paymill = int(float((float(preis) + float(lieferkosten) - float(rabatt) - float(
                                braforfreevalue) - float(storecredit_to_be_used) - float(credit_used))) * 100)
                            if price_paymill > 0:
                                klarna_feedback = generate_order_klarna(user, c, row[0], telefonnummer_rechnung,
                                                                        anrede_rechnung, vorname_rechnung,
                                                                        nachname_rechnung, strasse_rechnung,
                                                                        hausnummer_rechnung, plz_rechnung,
                                                                        stadt_rechnung, land_rechnung,
                                                                        unternehmensdetails_rechnung, ip_adresse,
                                                                        float(rabatt) - float(braforfreevalue) - float(
                                                                            storecredit_to_be_used) - float(
                                                                            credit_used), lieferkosten,
                                                                        geburtsdatum_tag, geburtsdatum_monat,
                                                                        geburtsdatum_jahr)
                                if klarna_feedback[1] == 2:
                                    klarna_order = klarna_feedback[0]

                                    bezahlt = "true"

                                    if bezahlt == "true":
                                        c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s)""" % (
                                        "order_confirmation_emails"), (
                                                  bestellnummer, get_userdata(user, c, 11), get_userdata(user, c, 0),
                                                  "Deine Bestellung bei Darling Lace", "nein", "no",))
                                        c.execute(
                                            """insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % (
                                            "pending_payments"), (
                                            user, "true", bestellnummer, strasse_rechnung, hausnummer_rechnung,
                                            stadt_rechnung, plz_rechnung, land_rechnung, anrede_rechnung,
                                            vorname_rechnung, nachname_rechnung, telefonnummer_rechnung,
                                            unternehmensdetails_rechnung, strasse_lieferadresse,
                                            hausnummer_lieferadresse, stadt_lieferadresse, plz_lieferadresse,
                                            land_lieferadresse, anrede_lieferadresse, vorname_lieferadresse,
                                            nachname_lieferadresse, telefonnummer_lieferadresse,
                                            unternehmensdetails_lieferadresse, zahlungsoption, preis, lieferkosten,
                                            rabatt, rabattcode, warenkorb_gerichte, warenkorb_anzahl, warenkorb_groesse,
                                            selected_zahlungsoption, shopping_type, braforfreecount, braforfreevalue,
                                            storecredit_to_be_used, klarna_order, "", "klarna", ip_adresse,
                                            geburtsdatum_tag, geburtsdatum_monat, geburtsdatum_jahr,))
                                        conn.commit()
                                        bestellen(user, c, conn, bestellnummer)
                                    else:
                                        c.execute(
                                            """insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % (
                                            "pending_payments"), (
                                            user, "false", bestellnummer, strasse_rechnung, hausnummer_rechnung,
                                            stadt_rechnung, plz_rechnung, land_rechnung, anrede_rechnung,
                                            vorname_rechnung, nachname_rechnung, telefonnummer_rechnung,
                                            unternehmensdetails_rechnung, strasse_lieferadresse,
                                            hausnummer_lieferadresse, stadt_lieferadresse, plz_lieferadresse,
                                            land_lieferadresse, anrede_lieferadresse, vorname_lieferadresse,
                                            nachname_lieferadresse, telefonnummer_lieferadresse,
                                            unternehmensdetails_lieferadresse, zahlungsoption, preis, lieferkosten,
                                            rabatt, rabattcode, warenkorb_gerichte, warenkorb_anzahl, warenkorb_groesse,
                                            selected_zahlungsoption, shopping_type, braforfreecount, braforfreevalue,
                                            storecredit_to_be_used, klarna_order, "", "klarna", ip_adresse,
                                            geburtsdatum_tag, geburtsdatum_monat, geburtsdatum_jahr,))
                                        conn.commit()

                                else:
                                    if klarna_feedback[1] == 1:
                                        klarna_order = klarna_feedback[0]
                                        c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s)""" % (
                                        "order_confirmation_emails"), (
                                                  bestellnummer, get_userdata(user, c, 11), get_userdata(user, c, 0),
                                                  "Deine Bestellung bei Darling Lace", "nein", "no",))
                                        c.execute(
                                            """insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % (
                                            "pending_payments"), (
                                            user, "true", bestellnummer, strasse_rechnung, hausnummer_rechnung,
                                            stadt_rechnung, plz_rechnung, land_rechnung, anrede_rechnung,
                                            vorname_rechnung, nachname_rechnung, telefonnummer_rechnung,
                                            unternehmensdetails_rechnung, strasse_lieferadresse,
                                            hausnummer_lieferadresse, stadt_lieferadresse, plz_lieferadresse,
                                            land_lieferadresse, anrede_lieferadresse, vorname_lieferadresse,
                                            nachname_lieferadresse, telefonnummer_lieferadresse,
                                            unternehmensdetails_lieferadresse, zahlungsoption, preis, lieferkosten,
                                            rabatt, rabattcode, warenkorb_gerichte, warenkorb_anzahl, warenkorb_groesse,
                                            selected_zahlungsoption, shopping_type, braforfreecount, braforfreevalue,
                                            storecredit_to_be_used, klarna_order, "", "klarna", ip_adresse,
                                            geburtsdatum_tag, geburtsdatum_monat, geburtsdatum_jahr,))
                                        conn.commit()
                                        bestellen(user, c, conn, bestellnummer)
                                        bezahlt = "true"
                                    else:
                                        c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s)""" % (
                                        "order_confirmation_emails"), (
                                                  bestellnummer, get_userdata(user, c, 11), get_userdata(user, c, 0),
                                                  "Deine Bestellung bei Darling Lace", "nein", "no",))
                                        c.execute(
                                            """insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % (
                                            "pending_payments"), (
                                            user, "true", bestellnummer, strasse_rechnung, hausnummer_rechnung,
                                            stadt_rechnung, plz_rechnung, land_rechnung, anrede_rechnung,
                                            vorname_rechnung, nachname_rechnung, telefonnummer_rechnung,
                                            unternehmensdetails_rechnung, strasse_lieferadresse,
                                            hausnummer_lieferadresse, stadt_lieferadresse, plz_lieferadresse,
                                            land_lieferadresse, anrede_lieferadresse, vorname_lieferadresse,
                                            nachname_lieferadresse, telefonnummer_lieferadresse,
                                            unternehmensdetails_lieferadresse, zahlungsoption, preis, lieferkosten,
                                            rabatt, rabattcode, warenkorb_gerichte, warenkorb_anzahl, warenkorb_groesse,
                                            selected_zahlungsoption, shopping_type, braforfreecount, braforfreevalue,
                                            storecredit_to_be_used, "klarna failure", "", "klarna", ip_adresse,
                                            geburtsdatum_tag, geburtsdatum_monat, geburtsdatum_jahr,))
                                        conn.commit()
                                        bestellen(user, c, conn, bestellnummer)
                                        bezahlt = "true"

                            if bezahlt == "true":
                                conn.close()
                                return HttpResponse(json.dumps(str(bestellnummer)), content_type='application/json')
                            else:
                                conn.close()
                                return HttpResponse(json.dumps(bezahlt), content_type='application/json')


                    else:
                        conn.close()

                        return HttpResponse(json.dumps(status_), content_type='application/json')




                else:

                    c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s)""" % ("gutscheine_werben"),
                              (date_short, -credit_used, "betrueger", "", user,))
                    c.execute("""delete from %s where gutscheinwert=%%s and userid=%%s""" % ("gutscheine_werben"),
                              (15, user,))
                    c.execute(
                        """update userdaten set credit=%s, geworben=%s,messageshownreferraldeleted=%s where gutscheincode=%s""",
                        (str(0), "nein", "yes", user,))
                    define_rebates(user, "", "", "", "", c, conn, define_standard_lieferadresse(user, c), "no", "no",
                                   "no")
                    status_ = "kann nicht geworben werden"
                    conn.commit()
                    conn.close()
                    return HttpResponse(json.dumps(status_), content_type='application/json')


def sofortueberweisung_successful(request, offset):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database')

    c = conn.cursor(buffered=True)

    transaktionsnummer = offset[10:18]

    x = str(request.session.session_key)

    status = 0

    c.execute("""select * from pending_payments """)
    for row_6 in c:
        if row_6[36] == transaktionsnummer:
            check_pending_payments(row_6[2], "true", c, conn, get_userid_from_session_id(c, x))

            status = 1
            conn.close()
            return HttpResponseRedirect("/account_page/bestellungen_ansehen/" + row_6[2])

    if status == 0:
        conn.close()
        return HttpResponseRedirect("/checkout/")


def sofortueberweisung_not_successful(request, offset):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database')

    c = conn.cursor(buffered=True)

    transaktionsnummer = offset[10:18]
    x = str(request.session.session_key)
    c.execute("""select * from pending_payments """)
    for row_6 in c:
        if row_6[36] == transaktionsnummer:
            check_pending_payments(row_6[2], "false", c, conn, get_userid_from_session_id(c, x))

    conn.close()
    return HttpResponseRedirect("/checkout/")


def sofortueberweisung_status(request, offset):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database')

    c = conn.cursor(buffered=True)
    print("status sofortueberweisung")
    print(offset)
    status = offset[43:len(offset)]
    bestellnummer = offset[24:32]
    x = str(request.session.session_key)
    user = get_userid_from_session_id(c, x)
    check_pending_payments(bestellnummer, "true", c, conn, user)

    if status == "pending" or "bezahlt":
        check_pending_payments(bestellnummer, "true", c, conn, user)
    else:
        check_pending_payments(bestellnummer, "false", c, conn, user)

    check_pending_payments(bestellnummer, "true", c, conn, user)
    conn.close()
    return HttpResponseRedirect("/account_page/bestellungen_ansehen/" + bestellnummer)


def get_userdata(user, c, index):
    c.execute("""select * from userdaten where gutscheincode=%s """, (user,))
    userdaten = c.fetchall()
    feedback = ""
    for row in userdaten:
        feedback = row[index]
    return feedback


def check_pending_payments(bestellnummer, feedback, c, conn, user):
    print "check_pending_payments"
    if feedback == "true":

        c.execute("""select * from pending_payments """)

        pending_payments = c.fetchall()
        for row_6 in pending_payments:
            if row_6[2] == bestellnummer:
                c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s)""" % ("order_confirmation_emails"), (
                bestellnummer, get_userdata(user, c, 11), get_userdata(user, c, 0), "Deine Bestellung bei Darling Lace",
                "nein", "no",))
                c.execute("""update pending_payments set accepted=%s where bestellnummer=%s""",
                          ("true", bestellnummer,))
                conn.commit()
                print "beestellen"
                bestellen(row_6[0], c, conn, bestellnummer)
    else:
        c.execute("""select * from pending_payments """)

        pending_payments = c.fetchall()
        for row_6 in c:

            if row_6[2] == bestellnummer:
                c.execute("""delete from pending_payments where bestellnummer=%s""", (bestellnummer,))
                conn.commit()


def bestellen(session_id, c, conn, bestellnummer_):
    print "bestellen(session_id,c,conn)"
    c.execute("""select * from pending_payments """)

    pending_payments = c.fetchall()
    for row_6 in pending_payments:
        print row_6[0] + "==" + session_id + "and" + row_6[1] + "==true"
        if row_6[0] == session_id and row_6[1] == "true" and bestellnummer_ == row_6[2]:
            bestellnummer = row_6[2]

            strasse_rechnung = row_6[3]
            hausnummer_rechnung = row_6[4]
            stadt_rechnung = row_6[5]
            plz_rechnung = row_6[6]
            land_rechnung = row_6[7]
            anrede_rechnung = row_6[8]
            vorname_rechnung = row_6[9]
            nachname_rechnung = row_6[10]
            telefonnummer_rechnung = row_6[11]
            unternehmensdetails_rechnung = row_6[12]
            strasse_lieferadresse = row_6[13]
            hausnummer_lieferadresse = row_6[14]
            stadt_lieferadresse = row_6[15]
            plz_lieferadresse = row_6[16]
            land_lieferadresse = row_6[17]
            anrede_lieferadresse = row_6[18]
            vorname_lieferadresse = row_6[19]
            nachname_lieferadresse = row_6[20]
            telefonnummer_lieferadresse = row_6[21]
            unternehmensdetails_lieferadresse = row_6[22]
            zahlungsoption = row_6[23]
            preis = row_6[24]
            lieferkosten = row_6[25]
            rabatt = row_6[26]
            rabattcode = row_6[27]
            warenkorb_gerichte = row_6[28]
            warenkorb_anzahl = row_6[29]
            warenkorb_groesse = row_6[30]
            selected_zahlungsoption = row_6[31]
            shopping_type = row_6[32]
            braforfreecount = row_6[33]
            braforfreevalue = row_6[34]
            storecredit_to_be_used = row_6[35]
            transaction_id = row_6[36]
            selected_credit_card = row_6[37]
            subscription_id = row_6[38]
            ip_adresse = row_6[39]

            geburtsdatum_tag = row_6[40]
            geburtsdatum_monat = row_6[41]
            geburtsdatum_jahr = row_6[42]

            gerichte = warenkorb_gerichte.split(",")
            groesse = warenkorb_groesse.split(",")
            anzahl = warenkorb_anzahl.split(",")
            gesamtanzahl = 0
            gesamtanzahl_sets = 0

            print("ASD")
            c.execute("""select * from userdaten where gutscheincode=%s """, (session_id,))

            userdaten = c.fetchall()

            current_time = datetime.datetime.now(pytz.timezone('Europe/Berlin')).time()
            now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))

            Wochentag = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
            Monat = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober",
                     "November", "Dezember"]
            date = str(now.day) + ". " + Monat[(now.month) - 1] + " " + str(now.year)
            date_short = str(now.day) + ". " + Monat[(now.month) - 1] + " " + str(now.year)
            date_for_VIP_member_since_variable = str(now.year) + "." + str((now.month) - 1) + "." + str(now.day)

            date_ = str(now.year) + str((now.month) - 1) + str(now.day)
            time_ = str(current_time)

            time__ = time_.replace(":", "")
            time__ = time__.replace(".", "")

            time___ = date_ + time__
            for row in userdaten:

                print("ASDasd")
                default_bra_size = row[58]
                default_panty_size = row[59]
                user = row[11]
                quiz = row[26]
                storecredit_existing = get_existing_store_credit(c, row[11])
                bra_for_free_existing = get_bra_for_free_in_VIP_model(c, row[11])
                rabattcode_geworben = ""
                cart_quantity = row[17]
                modelAB = row[47]
                sub_picture = row[48]
                credit_ = 0
                if row[10] > 0:
                    c.execute("""select * from gutscheine_werben where userid=%s """, (user,))
                    gutscheincode_data = c.fetchall()
                    gutscheincode_werbender = ""
                    credit_ = 0
                    for row_2 in gutscheincode_data:
                        credit_ = credit_ + row_2[1]
                        gutscheincode_werbender = row_2[3]
                    if credit_ == 15:
                        rabattcode_geworben = gutscheincode_werbender

                namebewerter = row[2][:1] + ". " + row[3]
                if check_haushalt_wurde_von_geworben(rabattcode_geworben, row[11],
                                                     strasse_rechnung + " " + hausnummer_rechnung, plz_rechnung,
                                                     telefonnummer_rechnung,
                                                     kreditkartennummer(row[11], selected_credit_card, c), c, conn,
                                                     user) == "false":

                    if credit_ == 15 and rabattcode_geworben != "":
                        c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s)""" % ("gutscheine_werben"),
                                  (date_short, 15, bestellnummer, "", rabattcode_geworben,))
                        c.execute("""select * from userdaten where gutscheincode=%s """, (rabattcode_geworben,))
                        userdaten = c.fetchall()
                        credit_werbender = 0
                        for row_3 in userdaten:
                            credit_werbender = row_3[10] + 15
                            c.execute("""update userdaten set credit=%s where gutscheincode=%s""",
                                      (str(credit_werbender), rabattcode_geworben,))
                    c.execute("""select * from cart_details where gutscheincode=%s and bestellt=%s""", (user, "nein"))
                    status_ = "ok"
                    for row_2 in c:
                        i = 0
                        status_ = "ok"

                        while i <= len(gerichte) - 1:

                            if str(row_2[0]) == str(gerichte[i]) and str(row_2[2]) == str(groesse[i]):

                                if str(row_2[1]) == str(anzahl[i]):
                                    if row_2[9] == "lingerie":
                                        gesamtanzahl_sets = gesamtanzahl_sets + int(anzahl[i])
                                    gesamtanzahl = gesamtanzahl + int(anzahl[i])

                            i = i + 1

                    if status_ == "ok":

                        if float(storecredit_existing) < float(storecredit_to_be_used):
                            status_ = "not enough storecredit"
                        if float(bra_for_free_existing) < float(braforfreecount):
                            status_ = "not enough bra for free"

                    if status_ == "ok":

                        count_rows_bestellt_table = c.execute("""select * from bestellt where gutscheincode=%s """,
                                                              (row[11],))
                        c.execute(count_rows_bestellt_table)
                        new_count_rows_bestellt_table = int(c.rowcount) + 1

                        session_id_ = "bestellt_" + time__ + "_" + session_id

                        status = 0
                        credit_used = 0

                        credit = row[10]
                        gutscheincode = row[11]
                        billing_amount = float(preis) + float(lieferkosten)

                        if credit > billing_amount:
                            credit_used = billing_amount
                        else:
                            credit_used = credit

                        remaining_credit = credit - credit_used
                        remaining_storecredit = float(storecredit_existing) - float(storecredit_to_be_used)

                        try:
                            count_rows_bestellt_table = c.execute("""select * from bestellt where bestellnummer=%s """,
                                                                  (bestellnummer,))
                            c.execute(count_rows_bestellt_table)
                            zaehler_bestellt = int(c.rowcount)
                        except:
                            zaehler_bestellt = 0

                        #   c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % ("bestellt_"+row[11]), (session_id_, adresse,stadt,plz,unternehmensdetails,vorname,nachname,telefonnummer,lieferdetails,zahlungsoption,name_kreditkarte(row[11],selected_zahlungsoption,c),kreditkartennummer(row[11],selected_zahlungsoption,c),ablaufdatum(row[11],selected_zahlungsoption,c),pruefziffer(row[11],selected_zahlungsoption,c),preis,lieferkosten,rabatt,rabattcode,date,"3",bestellnummer,str(credit_used),shopping_type,"Bestellt",time__,braforfreecount,braforfreevalue,storecredit_to_be_used,))

                        lieferdatum = select_lieferdatum(4)
                        if zaehler_bestellt == 0:
                            c.execute(
                                """insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % (
                                "bestellt"), (
                                session_id, strasse_rechnung, hausnummer_rechnung, stadt_rechnung, plz_rechnung,
                                land_rechnung, anrede_rechnung, vorname_rechnung, nachname_rechnung,
                                telefonnummer_rechnung, selected_zahlungsoption,
                                name_kreditkarte(row[11], selected_credit_card, c),
                                kreditkartennummer(row[11], selected_credit_card, c),
                                ablaufdatum(row[11], selected_credit_card, c),
                                pruefziffer(row[11], selected_credit_card, c), preis, lieferkosten, rabatt, rabattcode,
                                date, "3", bestellnummer, str(credit_used), shopping_type, "Bestellt",
                                new_count_rows_bestellt_table, braforfreecount, braforfreevalue, storecredit_to_be_used,
                                lieferdatum, "", "", "", "", "", "", "nein", "nein", transaction_id, "nein",
                                unternehmensdetails_rechnung, strasse_lieferadresse, hausnummer_lieferadresse,
                                stadt_lieferadresse, plz_lieferadresse, land_lieferadresse, anrede_lieferadresse,
                                vorname_lieferadresse, nachname_lieferadresse, telefonnummer_lieferadresse,
                                unternehmensdetails_lieferadresse, ip_adresse, row[11], "", "", geburtsdatum_tag,
                                geburtsdatum_monat, geburtsdatum_jahr,))
                        c.execute("""insert into %s values (%%s,%%s,%%s)""" % ("benutztegutscheincodes"),
                                  (bestellnummer, rabattcode, row[11]))

                        if row[23] == "false" and shopping_type == "VIP":
                            if geburtsdatum_tag == "":
                                c.execute(
                                    """update userdaten set cartquantity=%s,genutztergutscheincode=%s, shoppingtype=%s, shoppingtypeentschieden=%s, paymentidforsubscription=%s,neukunde=%s,selectedzahlungsoption=%s,VIPmembersince=%s,warenkorb=%s, bereitsbestellt=%s where gutscheincode=%s""",
                                    (cart_quantity - gesamtanzahl, "", shopping_type, "true", subscription_id, "false",
                                     selected_zahlungsoption, date_for_VIP_member_since_variable, "", "yes",
                                     session_id,))
                            else:
                                c.execute(
                                    """update userdaten set cartquantity=%s,genutztergutscheincode=%s, shoppingtype=%s, shoppingtypeentschieden=%s, paymentidforsubscription=%s,neukunde=%s,selectedzahlungsoption=%s,VIPmembersince=%s,warenkorb=%s, bereitsbestellt=%s,geburtsdatumtag=%s,geburtsdatummonat=%s,geburtsdatumjahr=%s  where gutscheincode=%s""",
                                    (cart_quantity - gesamtanzahl, "", shopping_type, "true", subscription_id, "false",
                                     selected_zahlungsoption, date_for_VIP_member_since_variable, "", "yes",
                                     geburtsdatum_tag, geburtsdatum_monat, geburtsdatum_jahr, session_id,))
                        else:
                            if geburtsdatum_tag == "":
                                c.execute(
                                    """update userdaten set cartquantity=%s,genutztergutscheincode=%s, shoppingtype=%s, neukunde=%s,selectedzahlungsoption=%s,warenkorb=%s, bereitsbestellt=%s where gutscheincode=%s""",
                                    (cart_quantity - gesamtanzahl, "", shopping_type, "false", selected_zahlungsoption,
                                     "", "yes", session_id,))
                            else:
                                c.execute(
                                    """update userdaten set cartquantity=%s,genutztergutscheincode=%s, shoppingtype=%s, neukunde=%s,selectedzahlungsoption=%s,warenkorb=%s, bereitsbestellt=%s,geburtsdatumtag=%s,geburtsdatummonat=%s,geburtsdatumjahr=%s where gutscheincode=%s""",
                                    (cart_quantity - gesamtanzahl, "", shopping_type, "false", selected_zahlungsoption,
                                     "", "yes", geburtsdatum_tag, geburtsdatum_monat, geburtsdatum_jahr, session_id,))

                        purchased_bras = int(gesamtanzahl_sets) - int(braforfreecount)

                        c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % (
                        "VIP_model_store_credit"), (
                                  date_for_VIP_member_since_variable, date_for_VIP_member_since_variable, time__,
                                  -float(storecredit_to_be_used), bestellnummer, "", "", braforfreecount,
                                  purchased_bras, transaction_id, date_.replace(".", ""), row[11]))

                        if credit_used != 0:
                            if rabattcode == "":
                                c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s)""" % ("gutscheine_werben"),
                                          (date_short, -credit_used, bestellnummer, "", row[11],))
                                c.execute("""update userdaten set credit=%s where gutscheincode=%s""",
                                          (remaining_credit, user,))
                            else:
                                if gutscheinwert_abrufen(rabattcode, c, gutscheincode, conn, "nein", user) == 0:
                                    c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s)""" % ("gutscheine_werben"),
                                              (date_short, -credit_used, bestellnummer, "", row[11],))
                                    c.execute("""update userdaten set credit=%s where gutscheincode=%s""",
                                              (str(0), user,))
                                else:
                                    billing_amount = float(preis) + float(lieferkosten) + float(
                                        gutscheinwert_abrufen(rabattcode, c, gutscheincode, conn, "nein", user))

                                    if credit > billing_amount:
                                        credit_used = billing_amount
                                    else:
                                        credit_used = credit

                                    remaining_credit = credit - credit_used

                                    c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s)""" % ("gutscheine_werben"),
                                              (date_short, -credit_used, bestellnummer, "", row[11],))

                                    c.execute("""update userdaten set credit=%s where gutscheincode=%s""",
                                              (remaining_credit, user,))

                        stylecode = ""
                        colorcode = ""

                        c.execute("""select * from cart_details where gutscheincode=%s and bestellt=%s""",
                                  (user, "nein",))

                        sessionid_table = c.fetchall()

                        for row_10 in sessionid_table:
                            print row_10[0]

                            if default_bra_size == "":
                                c.execute("""update userdaten set defaultbrasize=%s where gutscheincode=%s""",
                                          (row_10[2], user,))
                                default_bra_size = row_10[2]
                            if default_panty_size == "":
                                c.execute("""update userdaten set defaultpantysize=%s where gutscheincode=%s""",
                                          (row_10[3], user,))
                                default_panty_size = row_10[3]
                            c.execute("""select * from %s """ % ("stylecode"))
                            stylecode_ = c.fetchall()

                            print "jaaaaaannnnuuuuu"
                            for row_12 in stylecode_:
                                if row_10[9] == "lingerie":
                                    if row_12[1] == row_10[7]:
                                        if (row_10[4] == str(row_12[2])) and (row_10[2] == str(row_12[3])):
                                            bestelltemengebestellt = row_12[5] + row_10[1]
                                            c.execute(
                                                """update %s set bestelltemengebestellt=%%s where size=%%s and color=%%s and stylecode=%%s""" % (
                                                "stylecode"),
                                                (bestelltemengebestellt, row_12[3], row_10[4], row_10[7],))
                                            c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % (
                                            "supply_order_log"), (
                                                      gutscheincode, date, time__, row_10[7], row_10[4], row_10[2],
                                                      row_10[3], row_10[1],))

                                    print row_10[4] + "==" + str(row_12[2]) + "and" + row_10[3] + "==" + str(row_12[3])
                                    if (row_10[4] == str(row_12[2])) and row_10[3] == str(row_12[3]):
                                        bestelltemengebestellt = row_12[5] + row_10[1]

                                        c.execute(
                                            """update %s set bestelltemengebestellt=%%s where size=%%s and color=%%s and type=%%s""" % (
                                            "stylecode"), (bestelltemengebestellt, row_12[3], row_10[4], "panties",))
                                #                                            c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % ("supply_order_log"), (gutscheincode,date,time__,row_10[7],row_10[4],row_10[2],row_10[3],row_10[1],))

                                else:
                                    print row_10[4] + "==" + str(row_12[2]) + "and" + row_10[3] + "==" + str(row_12[3])
                                    if (row_10[4] == str(row_12[2])) and row_10[3] == str(row_12[3]):
                                        bestelltemengebestellt = row_12[5] + row_10[1]

                                        c.execute(
                                            """update %s set bestelltemengebestellt=%%s where size=%%s and color=%%s and type=%%s""" % (
                                            "stylecode"), (bestelltemengebestellt, row_12[3], row_10[4], row_12[0],))
                                        c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % (
                                        "supply_order_log"), (
                                                  gutscheincode, date, time__, row_10[7], row_10[4], row_10[2],
                                                  row_10[3], row_10[1],))

                            if quiz == "yes":
                                if stylecode != row_10[7] or colorcode != row_10[4]:
                                    stylecode = row_10[7]
                                    colorcode = row_10[4]

                        a = get_time_stamp_now()

                        c.execute(
                            """update cart_details set bestellt=%s, bestellnummer=%s where gutscheincode=%s and bestellt=%s""",
                            ("ja", bestellnummer, user, "nein",))
                        c.execute("""delete from %s where bestellnummer=%%s""" % ("pending_payments"), (bestellnummer,))

                        print "yes"
                else:

                    c.execute("""select * from userdaten where gutscheincode=%s """, (user,))

                    userdaten = c.fetchall()

                    for row in userdaten:
                        c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s)""" % ("gutscheine_werben"),
                                  (date_short, -credit_used, bestellnummer, "", row[11],))
                        c.execute("""delete from %s where gutscheinwert=%%s and userid=%%s""" % ("gutscheine_werben"),
                                  (15, row[11],))
                        c.execute(
                            """update userdaten set credit=%s, geworben=%s,messageshownreferraldeleted=%s where gutscheincode=%s""",
                            (str(0), "nein", "yes", user,))
                        status_ = "kann nicht geworben werden"

    conn.commit()


@csrf_exempt
def cart_aufrufen(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database')

    c = conn.cursor(buffered=True)

    x = str(request.session.session_key)
    login = "false"
    status = 0
    modelAB = ""
    sub_picture = ""
    user = ""
    credit = 0
    adressbuch = ""
    email = "not ok"
    VIP = "false"
    gutscheinwert = 0
    gutscheincode = ""

    login_window = request.GET.get('login')
    if login_window == None:
        login_window = ""

    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        for row in c:

            status = 1
            wishlist = row[65]
            bereitsbestellt = row[75]
            bereitsversandt = row[76]
            messageshownwarenkorbleer = row[79]
            warenkorb = row[66]
            definerebates = row[67]
            definerebatesbestellwert = row[68]
            definerebateslieferkosten = row[69]
            definerebatesrabatte = row[70]
            cart_gesamt = row[71]
            stylecodescolorcodesforfb = row[72]
            storecredit = get_existing_store_credit(c, row[11])
            bra_for_free = get_bra_for_free_in_VIP_model(c, row[11])
            quiz = row[26]
            selected_zahlungsoption = row[55]
            credit = row[10]
            email = row[0]
            user = row[11]
            vorname = row[2]
            nachname = row[3]
            letzteshoppingsicht = row[80]

            letztefilter = row[81]

            stadt = row[6]
            plz = row[4]
            modelAB = row[47]
            sub_picture = row[48]
            wishlist_quantity = row[16]
            cart_quantity = row[17]
            if (row[0] != "" and row[12] != "") or (row[0] != "" and row[1] != ""):
                login = "true"

            if row[21] != "":
                gutscheincode = row[21]
                gutscheinwert = gutscheinwert_abrufen(gutscheincode, c, user, conn, "nein", user)

            shopping_type = row[22]
            if row[22] == "VIP" and row[23] == "true":
                VIP = "true"

            if row[0] != "":
                email = "ok"
            if (row[0] != "" and row[12] != "") or (row[0] != "" and row[1] != ""):
                login = "true"

    if user != "":

        if check_whether_warenkorb_ist_leer(user, c) == 0:
            messageshownwarenkorbleer = "yes"
        else:
            messageshownwarenkorbleer = "no"

        get_content_for_facebookpixel_from_order_ = get_content_for_facebookpixel_from_order(x, "", c, user)
        get_stylecode_colorcode_from_order_ = get_stylecode_colorcode_from_order(x, "", c, user)

        if (len(warenkorb) > 2 and status == 1) or messageshownwarenkorbleer == "yes" or login_window == "login":
            t = get_template('cart.html')
            description_header = (
            "BHs und BH Sets für jede Größe und Brustform. Wir bieten lingerie in einer großen Auswahl an Farben an. Hochwertige Unterwäsche für Frauen günstig kaufen. BHs in vielen Designs, basic, sexy und bequeme BHs. Auf Rechnung kaufen mit 30 Tage Rückgaberecht. Kostenloser Versand.").encode(
                'utf8')

            html = t.render({'login_window': login_window, 'description_header': description_header,
                             'user_id_google_analytics': get_google_analytics_user_id(login, user),
                             'letztefilter': letztefilter, 'letzteshoppingsicht': letzteshoppingsicht,
                             'messageshownwarenkorbleer': messageshownwarenkorbleer, 'url': get_link_positioining(""),
                             'links': get_links(quiz), 'selected_zahlungsoption': selected_zahlungsoption,
                             'num_items': cart_gesamt, 'value_': definerebatesbestellwert,
                             'content_id_list': get_stylecode_colorcode_from_order_,
                             'contents_list': get_content_for_facebookpixel_from_order_, 'email': email,
                             'bereitsbestellt': bereitsbestellt, 'bereitsversandt': bereitsversandt,
                             'fb_link': 'https://www.darlinglace.com',
                             'fb_title': ("Liebst du Lingerie? Erhalte Dein BH Set ab 29,95 EUR!").encode('utf8'),
                             'fb_description': (
                             "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                                 'utf8'), 'fb_description': (
                "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                    'utf8'), 'fb_image': 'https://www.darlinglace.com/static/overall_picture_bra.jpg',
                             'vorname': vorname, 'nachname': nachname, 'stadt': stadt, 'plz': plz, 'wishlist': wishlist,
                             'warenkorb': warenkorb, 'favicon': get_favicon(), 'path': request.path,
                             'brand_name': 'Darling Lace', 'title': "Warenkorb | Darling Lace",
                             'shopping_type': shopping_type, 'rebates': definerebates, 'storecredit': storecredit,
                             'bra_for_free': bra_for_free, 'VIP': VIP, 'gutscheinwert': gutscheinwert,
                             'gutscheincode': gutscheincode, 'warenkorb': warenkorb, 'credit': credit, 'login': login})
            conn.close()
            return HttpResponse(html)
        else:
            #            if userid_from_path!="":
            #                path=request.path
            #                html=call_login_page(path,c,x)
            #                conn.close()
            #                return HttpResponse(html)
            #            else:
            conn.close()
            return HttpResponseRedirect("/Produktauswahl/BH Sets/")
    else:
        conn.close()
        return HttpResponseRedirect("/")


@csrf_exempt
def warenkorb_aufrufen(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database')

    c = conn.cursor(buffered=True)

    x = str(request.session.session_key)
    login = "false"
    status = 0
    modelAB = ""
    sub_picture = ""
    user = ""
    credit = 0
    adressbuch = ""
    email = "not ok"
    VIP = "false"
    gutscheinwert = 0
    gutscheincode = ""

    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        for row in c:
            wishlist = row[65]
            warenkorb = row[66]
            status = 1
            wishlist = row[65]
            warenkorb = row[66]
            definerebates = row[67]
            storecredit = get_existing_store_credit(c, row[11])
            bra_for_free = get_bra_for_free_in_VIP_model(c, row[11])
            definerebatesbestellwert = row[68]
            definerebateslieferkosten = row[69]
            definerebatesrabatte = row[70]
            selected_zahlungsoption = row[55]
            bereitsbestellt = row[75]
            bereitsversandt = row[76]
            credit = row[10]
            email = row[0]
            quiz = row[26]
            user = row[11]
            vorname = row[2]
            nachname = row[3]
            stadt = row[6]
            plz = row[4]
            letzteshoppingsicht = row[80]

            letztefilter = row[81]
            modelAB = row[47]
            sub_picture = row[48]
            wishlist_quantity = row[16]
            cart_quantity = row[17]
            if (row[0] != "" and row[12] != "") or (row[0] != "" and row[1] != ""):
                login = "true"

            if row[21] != "":
                gutscheincode = row[21]
                gutscheinwert = gutscheinwert_abrufen(gutscheincode, c, user, conn, "nein", user)
            shopping_type = row[22]
            if row[22] == "VIP" and row[23] == "true":
                VIP = "true"

            if (row[0] != "" and row[1] != "") or row[12] != "":
                email_check = "ok"
            else:
                email_check = "not ok"

            if (row[0] != "" and row[12] != "") or (row[0] != "" and row[1] != ""):
                login = "true"

    if user != "":

        print "length of warenkorb"
        print len(warenkorb)
        print warenkorb
        print status

        if check_whether_warenkorb_ist_leer(user, c) == 0:
            messageshownwarenkorbleer = "yes"
        else:
            messageshownwarenkorbleer = "no"

        if len(warenkorb) > 2 and status == 1:

            get_content_for_facebookpixel_from_order_ = get_content_for_facebookpixel_from_order(x, "", c, user)

            t = get_template('checkout.html')
            description_header = (
            "BHs und BH Sets für jede Größe und Brustform. Wir bieten lingerie in einer großen Auswahl an Farben an. Hochwertige Unterwäsche für Frauen günstig kaufen. BHs in vielen Designs, basic, sexy und bequeme BHs. Auf Rechnung kaufen mit 30 Tage Rückgaberecht. Kostenloser Versand.").encode(
                'utf8')

            html = t.render({'description_header': description_header,
                             'user_id_google_analytics': get_google_analytics_user_id(login, user),
                             'contents_list': get_content_for_facebookpixel_from_order_, 'letztefilter': letztefilter,
                             'letzteshoppingsicht': letzteshoppingsicht, 'url': get_link_positioining(""),
                             'links': get_links(quiz), 'email_check': email_check,
                             'allowed_countries': get_allowed_countries(c), 'email': email,
                             'bereitsbestellt': bereitsbestellt, 'bereitsversandt': bereitsversandt,
                             'fb_link': 'https://www.darlinglace.com',
                             'fb_title': ("Liebst du Lingerie? Erhalte Dein BH Set ab 29,95 EUR!").encode('utf8'),
                             'fb_description': (
                             "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                                 'utf8'), 'fb_description': (
                "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                    'utf8'), 'fb_image': 'https://www.darlinglace.com/static/overall_picture_bra.jpg',
                             'vorname': vorname, 'nachname': nachname, 'stadt': stadt, 'plz': plz, 'wishlist': wishlist,
                             'warenkorb': warenkorb, 'selected_zahlungsoption': selected_zahlungsoption,
                             'favicon': get_favicon(), 'path': request.path, 'brand_name': 'Darling Lace',
                             'title': "Kasse | Darling Lace", 'shopping_type': shopping_type, 'rebates': definerebates,
                             'storecredit': storecredit, 'bra_for_free': bra_for_free, 'VIP': VIP,
                             'gutscheinwert': gutscheinwert, 'gutscheincode': gutscheincode, 'warenkorb': warenkorb,
                             'credit': credit, 'adressbuch': define_adressbuch(user, c),
                             'zahlungsmethoden': define_zahlungsmethoden(user, c), 'login': login, 'email': email})
            return HttpResponse(html)


        else:
            return HttpResponseRedirect("/Produktauswahl/BH Sets/")
    else:
        return HttpResponseRedirect("/")


@csrf_exempt
def delete_empty_cart_message(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)
        x = str(request.session.session_key)

        c.execute("""update userdaten set messageshownwarenkorbleer=%s where gutscheincode=%s""",
                  ("", get_userid_from_session_id(c, x),))
        conn.commit()

        return HttpResponse(json.dumps(""), content_type='application/json')
    else:
        raise Http404


@csrf_exempt
def get_rabattname_from_request(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)
        x = str(request.session.session_key)

        try:
            c.execute("""select * from cart_details where gutscheincode=%s""", (user,))
            cart_gesamt = 0
            for row_2 in c:
                cart_gesamt = cart_gesamt + row_2[1]
        except:
            cart_gesamt = 0

        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            userdaten = c.fetchall()
            for row in userdaten:
                gutscheincode = row[21]
                user = row[11]

        return HttpResponse(json.dumps(get_rabattname(gutscheincode, cart_gesamt, c, user)),
                            content_type='application/json')
    else:
        raise Http404


def get_rabattname(gutscheincode, cart_gesamt, c, user):
    reload(sys)
    sys.setdefaultencoding("ISO-8859-1")

    c.execute("""select * from gutscheine """)
    gutscheine = c.fetchall()
    return_string = ""
    for row in gutscheine:
        print row[0] + "==" + gutscheincode
        if row[0] == gutscheincode:
            if row[4] == 0:
                preis = str("%.2f" % round(row[5], 2)).replace(".", ",")
                return_string = (""" Set für """ + str(preis) + """ EUR""").decode('windows-1252')
            if row[4] == 1:
                preis = str("%.2f" % round(row[6], 2)).replace(".", ",")
                return_string = "Rabatt von " + str(preis) + """ EUR"""
            if row[4] == 2:
                return_string = "Rabatt von " + str(int(row[7] * 100)) + "%"
            if row[4] == 3:
                i = 0
                zaehler = 0
                preis = 0

                if get_selected_VIP_model(user, c) == "VIP":

                    while i <= cart_gesamt - 1:
                        if i <= 4:
                            if row[8 + min(i, 4)] != 0:
                                zaehler = zaehler + 1
                                preis = preis + row[8 + min(i, 4)]

                        i = i + 1
                    preis = str("%.2f" % round(preis, 2)).replace(".", ",")
                else:
                    while i <= cart_gesamt - 1:
                        if i <= 4:
                            if row[17 + min(i, 4)] != 0:
                                zaehler = zaehler + 1
                                preis = preis + row[17 + min(i, 4)]

                        i = i + 1
                    preis = str("%.2f" % round(preis, 2)).replace(".", ",")

                if zaehler > 1:
                    return_string = (str(zaehler) + """ Sets für """ + str(preis) + """ EUR""").decode('windows-1252')
                else:
                    return_string = (str(zaehler) + """ Set für """ + str(preis) + """ EUR""").decode('windows-1252')

    return return_string


def get_allowed_countries(c):
    allowed_countries = []

    class Allowed_Countries(object):
        def __init__(self, land):
            self.land = land

    string1 = "Österreich"
    string1 = string1.encode('utf8')
    allowed_countries.append(Allowed_Countries(string1, ))

    string1 = "österreich"
    string1 = string1.encode('utf8')
    allowed_countries.append(Allowed_Countries(string1, ))
    allowed_countries.append(Allowed_Countries("Austria", ))
    allowed_countries.append(Allowed_Countries("austria", ))

    allowed_countries.append(Allowed_Countries("Deutschland", ))
    allowed_countries.append(Allowed_Countries("deutschland", ))
    allowed_countries.append(Allowed_Countries("Germany", ))
    allowed_countries.append(Allowed_Countries("germany", ))
    allowed_countries.append(Allowed_Countries("Schweiz", ))
    allowed_countries.append(Allowed_Countries("schweiz", ))
    allowed_countries.append(Allowed_Countries("Switzerland", ))
    allowed_countries.append(Allowed_Countries("switzerland", ))

    json_string = json.dumps([Allowed_Countries.__dict__ for Allowed_Countries in allowed_countries])

    return json_string


def get_favicon():
    return "/static/favicon_final.ico"


@csrf_exempt
def get_rebates(request):
    if request.is_ajax() and request.GET:
        bestellnummer = request.GET.get('bestellnummer')
        h = int(request.GET.get('item-length'))
        aenderung = request.GET.get('aenderung')
        n = request.GET.get('item')
        m = n.split(",")

        x = str(request.session.session_key)

        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')

        c = conn.cursor(buffered=True)

        rebates = define_rebates(user, bestellnummer, m, h, aenderung, c, conn, "", "no", "no", "no")
        conn.close()
        return HttpResponse(json.dumps(rebates), content_type='application/json')

    else:
        raise Http404


def get_warenwert(c, user):
    c.execute("""select * from cart_details where gutscheincode=%s ORDER BY preis DESC""", (user,))
    current_cart_database = c.fetchall()
    warenwert = 0

    for row_3 in current_cart_database:
        print "get_warenwert"
        print row_3[8]
        print row_3[1]
        warenwert = warenwert + row_3[8] * row_3[1]

    return warenwert


def gutscheinwert_abrufen_fuer_ruecksendung_2(gutscheincode, c, user, bestellnummer, erfolgte_ruecksendung):
    fehlermeldung = ""
    gutscheinwert = 0
    c.execute("""select * from gutscheine """)
    gutscheine = c.fetchall()
    for row in gutscheine:
        print(row[0] + "==" + gutscheincode)
        if row[0] == gutscheincode:

            if row[4] == 3:

                zaehler = 0
                erstes_set = row[8]
                zweites_set = row[9]
                drittes_set = row[10]
                viertes_set = row[11]
                mehralsvier_set = row[12]
                gutscheinwert = 0
                gutscheinwert_sub = 0

                if erfolgte_ruecksendung == "nein":
                    c.execute(
                        """select * from cart_details where gutscheincode=%s and bestellt=%s and bestellnummer=%s and zurueckgesendet=%s ORDER BY preis DESC""",
                        (user, "ja", bestellnummer, "nein",))
                else:
                    c.execute(
                        """select * from cart_details where gutscheincode=%s and bestellt=%s and bestellnummer=%s and zurueckgesendet=%s ORDER BY preis DESC""",
                        (user, "ja", bestellnummer, "ja",))
                current_cart_database = c.fetchall()
                for row_2 in current_cart_database:
                    sub_zaehler = 0

                    gutscheinwert_sub = 0

                    if row_2[2] != "" and row_2[3] != "":

                        if zaehler == 0 and erstes_set != 0:
                            if int(float(row_2[1]) - float(row_2[25])) > 0:
                                gutscheinwert_sub = gutscheinwert_sub - max(row_2[8] - erstes_set, 0)
                                sub_zaehler = sub_zaehler + 1

                            if erfolgte_ruecksendung == "nein":
                                if sub_zaehler < int(float(row_2[1]) - float(row_2[25])):
                                    zaehler = zaehler + 1
                            else:
                                if sub_zaehler < int(row_2[24]):
                                    zaehler = zaehler + 1

                        if zaehler == 1 and zweites_set != 0:
                            if int(float(row_2[1]) - float(row_2[25])) > 0:
                                gutscheinwert_sub = gutscheinwert_sub - max(row_2[8] - zweites_set, 0)
                                sub_zaehler = sub_zaehler + 1

                            if erfolgte_ruecksendung == "nein":
                                if sub_zaehler < int(float(row_2[1]) - float(row_2[25])):
                                    zaehler = zaehler + 1
                            else:
                                if sub_zaehler < int(row_2[24]):
                                    zaehler = zaehler + 1

                        if zaehler == 2 and drittes_set != 0:
                            if int(float(row_2[1]) - float(row_2[25])) > 0:
                                gutscheinwert_sub = gutscheinwert_sub - max(row_2[8] - drittes_set, 0)
                                sub_zaehler = sub_zaehler + 1

                            if erfolgte_ruecksendung == "nein":
                                if sub_zaehler < int(float(row_2[1]) - float(row_2[25])):
                                    zaehler = zaehler + 1
                            else:
                                if sub_zaehler < int(row_2[24]):
                                    zaehler = zaehler + 1

                        if zaehler == 3 and viertes_set != 0:
                            if int(float(row_2[1]) - float(row_2[25])) > 0:
                                gutscheinwert_sub = gutscheinwert_sub - max(row_2[8] - viertes_set, 0)
                                sub_zaehler = sub_zaehler + 1

                            if erfolgte_ruecksendung == "nein":
                                if sub_zaehler < int(float(row_2[1]) - float(row_2[25])):
                                    zaehler = zaehler + 1
                            else:
                                if sub_zaehler < int(row_2[24]):
                                    zaehler = zaehler + 1

                        if zaehler > 3 and mehralsvier_set != 0:
                            if int(float(row_2[1]) - float(row_2[25])) > 0:
                                gutscheinwert_sub = gutscheinwert_sub - max(row_2[8] - mehralsvier_set, 0)

                                sub_zaehler = sub_zaehler + 1
                            if erfolgte_ruecksendung == "nein":
                                if sub_zaehler < int(float(row_2[1]) - float(row_2[25])):
                                    zaehler = zaehler + 1
                            else:
                                if sub_zaehler < int(row_2[24]):
                                    zaehler = zaehler + 1

                        gutscheinwert = gutscheinwert + gutscheinwert_sub
                        zaehler = zaehler + 1

    return gutscheinwert


def get_selected_VIP_model(user, c):
    model = ""
    c.execute("""select * from userdaten where gutscheincode=%s""", (user,))
    userdaten = c.fetchall()
    for row in userdaten:
        model = row[22]

    return model


def gutscheinwert_abrufen(gutscheincode, c, session_key, conn, fehlermeldung_ja_nein, user):
    fehlermeldung = ""
    gutscheinwert = 0
    c.execute("""select * from gutscheine """)
    gutscheine = c.fetchall()
    fehlermeldung = "gutscheincode existiert nicht"
    for row in gutscheine:
        print(row[0] + "==" + gutscheincode)
        if row[0] == gutscheincode:
            fehlermeldung = ""
            print("guutschein")
            print(str(row[13]) + "<=" + str(get_warenwert(c, user)))
            if row[13] <= get_warenwert(c, user):
                print(row[4])
                if row[4] == 1:
                    gutscheinwert = float(row[6])
                    print "gutscheinwert"
                    print gutscheinwert

                if row[4] == 0:
                    c.execute("""select * from cart_details where gutscheincode=%s""", (user,))
                    current_cart_database = c.fetchall()
                    for row_2 in current_cart_database:
                        gutscheinwert = gutscheinwert + min(row[5] - row_2[8], 0) * row_2[1]

                        c.execute(
                            """update %s set gutscheinwert=%%s where bhgroesse=%%s and slipgroesse=%%s and stylecode=%%s and color=%%s and gutscheincode=%%s and bestellt=%%s""" % (
                            "cart_details"),
                            (min(row[5] - row_2[8], 0), row_2[2], row_2[3], row_2[7], row_2[4], user, "nein",))
                        conn.commit()
                if row[4] == 2:
                    print("20percent")
                    print(row[7])
                    gutscheinwert = -float(get_warenwert(c, user)) * (float(row[7]))
                    print(gutscheinwert)
                if row[4] == 3:

                    zaehler = 0
                    if get_selected_VIP_model(user, c) == "VIP":
                        erstes_set = row[8]
                        zweites_set = row[9]
                        drittes_set = row[10]
                        viertes_set = row[11]
                        mehralsvier_set = row[12]
                    else:
                        erstes_set = row[17]
                        zweites_set = row[18]
                        drittes_set = row[19]
                        viertes_set = row[20]
                        mehralsvier_set = row[21]

                    gutscheinwert = 0
                    gutscheinwert_sub = 0

                    c.execute("""update %s set gutscheinwert=%%s where gutscheincode=%%s and bestellt=%%s""" % (
                    "cart_details"), (0, user, "nein",))
                    conn.commit()

                    c.execute(
                        """select * from cart_details where gutscheincode=%s and bestellt=%s ORDER BY preis DESC""",
                        (user, "nein",))
                    current_cart_database = c.fetchall()
                    for row_2 in current_cart_database:
                        sub_zaehler = 0

                        gutscheinwert_sub = 0

                        if row_2[2] != "" and row_2[3] != "":

                            if zaehler == 0 and erstes_set != 0:
                                gutscheinwert_sub = gutscheinwert_sub - max(row_2[8] - erstes_set, 0)
                                sub_zaehler = sub_zaehler + 1

                                c.execute(
                                    """update %s set gutscheinwert=%%s where bhgroesse=%%s and slipgroesse=%%s and stylecode=%%s and color=%%s and gutscheincode=%%s and bestellt=%%s""" % (
                                    "cart_details"), (
                                    gutscheinwert_sub / row_2[1], row_2[2], row_2[3], row_2[7], row_2[4], user,
                                    "nein",))
                                conn.commit()

                                if sub_zaehler < int(row_2[1]):
                                    zaehler = zaehler + 1

                            if zaehler == 1 and zweites_set != 0:
                                gutscheinwert_sub = gutscheinwert_sub - max(row_2[8] - zweites_set, 0)
                                sub_zaehler = sub_zaehler + 1

                                c.execute(
                                    """update %s set gutscheinwert=%%s where bhgroesse=%%s and slipgroesse=%%s and stylecode=%%s and color=%%s and gutscheincode=%%s and bestellt=%%s""" % (
                                    "cart_details"), (
                                    gutscheinwert_sub / row_2[1], row_2[2], row_2[3], row_2[7], row_2[4], user,
                                    "nein",))
                                conn.commit()

                                if sub_zaehler < int(row_2[1]):
                                    zaehler = zaehler + 1

                            if zaehler == 2 and drittes_set != 0:
                                gutscheinwert_sub = gutscheinwert_sub - max(row_2[8] - drittes_set, 0)
                                sub_zaehler = sub_zaehler + 1

                                c.execute(
                                    """update %s set gutscheinwert=%%s where bhgroesse=%%s and slipgroesse=%%s and stylecode=%%s and color=%%s and gutscheincode=%%s and bestellt=%%s""" % (
                                    "cart_details"), (
                                    gutscheinwert_sub / row_2[1], row_2[2], row_2[3], row_2[7], row_2[4], user,
                                    "nein",))
                                conn.commit()

                                if sub_zaehler < int(row_2[1]):
                                    zaehler = zaehler + 1

                            if zaehler == 3 and viertes_set != 0:
                                gutscheinwert_sub = gutscheinwert_sub - max(row_2[8] - viertes_set, 0)
                                sub_zaehler = sub_zaehler + 1

                                c.execute(
                                    """update %s set gutscheinwert=%%s where bhgroesse=%%s and slipgroesse=%%s and stylecode=%%s and color=%%s and gutscheincode=%%s and bestellt=%%s""" % (
                                    "cart_details"), (
                                    gutscheinwert_sub / row_2[1], row_2[2], row_2[3], row_2[7], row_2[4], user,
                                    "nein",))
                                conn.commit()

                                if sub_zaehler < int(row_2[1]):
                                    zaehler = zaehler + 1

                            if zaehler > 3 and mehralsvier_set != 0:
                                gutscheinwert_sub = gutscheinwert_sub - max(row_2[8] - mehralsvier_set, 0)
                                c.execute(
                                    """update %s set gutscheinwert=%%s where bhgroesse=%%s and slipgroesse=%%s and stylecode=%%s and color=%%s and gutscheincode=%%s and bestellt=%%s""" % (
                                    "cart_details"), (
                                    gutscheinwert_sub / row_2[1], row_2[2], row_2[3], row_2[7], row_2[4], user,
                                    "nein",))
                                conn.commit()
                                sub_zaehler = sub_zaehler + 1
                                if sub_zaehler < int(row_2[1]):
                                    zaehler = zaehler + 1

                            gutscheinwert = gutscheinwert + gutscheinwert_sub
                            zaehler = zaehler + 1

            else:
                fehlermeldung = "mindestbestellwert nicht erreicht"
                print "mindestbestellwert nicht erreicht"
                c.execute("""update userdaten set genutztergutscheincode=%s where gutscheincode=%s""",
                          ("", session_key,))
                conn.commit()

    if fehlermeldung == "gutscheincode existiert nicht":
        fehlermeldung = "gutscheincode existiert nicht"
        print "gutscheincode existiert nicht"
        c.execute("""update userdaten set genutztergutscheincode=%s where gutscheincode=%s""", ("", session_key,))
        conn.commit()

    if fehlermeldung_ja_nein == "ja":
        c.execute("""update %s set gutscheinwert=%%s where gutscheincode=%%s and bestellt=%%s""" % ("cart_details"),
                  (0, user, "nein",))
        conn.commit()
        return fehlermeldung
    else:
        if gutscheinwert == 0:
            c.execute("""update %s set gutscheinwert=%%s where gutscheincode=%%s and bestellt=%%s""" % ("cart_details"),
                      (0, user, "nein",))
            conn.commit()
        return gutscheinwert


def monthToNum(shortMonth):
    return {
        'Januar': 1,
        'Februar': 2,
        'Maerz': 3,
        'April': 4,
        'Mai': 5,
        'Juni': 6,
        'Juli': 7,
        'August': 8,
        'September': 9,
        'October': 10,
        'November': 11,
        'Dezember': 12
    }[shortMonth]


@csrf_exempt
def warenkorb_abrufen(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database')
    c = conn.cursor(buffered=True)

    x = str(request.session.session_key)
    gutscheincode = ""
    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        userdaten = c.fetchall()
        for row in userdaten:
            user = row[11]
            modelAB = row[47]
            sub_picture = row[48]
            gutscheincode = row[21]
    gutscheinwert_abrufen(gutscheincode, c, user, conn, "nein", user)
    warenkorb = define_warenkorb(user, modelAB, sub_picture, c, conn)

    return HttpResponse(json.dumps(warenkorb), content_type='application/json')


def check_warenmenge(user, stylecode, colorcode, bh_groesse, slip_groesse, c):
    c.execute("""select * from cart_details where gutscheincode=%s""", (user,))

    current_cart = c.fetchall()
    anzahl = 0

    for row in current_cart:
        if bh_groesse != "":
            if row[7] == stylecode and row[2] == bh_groesse and row[3] == slip_groesse and row[4] == colorcode:
                anzahl = int(row[1])
        else:
            if row[7] == stylecode and row[3] == slip_groesse and row[2] == "" and row[4] == colorcode:
                anzahl = int(row[1])

    return anzahl


@csrf_exempt
def get_cart_from_server(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')

        c = conn.cursor(buffered=True)

        get_cart_data_and_rebates = request.GET.get('get_cart_data_and_rebates')

        x = str(request.session.session_key)
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        for row in c:
            user = row[11]
            facebookid = row[12]
            modelAB = row[47]
            sub_picture = row[48]

            warenkorb = define_warenkorb_object(user, modelAB, sub_picture, c, conn)

            if get_cart_data_and_rebates == "yes":
                feedback = get_warenkorb_and_rebates(warenkorb, define_rebates(user, "", "", "", "", c, conn,
                                                                               define_standard_lieferadresse(user, c),
                                                                               "no", "no", "no"))
            else:
                feedback = warenkorb

        return HttpResponse(json.dumps(feedback), content_type='application/json')


@csrf_exempt
def add_todo(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')

        c = conn.cursor(buffered=True)

        add_or_erase = request.GET.get('add_or_erase')
        anzahl_lingerie = request.GET.get('anzahl_lingerie')
        anzahl_panties = request.GET.get('anzahl_panties')
        stylecode_lingerie = request.GET.get('stylecode_lingerie')
        colorcode_lingerie = request.GET.get('colorcode_lingerie')
        colorcode_panties = request.GET.get('colorcode_panties')

        bh_groesse = request.GET.get('bh_groesse')
        slip_groesse_lingerie = request.GET.get('slip_groesse_lingerie')
        slip_groesse_panties = request.GET.get('slip_groesse_panties')

        windowwidth = request.GET.get('windowwidth')
        windowheight = request.GET.get('windowheight')

        get_cart_data_and_rebates = request.GET.get('get_cart_data_and_rebates')

        land = request.GET.get('land')
        warenkorb = ""
        panty_type = ""
        if slip_groesse_panties != "":
            slip_groesse_panties = slip_groesse_panties.split("(")
            slip_groesse_panties = slip_groesse_panties[0]

            panty_type = slip_groesse_panties.split(" ")
            panty_type = panty_type[0]

        x = str(request.session.session_key)
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        for row in c:
            user = row[11]
            facebookid = row[12]
            modelAB = row[47]
            sub_picture = row[48]

        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        Monat = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober",
                 "November", "Dezember"]
        now_date = str(now.day) + ". " + str(Monat[now.month - 1]) + " " + str(now.year)
        Y = now.year
        M = now.month
        D = now.day
        H = now.hour
        Mi = now.minute
        time = datetime.datetime.strptime(str(Y) + "-" + str(M) + "-" + str(D) + " " + str(H) + ":" + str(Mi),
                                          "%Y-%m-%d %H:%M")
        c.execute("""insert into Big_data_click_on_image values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (
        user, facebookid, modelAB, sub_picture, now_date, time, windowwidth, windowheight, stylecode_lingerie,
        colorcode_lingerie, "", "putincart", "", "",))
        conn.commit()

        feedback = ""

        x = str(request.session.session_key)

        print "add warenkorb"

        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            userdaten = c.fetchall()
            for row in userdaten:
                modelAB = row[47]
                sub_picture = row[48]
                user = row[11]

                shopping_type = row[22]
                if row[21] == "":
                    rabattcode = "willkommen"
                    c.execute("""update userdaten set genutztergutscheincode=%s where gutscheincode=%s""",
                              (rabattcode.upper(), row[11],))
                    conn.commit()

        genuegend_warenmenge_vorhanden = "false"

        if warenkorb == "":
            feedback_warenkorb_anpassen = warenkorb_anpassen(panty_type, shopping_type, user, anzahl_lingerie,
                                                             anzahl_panties, add_or_erase, stylecode_lingerie,
                                                             colorcode_lingerie, colorcode_panties, bh_groesse,
                                                             slip_groesse_lingerie, slip_groesse_panties, c, conn)

            if feedback_warenkorb_anpassen == "true":
                print "anpassen ok"
                if recheck_gutschein_wert(c, user, conn) != "error":
                    warenkorb = define_warenkorb_object(user, modelAB, sub_picture, c, conn)

                    define_rebates(user, "", "", "", "", c, conn, define_standard_lieferadresse(user, c), "no", "no",
                                   "no")

                    if get_cart_data_and_rebates == "yes":
                        feedback = get_warenkorb_and_rebates(warenkorb, define_rebates(user, "", "", "", "", c, conn,
                                                                                       define_standard_lieferadresse(
                                                                                           user, c), "no", "no", "no"))
                else:
                    warenkorb = "nicht genuegend warenwert fuer gutschein"



            else:
                warenkorb = feedback_warenkorb_anpassen

        if feedback == "":
            feedback = warenkorb

        return HttpResponse(json.dumps(feedback), content_type='application/json')



    else:
        raise Http404


def get_warenkorb_and_rebates_and_error_message(warenkorb_and_rebates, error):
    warenkorb_rebates_and_error = []

    class Warenkorb_Rebates_and_Error(object):
        def __init__(self, warenkorb_and_rebates, error):
            self.warenkorb_and_rebates = warenkorb_and_rebates
            self.error = error

    warenkorb_rebates_and_error.append(Warenkorb_Rebates_and_Error(warenkorb_and_rebates, error))

    json_string = json.dumps(
        [Warenkorb_Rebates_and_Error.__dict__ for Warenkorb_Rebates_and_Error in warenkorb_rebates_and_error])

    return json_string


def get_warenkorb_and_rebates(warenkorb, rebates):
    warenkorb_rebates = []

    class Warenkorb_Rebates(object):
        def __init__(self, warenkorb, rebates):
            self.warenkorb = warenkorb
            self.rebates = rebates

    warenkorb_rebates.append(Warenkorb_Rebates(warenkorb, rebates))

    json_string = json.dumps([Warenkorb_Rebates.__dict__ for Warenkorb_Rebates in warenkorb_rebates])

    return json_string


def warenkorb_anpassen(panty_type, shopping_type, user, anzahl_lingerie, anzahl_panties, add_or_erase,
                       stylecode_lingerie, colorcode_lingerie, colorcode_panties, bh_groesse, slip_groesse_lingerie,
                       slip_groesse_panties, c, conn):
    feedback = genuegend_warenmenge_vorhanden(panty_type, shopping_type, user, anzahl_lingerie, anzahl_panties,
                                              add_or_erase, stylecode_lingerie, colorcode_lingerie, colorcode_panties,
                                              bh_groesse, slip_groesse_lingerie, slip_groesse_panties, c, conn)

    if feedback == "true":
        return "true"
    else:
        return feedback


@csrf_exempt
def quiz_abrufen(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database')

    c = conn.cursor(buffered=True)

    x = str(request.session.session_key)

    showroom_stil = [[] for i in range(0)]
    showroom_color = [[] for i in range(0)]
    showroom_form = [[] for i in range(0)]
    showroom_position = [[] for i in range(0)]
    showroom_symmetrie = [[] for i in range(0)]
    showroom_sitz = [[] for i in range(0)]
    showroom_band_problems = [[] for i in range(0)]
    showroom_cup_problems = [[] for i in range(0)]

    showroom_stil_names = [[] for i in range(0)]
    showroom_color_names = [[] for i in range(0)]
    showroom_form_names = [[] for i in range(0)]
    showroom_position_names = [[] for i in range(0)]
    showroom_symmetrie_names = [[] for i in range(0)]
    showroom_sitz_names = [[] for i in range(0)]
    showroom_band_problems_names = [[] for i in range(0)]
    showroom_cup_problems_names = [[] for i in range(0)]

    x = str(request.session.session_key)
    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        userdaten = c.fetchall()
        for row in userdaten:
            quiztaken = row[26]

            showroom_stil.append(row[31])
            cup_based_on_quiz_character = row[36]

            showroom_color.append(row[38])
            showroom_color.append(row[39])
            showroom_color.append(row[40])
            showroom_color.append(row[41])

            showroom_form.append(row[32])
            showroom_position.append(row[33])
            showroom_symmetrie.append(row[34])
            showroom_sitz.append(row[35])

            showroom_band_problems.append(row[52])
            showroom_cup_problems.append(row[53])

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

            showroom_band_problems_names.append("Unterbrustband engt ein")
            showroom_band_problems_names.append("Unterbrustband sitzt perfekt")
            showroom_band_problems_names.append("Unterbrustband sitzt etwas locker")

            showroom_cup_problems_names.append("Cup/ Buegel druecken ein")
            showroom_cup_problems_names.append("Mittelsteg steht leicht ab")
            showroom_cup_problems_names.append("Meine Cups sitzen perfekt")
            showroom_cup_problems_names.append("Raender der Cups stehen ab")

            cup = row[36]
            band = row[37]
            age = row[46]
            competitor_brand = row[51]
            recommended_band = row[60]
            recommended_cup = row[61]

    i = 0
    stil_position = -1
    while i <= 3:
        if showroom_stil_names[i] == showroom_stil[0]:
            stil_position = i
        i = i + 1

    i = 0
    color_0 = -1
    color_1 = -1
    color_2 = -1
    color_3 = -1

    while i <= 3:
        if showroom_color[i] == 1:
            if i == 0:
                color_0 = 1
            if i == 1:
                color_1 = 1
            if i == 2:
                color_2 = 1
            if i == 3:
                color_3 = 1

        i = i + 1

    i = 0
    form_position = -1
    while i <= 1:
        if showroom_form_names[i] == showroom_form[0]:
            form_position = i
        i = i + 1

    i = 0
    position_position = -1
    while i <= 2:
        if showroom_position_names[i] == showroom_position[0]:
            position_position = i
        i = i + 1

    i = 0
    symmetrie_position = -1
    while i <= 1:
        if showroom_symmetrie_names[i] == showroom_symmetrie[0]:
            symmetrie_position = i
        i = i + 1

    i = 0
    sitz_position = -1
    while i <= 2:
        if showroom_sitz_names[i] == showroom_sitz[0]:
            sitz_position = i
        i = i + 1

    i = 0
    band_problems_position = -1
    while i <= 2:
        if showroom_band_problems_names[i] == showroom_band_problems[0]:
            band_problems_position = i
        i = i + 1

    i = 0
    cup_problems_position = -1
    while i <= 3:
        if showroom_cup_problems_names[i] == showroom_cup_problems[0]:
            cup_problems_position = i
        i = i + 1

    quiz = []

    class Quiz(object):
        def __init__(self, stil, color_0, color_1, color_2, color_3, form, position, symmetrie, sitz, quiztaken, cup,
                     band, age, competitor_brand, band_problems, cup_problems, recommended_band, recommended_cup):
            self.stil = stil
            self.color_0 = color_0
            self.color_1 = color_1
            self.color_2 = color_2
            self.color_3 = color_3
            self.form = form
            self.position = position
            self.symmetrie = symmetrie
            self.sitz = sitz
            self.quiztaken = quiztaken
            self.cup = cup
            self.band = band
            self.age = age
            self.competitor_brand = competitor_brand
            self.band_problems = band_problems
            self.cup_problems = cup_problems
            self.recommended_band = recommended_band
            self.recommended_cup = recommended_cup

    quiz.append(
        Quiz(stil_position, color_0, color_1, color_2, color_3, form_position, position_position, symmetrie_position,
             sitz_position, quiztaken, cup, band, age, competitor_brand, band_problems_position, cup_problems_position,
             recommended_band, recommended_cup))

    json_string = json.dumps([Quiz.__dict__ for Quiz in quiz])

    if cup_problems_position != -1 and cup_based_on_quiz_character != "":
        json_string_2 = band_cup_recommendation(c, conn, x)
    else:
        json_string_2 = ""

    quiz_object = []

    class Quiz_Object(object):
        def __init__(self, quizdata, band_cup_recommendation):
            self.quizdata = quizdata
            self.band_cup_recommendation = band_cup_recommendation

    quiz_object.append(Quiz_Object(json_string, json_string_2, ))

    json_string = json.dumps([Quiz_Object.__dict__ for Quiz_Object in quiz_object])

    return HttpResponse(json.dumps(json_string), content_type='application/json')


def band_cup_recommendation(c, conn, x):
    cup_table_1 = {0: 'AA',
                   1: 'A',
                   2: 'B',
                   3: 'C',
                   4: 'D',
                   5: 'E',
                   6: 'F',
                   7: 'G',
                   8: 'H',
                   9: 'I',
                   10: 'J',
                   11: 'K'

                   }

    cup_table_2 = {'AA': 0,
                   'A': 1,
                   'B': 2,
                   'C': 3,
                   'D': 4,
                   'E': 5,
                   'F': 6,
                   'G': 7,
                   'H': 8,
                   'I': 9,
                   'J': 10,
                   'K': 11,
                   'K': 12

                   }

    recommended_cup = ""
    recommended_band = ""
    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        userdaten = c.fetchall()
        for row in userdaten:
            band_problems = row[52]
            cup_problems = row[53]
            cup_based_on_quiz_character = row[36]
            print "cup_based_on_quiz_character"
            print row[36]
            cup_based_on_quiz_number = cup_table_2[cup_based_on_quiz_character]
            band_based_on_quiz = row[37]

            form = row[32]
            position = row[33]
            symmetrie = row[34]
            sitz = row[35]
            cup = row[36]

            c.execute("""select * from competitor_bra_problems """)
            competitor_bra_problems = c.fetchall()
            for row_2 in competitor_bra_problems:
                if row_2[0] == band_problems and row_2[1] == cup_problems:
                    recommended_cup_number = cup_based_on_quiz_number + row_2[3]
                    recommended_cup_character = cup_table_1[recommended_cup_number]

                    recommended_cup_number_alternative = cup_based_on_quiz_number + row_2[3]
                    recommended_cup_character_alternative = cup_table_1[recommended_cup_number_alternative]

                    recommended_band = int(band_based_on_quiz) + row_2[2]

                    empfehlungstext_sizing = row_2[5]

    c.execute("""update userdaten set recommendedband=%s, recommendedcup=%s where gutscheincode=%s""",
              (recommended_band, recommended_cup_character, get_userid_from_session_id(c, x),))
    conn.commit()

    c.execute("""select * from showroom_criteria """)
    showroom_criteria = c.fetchall()
    for row in showroom_criteria:
        if row[0] == form and row[1] == position and row[2] == symmetrie and row[3] == sitz and (
                row[4] == recommended_cup_character or recommended_cup_character == ""):
            empfehlungstext_type = row[13].encode('utf8')
    print(empfehlungstext_type)

    receommendations = []

    class Recommendations(object):
        def __init__(self, band_recommendation, cup_recommendation, empfehlungstext_sizing, empfehlungstext_type):
            self.band_recommendation = band_recommendation
            self.cup_recommendation = cup_recommendation
            self.empfehlungstext_sizing = empfehlungstext_sizing
            self.empfehlungstext_type = empfehlungstext_type

    receommendations.append(
        Recommendations(recommended_band, recommended_cup_character, empfehlungstext_sizing, empfehlungstext_type))

    json_string = json.dumps([Recommendations.__dict__ for Recommendations in receommendations])
    print("json_string")
    print(json_string)
    return json_string


@csrf_exempt
def quiz_beenden(request):
    if request.is_ajax() and request.POST:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)
        quiztaken = request.POST.get('quiztaken')
        stil = request.POST.get('stil')
        color_0 = request.POST.get('color_0')
        color_1 = request.POST.get('color_1')
        color_2 = request.POST.get('color_2')
        color_3 = request.POST.get('color_3')
        form = request.POST.get('form')
        position = request.POST.get('position')
        symmetrie = request.POST.get('symmetrie')
        sitz = request.POST.get('sitz')
        cup = request.POST.get('cup')
        band = request.POST.get('band')
        age = request.POST.get('age')
        seite = request.POST.get('seite')

        cup_recommendation = request.POST.get('cup_recommendation')
        band_recommendation = request.POST.get('band_recommendation')

        competitor_brand = request.POST.get('competitor_brand')
        band_problems = request.POST.get('band_problems')
        cup_problems = request.POST.get('cup_problems')

        if cup == "" and band != "":
            band = ""
        else:
            if cup != "" and band == "":
                cup = ""
        x = str(request.session.session_key)
        user = get_userid_from_session_id(c, x)
        if quiztaken == "no":
            if x != "None":
                c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
                userdaten = c.fetchall()
                for row in userdaten:
                    quiztaken == row[26]
                    defaultbrasize = row[60] + row[61]
                    user = row[11]

        if seite == "3":
            if stil == "0":
                c.execute(
                    """update userdaten set sexy=%s, hotromance=%s, classiccute=%s, playful=%s, dominantfactorstyle=%s where gutscheincode=%s""",
                    (0.5, 0.25, 0.1, 0.15, "sexy", user,))
            if stil == "1":
                c.execute(
                    """update userdaten set sexy=%s, hotromance=%s, classiccute=%s, playful=%s, dominantfactorstyle=%s where gutscheincode=%s""",
                    (0.15, 0.15, 0.2, 0.5, "playful", user,))
            if stil == "2":
                c.execute(
                    """update userdaten set sexy=%s, hotromance=%s, classiccute=%s, playful=%s, dominantfactorstyle=%s where gutscheincode=%s""",
                    (0.1, 0.1, 0.5, 0.3, "classiccute", user,))
            if stil == "3":
                c.execute(
                    """update userdaten set sexy=%s, hotromance=%s, classiccute=%s, playful=%s, dominantfactorstyle=%s where gutscheincode=%s""",
                    (0.25, 0.5, 0.1, 0.15, "romantic", user,))

        if seite == "4":
            if color_0 != "" or color_1 != "" or color_2 != "" or color_3 != "":
                c.execute(
                    """update userdaten set neutrals=%s, bright=%s, deep=%s, printedpattern=%s, dominantfactorcolors=%s where gutscheincode=%s""",
                    (float(color_0), float(color_1), float(color_2), float(color_3), "", user))

            if form == "0":
                c.execute("""update userdaten set Form=%s where gutscheincode=%s""", ("Rund", user))
            if form == "1":
                c.execute("""update userdaten set Form=%s where gutscheincode=%s""", ("Tropfenform", user))

        if seite == "5":
            if position == "0":
                c.execute("""update userdaten set Position=%s where gutscheincode=%s""", ("Mittig", user))
            if position == "1":
                c.execute("""update userdaten set Position=%s where gutscheincode=%s""", ("Leicht Ost-West", user))

            if position == "2":
                c.execute("""update userdaten set Position=%s where gutscheincode=%s""", ("Stark Ost-West", user))

        if seite == "6":
            if symmetrie == "0":
                c.execute("""update userdaten set Symmetrie=%s where gutscheincode=%s""", ("Symmetrisch", user))
            if symmetrie == "1":
                c.execute("""update userdaten set Symmetrie=%s where gutscheincode=%s""", ("Asymmetrisch", user))

        if seite == "7":
            if sitz == "0":
                c.execute("""update userdaten set Sitz=%s where gutscheincode=%s""", ("Gestuetzt", user))
            if sitz == "1":
                c.execute("""update userdaten set Sitz=%s where gutscheincode=%s""", ("Halb gestuetzt", user))

            if sitz == "2":
                c.execute("""update userdaten set Sitz=%s where gutscheincode=%s""", ("Nach unten geneigt", user))

        print seite

        if seite == "8":
            if age != "-1":
                c.execute("""update userdaten set Age=%s where gutscheincode=%s""", (age, user))

            print "asd"
            if band != "-1" and cup != "-1":
                print "band"
                print band + " " + cup
                c.execute("""update userdaten set Bandinquiz=%s, Cupinquiz=%s where gutscheincode=%s""",
                          (band, cup, user))

            if competitor_brand != "":
                c.execute("""update userdaten set competitorbrand=%s where gutscheincode=%s""",
                          (competitor_brand, user))

        if seite == "9":
            if band_problems == "0":
                c.execute("""update userdaten set bandproblems=%s where gutscheincode=%s""",
                          ("Unterbrustband engt ein", user))
            if band_problems == "1":
                c.execute("""update userdaten set bandproblems=%s where gutscheincode=%s""",
                          ("Unterbrustband sitzt perfekt", user))
            if band_problems == "2":
                c.execute("""update userdaten set bandproblems=%s where gutscheincode=%s""",
                          ("Unterbrustband sitzt etwas locker", user))

        if seite == "10":
            if cup_problems == "0":
                c.execute("""update userdaten set cupproblems=%s where gutscheincode=%s""",
                          ("Cup/ Buegel druecken ein", user))
            if cup_problems == "1":
                c.execute("""update userdaten set cupproblems=%s where gutscheincode=%s""",
                          ("Mittelsteg steht leicht ab", user))
            if cup_problems == "2":
                c.execute("""update userdaten set cupproblems=%s where gutscheincode=%s""",
                          ("Meine Cups sitzen perfekt", user))
            if cup_problems == "3":
                c.execute("""update userdaten set cupproblems=%s where gutscheincode=%s""",
                          ("Raender der Cups stehen ab", user))

        if quiztaken == "yes" and seite == "11":
            c.execute("""update userdaten set quiztaken=%s where gutscheincode=%s""", ("yes", user))

        conn.commit()

        if quiztaken == "yes":
            c.execute("""update userdaten set defaultbrasize=%s where gutscheincode=%s""",
                      (band_recommendation + cup_recommendation, user))
            conn.commit()
            generate_showroom(user, c, conn)

        if seite == "10":
            return HttpResponse(json.dumps(band_cup_recommendation(c, conn, user)), content_type='application/json')
        else:
            return HttpResponse(json.dumps(""), content_type='application/json')


def generate_showroom(c, conn, bandclickfirstid, cupclickfirstid, brandclickfirstid, bandclicksecondid,
                      cupclicksecondid, brandclicksecondid, question2, question3, question4, question5, question6,
                      question6a, question8, question9, pantyid, user):
    c.execute("""select * from groessenempfehlung_quiz""")
    groessenempfehlung_quiz = c.fetchall()
    zaehler_band = 0
    zaehler_cup = 0
    zaehler = 0
    band_anpassung = 0
    cup_anpassung = 0
    for row in groessenempfehlung_quiz:
        print row[3]
        if zaehler <= 7:

            if int(question2) == zaehler:
                band_anpassung = band_anpassung + row[1]
            if int(question3) == zaehler:
                band_anpassung = band_anpassung + row[2]

            if int(question4) == zaehler:
                band_anpassung = band_anpassung + row[3]

            if int(question5) == zaehler:
                band_anpassung = band_anpassung + row[4]

            if int(question6) == zaehler:
                band_anpassung = band_anpassung + row[5]

            if int(question9) == zaehler:
                band_anpassung = band_anpassung + row[9]
            print "band_anpassung"
            print(str(zaehler) + "," + str(band_anpassung) + "," + str(row[9]))
        else:

            if int(question2) == zaehler - 8:
                cup_anpassung = cup_anpassung + row[1]
            if int(question3) == zaehler - 8:
                cup_anpassung = cup_anpassung + row[2]

            if int(question4) == zaehler - 8:
                cup_anpassung = cup_anpassung + row[3]

            if int(question5) == zaehler - 8:
                cup_anpassung = cup_anpassung + row[4]

            if int(question6) == zaehler - 8:
                cup_anpassung = cup_anpassung + row[5]

            if int(question9) == zaehler - 8:
                cup_anpassung = cup_anpassung + row[8]
            print "cup_anpassung"
            print(str(zaehler) + "," + str(cup_anpassung) + "," + str(row[9]))

        zaehler = zaehler + 1

    cup_table_1 = {0: 'AAA',
                   1: 'AA',
                   2: 'A',
                   3: 'B',
                   4: 'C',
                   5: 'D',
                   6: 'E',
                   7: 'F',
                   8: 'G',
                   9: 'H',
                   10: 'I',
                   11: 'J',
                   12: 'K',
                   13: 'L'

                   }

    print "row[0]==brandclickfirstid and row[2]==cup_table_1[int(cupclickfirstid)]"

    c.execute("""select * from groessenempfehlung_quiz_andere_hersteller""")
    groessenempfehlung_quiz_andere_hersteller = c.fetchall()
    band_anpassung_hersteller_first = 0
    cup_anpassung_hersteller_first = 0
    band_anpassung_hersteller_second = -1
    cup_anpassung_hersteller_second = -1
    for row in groessenempfehlung_quiz_andere_hersteller:
        if row[1] != "":
            print row[0] + "==" + brandclickfirstid + "and" + str(row[1]) + "==" + str(60 + int(bandclickfirstid) * 5)
            if row[0] == brandclickfirstid and int(row[1]) == 60 + int(bandclickfirstid) * 5:
                band_anpassung_hersteller_first = row[3]
                print "band_anpassung_hersteller_first"
                print band_anpassung_hersteller_first

        print str(row[0]) + "==" + str(brandclickfirstid) + " and " + str(row[2]) + "==" + str(
            cup_table_1[int(cupclickfirstid)])
        if row[2] != "":
            print "cup_anpassung_hersteller_first"
            if row[0] == brandclickfirstid and str(row[2]) == str(cup_table_1[int(cupclickfirstid)]):
                cup_anpassung_hersteller_first = row[4]
                print cup_anpassung_hersteller_first

        if int(bandclicksecondid) != -1:
            if row[1] != "":
                if row[0] == brandclicksecondid and int(row[1]) == 60 + int(bandclicksecondid) * 5:
                    band_anpassung_hersteller_second = row[3]
            if row[2] != "":
                if row[0] == brandclicksecondid and row[2] == cup_table_1[int(cupclicksecondid)]:
                    cup_anpassung_hersteller_second = row[4]
    print cup_anpassung
    print cup_anpassung_hersteller_first

    print str(band_anpassung) + "," + str(band_anpassung_hersteller_first)
    band_aenderung = band_anpassung + band_anpassung_hersteller_first
    cup_aenderung = cup_anpassung + cup_anpassung_hersteller_first
    print band_aenderung
    print cup_aenderung

    band_empfehlung = 0
    if band_aenderung > 3.5:
        band_empfehlung = 1
    else:
        if int(bandclicksecondid) != -1:
            if band_aenderung > 2 and (int(bandclickfirstid) < int(bandclicksecondid) or (
                    int(band_anpassung_hersteller_second) != -1 and int(band_anpassung_hersteller_second) - int(
                    band_anpassung_hersteller_first) > 1)):
                band_empfehlung = 1

    if band_aenderung < -3.5:
        band_empfehlung = -1
    else:
        if int(bandclicksecondid) != -1:
            if band_aenderung < -2 and (int(bandclickfirstid) > int(bandclicksecondid) or (
                    int(band_anpassung_hersteller_second) != -1 and int(band_anpassung_hersteller_second) - int(
                    band_anpassung_hersteller_first) < -1)):
                band_empfehlung = -1

    cup_empfehlung = 0
    if band_empfehlung == 1:
        cup_aenderung = cup_aenderung - 2.5
    else:
        if band_empfehlung == -1:
            cup_aenderung = cup_aenderung + 2.5

    if cup_aenderung > 9:
        cup_empfehlung = 4
    else:
        if cup_aenderung > 6.5:
            cup_empfehlung = 3
        else:
            if cup_aenderung > 4:
                cup_empfehlung = 2
            else:
                if cup_aenderung > 1.5:
                    cup_empfehlung = 1

    if cup_aenderung < -9:
        cup_empfehlung = -4
    else:
        if cup_aenderung < -6.5:
            cup_empfehlung = -3
        else:
            if cup_aenderung < -4:
                cup_empfehlung = -2
            else:
                if cup_aenderung < -1.5:
                    cup_empfehlung = -1

    cup_calc = int(cupclickfirstid) + int(cup_empfehlung)
    band_calc = int(bandclickfirstid) + int(band_empfehlung)

    if cup_calc < 0:
        aenderung_cup_calc = -cup_calc

        cup_calc = cup_calc + aenderung_cup_calc
        cup_empfehlung = cup_empfehlung + aenderung_cup_calc

    if cup_calc > 8:
        aenderung_cup_calc = cup_calc - 8

        cup_calc = cup_calc - aenderung_cup_calc
        cup_empfehlung = cup_empfehlung - aenderung_cup_calc

    hilf_recommendedcup = cup_table_1[cup_calc]
    hilf_recommendedband = 60 + band_calc * 5

    if hilf_recommendedcup == "AAA" and hilf_recommendedband < 85:
        cup_calc = cup_calc + 1

    if hilf_recommendedcup == "AAA" and hilf_recommendedband == 85:
        cup_calc = cup_calc + 3

    if hilf_recommendedcup == "AA" and hilf_recommendedband == 85:
        cup_calc = cup_calc + 2

    if hilf_recommendedcup == "A" and hilf_recommendedband == 85:
        cup_calc = cup_calc + 1

    if hilf_recommendedcup == "A" and hilf_recommendedband == 90:
        cup_calc = cup_calc + 1

    if hilf_recommendedcup == "A" and hilf_recommendedband == 100:
        cup_calc = cup_calc + 2
        band_calc = band_calc - 1

    if hilf_recommendedcup == "B" and hilf_recommendedband == 95:
        cup_calc = cup_calc + 1

    print "bandclickfirstid"
    print bandclickfirstid
    print band_empfehlung

    print cupclickfirstid
    print cup_empfehlung
    recommendedband = 60 + band_calc * 5

    recommendedcup = cup_table_1[cup_calc]

    recommendedsizetext = -1

    if cup_empfehlung == 0 and band_empfehlung == 0:
        recommendedsizetext = 0

    if cup_empfehlung > 0 and band_empfehlung == 0:
        recommendedsizetext = 1

    if cup_empfehlung < 0 and band_empfehlung == 0:
        recommendedsizetext = 2

    if cup_empfehlung < 0 and band_empfehlung > 0:
        recommendedsizetext = 3

    if cup_empfehlung == 0 and band_empfehlung > 0:
        recommendedsizetext = 4

    if cup_empfehlung == 0 and band_empfehlung < 0:
        recommendedsizetext = 5

    if cup_empfehlung > 0 and band_empfehlung < 0:
        recommendedsizetext = 6

    c.execute(
        """update userdaten set recommendedsizetext=%s, bandempfehlungaenderung=%s,cupempfehlungaenderung=%s, recommendedband=%s, recommendedcup=%s where gutscheincode=%s""",
        (recommendedsizetext, band_empfehlung, cup_empfehlung, recommendedband, recommendedcup, user,))

    now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
    Y = now.year
    M = now.month
    D = now.day
    H = now.hour

    c.execute(
        """delete from %s where dayofshowroom=%%s and monthofshowroom=%%s and yearofshowroom=%%s and gutscheincode=%%s""" % (
        "showroom"), (D, M, Y, user))

    groessen_liste_complete = define_showroom_lingerie(c, recommendedband, recommendedcup, question8)
    print groessen_liste_complete
    i = 0
    while i <= len(groessen_liste_complete) - 1:
        print groessen_liste_complete[i][0]
        c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % ("showroom"), (
        groessen_liste_complete[i][0], groessen_liste_complete[i][1], D, M, Y, user, groessen_liste_complete[i][12]))
        if i == 7:
            i = len(groessen_liste_complete)
        i = i + 1

    c.execute("""update userdaten set dayofshowroom=%s, monthofshowroom=%s, yearofshowroom=%s where gutscheincode=%s""",
              (D, M, Y, user,))
    conn.commit()


def define_showroom_lingerie(c, band, cup, brustform_antwort_nr):
    print band
    print cup

    groessen_liste = []
    c.execute("""select * from %s where size=%%s""" % ("stylecode"), (str(band) + cup,))
    stylecode_daten = c.fetchall()
    for row_3 in stylecode_daten:

        menge = int(row_3[4]) - int(row_3[5])
        if menge > 0:

            c.execute("""select * from lingerieselection where stylecode=%s and colorcode=%s and productgroup=%s""",
                      (row_3[1], row_3[2], "lingerie",))
            lingerieselection_data = c.fetchall()
            for row_4 in lingerieselection_data:

                pad = []
                j = 0
                while j <= 3:
                    if row_4[40 + j] == "x":
                        pad.append(1)
                    else:
                        pad.append(0)
                    j = j + 1

                style = []
                j = 0
                while j <= 5:
                    if j < 4:
                        if row_4[21 + j] == "x":
                            style.append(1)
                        else:
                            style.append(0)

                    if j == 4:
                        if row_4[20] == "x":
                            style.append(1)
                        else:
                            style.append(0)

                    if j == 5:
                        if row_4[37] == "x":
                            style.append(1)
                        else:
                            style.append(0)

                    j = j + 1

                print row_4[0]
                print style

                groessen_liste.append(
                    [row_3[1], row_3[2], pad[0], pad[1], pad[2], pad[3], style[0], style[1], style[2], style[3],
                     style[4], style[5], ""])

    cup_table_3 = {'AAA': 0,
                   'AA': 1,
                   'A': 2,
                   'B': 3,
                   'C': 4,
                   'D': 5,
                   'E': 6,
                   'F': 7,
                   'G': 8,
                   'H': 9,
                   'I': 10,
                   'J': 11,
                   'K': 12,
                   'L': 13,
                   'Z': 26

                   }

    # matching of columns in table styleempfehlung with columns in table lingerieselection
    style_liste = {'10': 21,
                   '11': 22,
                   '12': 23,
                   '13': 24,
                   '14': 20,
                   '15': 37,

                   }

    padding_liste = {'6': 40,
                     '7': 41,
                     '8': 42,
                     '9': 43,

                     }

    print(cup)
    Cup_in_number = cup_table_3[cup]

    c.execute("""select * from styleempfehlung where AntwNr=%s""", (brustform_antwort_nr,))
    for row in c:
        print row[4]
        print row[5]
        print Cup_in_number
        print str(cup_table_3[row[4]]) + "<=" + str(Cup_in_number) + "and" + str(cup_table_3[row[5]]) + ">=" + str(
            Cup_in_number)
        if cup_table_3[row[4]] <= Cup_in_number and cup_table_3[row[5]] >= Cup_in_number:
            print str(band) + ">=" + str(row[2]) + "and " + str(band) + "<=" + str(row[3])
            if int(band) >= int(row[2]) and int(band) <= int(row[3]):
                print("yes")

                i = 0
                while i <= len(groessen_liste) - 1:
                    pad = []
                    j = 0
                    while j <= 3:
                        pad.append(int(row[6 + j]) * int(groessen_liste[i][2 + j]))
                        j = j + 1
                    print groessen_liste[i][0]
                    print pad
                    max_pad = max(pad[0], pad[1], pad[2], pad[3])

                    style = []
                    j = 0
                    while j <= 5:
                        style.append(int(row[10 + j]) * int(groessen_liste[i][6 + j]))
                        j = j + 1
                    max_style = max(style[0], style[1], style[2], style[3], style[4], style[5])

                    print style

                    print max_pad
                    print max_style

                    score = int(max_pad) + int(max_style)
                    print score
                    groessen_liste[i][12] = score
                    i = i + 1

    sorted_by_second = sorted(groessen_liste, key=lambda tup: tup[12], reverse=True)

    print sorted_by_second

    return sorted_by_second


def link_to_detail_sites(request, offset, redirect_link):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database')

    c = conn.cursor(buffered=True)

    x = str(request.session.session_key)
    login = "false"
    status = 0
    modelAB = ""
    sub_picture = ""
    user = ""

    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        for row in c:
            status = 1
            bereitsbestellt = row[75]
            bereitsversandt = row[76]
            neukunde = row[57]
            wishlist = row[65]
            warenkorb = row[66]
            letzteshoppingsicht = row[80]
            letztefilter = row[81]

            if row[26] == "yes":
                quiz_footer = "true"
            else:
                quiz_footer = row[54]

            recommended_band = row[60]
            recommended_cup = row[61]
            pantyid = row[53]
            email = row[0]
            user = row[11]
            vorname = row[2]
            nachname = row[3]
            default_bra_size = row[58]
            default_panty_size = row[59]
            facebookid = row[12]
            quiz = row[26]
            stadt = row[6]
            plz = row[4]
            modelAB = row[47]
            sub_picture = row[48]
            wishlist_quantity = row[16]
            cart_quantity = row[17]
            if (row[0] != "" and row[12] != "") or (row[0] != "" and row[1] != ""):
                login = "true"
            if row[22] == "VIP" and row[23] == "true":
                VIP = "VIP"
            else:
                VIP = "Regular"

    if status == 0:
        if x != "None":
            x = str(request.session.session_key)
            create_user(x, c, conn)
        else:
            print(request.path + ",create_new_request," + x)
            log_out_do_it(x, c, conn)
            request.session.create()
            x = str(request.session.session_key)
            create_user(x, c, conn)

        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            for row in c:
                wishlist = row[65]
                bereitsbestellt = row[75]
                bereitsversandt = row[76]
                neukunde = row[57]
                warenkorb = row[66]
                letzteshoppingsicht = row[80]

                letztefilter = row[81]

                if row[26] == "yes":
                    quiz_footer = "true"
                else:
                    quiz_footer = row[54]

                recommended_band = row[60]
                recommended_cup = row[61]

                pantyid = row[53]
                email = row[0]
                user = row[11]
                vorname = row[2]
                nachname = row[3]

                default_bra_size = row[58]
                default_panty_size = row[59]
                facebookid = row[12]
                quiz = row[26]
                stadt = row[6]
                plz = row[4]
                modelAB = row[47]
                sub_picture = row[48]
                wishlist_quantity = row[16]
                cart_quantity = row[17]
                if row[22] == "VIP" and row[23] == "true":
                    VIP = "VIP"
                else:
                    VIP = "Regular"

    print("user")
    print(user)
    if user != "":
        sizes = get_lingerie_selection_sizes(redirect_link, link_group_bestimmen(offset), c)

        if pantyid != "" and pantyid != -1:
            panty_matching_id = {0: "XXS",
                                 1: "XS",
                                 2: "S",
                                 3: "M",
                                 4: "L",
                                 5: "XL",
                                 6: "XXL"

                                 }
            pantyid = panty_matching_id[pantyid]

        print "gericht_template.html"
        print offset

        t = get_template('gericht_template.html')
        link_positioning = get_link_positioining(offset)
        lingerie = get_lingerie_selection_filter(link_group_bestimmen(offset), "", "", "", "", user, redirect_link, "",
                                                 "", "", "", "", "", "", modelAB, sub_picture, c)
        lingerie_details = json.loads(lingerie)
        lingerie_picture = json.loads(lingerie_details[0]['pic'])

        lingerie_name = lingerie_details[0]['name']
        lingerie_link = lingerie_details[0]['link']
        print "lingerie_picture[0]"
        print lingerie_picture[0]
        lingerie_picture = lingerie_picture[0]['link']
        lingerie_shortdescription = lingerie_details[0]['descriptionshort']

        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        Monat = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober",
                 "November", "Dezember"]
        now_date = str(now.day) + ". " + str(Monat[now.month - 1]) + " " + str(now.year)
        Y = now.year
        M = now.month
        D = now.day
        H = now.hour
        Mi = now.minute
        time = datetime.datetime.strptime(str(Y) + "-" + str(M) + "-" + str(D) + " " + str(H) + ":" + str(Mi),
                                          "%Y-%m-%d %H:%M")

        c.execute("""insert into Big_data_click_on_image values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (
        user, facebookid, modelAB, sub_picture, now_date, time, "", "", lingerie_details[0]['stylecode'],
        lingerie_details[0]['colorcode'], lingerie_name, "", "", "",))
        conn.commit()
        print("ok")

        lingerie_details_for_title = lingerie_details[0]['details'].split("<br>")
        try:
            lingerie_details_for_title = lingerie_details_for_title[0][2:] + ": " + lingerie_details_for_title[1][3:]
        except:
            lingerie_details_for_title = "Darling Lace"

        if len(lingerie) != 2:
            html = t.render({'quiz_footer': quiz_footer, 'panty': pantyid, 'recommended_band': recommended_band,
                             'recommended_cup': recommended_cup, 'description_header': lingerie_details[0]['details'],
                             'user_id_google_analytics': get_google_analytics_user_id(login, user),
                             'letztefilter': letztefilter, 'letzteshoppingsicht': letzteshoppingsicht,
                             'lingerie_price': lingerie_details[0]['pricesubscription'],
                             'lingerie_picture': lingerie_picture,
                             'lingerie_descriptionshort': lingerie_shortdescription, 'lingerie_name': lingerie_name,
                             'gutscheincode': user, 'default_bra_size': default_bra_size,
                             'default_panty_size': default_panty_size, 'email': email,
                             'bereitsbestellt': bereitsbestellt, 'bereitsversandt': bereitsversandt,
                             'fb_link': 'https://www.darlinglace.com/Produktauswahl/' + lingerie_link + '/' + lingerie_name,
                             'fb_title': (lingerie_details_for_title).encode('utf8'),
                             'fb_description': (lingerie_shortdescription).encode('utf8'),
                             'fb_image': 'https://www.darlinglace.com/' + lingerie_picture, 'vorname': vorname,
                             'nachname': nachname, 'stadt': stadt, 'plz': plz, 'wishlist': wishlist,
                             'warenkorb': warenkorb, 'favicon': get_favicon(), 'path': request.path,
                             'brand_name': 'Darling Lace',
                             'pricesforaddlpanty': get_pricesforaddlpanty(redirect_link, VIP, c), 'VIP': VIP,
                             'title': (lingerie_details_for_title + " | Darling Lace").encode('utf8'),
                             'colors': get_other_colors("", redirect_link, link_group_bestimmen(offset), c),
                             'gesamtbewertung': get_lingerie_selection_gesamtbewertung(redirect_link, c),
                             'bewertungen_detail': get_lingerie_selection_bewertungen(redirect_link, c), 'sizes': sizes,
                             'index': offset, 'login': login, 'lingerie_offerings': lingerie, 'url': link_positioning,
                             'links': get_links(quiz)})
            conn.close()
            return HttpResponse(html)
        else:
            print("length")
            conn.close()
            return HttpResponseRedirect("/")
    else:
        conn.close()
        return HttpResponseRedirect("/")


def get_google_analytics_user_id(login, user):
    if login == "true":
        return user
    else:
        return "Keine"


def get_groessentabelle(c):
    c.execute("""select * from groessentabelle """)
    for row in c:
        uebersicht = row[0]
        detailliert = row[1]

    groessentabelle = []

    class Groessentabelle(object):
        def __init__(self, uebersicht, detailliert):
            self.uebersicht = uebersicht
            self.detailliert = detailliert

    groessentabelle.append(Groessentabelle(uebersicht, detailliert))

    json_string = json.dumps([Groessentabelle.__dict__ for Groessentabelle in groessentabelle])

    return json_string


def call_login_page(path, c, x):
    login = "false"
    status = 0
    modelAB = ""
    sub_picture = ""
    user = ""

    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        for row in c:
            status = 1
            bereitsbestellt = row[75]
            bereitsversandt = row[76]
            wishlist = row[65]
            warenkorb = row[66]
            email = row[0]
            user = row[11]
            vorname = row[2]
            nachname = row[3]
            default_bra_size = row[58]
            default_panty_size = row[59]
            facebookid = row[12]
            quiz = row[26]
            stadt = row[6]
            plz = row[4]
            modelAB = row[47]
            sub_picture = row[48]
            wishlist_quantity = row[16]
            cart_quantity = row[17]
            if (row[0] != "" and row[12] != "") or (row[0] != "" and row[1] != ""):
                login = "true"
            if row[22] == "VIP" and row[23] == "true":
                VIP = "VIP"
            else:
                VIP = "Regular"

    if status == 0:
        if x != "None":
            x = str(request.session.session_key)
            create_user(x, c, conn)
        else:
            print(request.path + ",create_new_request," + x)
            log_out_do_it(x, c, conn)
            request.session.create()
            x = str(request.session.session_key)
            create_user(x, c, conn)

        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            for row in c:
                wishlist = row[65]
                bereitsbestellt = row[75]
                bereitsversandt = row[76]
                warenkorb = row[66]
                email = row[0]
                user = row[11]
                vorname = row[2]
                nachname = row[3]
                default_bra_size = row[58]
                default_panty_size = row[59]
                facebookid = row[12]
                quiz = row[26]
                stadt = row[6]
                plz = row[4]
                modelAB = row[47]
                sub_picture = row[48]
                wishlist_quantity = row[16]
                cart_quantity = row[17]
                if row[22] == "VIP" and row[23] == "true":
                    VIP = "VIP"
                else:
                    VIP = "Regular"

    if user != "":
        t = get_template('anmelden_seite.html')
        description_header = (
        "BHs und BH Sets für jede Größe und Brustform. Wir bieten lingerie in einer großen Auswahl an Farben an. Hochwertige Unterwäsche für Frauen günstig kaufen. BHs in vielen Designs, basic, sexy und bequeme BHs. Auf Rechnung kaufen mit 30 Tage Rückgaberecht. Kostenloser Versand.").encode(
            'utf8')

        html = t.render({'url': get_link_positioining(""), 'description_header': description_header,
                         'user_id_google_analytics': get_google_analytics_user_id(login, user), 'email': email,
                         'bereitsbestellt': bereitsbestellt, 'bereitsversandt': bereitsversandt,
                         'fb_link': 'https://www.darlinglace.com',
                         'fb_title': ("Liebst du Lingerie? Erhalte Dein BH Set ab 29,95 EUR!").encode('utf8'),
                         'fb_description': (
                         "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                             'utf8'), 'fb_description': (
            "Es ist ganz einfach - Wähle Dein wunderschönes BH Set aus und erhalte eine Online Passform-Beratung. Versand & Retoure sind umsonst!").encode(
                'utf8'), 'fb_image': 'https://www.darlinglace.com/static/overall_picture_bra.jpg', 'vorname': vorname,
                         'nachname': nachname, 'stadt': stadt, 'plz': plz, 'wishlist': wishlist, 'warenkorb': warenkorb,
                         'link_redirect': path, 'favicon': get_favicon(), 'brand_name': 'Darling Lace', 'VIP': VIP,
                         'title': "Anmelden | Darling Lace", 'bestellungen': define_bestellung(user, "all", c, "nein"),
                         'wishlist': wishlist, 'warenkorb': warenkorb, 'login': login, 'links': get_links(quiz)})
        return html
    else:
        return ""


@csrf_exempt
def send_email_support(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)

        von = request.GET.get('von')
        email = request.GET.get('email')
        betreff = request.GET.get('betreff')
        message = request.GET.get('message')
        creds = {
            'email': 'service@darlinglace.com',
            'token': 'oY8q9R9T4io7ZwQ1KdDktKwXgF3sWhMneMECjpL0',
            'subdomain': 'darlinglace'
        }
        zenpy_client = Zenpy(**creds)

        zenpy_client.tickets.create(
            Ticket(description=message, subject=betreff,
                   requester=User(name=von, email=email))
        )

        conn.close()
        return HttpResponse(json.dumps("email sent"), content_type='application/json')

    else:
        raise Http404


@csrf_exempt
def big_data_initial_input_detailed_page(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)

        stylecode = request.GET.get('stylecode')
        colorcode = request.GET.get('colorcode')
        windowwidth = request.GET.get('windowwidth')
        windowheight = request.GET.get('windowheight')

        x = str(request.session.session_key)
        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            userdaten = c.fetchall()
            for row in userdaten:
                user = row[11]
                facebookid = row[12]
                modelAB = row[47]
                sub_picture = row[48]

        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        Monat = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober",
                 "November", "Dezember"]
        now_date = str(now.day) + ". " + str(Monat[now.month - 1]) + " " + str(now.year)
        Y = now.year
        M = now.month
        D = now.day
        H = now.hour
        Mi = now.minute
        time = datetime.datetime.strptime(str(Y) + "-" + str(M) + "-" + str(D) + " " + str(H) + ":" + str(Mi),
                                          "%Y-%m-%d %H:%M")
        c.execute("""insert into Big_data_click_on_image values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (
        user, facebookid, modelAB, sub_picture, now_date, time, windowwidth, windowheight, stylecode, colorcode, "", "",
        "", "",))
        conn.commit()
        conn.close()
        return HttpResponse(json.dumps(""), content_type='application/json')

    else:
        raise Http404


@csrf_exempt
def big_data_farbe_click(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)

        stylecode = request.GET.get('stylecode')
        colorcode = request.GET.get('colorcode')
        pictureclicked = request.GET.get('pictureclicked')

        windowwidth = request.GET.get('windowwidth')
        windowheight = request.GET.get('windowheight')

        x = str(request.session.session_key)
        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            userdaten = c.fetchall()
            for row in userdaten:
                user = row[11]
                facebookid = row[12]
                modelAB = row[47]
                sub_picture = row[48]

        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        Monat = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober",
                 "November", "Dezember"]
        now_date = str(now.day) + ". " + str(Monat[now.month - 1]) + " " + str(now.year)
        Y = now.year
        M = now.month
        D = now.day
        H = now.hour
        Mi = now.minute
        time = datetime.datetime.strptime(str(Y) + "-" + str(M) + "-" + str(D) + " " + str(H) + ":" + str(Mi),
                                          "%Y-%m-%d %H:%M")

        c.execute("""insert into Big_data_click_on_image values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (
        user, facebookid, modelAB, sub_picture, now_date, time, windowwidth, windowheight, stylecode, colorcode,
        pictureclicked, "", "", "",))
        conn.commit()
        conn.close()
        return HttpResponse(json.dumps(""), content_type='application/json')

    else:
        raise Http404


@csrf_exempt
def big_data_picture_clicked(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)

        stylecode = request.GET.get('stylecode')
        colorcode = request.GET.get('colorcode')
        pictureclicked = request.GET.get('pictureclicked')

        windowwidth = request.GET.get('windowwidth')
        windowheight = request.GET.get('windowheight')

        x = str(request.session.session_key)
        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            userdaten = c.fetchall()
            for row in userdaten:
                user = row[11]
                facebookid = row[12]
                modelAB = row[47]
                sub_picture = row[48]

        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        Monat = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober",
                 "November", "Dezember"]
        now_date = str(now.day) + ". " + str(Monat[now.month - 1]) + " " + str(now.year)
        Y = now.year
        M = now.month
        D = now.day
        H = now.hour
        Mi = now.minute
        time = datetime.datetime.strptime(str(Y) + "-" + str(M) + "-" + str(D) + " " + str(H) + ":" + str(Mi),
                                          "%Y-%m-%d %H:%M")

        c.execute("""insert into Big_data_click_on_image values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (
        user, facebookid, modelAB, sub_picture, now_date, time, windowwidth, windowheight, stylecode, colorcode,
        pictureclicked, "", "", "",))
        conn.commit()
        conn.close()
        return HttpResponse(json.dumps(""), content_type='application/json')

    else:
        raise Http404


@csrf_exempt
def big_data_cart_put(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)

        stylecode = request.GET.get('stylecode')
        colorcode = request.GET.get('colorcode')
        putincart = request.GET.get('putincart')
        windowwidth = request.GET.get('windowwidth')
        windowheight = request.GET.get('windowheight')

        x = str(request.session.session_key)
        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            for row in c:
                user = row[11]
                facebookid = row[12]
                modelAB = row[47]
                sub_picture = row[48]

        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        Monat = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober",
                 "November", "Dezember"]
        now_date = str(now.day) + ". " + str(Monat[now.month - 1]) + " " + str(now.year)
        Y = now.year
        M = now.month
        D = now.day
        H = now.hour
        Mi = now.minute
        time = datetime.datetime.strptime(str(Y) + "-" + str(M) + "-" + str(D) + " " + str(H) + ":" + str(Mi),
                                          "%Y-%m-%d %H:%M")
        c.execute("""insert into Big_data_click_on_image values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (
        user, facebookid, modelAB, sub_picture, now_date, time, windowwidth, windowheight, stylecode, colorcode, "",
        putincart, "", "",))
        conn.commit()
        conn.close()
        return HttpResponse(json.dumps(""), content_type='application/json')

    else:
        raise Http404


@csrf_exempt
def big_data_wishlist_put(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)

        stylecode = request.GET.get('stylecode')
        colorcode = request.GET.get('colorcode')
        putinwishlist = request.GET.get('putinwishlist')
        windowwidth = request.GET.get('windowwidth')
        windowheight = request.GET.get('windowheight')

        x = str(request.session.session_key)
        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            userdaten = c.fetchall()
            for row in userdaten:
                user = row[11]
                facebookid = row[12]
                modelAB = row[47]
                sub_picture = row[48]

        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        Monat = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober",
                 "November", "Dezember"]
        now_date = str(now.day) + ". " + str(Monat[now.month - 1]) + " " + str(now.year)
        Y = now.year
        M = now.month
        D = now.day
        H = now.hour
        Mi = now.minute
        time = datetime.datetime.strptime(str(Y) + "-" + str(M) + "-" + str(D) + " " + str(H) + ":" + str(Mi),
                                          "%Y-%m-%d %H:%M")
        c.execute("""insert into Big_data_click_on_image values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (
        user, facebookid, modelAB, sub_picture, now_date, time, windowwidth, windowheight, stylecode, colorcode, "", "",
        putinwishlist, "",))
        conn.commit()
        conn.close()
        return HttpResponse(json.dumps(""), content_type='application/json')

    else:
        raise Http404


@csrf_exempt
def laenderinteresse(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)

        land = request.GET.get('land')

        x = str(request.session.session_key)
        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            userdaten = c.fetchall()
            for row in userdaten:
                email = row[0]

        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        Monat = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober",
                 "November", "Dezember"]
        now_date = str(now.day) + ". " + str(Monat[now.month - 1]) + " " + str(now.year)

        c.execute("""insert into laenderinteresse values (%s,%s,%s)""", (land, email, now_date,))
        conn.commit()

        conn.close()

        return HttpResponse(json.dumps(""), content_type='application/json')

    else:
        raise Http404


@csrf_exempt
def big_data_initial_input_main_page(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)

        windowwidth = request.GET.get('windowwidth')
        windowheight = request.GET.get('windowheight')

        x = str(request.session.session_key)
        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            userdaten = c.fetchall()
            for row in userdaten:
                user = row[11]
                facebookid = row[12]
                modelAB = row[47]
                sub_picture = row[48]

        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        Monat = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober",
                 "November", "Dezember"]
        now_date = str(now.day) + ". " + str(Monat[now.month - 1]) + " " + str(now.year)
        Y = now.year
        M = now.month
        D = now.day
        H = now.hour
        Mi = now.minute
        time = datetime.datetime.strptime(str(Y) + "-" + str(M) + "-" + str(D) + " " + str(H) + ":" + str(Mi),
                                          "%Y-%m-%d %H:%M")
        c.execute("""insert into Big_data_click_on_main_page values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (
        user, facebookid, modelAB, sub_picture, now_date, time, windowwidth, windowheight, "", "", "", "", "", "",))
        conn.commit()

        conn.close()
        return HttpResponse(json.dumps(""), content_type='application/json')

    else:
        raise Http404


@csrf_exempt
def big_data_wishlist_click_main_page(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)

        stylecode = request.GET.get('stylecode')
        colorcode = request.GET.get('colorcode')
        putinwishlist = request.GET.get('putinwishlist')
        position = request.GET.get('position')

        windowwidth = request.GET.get('windowwidth')
        windowheight = request.GET.get('windowheight')

        x = str(request.session.session_key)
        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            userdaten = c.fetchall()
            for row in userdaten:
                user = row[11]
                facebookid = row[12]
                modelAB = row[47]
                sub_picture = row[48]

        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        Monat = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober",
                 "November", "Dezember"]
        now_date = str(now.day) + ". " + str(Monat[now.month - 1]) + " " + str(now.year)
        Y = now.year
        M = now.month
        D = now.day
        H = now.hour
        Mi = now.minute
        time = datetime.datetime.strptime(str(Y) + "-" + str(M) + "-" + str(D) + " " + str(H) + ":" + str(Mi),
                                          "%Y-%m-%d %H:%M")
        c.execute("""insert into Big_data_click_on_main_page values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (
        user, facebookid, modelAB, sub_picture, now_date, time, windowwidth, windowheight, stylecode, colorcode,
        position, "", putinwishlist, "",))
        conn.commit()

        conn.close()

        return HttpResponse(json.dumps(""), content_type='application/json')

    else:
        raise Http404


@csrf_exempt
def big_data_filter_click_main_page(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)

        filter = request.GET.get('filter')

        windowwidth = request.GET.get('windowwidth')
        windowheight = request.GET.get('windowheight')

        x = str(request.session.session_key)
        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            userdaten = c.fetchall()
            for row in userdaten:
                user = row[11]
                facebookid = row[12]
                modelAB = row[47]
                sub_picture = row[48]

        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        Monat = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober",
                 "November", "Dezember"]
        now_date = str(now.day) + ". " + str(Monat[now.month - 1]) + " " + str(now.year)
        Y = now.year
        M = now.month
        D = now.day
        H = now.hour
        Mi = now.minute
        time = datetime.datetime.strptime(str(Y) + "-" + str(M) + "-" + str(D) + " " + str(H) + ":" + str(Mi),
                                          "%Y-%m-%d %H:%M")
        c.execute("""insert into Big_data_click_on_main_page values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (
        user, facebookid, modelAB, sub_picture, now_date, time, windowwidth, windowheight, "", "", "", filter, "", "",))
        conn.commit()

        conn.close()

        return HttpResponse(json.dumps(""), content_type='application/json')

    else:
        raise Http404


@csrf_exempt
def big_data_color_click_main_page(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)

        stylecode = request.GET.get('stylecode')
        colorcode = request.GET.get('colorcode')
        farbe = request.GET.get('farbe')
        position = request.GET.get('position')

        windowwidth = request.GET.get('windowwidth')
        windowheight = request.GET.get('windowheight')

        x = str(request.session.session_key)
        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            userdaten = c.fetchall()
            for row in userdaten:
                user = row[11]
                facebookid = row[12]
                modelAB = row[47]
                sub_picture = row[48]

                now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
                Monat = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober",
                         "November", "Dezember"]
                now_date = str(now.day) + ". " + str(Monat[now.month - 1]) + " " + str(now.year)
                Y = now.year
                M = now.month
                D = now.day
                H = now.hour
                Mi = now.minute
                time = datetime.datetime.strptime(str(Y) + "-" + str(M) + "-" + str(D) + " " + str(H) + ":" + str(Mi),
                                                  "%Y-%m-%d %H:%M")
                c.execute(
                    """insert into Big_data_click_on_main_page values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (
                    user, facebookid, modelAB, sub_picture, now_date, time, windowwidth, windowheight, stylecode,
                    colorcode, position, "", "", farbe,))
                conn.commit()

        conn.close()

        return HttpResponse(json.dumps(""), content_type='application/json')

    else:
        raise Http404


@csrf_exempt
def big_data_picture_click_main_page(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)

        stylecode = request.GET.get('stylecode')
        colorcode = request.GET.get('colorcode')
        position = request.GET.get('position')

        windowwidth = request.GET.get('windowwidth')
        windowheight = request.GET.get('windowheight')

        x = str(request.session.session_key)
        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            userdaten = c.fetchall()
            for row in userdaten:
                user = row[11]
                facebookid = row[12]
                modelAB = row[47]
                sub_picture = row[48]

        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        Monat = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober",
                 "November", "Dezember"]
        now_date = str(now.day) + ". " + str(Monat[now.month - 1]) + " " + str(now.year)
        Y = now.year
        M = now.month
        D = now.day
        H = now.hour
        Mi = now.minute
        time = datetime.datetime.strptime(str(Y) + "-" + str(M) + "-" + str(D) + " " + str(H) + ":" + str(Mi),
                                          "%Y-%m-%d %H:%M")
        c.execute("""insert into Big_data_click_on_main_page values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (
        user, facebookid, modelAB, sub_picture, now_date, time, windowwidth, windowheight, stylecode, colorcode,
        position, "", "", "",))
        conn.commit()

        conn.close()

        return HttpResponse(json.dumps(""), content_type='application/json')

    else:
        raise Http404


def adapt_showroom(user, style_name, percent):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database')
    c = conn.cursor(buffered=True)

    c.execute("""select * from lingerieselection """)
    for row in c:
        if row[0] == style_name:
            stil = row[19]
            color = row[35]
            shape = row[25]
            padding = row[30]

    showroom_stil = [[] for i in range(0)]
    showroom_color = [[] for i in range(0)]
    showroom_padding = [[] for i in range(0)]
    showroom_shape = [[] for i in range(0)]

    showroom_stil_names = [[] for i in range(0)]
    showroom_color_names = [[] for i in range(0)]
    showroom_padding_names = [[] for i in range(0)]
    showroom_shape_names = [[] for i in range(0)]

    c.execute("""select * from userdaten where gutscheincode=%s """, (user,))
    for row in c:

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

        i = 0
        stil_dominant = 0
        delta = 0
        teiler = 3
        while i <= 3:
            if showroom_stil_names[i] != stil:
                if row[27 + i] == 0:
                    teiler = max(teiler - 1, 1)
            i = i + 1
        i = 0
        while i <= 3:
            if (delta < min(max(0, row[27 + i] + percent), 100)):
                delta = min(max(0, row[27 + i] + percent), 100)
                stil_dominant = i

            if showroom_stil_names[i] == stil:
                showroom_stil.append(min(max(0, row[27 + i] + percent), 100))
            else:
                showroom_stil.append(min(max(0, row[27 + i] - percent / teiler), 100))
            i = i + 1

        i = 0
        color_dominant = 0
        delta = 0
        teiler = 3
        while i <= 3:
            if showroom_color_names[i] != color:
                if row[44 + i] == 0:
                    teiler = max(teiler - 1, 1)
            i = i + 1
        i = 0

        while i <= 3:
            if (delta < min(max(0, row[44 + i] + percent), 100)):
                delta = min(max(0, row[44 + i] + percent), 100)
                color_dominant = i
            if showroom_color_names[i] == color:
                showroom_color.append(min(max(0, row[44 + i] + percent), 100))
            else:
                showroom_color.append(min(max(0, row[44 + i] - percent / teiler), 100))
            i = i + 1

        i = 0
        padding_dominant = 0
        delta = 0
        teiler = 3
        while i <= 3:

            if showroom_padding_names[i] != padding:

                if row[38 + i] == 0:
                    teiler = max(teiler - 1, 1)
            i = i + 1
        i = 0

        while i <= 3:
            if (delta < min(max(0, row[39 + i] + percent), 100)):
                delta = min(max(0, row[39 + i] + percent), 100)
                padding_dominant = i
            if showroom_padding_names[i] == padding:
                showroom_padding.append(min(max(0, row[39 + i] + percent), 100))
            else:
                showroom_padding.append(min(max(0, row[39 + i] - percent / teiler), 100))
            i = i + 1

        i = 0
        padding_shape = 0
        delta = 0
        teiler = 4
        while i <= 4:
            if showroom_shape_names[i] != shape:
                if row[33 + i] == 0:
                    teiler = max(teiler - 1, 1)
            i = i + 1
        i = 0

        while i <= 4:
            if (delta < min(max(0, row[33 + i] + percent), 100)):
                delta = min(max(0, row[33 + i] + percent), 100)
                shape_dominant = i
            if showroom_shape_names[i] == shape:
                showroom_shape.append(min(max(0, row[33 + i] + percent), 100))
            else:
                showroom_shape.append(min(max(0, row[33 + i] - percent / teiler), 100))
            i = i + 1

    c.execute(
        """update userdaten set dominantfactorstyle=%s, sexy=%s, hotromance=%s, classiccute=%s, playful=%s where gutscheincode=%s""",
        (showroom_stil_names[stil_dominant], showroom_stil[0], showroom_stil[1], showroom_stil[2], showroom_stil[3],
         user,))
    c.execute(
        """update userdaten set dominantfactorshape=%s, demi=%s, balconette=%s, bralette=%s, plunge=%s, fullcoverage=%s where gutscheincode=%s""",
        (showroom_shape_names[shape_dominant], showroom_shape[0], showroom_shape[1], showroom_shape[2],
         showroom_shape[3], showroom_shape[4], user,))
    c.execute(
        """update userdaten set dominantfactorpadding=%s,unlined=%s, lightlylined=%s, padded=%s, 2cups=%s where gutscheincode=%s""",
        (showroom_padding_names[padding_dominant], showroom_padding[0], showroom_padding[1], showroom_padding[2],
         showroom_padding[3], user,))
    c.execute(
        """update userdaten set dominantfactorcolors=%s,neutrals=%s, bright=%s, deep=%s, printedpattern=%s where gutscheincode=%s""",
        (showroom_color_names[color_dominant], showroom_color[0], showroom_color[1], showroom_color[2],
         showroom_color[3], user,))
    conn.commit()

    generate_showroom(user, c, conn)


@csrf_exempt
def onleave_message_abrufen(request):
    if request.is_ajax() and request.GET:
        conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                       user='maxfischer2',
                                       password='okano1988', database='maxfischer2database')
        c = conn.cursor(buffered=True)

        x = str(request.session.session_key)

        feedback = "ok"
        if x != "None":
            c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
            userdaten = c.fetchall()
            for row in userdaten:
                if row[0] != "" and row[12] != "":
                    feedback = "not ok"
        conn.close()
        return HttpResponse(json.dumps(feedback), content_type='application/json')

    else:
        raise Http404


def log_out_do_it(x, c, conn):
    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        userdaten = c.fetchall()
        for row in userdaten:
            c.execute("""update userdaten set lastsessionid=%s where gutscheincode=%s""", ("", row[11],))
            conn.commit()


def log_out(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database')
    c = conn.cursor(buffered=True)

    x = str(request.session.session_key)

    c.execute("""update userdaten set lastsessionid=%s where lastsessionid=%s""", ("", x,))
    conn.commit()

    print(request.path + ",create_new_request," + x)
    request.session.create()
    x = str(request.session.session_key)
    print x
    create_user(x, c, conn)

    conn.close()

    return HttpResponseRedirect("/")


def perform_security_check(request):
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database')
    c = conn.cursor(buffered=True)

    x = str(request.session.session_key)
    zaehler = 0
    if x != "None":
        c.execute("""select * from userdaten where gutscheincode=%s """, (get_userid_from_session_id(c, x),))
        userdaten = c.fetchall()
        for row in userdaten:
            zaehler = zaehler + 1


def check_availability(c, conn):
    c.execute("""select * from lingerieselection """)

    lingerieselection = c.fetchall()

    for row in lingerieselection:

        menge_bh = 0
        menge_panty = 0
        c.execute("""select * from %s """ % ("stylecode"))
        for row_2 in c:
            if row[13] == row_2[2] and row[12] == row_2[1]:
                if row_2[0] == "BH":
                    menge_bh = menge_bh + int(row_2[4]) - int(row_2[5])
                else:
                    menge_panty = menge_panty + int(row_2[4]) - int(row_2[5])

        if menge_bh > 0 and menge_panty > 0:
            c.execute("""update lingerieselection set active=%s where name=%s""", ("yes", row[0],))
        else:
            c.execute("""update lingerieselection set active=%s where name=%s""", ("no", row[0],))

    conn.commit()


def get_time_stamp_now():
    now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
    Y = now.year
    M = now.month
    D = now.day
    H = now.hour
    Mi = now.minute
    d1 = datetime.datetime.strptime(str(Y) + "-" + str(M) + "-" + str(D) + " " + str(H) + ":" + str(Mi),
                                    "%Y-%m-%d %H:%M")

    return d1


def get_date_stamp_now():
    now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))

    Monat = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November",
             "Dezember"]
    d1 = str(now.day) + ". " + Monat[(now.month) - 1] + " " + str(now.year)

    return d1


def freimengen_in_warenkorb_aktualisieren():
    conn.close()
    d.close()

    return q


def select_lieferdatum(days_):
    now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
    i = 0
    while (i <= days_ - 1):
        future = now + datetime.timedelta(days=i)
        TagInWoche = future.weekday()

        if (TagInWoche == 5 or TagInWoche == 6):
            days_ = days_ + 1
        i = i + 1

    Monat = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November",
             "Dezember"]
    future_date = str(future.day) + ". " + str(Monat[future.month - 1]) + " " + str(future.year)
    return future_date


def ausgewaehlten_tag_abrufen(ausgewaehlter_tag):
    Wochentag = ["MO", "DI", "MI", "DO", "FR", "SA", "SO"]
    Monat = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November",
             "Dezember"]

    datum_output = ""
    ausgewaehlter_tag = int(ausgewaehlter_tag)
    i = 0
    wochentag = -1

    now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))

    while (i <= 10):
        future = now + datetime.timedelta(days=i)
        TagInWoche = future.weekday()

        if (TagInWoche == 5 or TagInWoche == 6):
            datum_output = datum_output + "Wochenende" + ","
            datum_output = datum_output + str(future.day) + ","
            datum_output = datum_output + str(future.weekday()) + ","
            datum_output = datum_output + str(future.month - 1) + ","
            datum_output = datum_output + str(future.year) + ","
            datum_output = datum_output + "0"

            if (i == 0):
                DatumZukunft_ = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
                DatumZukunft_ = DatumZukunft_ - datetime.timedelta(days=1)
                datum_output = datum_output + "," + str(DatumZukunft_.weekday())
            datum_output = datum_output + ";"


        else:
            datum_output = datum_output + "Wochentag" + ","
            datum_output = datum_output + str(future.day) + ","
            datum_output = datum_output + str(future.weekday()) + ","
            datum_output = datum_output + str(future.month - 1) + ","
            datum_output = datum_output + str(future.year) + ","
            wochentag = wochentag + 1;

            if (wochentag == ausgewaehlter_tag):
                datum_output = datum_output + "1;"
                output = []
                output.append(str(future.day) + ". " + Monat[future.month - 1] + " " + str(future.year))
            else:
                datum_output = datum_output + "0;"
        i = i + 1

    return output


def ausgewaehlten_wochentag_abrufen(ausgewaehlter_tag):
    Wochentag = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
    Monat = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November",
             "Dezember"]

    datum_output = ""
    ausgewaehlter_tag = int(ausgewaehlter_tag)
    i = 0
    wochentag = -1

    now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))

    while (i <= 10):
        future = now + datetime.timedelta(days=i)
        TagInWoche = future.weekday()

        if (TagInWoche == 5 or TagInWoche == 6):
            datum_output = datum_output + "Wochenende" + ","
            datum_output = datum_output + str(future.day) + ","
            datum_output = datum_output + str(future.weekday()) + ","
            datum_output = datum_output + str(future.month - 1) + ","
            datum_output = datum_output + str(future.year) + ","
            datum_output = datum_output + "0"

            if (i == 0):
                DatumZukunft_ = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
                DatumZukunft_ = DatumZukunft_ - datetime.timedelta(days=1)
                datum_output = datum_output + "," + str(DatumZukunft_.weekday())
            datum_output = datum_output + ";"


        else:
            datum_output = datum_output + "Wochentag" + ","
            datum_output = datum_output + str(future.day) + ","
            datum_output = datum_output + str(future.weekday()) + ","
            datum_output = datum_output + str(future.month - 1) + ","
            datum_output = datum_output + str(future.year) + ","
            wochentag = wochentag + 1;

            if (wochentag == ausgewaehlter_tag):
                datum_output = datum_output + "1;"
                output = Wochentag[future.weekday()]
            else:
                datum_output = datum_output + "0;"
        i = i + 1

    return output


def check_month_VIP(user_id, c, VIP_member_since):
    now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
    c.execute("""select * from VIP_model_store_credit where gutscheincode=%s """, (user_id,))
    VIP_model_store_credit = c.fetchall()
    already_skipped = "false"
    VIP_date = VIP_member_since.split(".")
    for row in VIP_model_store_credit:
        neukunde = "false"
        print VIP_date[1] + "==" + str(now.month - 1) + "and" + VIP_date[0] + "==" + str(now.year)
        if VIP_date[1] == str(now.month - 1) and VIP_date[0] == str(now.year):
            neukunde = "true"
        print("neukunde")
        print(neukunde)
        if neukunde == "false":
            if now.day >= 1 and now.day <= 10:
                print VIP_date[1] + "==" + str(now.month - 1) + "and" + VIP_date[0] + "==" + str(now.year) + "and (" + \
                      row[6] + "==true or " + row[4] + "!="
                if VIP_date[1] == str(now.month - 1) and VIP_date[0] == str(now.year) and (
                        row[6] == "true" or row[4] != ""):
                    already_skipped = "true"
            else:
                already_skipped = "true"
        else:
            already_skipped = "true"

    print "already_skipped"
    return already_skipped


def delta_days(date_VIP, date_now):
    date_now_format = datetime.datetime.strptime(date_now, "%Y%m%d").date()
    date_VIP_format = datetime.datetime.strptime(date_VIP, "%Y%m%d").date()
    delta = date_now_format - date_VIP_format


def check_rueckerstattung_month_VIP(c, code):
    c.execute("""select * from VIP_model_store_credit where gutscheincode=%s """, (code,))
    VIP_model_store_credit = c.fetchall()
    used_storecredit = 0
    granted_storecredit_total = 0
    payback = 0
    for row_2 in VIP_model_store_credit:
        if row_2[3] > 0:
            granted_storecredit_total = granted_storecredit_total + row_2[3]
        if row_2[3] < 0:
            used_storecredit = used_storecredit + row_2[3]

    payback = granted_storecredit_total + used_storecredit

    return payback


def pursue_VIP_payments(request):
    now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
    current_time = datetime.datetime.now(pytz.timezone('Europe/Berlin')).time()

    time_ = str(current_time)

    time__ = time_.replace(":", "")
    time__ = time__.replace(".", "")

    date_ = str(now.year) + "." + str((now.month) - 1) + "." + str(now.day)
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',
                                   user='maxfischer2',
                                   password='okano1988', database='maxfischer2database')
    c = conn.cursor(buffered=True)

    if now.day >= 2:
        c.execute("""select * from userdaten """)
        userdaten = c.fetchall()
        feedback = ""
        for row in userdaten:
            if row[22] == "VIP" and row[23] == "true":
                c.execute("""select * from VIP_model_store_credit where gutscheincode=%s """, (row[11],))
                VIP_model_store_credit = c.fetchall()
                abgebucht = "false"

                for row_2 in VIP_model_store_credit:
                    date_VIP = row_2[0].split(".")
                    if date_VIP[1] == str(now.month - 1) and date_VIP[0] == str(now.year) and row_2[3] != 0 and row_2[
                        4] != "":
                        abgebucht = "true"
                if abgebucht == "false" and check_month_VIP(row[11], c, row[24]) == "true":

                    transaction_id = credit_card_add_new_transaction(row[56], 2995, "EUR",
                                                                     "Darling Lace VIP Store Credit: " + str(
                                                                         now.month) + "/" + str(now.year), row[50])
                    bezahlt = ""
                    while bezahlt == "":
                        feedback_from_transaction = check_transaction(transaction_id)

                        if feedback_from_transaction == "true":
                            bezahlt = "true"
                            c.execute("""insert into %s values (%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)""" % (
                            "VIP_model_store_credit"), (
                                      date_, date_, time__, 29.95, "", "no", "", 0, 0, transaction_id.id,
                                      date_.replace(".", ""), row[11]))
                            conn.commit()


