import boto3
from botocore.exceptions import NoCredentialsError
import os
from dotenv import load_dotenv

load_dotenv()

def upload_to_aws(local_file, bucket, s3_file):
  ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
  SECRET_KEY = os.getenv('AWS_SECRET_KEY')
  REGION = os.getenv('AWS_REGION')  
  s3 = boto3.client(service_name='s3', 
                      region_name= REGION,
                      aws_access_key_id= ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)
    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

bucket_name = 'XXXXXXXXXXXXXXXX'
upload_to_aws('path/to/your/file', bucket_name)
