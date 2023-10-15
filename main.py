import requests
import os
import pickle
from pprint import pprint
from flight_search import FlightSearch
from flight_data import FlightData
from twilio.rest import Client
from data_manager import DataManager

# TWILIO_sid = os.environ.get('TWILIO_sid')
# TWILIO_auth_token = os.environ.get('TWILIO_auth_token')
# client = Client(TWILIO_sid, TWILIO_auth_token)

# data = DataManager().load_and_save_sheet()
# with open("cities_info.pkl", 'wb') as file:
#     pickle.dump(data, file)

with open('cities_info.pkl', 'rb') as f:
    sheet_data = pickle.load(f)
# pprint(sheet_data)

sheety_endpoint = os.environ.get('sheety_endpoint')
sheety_bearer_token = os.environ.get('sheety_bearer_token')
sheety_headers = {'Authorization': sheety_bearer_token}
put_url = "https://api.sheety.co/2de1bb8eccea47d7b39476252352b2f3/ankitFlightPlanning/prices/"


def fill_iata(sheet_data):
    row_id = 2
    for city_info in sheet_data:
        city = city_info['city']
        iata_code = FlightSearch(city).iata_code()
        put_param = {
            'price': {
                "iataCode": iata_code
            }
        }
        requests.put(url=f"{put_url}{row_id}", json=put_param, headers=sheety_headers)
        row_id += 1
# fill_iata(sheet_data)

# Printing minimum flight price for every city in the list

# for city_info in sheet_data:
#     flight_data = FlightData(city_info['iataCode']).get_flight_data()
#     if (flight_data['price']) < (city_info['lowestPrice']):
#         article = f"Low price alert! Only INR{flight_data['price']} to fly from {flight_data['cityFrom']} to " \
#                   f"{flight_data['cityTo']} from {flight_data['local_departure'].split('T')[0]} for " \
#                   f"{flight_data['nightsInDest']} days"
#
#         message = client.messages.create(
#             body=article,
#             from_='+17408428638',
#             to='+918981329207'
#         )


