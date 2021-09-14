import datetime
import logging
import os
import sys
from pathlib import Path
from time import strftime

import boto3
from flask import Flask, jsonify, request

from config import default

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config.from_object(default)

date_raw = datetime.datetime.now()
date_processed = f"{date_raw.year}-{date_raw.month}-{date_raw.day}_{date_raw.hour}-{date_raw.minute}-{date_raw.second}"

# noinspection PyArgumentList
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s",
                    handlers=[
                        logging.FileHandler(datetime.datetime.now().strftime(
                            f'{app.config.get("LOG_DIR")}/restore_log_{date_processed}.log')),
                        logging.StreamHandler(sys.stdout)
                    ]
                    )

logging.info(f"Original Config: {app.config}")
override_config = Path(app.config.get('CONFIG_DIR'), os.getenv("APP_CONFIG_DIR")).with_suffix('.py')
app.config.from_pyfile(override_config)
logging.info(f"Override Config: {app.config}")


@app.after_request
def after_request(response):
    timestamp = strftime('[%Y-%b-%d %H:%M]')
    logging.info('%s %s %s %s %s %s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path,
                 response.status)
    return response


@app.route('/', methods=['GET'])
def home():
    message = 'Flask is UP and RUNNING'
    return jsonify(message)


@app.route('/restoreObject', methods=['POST'])
def restore_object():
    s3 = boto3.resource('s3', verify=False)
    try:
        bucket_name = request.json['s3Bucket']
        bucket = s3.Bucket(bucket_name)
        key = request.json['s3Key']
        try:
            bucket.meta.client.restore_object(Bucket=bucket_name, Key=key, RestoreRequest={'Days': 1, 'GlacierJobParameters': {'Tier': 'Standard'}})
        except Exception as e:
            logging.error({"Problem Restoring": str(e)})
            return {"Problem Restoring": str(e)}

    except Exception as e:
        logging.error({"Problem with Request, possibly incorrect property name!": str(e)})
        return {"Problem with Request, possibly incorrect property name!": str(e)}

    logging.info({"Successful Restore": os.path.join(bucket_name, key)})
    return {"Restore Successfully Triggered": os.path.join(bucket_name, key)}


if __name__ == "__main__":
    from waitress import serve

    serve(app, host="0.0.0.0", port=1337)
