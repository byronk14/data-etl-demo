import json
import requests



def get_api_request(method, api_url):
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


res = get_api_request('GET', 'https://nba-stats-db.herokuapp.com/api/playerdata/namea/Devin Bookear')
print(res)