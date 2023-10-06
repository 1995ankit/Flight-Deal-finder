import requests
import os





class DataManager:
    def __init__(self):
        self.sheety_endpoint = os.environ.get('sheety_endpoint')
        self.sheety_bearer_token = os.environ.get('sheety_bearer_token')
        self.sheety_headers = {'Authorization': self.sheety_bearer_token}

    def load_and_save_sheet(self):
        response = requests.get(url=self.sheety_endpoint, headers=self.sheety_headers)
        sheet_data = response.json()['prices']
        return(sheet_data)


