#!/usr/bin/env python

import random
import urllib.request

def main():
    url = (random.choice(list(open('parrots.txt'))))
    urllib.request.urlretrieve(url, "../parrot.jpg")

main()
