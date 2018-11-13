#!/usr/bin/env python

import boto3
import random
from smart_open import smart_open
import urllib.request


def main():
    # download random parrot
    parrots = smart_open('s3://parrot.today/parrots.txt', encoding='utf8')
    url = (random.choice(list(parrots)))
    urllib.request.urlretrieve(url, "/tmp/parrot.jpg")

    # upload random parrot to s3
    s3 = boto3.client("s3")
    bucket = "parrot.today"
    client = boto3.resource("s3")
    client.meta.client.upload_file("/tmp/parrot.jpg", bucket, "parrot.jpg",
                                   ExtraArgs={'ACL': 'public-read'})


main()
