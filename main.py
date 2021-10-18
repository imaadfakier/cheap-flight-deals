# This file will need to use the DataManager, FlightSearch,
# FlightData, NotificationManager classes to achieve the program requirements.

import requests
import data_manager, \
    flight_data, \
    flight_search, \
    notification_manager
import config
import collections
import datetime

# --- kiwi api
CITIES = ['Paris', 'Berlin', 'Tokyo', 'Sydney', 'Istanbul', 'Kuala Lumpur', 'New York', 'San Francisco', 'Cape Town']
KIWI_API_KEY = config.KIWI_API_KEY
KIWI_BASE_URL = 'enter base url'
KIWI_LOCATIONS_ENDPOINT = 'enter locations endpoint'

kiwi_locations_url = KIWI_BASE_URL + KIWI_LOCATIONS_ENDPOINT

kiwi_locations_parameters = {
    'term': ''
}

kiwi_locations_headers = {
    'apikey': KIWI_API_KEY
}

IATA_CODES = collections.defaultdict()
# print(IATA_CODES)

for city in CITIES:
    kiwi_locations_parameters['term'] = city
    response = requests.get(url=kiwi_locations_url, params=kiwi_locations_parameters, headers=kiwi_locations_headers)
    iata_code = response.json()['locations'][0]['code']
    IATA_CODES[city] = iata_code
# ---

data_manager = data_manager.DataManager()
# data_manager.bulk_update_desired_flight_deals_information(IATA_CODES)

flight_search = flight_search.FlightSearch(data_manager_obj=data_manager)
flights_info = flight_search.get_flights_info(
    date_from=datetime.date.today(),
    date_to=datetime.date.today() + datetime.timedelta(weeks=6),
    nights_in_dst_from=7,
    nights_in_dst_to=28,
    max_stopovers=1,
    via_city='Ho Chi Minh'
)
# print(flights_info)

flight_data = flight_data.FlightData(flights_info)

if len(flight_data.flights_data_per_city) > 0:
    notification_manager = notification_manager.NotificationManager()

    for cheap_flight_info in flight_data.flights_data_per_city:
        notification_manager.send_sms_notification(cheap_flight_info)
        notification_manager.send_email_notification(cheap_flight_info)
else:
    print('No available flights.')
