#!/usr/env python3


import cgi,cgitb
import sys
print "Content-Type: text/html; charset=utf-8\n\n";


form = cgi.FieldStorage()
mas =form.getvalue('fname')
mas1 =form.getvalue('lname')

#print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
#print "<title>COS lookup </title>"
print "</head>"
print "<body>"
print "Found the below class of services<br>"
#print "<h2>Hello %s %s</h2>" % (mas, mas1)
print "</body>"
print "</html>"
