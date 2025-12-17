#code to zoom api authorization and tokens
import json

import os
from dotenv import load_dotenv

import time

import requests
from requests.auth import HTTPBasicAuth


def zoom_request_token() -> dict[str,str]:

    load_dotenv()

    payload = {'grant_type':'account_credentials', 'account_id':os.getenv('ACCOUNT_ID')}
    auth = HTTPBasicAuth(os.getenv('CLIENT_ID'), os.getenv('CLIENT_SECRET'))

    response = requests.post(url=os.getenv('ZOOM_OAUTH_ENDPOINT'),data=payload, auth=auth)

    zoom_access_token = response.json()
    expires_at = time.time() + zoom_access_token['expires_in']

    zoom_access_token.update({'expires_at':expires_at})

    with open('..//logs/zoom_access_token','w') as json_file:
        json.dump(zoom_access_token,json_file, indent=4)

    return zoom_access_token

if __name__ == '__main__':
    token = zoom_request_token()

    for key, value in token.items():
        print(f'{key}:{value}')