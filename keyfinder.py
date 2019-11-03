import os, binascii, hashlib, base58, ecdsa
import requests
import threading
import sys
from lxml.html import fromstring
from itertools import cycle
import traceback
import time


def ripemd160(x):
    d = hashlib.new('ripemd160')
    d.update(x)
    return d
def findBTC():
    counter = 0
    i = 0
    while(counter==0):  # number of key pairs to generate`

            # print("Request #%d" % j)
            # generate private key , uncompressed WIF starts with "5"
            priv_key = os.urandom(32)
            fullkey = '80' + binascii.hexlify(priv_key).decode()
            sha256a = hashlib.sha256(binascii.unhexlify(fullkey)).hexdigest()
            sha256b = hashlib.sha256(binascii.unhexlify(sha256a)).hexdigest()
            WIF = base58.b58encode(binascii.unhexlify(fullkey + sha256b[:8]))
            #print(priv_key)
            print(sha256b)
            print(WIF.decode())
            sys.exit(0)


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