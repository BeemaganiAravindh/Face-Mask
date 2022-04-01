from fileinput import filename
import datetime as dt
import time
from pathlib import Path
import smtplib
from glob import *
from email.message import EmailMessage
from stat import FILE_ATTRIBUTE_NO_SCRUB_DATA
msg= EmailMessage()
msg['subject']='Project'
msg['From']='teamate'
msg['To']='beemaganiaravindh@gmail.com,pavankalyan0702@gmail.com,nanduchapati@gmail.com'

for files in Path("C:/Users/beema/PAAVAM/MaskImages").glob('**/*'):
    with open (files,"rb") as f:
        data=f.read()
        name=f.name
        msg.add_attachment(data,maintype="application",subtype="jpg",filename=name)
with smtplib.SMTP_SSL('smtp.gmail.com',465) as server :
    server.login('majorprojectTKR@gmail.com','Swapna@123')
    
    server.send_message(msg)
print('sent!!')
