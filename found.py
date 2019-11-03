import os
import requests
import threading
import sys
from lxml.html import fromstring
from itertools import cycle
import traceback
import time


def findBTC():
    counter = 0
    i = 0
    f = open("found.txt", "r")

    for x in f:
        g = open("balfound.txt", "r")
        for y in g:
            try:
                i = i + 1
                print(x)
                print(y)
                if x == y:
                    counter = 1;
                    print("Bitcoin Address", str(i) + ": " + x, file=open("ooutput.txt", "a"))
                    sys.exit(0)
            except:
                print("Skipping. Connnection error")


def main():
    findBTC()


if __name__ == "__main__":
    main()