import logging
import sys
import time
import boto3
from botocore.errorfactory import ClientError
import botocore

master_start_time = time.time()
verify_text_file = r"C:\Fran_Files\verify.txt"
log_file_location = r"C:\Fran_Files\s3_object_checker_log_3.txt"
bucket = "frans-bucket"
object_prefix = "fran_testing/prefix2"

# noinspection PyArgumentList
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s",
                    handlers=[
                        logging.FileHandler(log_file_location),
                        logging.StreamHandler(sys.stdout)
                    ]
                    )
#s3 = boto3.client('s3')
s3 = boto3.resource('s3')

count = 0
success_count = 0
error_list = []

with open(verify_text_file) as text_file:
    for line in text_file:

        full_prefix = object_prefix + "/" + line.strip()
        #logging.info(f"Verifying {full_prefix} exists")

        try:
            s3.Object(bucket, full_prefix).load()
            logging.info(f"{full_prefix} exists")
            success_count += 1

        except botocore.exceptions.ClientError as e:
            error_list.append(full_prefix)
            if e.response['Error']['Code'] == "404":
                logging.error(f"{line.strip()} DOES NOT EXIST: Returned 404")
                #logging.error(f"error: {e}")
            else:
                logging.error(f"{line.strip()}DOES NOT EXIST: Returned other error")
                logging.error(f"error: {e}")

        # option 2 if option 1 doesnt work
        # try:
        #     s3.head_object(Bucket=bucket, Key=full_prefix)
        #     logging.info(f"{full_prefix} exists")
        # except ClientError as e:
        #     logging.error(f"{line.strip()} DOES NOT EXIST: Returned 404")

        count += 1

logging.info(f"Program Complete: Succesfully verified {success_count} out of {count} objects")
logging.info(f'Program took {(time.time() - master_start_time)} seconds to complete.\n')

