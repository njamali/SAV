import urllib.request

import re

def expire():

    try:
        Dom = input("Please enter domain name: ")

    except :
        print("Error: domain name was entered wrong,\
         make sure http or https is not in the domain: ")

    link = "https://who.is/whois/" + Dom

    try:
        handler = urllib.request.Request(link)

    except:
        print("link is not vaild: ")

    with urllib.request.urlopen(handler) as response:
        the_page = response.read().decode('utf-8')

    text = str(the_page)

    text2 = text.rindex('Expires On</div>')

    text2 += 67

    print(text[text2:(text2 + 10)])