#!/usr/bin/env python

import random
import urllib.request


def main():
    url = (random.choice(list(open('/tmp/parrots.txt'))))
    urllib.request.urlretrieve(url, "/tmp/parrot.jpg")

main()
