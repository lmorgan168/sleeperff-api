import requests
import requests.packages
from typing import List, Dict

class RestAdapter:
    def __init__(self, hostname: str, ver: str = 'v1'):
        self.url = "https://{}/{}/".format(hostname, ver)
    
    def get(self, endpoint: str) -> List[Dict]:
        full_url = self.url + endpoint
        response = requests.get(full_url)
        data_out = response.json()
        if response.status_code >= 200 and response.status_code <=299:
            return data_out
        raise Exception(data_out['message']) # raise custom exceptions later


