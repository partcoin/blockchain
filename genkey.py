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
            #Grabbing IP and corresponding PORT
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies

def ripemd160(x):
    d = hashlib.new('ripemd160')
    d.update(x)
    return d
def findBTC():
    counter = 0
    i = 0
    while(counter==0):  # number of key pairs to generate`
        proxies = get_proxies()
        proxy_pool = cycle(proxies)
        for j in range(1, 11):
            proxy = next(proxy_pool)
            # print("Request #%d" % j)
            # generate private key , uncompressed WIF starts with "5"
            priv_key = os.urandom(32)
            fullkey = '80' + binascii.hexlify(priv_key).decode()
            sha256a = hashlib.sha256(binascii.unhexlify(fullkey)).hexdigest()
            sha256b = hashlib.sha256(binascii.unhexlify(sha256a)).hexdigest()
            WIF = base58.b58encode(binascii.unhexlify(fullkey + sha256b[:8]))

            # get public key , uncompressed address starts with "1"
            sk = ecdsa.SigningKey.from_string(priv_key, curve=ecdsa.SECP256k1)
            vk = sk.get_verifying_key()
            publ_key = '04' + binascii.hexlify(vk.to_string()).decode()
            hash160 = ripemd160(hashlib.sha256(binascii.unhexlify(publ_key)).digest()).digest()
            publ_addr_a = b"\x00" + hash160
            checksum = hashlib.sha256(hashlib.sha256(publ_addr_a).digest()).digest()[:4]
            publ_addr_b = base58.b58encode(publ_addr_a + checksum)
            i = i+1
            try:
                from requests_html import HTMLSession
                session = HTMLSession(browser_args=["--proxy-server=proxy"])
                res = session.get('https://blockchain.com/btc/address/' + publ_addr_b.decode())
                #res = requests.get('https://blockchain.com/btc/address/' + publ_addr_b.decode())
                about = res.html.find('td#final_balance', first=True)
                l = about.text.split(' ')
                print(float(l[0]))
                print('Private Key    ', str(i) + ": " + WIF.decode())
                print("Bitcoin Address", str(i) + ": " + publ_addr_b.decode())
                if (float(l[0]) > 0):
                    counter = 1;
                    print('BTC Wallet found with balance breaking...', str(i), file=open("output.txt", "a"))
                    print('Private Key    ', str(i) + ": " + WIF.decode(), file=open("output.txt", "a"))
                    print("Bitcoin Address", str(i) + ": " + publ_addr_b.decode(), file=open("output.txt", "a"))
                    print(float(l[0]), file=open("output.txt", "a"))
                    sys.exit()
            except:
                print("Skipping. Connnection error")
def main():
    findBTC()
   # threads = []
   # for i in range(1):
    #    time.sleep(1.0)
     #   threads.append(threading.Thread(target=findBTC(),args=()))
    #for t in threads:
     #   time.sleep(1)
      #  t.start()
    #for t in threads:
     #   t.join()//

if __name__ == "__main__":
    main()