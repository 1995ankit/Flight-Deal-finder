import requests
from datetime import datetime, timedelta
import os

class FlightData:

    def __init__(self, sheet_data, to_city):
        self.from_city = "BOM"
        self.headers = {'apikey': os.environ.get("kiwi_api_key")}
        self.to_city = to_city
        self.url = "https://api.tequila.kiwi.com/v2/search"
        self.current_date = datetime.today()
        self.tomorrow = (self.current_date + timedelta(days=1)).strftime('%d/%m/%Y')
        self.sixmonthslater = (self.current_date + timedelta(days=180)).strftime('%d/%m/%Y')

    def get_flight_data(self):
        params = {
            'fly_from': self.from_city,
            'fly_to': self.to_city,
            'dateFrom': self.tomorrow,
            'dateTo': self.sixmonthslater,
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'curr': 'INR',
            'max_stopovers': 2
        }

        response = requests.get(url=self.url, params=params, headers=self.headers)
        data = response.json()['data'][0]
        return data

