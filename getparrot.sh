#!/bin/sh

python randm.py > current.txt
cat current.txt | xargs -n1 wget -O parrot.jpg
