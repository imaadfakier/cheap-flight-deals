# This class is responsible for sending notifications with the deal flight details.

from twilio.rest import Client
import config
import smtplib


class NotificationManager:
    """Sends an SMS and email notification containing the cheapest flight details."""

    # class attributes
    # ...

    def __init__(self):
        self.message = ''
        # self.send_sms_notification()

    def send_sms_notification(self, cheap_flight_details):
        client = Client(config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN)
        self.message = client.messages.create(
            body=f'Low price alert! Only £{cheap_flight_details[4]} to fly from '
                 f'{cheap_flight_details[0]}-{cheap_flight_details[1]} to '
                 f'{cheap_flight_details[2]}-{cheap_flight_details[3]}, from '
                 f'{cheap_flight_details[5]} to {cheap_flight_details[6]}.',
            from_='enter phone number',
            to='enter phone number',
        )
        return self.message.status

    def send_email_notification(self, cheap_flight_details):
        with smtplib.SMTP(host=config.SMTP_SERVER_ADDRESS) as connection:
            connection.starttls()
            connection.login(user=config.TEST_SENDER_EMAIL, password=config.TEST_SENDER_EMAIL_PASSWORD)
            email_subject_line = 'Subject:New Low Price Flight -> {departure_city} - {destination_city}! \n\n'\
                .format(
                    departure_city=cheap_flight_details[0],
                    destination_city=cheap_flight_details[2]
                )
            email_subject_line_unicode = email_subject_line.encode()  # utf-8 is the default encoding (type)
            flight_booking_link = f'https://www.google.co.uk/flights?hl=en#flt=' \
                                  f'{cheap_flight_details[1]}.{cheap_flight_details[3]}.' \
                                  f'{cheap_flight_details[5]}*{cheap_flight_details[3]}.' \
                                  f'{cheap_flight_details[1]}.{cheap_flight_details[6]}'
            # flight_booking_link_unicode = flight_booking_link.encode('utf-8')
            cheap_flight_info = 'Low price alert! Only \u00A3{flight_price} to fly from ' \
                                '{departure_city}-{departure_airport_iata_code} to ' \
                                '{destination_city}-{destination_airport_iata_code}, ' \
                                'from {outbound_date} to {inbound_date}.\n' \
                                '{flight_booking_link}' \
                .format(
                    flight_price=cheap_flight_details[4],
                    departure_city=cheap_flight_details[0],
                    departure_airport_iata_code=cheap_flight_details[1],
                    destination_city=cheap_flight_details[2],
                    destination_airport_iata_code=cheap_flight_details[3],
                    outbound_date=cheap_flight_details[5],
                    inbound_date=cheap_flight_details[6],
                    flight_booking_link=flight_booking_link
                )
            cheap_flight_info_unicode = cheap_flight_info.encode('utf-8')
            connection.sendmail(
                from_addr=config.TEST_SENDER_EMAIL,
                to_addrs=config.TEST_RECEIVER_EMAIL,
                msg=email_subject_line_unicode + cheap_flight_info_unicode
            )
        print('Email(s) sent.')
