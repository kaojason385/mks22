#! /usr/bin/python

import cgi

import cgitb
cgitb.enable()

HTML_HEADER = 'Content-type:text/html\r\n\r\n'

Top_HTML = """
<html>
<head>
<title>CGI Test 2</title>
</head>
<body>
<b>Nihao Jason</b>
"""

Bottom_HTML = "</body></html>"

def ShowInputElements():
    form = cgi.FieldStorage()
    print(HTML_HEADER + Top_HTML)
    print(form.getvalue('name'))
    print(form.getvalue('num'))
    print(Bottom_HTML)

ShowInputElements()
