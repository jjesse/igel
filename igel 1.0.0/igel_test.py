import requests
import logging
import json

logging.info('===>Starting IGEL Test Script')

# Initialize response
response = {}

# Make the API Call
try:
    api_hostname = params.get('connect_igel_hostname', '')
    api_port = params.get('connect_igel_port', 8443)
    cookie = params.get('connect_authorization_token', '')
    proxy_ip = params.get('connect_proxy_ip', '')
    proxy_port = params.get('connect_proxy_port', '')
    proxy_username = params.get('connect_proxy_username', '')
    proxy_password = params.get('connect_proxy_password', '')

    if not api_hostname:
        logging.warning('Hostname/IP not specified!')

    if not cookie:
        logging.warning('Authorization cookie not specified')

    payload = {}
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'charset': 'utf-8',
        'User-Agent': 'FSCT/2.16.2022',
        'Cookie': cookie
    }

    url = f'https://{api_hostname}:{api_port}/umsapi/v3/thinclients'
    resp = requests.request('GET', url, headers=headers, data=payload, verify=False, allow_redirects=True)

    if resp is None:
        response['succeeded'] = False
        response['result_msg'] = 'No response from IGEL UMS.'
    elif resp.status_code == 200:
        response['succeeded'] = True
        response['result_msg'] = 'Successfully connected to IGEL UMS.'
        response_json = json.loads(resp.content)
        logging.debug(response_json)
    else:
        response['succeeded'] = False
        response['result_msg'] = f'Error Code {resp.status_code} received from IGEL UMS.'
except requests.exceptions.RequestException as e:
    response['succeeded'] = False
    response['result_msg'] = f'Could not connect to IGEL UMS. Exception occurred. {e}'
except Exception as e:
    response['succeeded'] = False
    response['result_msg'] = f'Unknown error: {e}'

logging.debug(f'Test Script Returned Response: {response}')

logging.info('===>Ending IGEL Test Script')
