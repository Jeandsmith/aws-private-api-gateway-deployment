import requests
import os

def handler (event, context):
    response = requests.get(os.environ["PRIVATE_API"])  

    return {
        "statusCode": response.status_code,
        "body": response.text,
        "headers": {
            "Content-Type": "application/json"
        }
    }