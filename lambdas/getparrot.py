import boto3
import random
import urllib.request


def lambda_handler(event, context):
    BUCKET_NAME = "parrot.today"
    URL_LINKS = "parrots.txt"
    IMAGE = "parrot.jpg"

    s3 = boto3.resource("s3")
    s3.Bucket(BUCKET_NAME).download_file(URL_LINKS, URL_LINKS)
    url = (random.choice(list(open(URL_LINKS))))
    urllib.request.urlretrieve(url, IMAGE)
    s3.Bucket(BUCKET_NAME).upload_file(IMAGE,
                                       IMAGE, ExtraArgs={"ContentType": "image/jpeg", "ACL": "public-read"})
