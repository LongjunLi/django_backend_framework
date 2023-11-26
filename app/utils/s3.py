import os
import boto3
from botocore.client import Config

from django.conf import settings

from app.utils.log import log


def upload_file(filename, buffer):
    try:
        file_path_key = os.path.join(settings.AWS_UPLOAD_FOLDER, filename)
        s3 = boto3.client("s3",
                          aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                          region_name=settings.AWS_S3_REGION_NAME,
                          config=Config(signature_version="s3", s3={"addressing_style": "path"}))
        s3.put_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME,
                      Key=file_path_key,
                      Body=buffer)
        # url = s3.generate_presigned_url("get_object",
        #                                 Params = {"Bucket": settings.AWS_STORAGE_BUCKET_NAME,
        #                                           "Key": os.path.join(settings.AWS_UPLOAD_FOLDER, filename)},
        #                                 ExpiresIn = 63072000)
        url = f"https://{settings.AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/{file_path_key}"
        return url
    except:
        log(f"Cannot upload file: {filename}", "upload_file")
        return None


def get_url(filename):
    try:
        file_path_key = os.path.join(settings.AWS_UPLOAD_FOLDER, filename)
        # s3 = boto3.client("s3",
        #                   aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        #                   aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        #                   region_name=settings.AWS_S3_REGION_NAME,
        #                   config=Config(signature_version="s3",s3={"addressing_style": "path"}))
        # url = s3.generate_presigned_url("get_object",
        #                                 Params = {"Bucket": settings.AWS_STORAGE_BUCKET_NAME,
        #                                           "Key": os.path.join(settings.AWS_UPLOAD_FOLDER, filename)},
        #                                 ExpiresIn = 63072000)
        url = f"https://{settings.AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/{file_path_key}"
        return url
    except:
        log(f"Cannot get url: {filename}", "get_url")
        return None
