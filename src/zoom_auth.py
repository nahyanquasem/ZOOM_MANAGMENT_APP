#code to zoom api authorization and tokens
import json
import os
import time
from pathlib import Path

import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth


class ZoomAccessToken:

    def __init__(self, p_token_path):
        self.__access_token = ''
        self.__expires_at = 0.0
        self.__token_path = p_token_path


    @property
    def access_token(self):
        return self.__access_token


    @property
    def expires_at(self):
        return self.__expires_at


    def initialize_access_token(self):
        self.get_zoom_access_token()


    def __is_expired(self):
        return time.time() + 60 > self.__expires_at


    def __is_token_cached(self):
        return Path(self.__token_path).is_file()


    def __load_cached_token(self):
        with open(self.__token_path,'r') as file:
            zoom_access_token = json.load(file)
        return zoom_access_token


    def __store_cached_token(self, p_token):
        with open(self.__token_path,'w') as file:
            json.dump(p_token, file, indent=4)


    def get_zoom_access_token(self) -> None:

        if not self.__is_token_cached():
            self.__zoom_request_token()

        else:

            zoom_access_token = self.__load_cached_token()
            self.__expires_at = zoom_access_token['expires_at']

            if self.__is_expired():
                self.__zoom_request_token()
            else:
                self.__access_token = zoom_access_token['access_token']


    def __zoom_request_token(self) -> None:

        payload = {'grant_type':'account_credentials', 'account_id':os.getenv('ACCOUNT_ID')}
        auth = HTTPBasicAuth(os.getenv('CLIENT_ID'), os.getenv('CLIENT_SECRET'))

        response = requests.post(url=os.getenv('ZOOM_OAUTH_ENDPOINT'),data=payload, auth=auth)

        zoom_access_token = response.json()
        expires_at = time.time() + zoom_access_token['expires_in']

        zoom_access_token.update({'expires_at':expires_at})

        self.__store_cached_token(zoom_access_token)

        self.__access_token = zoom_access_token['access_token']
        self.__expires_at = zoom_access_token['expires_at']




if __name__ == '__main__':
    load_dotenv()
    token = ZoomAccessToken(os.getenv('ACCESS_TOKEN_FILE'))
    token.initialize_access_token()

    print(token.access_token)
