import json
from api_call import get_api_request


class NBADataWrapper(object):
    '''Class for requesting and organizing data from NBA API'''
    
    def __init__(self, api_url=None, method='GET', api_response=None):
        self.api_url = api_url
        self.method = method
        self.api_response = api_response
        self.data = {}

    def set_API_imurl(self, api_url):
        self.api_url = api_url

    def get_data(self):
        api_response = get_api_request(self.method, self.api_url)
        self.api_response = api_response['body']


    #def hydrate(self, api_response):




if __name__ == "__main__":
    pass