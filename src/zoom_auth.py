#code to zoom api authorization and tokens

import os
from dotenv import load_dotenv

import requests
from requests.auth import HTTPBasicAuth


def zoom_request_token():

    load_dotenv()

    payload = {'grant_type':'account_credentials', 'account_id':os.getenv('ACCOUNT_ID')}
    auth = HTTPBasicAuth(os.getenv('CLIENT_ID'), os.getenv('CLIENT_SECRET'))

    response = requests.post(url=os.getenv('ZOOM_OAUTH_ENDPOINT'),data=payload, auth=auth)









if __name__ == '__main__':
    pass