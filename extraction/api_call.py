import json
import requests



def _get_api_request(method, api_url):
    response = requests.request(method, api_url)

    if response.status_code == 200:
        return {
            'status_code': response.status_code,
            'body': response.json()
        }
    else:
        return {
            'status_code': response.status_code,
            'body': response.reason
        }
