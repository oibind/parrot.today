import boto3
import random
import urllib.request


def main():
    s3 = boto3.resource("s3")
    bucket = "parrot.today"
    s3.Bucket(bucket).download_file("parrots.txt", "/tmp/parrots.txt")
    url = (random.choice(list(open('/tmp/parrots.txt'))))
    urllib.request.urlretrieve(url, "/tmp/parrot.jpg")
    s3.Bucket(bucket).upload_file("/tmp/parrot.jpg",
                                  "parrot.jpg", ExtraArgs={"ACL": "public-read"})
