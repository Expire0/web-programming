#!/usr/bin/env python3

#https://docs.python.org/3/library/smtplib.html#smtp-example
#https://docs.python.org/3/library/email-examples.html

#simple processing form

import cgi,cgitb
import sys
import smtplib
from email.mime.text import MIMEText
print ("Content-Type: text/html; charset=utf-8")
print ()
cgitb.enable()


form = cgi.FieldStorage()
#kam = "kammy"
#don = "philly"
pname =form.getvalue('fname')
plname =form.getvalue('lname')
pemail =form.getvalue('email')
pcomment =form.getvalue('comment')

#print "Content-type:text/html\r\n\r\n"
print ("<html>")
print ("<head>")
print ("<title> changeme </title>")
print ("</head>")
print ("<body>")
print ("""
       some content
      <br>""")
#print "<h2>Hello %s %s</h2>" % (mas, mas1)
print ("</body>")
print ("</html>")


#msg = MIMEText(kam + "\n" +  don)
msg = MIMEText(pname + "\t" + plname + "\n" + pemail + "\n" + pcomment)

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = '<email subject> '
msg['From'] = "<email from>"
msg['To'] = "<email to>"

# Send the message via our own SMTP server.
s = smtplib.SMTP('mail server','port')
s.send_message(msg)
s.quit()
