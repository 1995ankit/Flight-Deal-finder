import requests
import os

class FlightSearch:

    def __init__(self, city):
        self.headers = {'apikey': os.environ.get('kiwi_api_key')}
        self.url = 'https://api.tequila.kiwi.com/locations/query'
        self.city = city

    # function returns the iata code for the city provided during the class object creation.
    def iata_code(self):
        params = {
            'term': self.city,
            'location_types': 'city'
        }
        response = requests.get(url=self.url, params=params, headers=self.headers)
        iata_code = response.json()['locations'][0]['code']
        return iata_code


