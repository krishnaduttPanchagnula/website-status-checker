# importing the modules
import requests
from bs4 import BeautifulSoup
import smtplib, ssl
from emailaddress import sender_email,receiver_email


# target url
url = 'https://morrisonsupply.reece.com/'

#title of the page in HTML 
title = 'Reece Business Portal'
  
# making requests instance
reqs = requests.get(url)

# Configureing the email(smtp,ssl) settings
port = 587  # To start tls
smtp_server = "smtp.gmail.com"
sender_email = sender_email
receiver_email = receiver_email
password = input("Type your password and press enter:")

# establishing secure ssl connection
context = ssl.create_default_context()
  
test = 'asdfdsfdfs'
# Check if the website is returning the correct status code
if reqs.status_code == 200:
  param1 = True
else:
  param1 = False

# Getting HTML of the website using the BeautifulSoup module
soup = BeautifulSoup(reqs.text, 'html.parser')

# Find the title of the webpage and check if it is the one wanted
if soup.title.text == title: 
  param2 = True
else:
  param2 = False

# Check if requests and title is the one desired
if param1 == True and param2 == True:
  message = """\
Subject: Greetings from the website checker

everyting is working perfectly"""
  
elif param1 == False and param2 == True:
  message = """\
Subject: Greetings from the website checker

The website is working, but web request is having issues"""
 
 
else:
  message = """\
Subject: Greetings from the website checker

The website and web requests are down"""


with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  
    server.starttls(context=context)
    
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)