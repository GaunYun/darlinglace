
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
#c.execute("""insert into `test_table` value (2,'asddsf')""")
import sched, time




def create_matching_table_stammdaten_stylecodes():
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database', charset='utf8')
    c = conn.cursor(buffered=True)







    cup_table = {'AA':0,
           'A':1,
           'B':2,
           'C':3,
           'D':4,
           'E':5,
           'F':6,
           'G':7,
           
        }


    band_table = {'65':0,
           '70':1,
           '75':2,
           '80':3,
           '85':4,
           '90':5,
           '95':6,
            
           
        }




    style_table_panty = {'Bikini':0,
           'Hipster':1,
           'Boyshort':2,
           'Thong':3,
           
        }


    size_table_panty = {
            'XXS':0,
            'XS':1,
            'S':2,
           'M':3,
           'L':4,
           'XL':5,
           'XXL':6,

            
           
        }
        

    c.execute ("""select * from lingerieselection ORDER BY position ASC""")
    lingerieselection=c.fetchall()
    for row in lingerieselection:
        if row[7]=="yes":
            list=[]
            i=0
            while i<=87:
                list.append("")
                i=i+1
            c.execute ("""select * from stylecode where stylecode=%s and color=%s""",(row[12],row[13],))
            stylecode_data=c.fetchall()
            for row_2 in stylecode_data:
                
                menge=int(row_2[4])-int(row_2[5])
                if menge>0:
                    if row[8]=="lingerie":
                        if row_2[0]=="BH":
                            if row_2[3]=="Bralette S":
                                list[56]="1"
                            else:
                                if row_2[3]=="Bralette M":
                                    list[57]="1"
                                else:
                                    if row_2[3]=="Bralette L":
                                        list[58]="1"
                                    else:
                                        if row_2[3]=="Bralette XL":
                                            list[59]="1"
                                        else:
                        
                                            band=row_2[3][:2]
                                            cup=row_2[3][2:]

                                            cup_number=cup_table[cup]
                                            band_number=band_table[band]



                                            list[band_number*8+cup_number]="1"

                    else:
                        if row_2[0]=="panties":

                            panty_type=row_2[3].split(" ")
                            type_number=style_table_panty[panty_type[0]]
                            size_number=size_table_panty[panty_type[1]]




                            list[type_number*7+size_number+60]="1"

            c.execute("""update matching_table_stammdaten_stylecodes set 65AA=%s,65A=%s,65B=%s,65C=%s,65D=%s,65E=%s,65F=%s,65G=%s,70AA=%s,70A=%s,70B=%s,70C=%s,70D=%s,70E=%s,70F=%s,70G=%s,75AA=%s,75A=%s,75B=%s,75C=%s,75D=%s,75E=%s,75F=%s,75G=%s,80AA=%s,80A=%s,80B=%s,80C=%s,80D=%s,80E=%s,80F=%s,80G=%s,85AA=%s,85A=%s,85B=%s,85C=%s,85D=%s,85E=%s,85F=%s,85G=%s,90AA=%s,90A=%s,90B=%s,90C=%s,90D=%s,90E=%s,90F=%s,90G=%s,95AA=%s,95A=%s,95B=%s,95C=%s,95D=%s,95E=%s,95F=%s,95G=%s,BraletteS=%s,BraletteM=%s,BraletteL=%s,BraletteXL=%s,BikiniXXS=%s,BikiniXS=%s,BikiniS=%s,BikiniM=%s,BikiniL=%s,BikiniXl=%s,BikiniXXL=%s,HipsterXXS=%s,HipsterXS=%s,HipsterS=%s,HipsterM=%s,HipsterL=%s,HipsterXl=%s,HipsterXXL=%s,BoyshortXXS=%s,BoyshortXS=%s,BoyshortS=%s,BoyshortM=%s,BoyshortL=%s,BoyshortXl=%s,BoyshortXXL=%s,ThongXXS=%s,ThongXS=%s,ThongS=%s,ThongM=%s,ThongL=%s,ThongXl=%s,ThongXXL=%s where stylecode=%s and colorcode=%s and productgroup=%s and pantytype=%s""",(list[0],list[1],list[2],list[3],list[4],list[5],list[6],list[7],list[8],list[9],list[10],list[11],list[12],list[13],list[14],list[15],list[16],list[17],list[18],list[19],list[20],list[21],list[22],list[23],list[24],list[25],list[26],list[27],list[28],list[29],list[30],list[31],list[32],list[33],list[34],list[35],list[36],list[37],list[38],list[39],list[40],list[41],list[42],list[43],list[44],list[45],list[46],list[47],list[48],list[49],list[50],list[51],list[52],list[53],list[54],list[55],list[56],list[57],list[58],list[59],list[60],list[61],list[62],list[63],list[64],list[65],list[66],list[67],list[68],list[69],list[70],list[71],list[72],list[73],list[74],list[75],list[76],list[77],list[78],list[79],list[80],list[81],list[82],list[83],list[84],list[85],list[86],list[87],row[12],row[13],row[8],row[2],))

     
    conn.commit()


def generate_standard_product_library():
    conn = mysql.connector.Connect(host='aa1tmrdkp2c8625.crplnx7dr6br.eu-central-1.rds.amazonaws.com',user='maxfischer2',\
                                password='okano1988',database='maxfischer2database', charset='utf8')
    c = conn.cursor(buffered=True)






    lingerie_offerings_0_0_lingerie=get_lingerie_selection_filter("lingerie","","","","","","","","","","","","","",0,0,c)
    lingerie_offerings_0_1_lingerie=get_lingerie_selection_filter("lingerie","","","","","","","","","","","","","",0,1,c)
    lingerie_offerings_0_2_lingerie=get_lingerie_selection_filter("lingerie","","","","","","","","","","","","","",0,2,c)

    lingerie_offerings_1_0_lingerie=get_lingerie_selection_filter("lingerie","","","","","","","","","","","","","",1,0,c)
    lingerie_offerings_1_1_lingerie=get_lingerie_selection_filter("lingerie","","","","","","","","","","","","","",1,1,c)
    lingerie_offerings_1_2_lingerie=get_lingerie_selection_filter("lingerie","","","","","","","","","","","","","",1,2,c)

    colors_lingerie=get_other_colors("","","lingerie",c)
    filter_lingerie=load_style_filter("","","","","","BH Sets","","","","",c)


    lingerie_offerings_0_0_panties=get_lingerie_selection_filter("panties","","","","","","","","","","","","","",0,0,c)
    lingerie_offerings_0_1_panties=get_lingerie_selection_filter("panties","","","","","","","","","","","","","",0,1,c)
    lingerie_offerings_0_2_panties=get_lingerie_selection_filter("panties","","","","","","","","","","","","","",0,2,c)

    lingerie_offerings_1_0_panties=get_lingerie_selection_filter("panties","","","","","","","","","","","","","",1,0,c)
    lingerie_offerings_1_1_panties=get_lingerie_selection_filter("panties","","","","","","","","","","","","","",1,1,c)
    lingerie_offerings_1_2_panties=get_lingerie_selection_filter("panties","","","","","","","","","","","","","",1,2,c)

    colors_panties=get_other_colors("","","panties",c)

    filter_panties=load_style_filter("","","","","","Slips","","","","",c)

    c.execute("""update standard_product_library set lingerieselection=%s,colors=%s,filter=%s where productgroup=%s and modelAB=%s and subpicture=%s""",(lingerie_offerings_0_0_lingerie,colors_lingerie,filter_lingerie,"lingerie",0,0,))
    c.execute("""update standard_product_library set lingerieselection=%s,colors=%s,filter=%s where productgroup=%s and modelAB=%s and subpicture=%s""",(lingerie_offerings_0_1_lingerie,colors_lingerie,filter_lingerie,"lingerie",0,1,))
    c.execute("""update standard_product_library set lingerieselection=%s,colors=%s,filter=%s where productgroup=%s and modelAB=%s and subpicture=%s""",(lingerie_offerings_0_2_lingerie,colors_lingerie,filter_lingerie,"lingerie",0,2,))
    c.execute("""update standard_product_library set lingerieselection=%s,colors=%s,filter=%s where productgroup=%s and modelAB=%s and subpicture=%s""",(lingerie_offerings_1_0_lingerie,colors_lingerie,filter_lingerie,"lingerie",1,0,))
    c.execute("""update standard_product_library set lingerieselection=%s,colors=%s,filter=%s where productgroup=%s and modelAB=%s and subpicture=%s""",(lingerie_offerings_1_1_lingerie,colors_lingerie,filter_lingerie,"lingerie",1,1,))
    c.execute("""update standard_product_library set lingerieselection=%s,colors=%s,filter=%s where productgroup=%s and modelAB=%s and subpicture=%s""",(lingerie_offerings_1_2_lingerie,colors_lingerie,filter_lingerie,"lingerie",1,2,))



    c.execute("""update standard_product_library set lingerieselection=%s,colors=%s,filter=%s where productgroup=%s and modelAB=%s and subpicture=%s""",(lingerie_offerings_0_0_panties,colors_panties,filter_panties,"panties",0,0,))
    c.execute("""update standard_product_library set lingerieselection=%s,colors=%s,filter=%s where productgroup=%s and modelAB=%s and subpicture=%s""",(lingerie_offerings_0_1_panties,colors_panties,filter_panties,"panties",0,1,))
    c.execute("""update standard_product_library set lingerieselection=%s,colors=%s,filter=%s where productgroup=%s and modelAB=%s and subpicture=%s""",(lingerie_offerings_0_2_panties,colors_panties,filter_panties,"panties",0,2,))
    c.execute("""update standard_product_library set lingerieselection=%s,colors=%s,filter=%s where productgroup=%s and modelAB=%s and subpicture=%s""",(lingerie_offerings_1_0_panties,colors_panties,filter_panties,"panties",1,0,))
    c.execute("""update standard_product_library set lingerieselection=%s,colors=%s,filter=%s where productgroup=%s and modelAB=%s and subpicture=%s""",(lingerie_offerings_1_1_panties,colors_panties,filter_panties,"panties",1,1,))
    c.execute("""update standard_product_library set lingerieselection=%s,colors=%s,filter=%s where productgroup=%s and modelAB=%s and subpicture=%s""",(lingerie_offerings_1_2_panties,colors_panties,filter_panties,"panties",1,2,))


    
    conn.commit()


def get_lingerie_selection_filter(group1,group2,group3,color,size,user,name,day,month,year,filter_style,filter_color,filter_padding,filter_size,modelAB,sub_picture,c):
    lingerie = []


            
    class Lingerie(object):
        def __init__(self,name,sizerange,pic,priceregular,pricesubscription,description,details,active,productgroup,wishlist,descriptionshort,stylecode,colorcode,position,stylegroup,link,stylegroupcode):
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
            self.stylegroup=stylegroup
            self.link=link
            self.stylegroupcode=stylegroupcode



    styles = [[] for i in range(13)]
    color = [[] for i in range(15)]
    padding = [[] for i in range(4)]
    sizes= [[] for i in range(90)]


    if group1!="panties":
        i=0
        filter_style_index=-1
        c.execute ("""select * from style """)
        for row in c:
            if row[0]==filter_style:
                filter_style_index=i
            i=i+1
    else:
        i=0
        filter_style_index=-1
        c.execute ("""select * from stylepanty """)
        for row in c:
            if row[0]==filter_style:
                filter_style_index=i
            i=i+1
            

 
 
    i=0
    filter_color_index=-1
    c.execute ("""select * from color """)
    for row in c:
        if row[0]==filter_color:
            filter_color_index=row[1]
        i=i+1
 
    i=0
    filter_padding_index=-1
    c.execute ("""select * from padding """)
    for row in c:
        if row[0]==filter_padding:
            filter_padding_index=i

        i=i+1
 
 




    c.execute ("""select * from lingerieselection ORDER BY position ASC""")

    lingerieselection=c.fetchall()


    for row in lingerieselection:
        link=link_name_bestimmen(row[8])
        stylegroup=get_main_style_group(row[21],row[22],row[23],row[24])
        if row[7]=="yes":
            if name=="":

                if filter_style=="" and filter_color=="" and filter_padding=="" and filter_size=="":

                    if row[8]==group1 or row[8]==group2 or row[8]==group3:

                        if row[14]=="true":

                            priceregular=row[3]-row[13]
                            pricesubscription=row[4]-row[13]
                        else:
                            priceregular=row[3]
                            pricesubscription=row[4]
                        print row[0]


                        if name=="":
                            details=""
                            description=""
                        else:
                            description=row[5]
                            details=row[6]

                            
                        lingerie.append(Lingerie(row[0],row[1],get_pictures_from_consolidated_table(c,row[12],row[13],modelAB,sub_picture,row[2],"all","small"),priceregular,pricesubscription,description,details,row[7],row[8],"",row[9],row[12],row[13],row[51],stylegroup,link,row[57],))
                    else:
                        if group1=="Dein Showroom" and row[8]=="lingerie":
                            c.execute ("""select * from showroom where gutscheincode=%s """,(user,))

                            showroom_data=c.fetchall()

                            for row_2 in showroom_data:


                                if row_2[0]==row[12] and row_2[1]==row[13] and row_2[2]==day and row_2[3]==month and row_2[4]==year:                          
                                    if row[14]=="true":
                                        priceregular=row[3]-row[14]
                                        pricesubscription=row[4]-row[14]
                                    else:
                                        priceregular=row[3]
                                        pricesubscription=row[4]


                                    if name=="":
                                        details=""
                                        description=""
                                    else:
                                        description=row[5]
                                        details=row[6]


                            
                                    lingerie.append(Lingerie(row[0],row[1],get_pictures_from_consolidated_table(c,row[12],row[13],modelAB,sub_picture,row[2],"all","small"),priceregular,pricesubscription,description,details,row[7],row[8],"",row[9],row[12],row[13],row[51],stylegroup,link,row[57],))
                        else:
                            
                            if group1=="Wunschliste":


                                c.execute ("""select * from wishlist where gutscheincode=%s """,(user,))

                                wishlist_data=c.fetchall()


                                for row_2 in wishlist_data:

                                    if row_2[0]==row[12] and row_2[1]==row[13] and row[8]==row_2[3]:

                                        if row[14]=="true":
                                            priceregular=row[3]-row[14]
                                            pricesubscription=row[4]-row[14]
                                        else:
                                            priceregular=row[3]
                                            pricesubscription=row[4]



                                        if name=="":
                                            details=""
                                            description=""
                                        else:
                                            description=row[5]
                                            details=row[6]


                                        
                                        lingerie.append(Lingerie(row[0],row[1],get_pictures_from_consolidated_table(c,row[12],row[13],modelAB,sub_picture,row[2],"all","small"),priceregular,pricesubscription,description,details,row[7],row[8],"",row[9],row[12],row[13],row[51],stylegroup,link,row[57],))

                                            
                                    
                else:

                    
                    
                    if row[8]==group1 or row[8]==group2 or row[8]==group3:

                        size_check="not ok"
                        if filter_size!="":
                            size_check=check_quantities_of_style(c,row[12],row[13],filter_size,group1,row[2])
                        else:
                            size_check="ok"

                        if size_check=="ok":
                            if group1=="lingerie":
                                if filter_style_index>4:
                                    zaehler=filter_style_index+5
                                else:
                                    zaehler=filter_style_index
                                if (row[20+zaehler]=="x" or filter_style_index==-1)  and (row[50]==filter_color_index or filter_color_index==-1) and (row[40+filter_padding_index]=="x" or filter_padding_index==-1):
                                    if row[15]=="true":
                                        priceregular=row[3]-row[14]
                                        pricesubscription=row[4]-row[14]
                                    else:
                                        priceregular=row[3]
                                        pricesubscription=row[4]
                                    lingerie.append(Lingerie(row[0],row[1],get_pictures_from_consolidated_table(c,row[12],row[13],modelAB,sub_picture,row[2],"all","small"),priceregular,pricesubscription,row[5],row[6],row[7],row[8],"",row[9],row[12],row[13],row[51],stylegroup,link,row[57],))
                            else:
                                if (row[25+filter_style_index]=="x" or filter_style_index==-1)  and (row[50]==filter_color_index or filter_color_index==-1):
                                    if row[15]=="true":
                                        priceregular=row[3]-row[14]
                                        pricesubscription=row[4]-row[14]
                                    else:
                                        priceregular=row[3]
                                        pricesubscription=row[4]


                                    if name=="":
                                        details=""
                                        description=""
                                    else:
                                        description=row[5]
                                        details=row[6]


                                            
                                    lingerie.append(Lingerie(row[0],row[1],get_pictures_from_consolidated_table(c,row[12],row[13],modelAB,sub_picture,row[2],"all","small"),priceregular,pricesubscription,description,details,row[7],row[8],"",row[9],row[12],row[13],row[51],stylegroup,link,row[57],))

                            

 
                                    
            else:
                if row[0]==name:
                    if row[8]==group1 or row[8]==group2 or row[8]==group3:
                        if row[14]=="true":
                            priceregular=row[3]-row[13]
                            pricesubscription=row[4]-row[13]
                        else:
                            priceregular=row[3]
                            pricesubscription=row[4]




                        if name=="":
                            details=""
                            description=""
                        else:
                            description=row[5]
                            details=row[6]
                        lingerie.append(Lingerie(row[0],row[1],get_pictures_from_consolidated_table(c,row[12],row[13],modelAB,sub_picture,row[2],"all","big"),priceregular,pricesubscription,description,details,row[7],row[8],"",row[9],row[12],row[13],row[51],stylegroup,link,row[57],))


    
    json_string = json.dumps([Lingerie.__dict__ for Lingerie in lingerie])
    

    return json_string


def get_main_style_group(bralette,plunge,balconette,fullcup):
    stylegroup=""

    if plunge=="x":
        stylegroup="Plunge"
    if balconette=="x":
        stylegroup="Balconette"
    if bralette=="x":
        stylegroup="Bralette"
    if fullcup=="x":
        stylegroup="Full Cup"


    return stylegroup


def link_name_bestimmen(group):
    links = {"lingerie":"BH Sets" ,
           "panties":"Slips",
           "no":"Dein Showroom" ,
#           "VIP Box" : "no",

          "Geschenkkarten":"Geschenkkarten" ,
          "BH_Box":"BH Box" ,

             0:"",
            }

    return links[group]


def get_pictures_from_consolidated_table(c,stylecode,colorcode,modelAB,sub_picture,pantytype,firstorall,bigorsmall):


    
    c.execute ("""select * from consolidated_picturelibrary where modelAB=%s and subpicture=%s and stylecode=%s and colorcode=%s and firtorall=%s and bigorsmall=%s """,(modelAB,sub_picture,stylecode,colorcode,firstorall,bigorsmall,))

    consolidated_picturelibrary=c.fetchall()
    picture=""
    for row in consolidated_picturelibrary:
        picture=row[6]
    return picture


def get_other_colors(style,name,group1,c):
    lingerie = []
            
    class Lingerie(object):
        def __init__(self,style,colorcode,detaildatabase,pic,name,stylegroupcode):
            self.style=style
            self.colorcode=colorcode
            self.detaildatabase=detaildatabase
            self.pic=pic
            self.name=name
            self.stylegroupcode=stylegroupcode
            

    



    print("get_other_colors")


    

    if name!="":
        c.execute ("""select * from lingerieselection where active=%s and productgroup=%s""",("yes",group1))

        lingerieselection=c.fetchall()
        for row in lingerieselection:
            if row[0]==name:
                if group1=="lingerie":
                    stylegroupcode=row[57]
                else:
                    stylegroupcode=row[57]
                

                c.execute ("""select * from lingerieselection where active=%s and productgroup=%s""",("yes",group1))
                lingerieselection_2=c.fetchall()
                
                for row_2 in lingerieselection_2:
                    if group1=="lingerie":
                        if row_2[57]==stylegroupcode:
                            
                            lingerie.append(Lingerie(row_2[12],row_2[13],row_2[0],row_2[55],row_2[0],stylegroupcode,))
                    else:
                        if group1=="panties":
                            if row_2[57]==stylegroupcode:
                                lingerie.append(Lingerie(row_2[12],row_2[13],row_2[0],row_2[55],row_2[0],stylegroupcode,))

    else:
        if group1!="":

            c.execute ("""select * from lingerieselection where productgroup=%s and active=%s """,(group1,"yes"))
            lingerieselection=c.fetchall()

            for row in lingerieselection:
                existiert="nein"
                stylegroupcode=row[57]
        
                c.execute ("""select * from lingerieselection where productgroup=%s and active=%s """,(group1,"yes"))
                lingerieselection_2=c.fetchall()

                for row_2 in lingerieselection_2:
                    if row_2[57]==stylegroupcode and existiert=="nein" and row_2[0]==row[0]:
                        lingerie.append(Lingerie(row_2[12],row_2[13],row_2[0],row_2[55],row_2[0],stylegroupcode,))
                        existiert="ja"

    json_string = json.dumps([Lingerie.__dict__ for Lingerie in lingerie])


    return json_string


def load_style_filter(filter_style,filter_color,filter_size,click_last,filter_padding,link,user,day,month,year,c):
    reload(sys)
    sys.setdefaultencoding("ISO-8859-1")

    filter_ = []
 
 
           
    class Filter(object):
        def __init__(self,group,name,show,selected):
            self.group=group
            self.name=name
            self.show=show
            self.selected=selected
 

   
    print link

    if link=="Slips":
        link="panties"
    
 
    list=get_styles(filter_style,filter_color,filter_size,filter_padding,"",0,link,user,day,month,year,c)

    print "load_style_filter"

    styles=list[0][0]
    color=list[1][0]
    padding=list[2][0]
    sizes=list[3][0]



    if link!="panties":
        i=0
        while i<=12:
            if styles[i][1]==1:
                if styles[i][0]==filter_style:
                    filter_.append(Filter("Styles",styles[i][0],"true","true"))
                else:
                    filter_.append(Filter("Styles",styles[i][0],"true","false"))
            else:
                filter_.append(Filter("Styles",styles[i][0],"false","false"))
            i=i+1
     
        i=0
        while i<=6:
            if color[i][1]==1:
                if color[i][0]==filter_color:
                    filter_.append(Filter("Color",color[i][0],"true","true"))
                else:
                    filter_.append(Filter("Color",color[i][0],"true","false"))
            else:
                filter_.append(Filter("Color",color[i][0],"false","false"))
            i=i+1
     
        i=0
        while i<=3:
            if padding[i][1]==1:
                if padding[i][0]==filter_padding:
                    filter_.append(Filter("Padding",padding[i][0],"true","true"))
                else:
                    filter_.append(Filter("Padding",padding[i][0],"true","false"))
            else:
                filter_.append(Filter("Padding",padding[i][0],"false","false"))
            i=i+1
     

     
     
        i=0   
        while i<=59:
            if sizes[i][1]==1:
                if sizes[i][0]==filter_size:
                    filter_.append(Filter("Sizes",sizes[i][0],"true","true"))
                else:
                    filter_.append(Filter("Sizes",sizes[i][0],"true","false"))    
            else:
                filter_.append(Filter("Sizes",sizes[i][0],"false","false"))
            i=i+1
    else:
        print "load_style_filter geht los"
        i=0
        while i<=4:
            if styles[i][1]==1:
                if styles[i][0]==filter_style:
                    filter_.append(Filter("Styles",styles[i][0],"true","true"))
                else:
                    filter_.append(Filter("Styles",styles[i][0],"true","false"))
            else:
                filter_.append(Filter("Styles",styles[i][0],"false","false"))
            i=i+1
     
        i=0
        while i<=6:
            if color[i][1]==1:
                if color[i][0]==filter_color:
                    filter_.append(Filter("Color",color[i][0],"true","true"))
                else:
                    filter_.append(Filter("Color",color[i][0],"true","false"))
            else:
                filter_.append(Filter("Color",color[i][0],"false","false"))
            i=i+1

        i=0   
        while i<=6:
            if sizes[i][1]==1:
                if sizes[i][0]==filter_size:
                    filter_.append(Filter("Sizes",sizes[i][0],"true","true"))
                else:
                    filter_.append(Filter("Sizes",sizes[i][0],"true","false"))
            else:
                filter_.append(Filter("Sizes",sizes[i][0],"false","false"))
            i=i+1        
 
    json_string = json.dumps([Filter.__dict__ for Filter in filter_])
	
    print(json_string)
 
    return json_string


def get_styles(filter_style_,filter_color_,filter_size_,filter_padding_,last_click,id,link,user,day,month,year,c):


    reload(sys)
    sys.setdefaultencoding("ISO-8859-1")
   
    styles = [[] for i in range(13)]
    color = [[] for i in range(14)]
    padding = [[] for i in range(4)]
    sizes= [[] for i in range(90)]
    sizes_dict= {}


    list = [[] for i in range(5)]
    now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))

  
    i=0


    if link!="panties":
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
            color[i].append(row[1])
            i=i+1
     
     
        i=0
        c.execute ("""select * from padding """)
        for row in c:
            padding[i].append(row[0])
            padding[i].append(0)
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
            color[i].append(row[1])
            i=i+1

     
        i=0
        c.execute ("""select * from sizespanty""")
        for row in c:
            sizes_dict[row[0]]=i
            sizes[i].append(row[0])
            sizes[i].append(0)
            i=i+1

    now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))

    







    print("filter")
    print(styles)
    index=0
    c.execute ("""select * from lingerieselection ORDER BY position ASC""")

    lingerieselection=c.fetchall()
    for row in lingerieselection:
        if link!="Dein Showroom":

            if link=="BH Sets" or link=="lingerie":


                if row[7]=="yes":

                               
                    id=0

                    while id<=3:
                        print(id)
                        if filter_color_=="" and filter_style_=="" and filter_size_=="" and filter_padding_=="":
                            filter_style=filter_style_
                            filter_color=filter_color_
                            filter_size=filter_size_
                            filter_padding=filter_padding_
                            id=4
                        else:
                            if id==0:
                                filter_style=""
                                filter_color=filter_color_
                                filter_size=filter_size_
                                filter_padding=filter_padding_
                            if id==1:

                                filter_style=filter_style_
                                filter_color=""
                                filter_size=filter_size_
                                filter_padding=filter_padding_
                            if id==2:

                                filter_style=filter_style_
                                filter_color=filter_color_
                                filter_size=filter_size_
                                filter_padding=""
                            if id==3:

                                filter_style=filter_style_
                                filter_color=filter_color_
                                filter_size=""
                                filter_padding=filter_padding_
                        i=0
                        
                        print(row[0])
                        while i<=12:
                            if last_click=="":
                                
                                if i>4:
                                    zaehler=i+5
                                else:
                                    zaehler=i
                                if (row[20+zaehler]=="x" and styles[i][0]==filter_style) or (filter_style=="" and row[20+zaehler]=="x"):
                                    j=0
                                    
                                    while j<=6:
                                        if (row[50]==color[j][2] and filter_color==color[j][0]) or (filter_color=="" and row[50]==color[j][2]):
                 
                                            k=0
                                            
                                            while k<=3:
                                                if (row[40+k]=="x" and padding[k][0]==filter_padding) or (filter_padding=="" and row[40+k]=="x"):
                 

                                                            g=0

                                                        
                                                                
                                                            if filter_size=="":





                                                                if id==0:
                                                                    c.execute ("""select * from %s where color='%s' and stylecode='%s'""" % ("stylecode", row[13],row[12],))
                                                                    rows=c.fetchall()

                                                                    if len(rows)>0:                                                                  
                                                                        styles[i][1]=1
                                                                if id==1:
                                                                    c.execute ("""select * from %s where color='%s' and stylecode='%s'""" % ("stylecode", row[13],row[12],))
                                                                    rows=c.fetchall()
																
                                                                    if len(rows)>0: 
                                                                        color[j][1]=1
                                                                    
                                                                if id==2:
                                                                    
                                                                    c.execute ("""select * from %s where color='%s' and stylecode='%s'""" % ("stylecode", row[13],row[12],))
                                                                    rows=c.fetchall()
                                                                    if len(rows)>0:
                                                                        padding[k][1]=1


                                                                if id==3:
                                                                    c.execute ("""select * from %s where color='%s' and stylecode='%s'""" % ("stylecode", row[13],row[12],))
                                                                    for row_2 in c: 
                                                                        menge=int(row_2[4])-int(row_2[5])
                                                                        if menge>0:                                                                   
                                                                            try:
                                                                                
                                                                                sizes[sizes_dict[row_2[3]]][1]=1


                                                                                
                                                                            except:
                                                                                id=id
                                                                if id==4:


                                                                    now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))

                                                                    c.execute ("""select * from %s where color='%s' and type='%s' and stylecode='%s'""" % ("stylecode", row[13],"BH",row[12],))
                                                                    for row_2 in c: 
                                                                        menge=int(row_2[4])-int(row_2[5])
                                                                        if menge>0:                                                                   
                                                                            try:
                                                                                styles[i][1]=1
                                                                                color[j][1]=1
                                                                                padding[k][1]=1
                                                                                
                                                                                sizes[sizes_dict[row_2[3]]][1]=1


                                                                                
                                                                            except:
                                                                                id=id

                                                        
                                                            else:
                                                                c.execute ("""select * from %s where color='%s' and size='%s' and stylecode='%s'""" % ("stylecode", row[13],filter_size,row[12],))
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
                                                                            
                                                                            try:
                                                                                
                                                                                sizes[sizes_dict[row_2[3]]][1]=1


                                                                                
                                                                            except:
                                                                                id=id

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
                            id=2
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
                        
                        while i<=4:
                            if last_click=="":
                                
                                if (row[25+i]=="x" and styles[i][0]==filter_style) or (filter_style=="" and row[25+i]=="x"):
                                    j=0
                                    
                                    while j<=6:
                                        if (row[50]==color[j][2] and filter_color==color[j][0]) or (filter_color=="" and row[50]==color[j][2]):


                                        
                                                
                                            if filter_size=="":





                                                if id==0:
                                                    c.execute ("""select * from %s where color='%s' and stylecode='%s'""" % ("stylecode", row[13],row[12],))
                                                    rows=c.fetchall()
                                                    if len(rows)>0:                                                                  
                                                        styles[i][1]=1
                                                if id==1:
                                                    c.execute ("""select * from %s where color='%s' and stylecode='%s'""" % ("stylecode", row[13],row[12],))
                                                    rows=c.fetchall()
                                                    if len(rows)>0: 
                                                        color[j][1]=1
                                                    

                                                if id==2:
                                                    c.execute ("""select * from %s where color='%s' and stylecode='%s'""" % ("stylecode", row[13],row[12],))
                                                    for row_2 in c: 
                                                        menge=int(row_2[4])-int(row_2[5])
                                                        if menge>0:

                                                            styles[i][1]=1
                                                            color[j][1]=1
                                                            try:
                                                                groesse=row_2[3]
                                                                groesse=groesse.split(" ")
                                                                sizes[sizes_dict[groesse[1]]][1]=1


                                                                
                                                            except:
                                                                id=id


                                        
                                            else:
                                                c.execute ("""select * from %s where color='%s' and size='%s' and type='%s'""" % ("stylecode", row[13],filter_size,"panties",))
                                                for row_2 in c:
                                                    

                                                    menge=int(row_2[4])-int(row_2[5])
                                                    if menge>0:


                                                        if id==0:
                                                            styles[i][1]=1
                                                        if id==1:                              
                                                            color[j][1]=1
                                                        if id==2:                              
                                                            
                                                            try:
                                                                
                                                                groesse=row_2[3]
                                                                groesse=groesse.split(" ")
                                                                sizes[sizes_dict[groesse[1]]][1]=1
                                                            except:
                                                                id=id

                                        j=j+1
                            i=i+1
                        id=id+1                
        else:

            c.execute ("""select * from showroom where gutscheincode=%s """,(user,))
            showroom_data=c.fetchall()
            for row_3 in showroom_data:

                if row_3[0]==row[11] and row_3[1]==row[12] and row_3[2]==day and row_3[3]==month and row_3[4]==year: 


                    if row[7]=="yes":

                                   
                        id=0

                        while id<=3:
                            if filter_color_=="" and filter_style_=="" and filter_size_=="" and filter_padding_=="":
                                filter_style=filter_style_
                                filter_color=filter_color_
                                filter_size=filter_size_
                                filter_padding=filter_padding_
                                id=4
                            else:
                                if id==0:
                                    filter_style=""
                                    filter_color=filter_color_
                                    filter_size=filter_size_
                                    filter_padding=filter_padding_
                                if id==1:

                                    filter_style=filter_style_
                                    filter_color=""
                                    filter_size=filter_size_
                                    filter_padding=filter_padding_
                                if id==2:

                                    filter_style=filter_style_
                                    filter_color=filter_color_
                                    filter_size=filter_size_
                                    filter_padding=""
                                if id==3:

                                    filter_style=filter_style_
                                    filter_color=filter_color_
                                    filter_feature=filter_feature_
                                    filter_size=""
                                    filter_padding=filter_padding_
                            i=0
                            

                            while i<=12:
                                if last_click=="":
                                    
                                    if i>4:
                                        zaehler=i+5
                                    else:
                                        zaehler=i
                                    if (row[20+zaehler]=="x" and styles[i][0]==filter_style) or (filter_style=="" and row[20+zaehler]=="x"):
     #                                   print(row[21+zaehler]+"==x and "+styles[i][0]+"=="+filter_style+") or ("+filter_style+"== and "+row[21+zaehler]+"==x")
                                        j=0
                                        
                                        while j<=6:
                                           # print(str(row[50])+"=="+str(color[j][2]) +"and "+str(filter_color)+"=="+str(color[j][0]) +"or "+str(filter_color)+"== and "+str(row[50])+"=="+str(color[j][2]))
                                            if (row[50]==color[j][2] and filter_color==color[j][0]) or (filter_color=="" and row[50]==color[j][2]):
                     
                                                k=0
                                                
                                                while k<=3:
                                                    if (row[40+k]=="x" and padding[k][0]==filter_padding) or (filter_padding=="" and row[40+k]=="x"):

                                                            
                                                                    
                                                                if filter_size=="":





                                                                    if id==0:
                                                                        c.execute ("""select * from %s where color='%s' and stylecode='%s'""" % ("stylecode", row[13],row[12],))
                                                                        rows=c.fetchall()
                                                                        if len(rows)>0:                                                                  
                                                                            styles[i][1]=1
                                                                    if id==1:
                                                                        c.execute ("""select * from %s where color='%s' and stylecode='%s'""" % ("stylecode", row[13],row[12],))
                                                                        rows=c.fetchall()
                                                                        if len(rows)>0: 
                                                                            color[j][1]=1
                                                                        
                                                                    if id==2:
                                                                        
                                                                        c.execute ("""select * from %s where color='%s' and stylecode='%s'""" % ("stylecode", row[13],row[12],))
                                                                        rows=c.fetchall()
                                                                        if len(rows)>0:
                                                                            padding[k][1]=1


                                                                    if id==3:
                                                                        c.execute ("""select * from %s where color='%s' and stylecode='%s'""" % ("stylecode", row[13],row[12],))
                                                                        for row_2 in c: 
                                                                            menge=int(row_2[4])-int(row_2[5])
                                                                            if menge>0:                                                                   
                                                                                try:
                                                                                    
                                                                                    sizes[sizes_dict[row_2[3]]][1]=1


                                                                                    
                                                                                except:
                                                                                    id=id
                                                                    if id==4:


                                                                        now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))

                                                                        c.execute ("""select * from %s where color='%s' and type='%s' and stylecode='%s'""" % ("stylecode", row[13],"BH",row[12],))
                                                                        for row_2 in c: 
                                                                            menge=int(row_2[4])-int(row_2[5])
                                                                            if menge>0:                                                                   
                                                                                try:
                                                                                    styles[i][1]=1
                                                                                    color[j][1]=1
                                                                                    padding[k][1]=1
                                                                                    
                                                                                    sizes[sizes_dict[row_2[3]]][1]=1


                                                                                    
                                                                                except:
                                                                                    id=id

                                                            
                                                                else:
                                                                    c.execute ("""select * from %s where color='%s' and size='%s' and stylecode='%s'""" % ("stylecode", row[13],filter_size,row[12],))
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
                                                                                
                                                                                try:
                                                                                    
                                                                                    sizes[sizes_dict[row_2[3]]][1]=1

                                                                                except:
                                                                                    id=id

                                                    k=k+1
                                            j=j+1
                                i=i+1
                            id=id+1 
    now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
    print("fertig")

    list[0].append(styles)
    list[1].append(color)
    list[2].append(padding)
    list[3].append(sizes)
    return list

timer=0
s = sched.scheduler(time.time, time.sleep)
def do_something(sc): 
    global timer

    generate_standard_product_library()
    create_matching_table_stammdaten_stylecodes()
    
    timer=timer+1
    if timer <=14:
        s.enter(120, 1, do_something, (sc,))

if timer <=14:
    s.enter(120, 1, do_something, (s,))
    s.run()
print "timer"
print timer
