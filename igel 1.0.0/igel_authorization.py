from base64 import b64encode
import requests
import logging
import json

logging.info('===>Starting IGEL Authorization Script')

# All server configuration fields will be available in the 'params' dictionary.
api_hostname = params.get('connect_igel_hostname', '')
api_port = params.get('connect_igel_port', 8443)
api_user = params.get('connect_igel_username', '')
api_pass = params.get('connect_igel_password', '')
api_user_pass = f'{api_user}:{api_pass}'.encode()
api_basic_auth = b64encode(api_user_pass).decode()

proxy_ip = params.get('connect_proxy_ip', '')
proxy_port = params.get('connect_proxy_port', '')
proxy_username = params.get('connect_proxy_username', '')
proxy_password = params.get('connect_proxy_password', '')

# Initialize response
response = {'token': ''}

# Make the API Call
try:
    payload = {}
    headers = {
        'Authorization': f'Basic {api_basic_auth}',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'charset': 'utf-8',
        'User-Agent': 'FSCT/2.16.2022'
    }

    url = f'https://{api_hostname}:{api_port}/umsapi/v3/login'
    resp = requests.request('POST', url, headers=headers, data=payload, verify=False, allow_redirects=True)

    if resp is None:
        response['error'] = 'No response from IGEL UMS.'
    elif resp.status_code == 200:
        response_json = json.loads(resp.content)
        logging.debug(response_json)
        response['token'] = response_json.get('message', '')
    else:
        response['error'] = f'Error Code {resp.status_code} received from IGEL UMS.'
except requests.exceptions.RequestException as e:
    response['error'] = f'Could not connect to IGEL UMS. Exception occurred. {e}'
except Exception as e:
    response['error'] = f'Unknown error: {e}'

logging.debug(f'Authorization Script Returned Response: {response}')

logging.info('===>Ending IGEL Authorization Script')
