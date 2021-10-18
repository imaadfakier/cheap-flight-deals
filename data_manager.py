# This class is responsible for talking to the Google Sheet.

import requests
import requests.auth
# from collections import OrderedDict
import collections
import config

SHEETY_BASE_URL = 'enter base url'

SHEETY_SHOW_ENDPOINT = 'enter show endpoint'
SHEETY_ADD_ENDPOINT = SHEETY_SHOW_ENDPOINT
SHEETY_EDIT_ENDPOINT = 'enter edit endpoint'
SHEETY_REMOVE_ENDPOINT = 'enter remove endpoint'

SHEETY_AUTH_USERNAME = config.SHEETY_AUTH_USERNAME
SHEETY_AUTH_PASSWORD = config.SHEETY_AUTH_PASSWORD


class DataManager:
    """
    Interacts with Sheety API to GET, POST, PUT and DELETE data from a Google Sheet.
    """

    # class attributes (available to each and every instance)
    BASE_URL = SHEETY_BASE_URL
    DISPLAY_ENDPOINT = SHEETY_SHOW_ENDPOINT
    ADD_ENDPOINT = SHEETY_ADD_ENDPOINT
    edit_endpoint = SHEETY_EDIT_ENDPOINT
    USERNAME = SHEETY_AUTH_USERNAME
    PASSWORD = SHEETY_AUTH_PASSWORD

    def __init__(self):
        pass

    def get_desired_flight_deal_iata_code(self):
        pass

    def get_all_desired_flight_deal_iata_codes(self):
        url = self.BASE_URL + self.DISPLAY_ENDPOINT
        response = requests.get(
            url=url,
            auth=requests.auth.HTTPBasicAuth(
                username=self.USERNAME,
                password=self.PASSWORD
            )
        )
        response.raise_for_status()
        data = response.json()
        return [(data['prices'][index]['iataCode'], data['prices'][index]['lowestPrice'])
                for index in range(len(data['prices']))]

    def add_new_desired_flight_deal_information(self):
        pass

    def bulk_update_desired_flight_deals_information(self, city_airport_codes: dict):
        ordered_country_airport_codes = collections.OrderedDict(city_airport_codes)
        tuple_list_city_airport_codes = list(ordered_country_airport_codes.items())

        # for index in range(len(country_airport_codes)):
        # for index in range(2, len(country_airport_codes)):
        for index in range(2, len(city_airport_codes) + 2):
            # url = self.EDIT_ENDPOINT.format(index)
            # url = self.BASE_URL + self.edit_endpoint.format(index)
            # url = self.BASE_URL + self.edit_endpoint.format(object_id=index)  # object id starts from one - not zero
            # url = self.BASE_URL + self.edit_endpoint.format(object_id=index + 1)
            url = self.BASE_URL + self.edit_endpoint.format(object_id=index)
            # print(url)
            sheety_update_parameters = {
                'price': {
                    # 'city': 'Paris',
                    # 'iataCode': tuple_list_city_airport_codes[index][1],
                    'iataCode': tuple_list_city_airport_codes[index - 2][1],
                    # 'lowestPrice': 54
                }
            }
            # print(sheety_put_parameters)
            # response = requests.put(url=url, json=sheety_update_parameters,
            #                         auth=requests.auth.HTTPBasicAuth(self.USERNAME, self.PASSWORD))
            # print(self.USERNAME)
            # print(self.PASSWORD)
            response = requests.put(url=url, json=sheety_update_parameters, auth=(self.USERNAME, self.PASSWORD))
            response.raise_for_status()
            # print(response.status_code)
            # print(response.text)

    def update_desired_flight_deal_information(self):
        pass

    def delete_desired_flight_deal_information(self):
        pass
