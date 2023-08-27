import requests
from dotenv import load_dotenv
import os

load_dotenv()

CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')

DOMAIN = 'https://login.salesforce.com'

json_data = {
    'grant_type': 'password',
    'client_id': CONSUMER_KEY,
    'client_secret': CONSUMER_SECRET,
    'username': os.getenv('USERNAME'),
    'password': os.getenv('PASSWORD')
}

response_access_token = requests.post(DOMAIN + '/services/oauth2/token', data = json_data)

print(response_access_token.status_code)
print(response_access_token.json())

if response_access_token.status_code == 200:
    print('Access token successful')

headers = {
    'Authorization': 'Bearer ' + response_access_token.json()['access_token'] 
}

INSTANCE = response_access_token.json()['instance_url']

response_sobject = requests.get(INSTANCE + '/services/data/v53.0/sobjects/Account', headers=headers)
print(response_sobject.reason)
print(response_sobject.json())