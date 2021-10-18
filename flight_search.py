# This class is responsible for talking to the Flight Search API.

import requests
import datetime
import config
import data_manager
import collections
import pprint

KIWI_FLIGHT_SEARCH_BASE_URL = 'enter base url'
FLIGHT_SEARCH_ENDPOINT = 'enter search endpoint'
KIWI_HEADERS = {
    'apikey': config.KIWI_API_KEY
}

# flight_info = dict()
# flight_info = collections.defaultdict()
# airports_with_flights_info = tuple()
airports_with_flights_info = list()

class FlightSearch:
    """Sends requests to the Flight Search (Web) Server via the Flight Search
    API to check for the cheapest flights between two cities from a specified
    point in time to another point in time"""

    # class attributes
    BASE_URL = KIWI_FLIGHT_SEARCH_BASE_URL
    ENDPOINT = FLIGHT_SEARCH_ENDPOINT
    HEADERS = KIWI_HEADERS

    def __init__(self, data_manager_obj: data_manager.DataManager):
        self.url = self.BASE_URL + self.ENDPOINT
        self.data_manager_instance = data_manager_obj

    def get_flights_info(self, date_from: datetime, date_to: datetime,
                         nights_in_dst_from: int, nights_in_dst_to: int,
                         max_stopovers=0, via_city='') -> tuple:
        airports_with_prices = self.data_manager_instance.get_all_desired_flight_deal_iata_codes()

        for destination_airport, desired_price_max in airports_with_prices:
            kiwi_flight_search_parameters = {
                'fly_from': 'LON',
                'fly_to': destination_airport,
                'date_from': date_from.strftime('%d/%m/%Y'),
                'date_to': date_to.strftime(format('%d/%m/%Y')),
                'nights_in_dst_from': nights_in_dst_from,
                'nights_in_dst_to': nights_in_dst_to,
                'flight_type': 'round',
                'one_for_city': 1,
                'price_to': desired_price_max - 1,
                'curr': 'GBP',
                'max_stopovers': 1,
            }

            response = requests.get(url=self.url, params=kiwi_flight_search_parameters, headers=self.HEADERS)
            response.raise_for_status()
            flight_info = response.json()['data']  # MUST BE CHANGED WHEN YOU REFACTOR (HINT: ADD EXCEPTION HANDLING)
            airports_with_flights_info.append((destination_airport, flight_info))

        return tuple(airports_with_flights_info)
