# This class is responsible for structuring the flight data.

class FlightData:
    """Responsible for structuring the flight data."""

    # class attributes
    # ...

    def __init__(self, flights_info):
        self.flights_data = flights_info
        # self.flights_data_per_city = [self.structure_file_data()]
        # print(self.flights_data_per_city)
        self.flights_data_per_city = []
        self.structure_file_data()

    def structure_file_data(self):
        for departure_airport, potential_flight_info in self.flights_data:
            try:
                city_from = potential_flight_info[0]['cityFrom']
                fly_from = potential_flight_info[0]['flyFrom']
                city_to = potential_flight_info[0]['cityTo']
                fly_to = potential_flight_info[0]['flyTo']
                flight_price = potential_flight_info[0]['price']
                flight_departure_date = potential_flight_info[0]['route'][0]['local_departure'].split('T').pop(0)
                flight_arrival_date = potential_flight_info[0]['route'][1]['local_arrival'].split('T').pop(0)
                self.flights_data_per_city.append(
                    (
                        city_from,
                        fly_from,
                        city_to,
                        fly_to,
                        flight_price,
                        flight_departure_date,
                        flight_arrival_date,
                    )
                )
            # except IndexError('List index out of range!') as e:  # TypeError: catching classes that do not inherit
                                                                   # from BaseException is not allowed
            except IndexError as e:
                print(f'No cheap flight available for LON -> {departure_airport}')
                continue

