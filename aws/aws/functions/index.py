import requests
import os

def handler (event, context):
    response = requests.get(os.environ["PRIVATE_API"])  