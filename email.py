import sendgrid
from sendgrid.helpers.mail import *
import pandas as pd
import mysql.connector
#Connect to Mysql
mydb = mysql.connector.connect(
    host="mysqlServer", user="mysqlUser", password="mysqlUserPsswd", database="mysqlDb"
)
connection = mydb.cursor()
#Select Table with pandas
frame = pd.read_sql("SELECT * FROM MYSQLTABLE", mydb)
#Select Column Of Emails
emaily = frame["emaily"]
#ForLoop Over Emails
for i in range(len(emaily)):
    emails = emaily[i]
    #Open the html file you'd like to send
    with open(
        "/path/to/html",
        "r",
        encoding="utf-8",
    ) as f:
        #Reading the html file
        ht = f.read()
    sg = sendgrid.SendGridAPIClient(
        "api-key"
    )
    mail = Mail()
    from_email = Email("from-email")
    print(emails)
    to_email = Email(emails)
    
    subject = "subject"
    per = Personalization()
    mail.from_email = from_email
    mail.subject = subject
    html_content = Content("text/html", ht)
    plain_content = Content("text/plain", "plain-text")

    ###Add plain content first
    mail.add_content(plain_content)
    ###Add HTML content next
    mail.add_content(html_content)
    per.add_to(to_email)
    mail.add_personalization(per)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response)