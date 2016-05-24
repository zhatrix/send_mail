#!/usr/bin/python
# -*- coding: utf-8 -*-
# 
import os
import smtplib
# from datetime import date,datetime
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText  
from email.mime.image import MIMEImage
from email.header import Header

# your mail smtp sever address
mail_host = 'smtp.example.com'

# your mail name and password 
user = 'abc@example.com'
pwd = 'your password'
#  send mail to these addresses
to = ['ced@example.com','name@example.com']

title = 'your mail title' 
content = 'hello world , or other words'

def SendEmail(user, pwd, to, title, content, htmlpath = None,filepath = None):
    msg = MIMEMultipart('alternative')
    if filepath != None and filepath != []:
        att = MIMEText(open(filepath, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="' + os.path.basename(filepath) + '"'
        msg.attach(att)
    
    if htmlpath != None and htmlpath != []:
        part = MIMEText(open(htmlpath, 'rb').read().decode("utf-8"),'html','utf-8')
        msg.attach(part)
    
    part1 = MIMEText(content, 'plain','utf-8')
    msg.attach(part1)   
    msg['to'] = ', '.join(to)
    msg['from'] = user
    msg['subject'] = Header(title, 'utf-8')
    msg.preamble = 'Our family reunion'
    server = smtplib.SMTP(mail_host)
    server.login(user,pwd)
    try:
        server.sendmail(user, to, msg.as_string())
        print("Email/attachment has been delivered")
        server.close()
    except:
        print("Problem is sending Email")
    os.remove(filepath)  # remove file after send attachment