#!/bin/sh

aws s3 cp s3://parrot.today/parrots.txt /tmp/parrots.txt
./getparrot.py
aws s3 cp /tmp/parrot.jpg s3://parrot.today/ --acl public-read --storage-class STANDARD
