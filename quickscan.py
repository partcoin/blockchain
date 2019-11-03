import requests
import os
import sys
from lxml.html import fromstring
from itertools import cycle
import traceback

f = open("D:\\REST-API\\output.txt", "r")
i=68855
lines=f.readlines()
while (i < len(lines)):
    address=lines[i].split(': ')[1].split("\n")[0]
    print(address)
    from requests_html import HTMLSession

    session = HTMLSession()
    res = session.get('https://www.blockchain.com/btc/address/' + address)
    about = res.html.find('td#final_balance', first=True)
    l = about.text.split(' ')
    print(float(l[0]))
    if (float(l[0]) > 0):

        print('milgaya malamal golmal breaking...', )
        print('Private Key    ', str(i) + ": " + WIF.decode())
        print("Bitcoin Address", str(i) + ": " + address)
        print(float(l[0]))
        sys.exit()

    i=i+3
    #print(i)

print("DONE BHAIYYA KUCH nAHI")