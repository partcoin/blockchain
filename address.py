import os, binascii, hashlib, base58, ecdsa
import requests
import threading
import sys
from lxml.html import fromstring
from itertools import cycle
import traceback
import time


def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            # Grabbing IP and corresponding PORT
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies


def findBTC():
    counter = 0
    i = 0
    f = open("demofile.txt", "r")
    while (counter == 0):  # number of key pairs to generate`
        proxies = get_proxies()
        proxy_pool = cycle(proxies)
        for j in range(1, 11):
            proxy = next(proxy_pool)
            print("Request #%d" % j)
            i = i + 1
            for x in f:
                print(x)
                try:
                    from requests_html import HTMLSession
                    session = HTMLSession(browser_args=["--proxy-server=proxy"])
                    res = session.get('https://blockchain.com/btc/address/' + x)
                    about = res.html.find('td#final_balance', first=True)
                    l = about.text.split(' ')
                    print(float(l[0]))
                    if (float(l[0]) > 0):
                        counter = 1;
                        print('BTC Wallet found with balance breaking...', str(i), file=open("newoutput.txt", "a"))
                        print("Bitcoin Address", str(i) + ": " + x, file=open("newoutput.txt", "a"))
                        print(float(l[0]), file=open("newoutput.txt", "a"))
                        sys.exit()
                except:
                        print("Skipping. Connnection error")


def main():
    findBTC()


if __name__ == "__main__":
    main()