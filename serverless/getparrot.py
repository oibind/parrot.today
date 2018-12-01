import os
import boto3
import random
import urllib.request


def getparrot(event, context):

    BUCKET_NAME = "parrot.today"
    URL_LIST = "parrots.txt"
    IMG = "parrot.jpg"

    # delete tmp storage to stop amazon complaining
    dirPath = "/tmp/"
    fileList = os.listdir(dirPath)
    for fileName in fileList:
        os.remove(dirPath+"/"+fileName)

    s3 = boto3.resource("s3")
    s3.Bucket(BUCKET_NAME).download_file(URL_LIST, "/tmp/"+URL_LIST)
    url = (random.choice(list(open("/tmp/"+URL_LIST))))
    urllib.request.urlretrieve(url, "/tmp/"+IMG)
    s3.Bucket(BUCKET_NAME).upload_file("/tmp/"+IMG, IMG,
                                       ExtraArgs={"ContentType": "image/jpeg", "ACL": "public-read"})
