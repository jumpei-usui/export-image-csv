import os
import boto3
from PIL import Image
from io import BytesIO


def handler(event, context):
    download_bucket_name = os.environ.get("DOWNLOAD_BUCKET_NAME")
    upload_bucket_name = os.environ.get("UPLOAD_BUCKET_NAME")

    file_name = event
    body_name, _ = os.path.splitext(file_name)

    s3 = boto3.resource("s3")
    download_bucket = s3.Bucket(download_bucket_name)
    obj = download_bucket.Object(file_name)

    download_buffer = BytesIO()
    obj.download_fileobj(download_buffer)

    img = Image.open(download_buffer)

    resize_ratio = img.height / 300
    resize_img = img.resize(size=(int(img.width / resize_ratio), 300))

    if resize_img.mode != "RGB":
        resize_img = img.convert("RGB")

    upload_buffer = BytesIO()
    resize_img.save(upload_buffer, format='JPEG')

    upload_buffer.seek(0)
    upload_bucket = s3.Bucket(upload_bucket_name)
    upload_bucket.upload_fileobj(upload_buffer, Key=f"{body_name}.jpg")
