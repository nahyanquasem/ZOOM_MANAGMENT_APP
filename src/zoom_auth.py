#code to zoom api authorization and tokens
import json

import os
from dotenv import load_dotenv

import time

import requests
from requests.auth import HTTPBasicAuth

from pathlib import Path

class ZoomAccessToken:

    def __init__(self):
        load_dotenv()
        self.__access_token = ''
        self.__expires_at = 0.0


    @property
    def access_token(self):
        return self.__access_token


    @property
    def expires_at(self):
        return self.__expires_at


    def __is_expired(self):
        return time.time() + 60 > self.__expires_at


    def initialize_access_token(self):
        self.get_zoom_access_token()


    def get_zoom_access_token(self) -> None:

        token_file_path = Path('..//logs/zoom_access_token.json')

        if not token_file_path.is_file():
            self.zoom_request_token()

        else:

            with open(token_file_path,'r') as json_file:
                zoom_access_token = json.load(json_file)

            self.__expires_at = zoom_access_token['expires_at']

            if self.__is_expired():
                self.zoom_request_token()
            else:
                self.__access_token = zoom_access_token['access_token']


    def zoom_request_token(self) -> None:

        payload = {'grant_type':'account_credentials', 'account_id':os.getenv('ACCOUNT_ID')}
        auth = HTTPBasicAuth(os.getenv('CLIENT_ID'), os.getenv('CLIENT_SECRET'))

        response = requests.post(url=os.getenv('ZOOM_OAUTH_ENDPOINT'),data=payload, auth=auth)

        zoom_access_token = response.json()
        expires_at = time.time() + zoom_access_token['expires_in']

        zoom_access_token.update({'expires_at':expires_at})

        with open('..//logs/zoom_access_token.json','w') as json_file:
            json.dump(zoom_access_token,json_file, indent=4)

        self.__access_token = zoom_access_token['access_token']
        self.__expires_at = zoom_access_token['expires_at']




if __name__ == '__main__':
    token = ZoomAccessToken()
    token.initialize_access_token()

    print(token.access_token)