import os
from dotenv import load_dotenv




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    load_dotenv()

    print(f'{os.getenv('zoom_oauth_endpoint')}')
    print(f'{os.getenv('client_secret')}')
