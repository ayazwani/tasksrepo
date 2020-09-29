
import os
import requests
import base64
import json
import csv
#nano env/bin/activate
#eport CLIENT_KEYS="YOUR KEY"
#export CLIENT_SECRET="YOUR SECRET"

client_key = os.environ.get("CLIENT_KEYS")
client_secret_key =os.environ.get("CLIENT_SECRET")
print(client_key)

key_secret = '{}:{}'.format(client_key, client_secret_key).encode('ascii')
b64_encoded_key = base64.b64encode(key_secret)
b64_encoded_key = b64_encoded_key.decode('ascii')

base_url = 'https://api.twitter.com/'
auth_url = '{}oauth2/token'.format(base_url)

auth_headers = {
    'Authorization': 'Basic {}'.format(b64_encoded_key),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

auth_data = {
    'grant_type': 'client_credentials'
}

auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)

print(auth_resp.status_code)

auth_resp.json().keys()

access_token = auth_resp.json()['access_token']

search_headers = {
    'Authorization': 'Bearer {}'.format(access_token)    
}

search_params = {
    'q': 'Kashmir',
    'result_type': 'recent',
    'count': 500
}

search_url = '{}1.1/search/tweets.json'.format(base_url)

search_resp = requests.get(search_url, headers=search_headers, params=search_params)

print(search_resp.status_code)

tweet_data = search_resp.json()

#for x in tweet_data['statuses']:
#   print(x['text'] + '\n')

t_data = tweet_data['statuses']

dfile = open('t1.csv','w')
csv_writer = csv.writer(dfile)
count = 0
for s in t_data:
    if(count == 0):
        header = s.keys()
        csv_writer.writerow(header)
        count+=1
    csv_writer.writerow(s.values())
dfile.close()

