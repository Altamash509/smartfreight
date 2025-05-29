import boto3
import os
from dotenv import load_dotenv
from botocore.exceptions import NoCredentialsError, ClientError
from pathlib import Path

# Load AWS credentials from .env
load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION", "us-east-2")
BUCKET_NAME = "smartfreight-data-lake"

# Local file to upload
LOCAL_FILE = Path("data/local_raw/shipments_bronze.json")
S3_KEY = "bronze/shipments_bronze.json"  # S3 folder structure

def upload_file_to_s3(local_file, bucket, s3_key):
    s3 = boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION
    )

    try:
        s3.upload_file(str(local_file), bucket, s3_key)
        print(f"✅ Uploaded {local_file} to s3://{bucket}/{s3_key}")
    except FileNotFoundError:
        print(f"❌ The file {local_file} was not found.")
    except NoCredentialsError:
        print("❌ AWS credentials not available.")
    except ClientError as e:
        print(f"❌ Failed to upload: {e}")

if __name__ == "__main__":
    upload_file_to_s3(LOCAL_FILE, BUCKET_NAME, S3_KEY)
