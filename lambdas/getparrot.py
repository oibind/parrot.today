import boto3
import random
import urllib.request


def lambda_handler(event, context):
    
    BUCKET_NAME = "parrot.today"
    URL_LIST = "parrots.txt"
    IMG = "parrot.jpg"

    s3 = boto3.resource("s3")
    s3.Bucket(BUCKET_NAME).download_file(URL_LIST, "/tmp/"+URL_LIST)
    url = (random.choice(list(open("/tmp/"+URL_LIST))))
    urllib.request.urlretrieve(url, "/tmp/"+IMG)
    s3.Bucket(BUCKET_NAME).upload_file("/tmp/"+IMG,
                                  IMG, ExtraArgs={"ContentType": "image/jpeg", "ACL": "public-read"})
