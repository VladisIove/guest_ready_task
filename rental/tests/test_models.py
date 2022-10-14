from datetime import datetime
from unittest import TestCase

from django.conf import settings
from django.core.management import call_command

from rental.models import Rental, Reservation


class ReservationTestCase(TestCase):
    databases = settings.DATABASES
    DATE_FORMAT = "%Y-%m-%d"

    def test_get_reservation_report_without_reservation(self):
        Rental.objects.all().delete()
        Reservation.objects.all().delete()
        reservation_report = Reservation.get_reservation_report()
        self.assertEqual(reservation_report, [])
        
    def test_get_reservation_report_with_reservation(self):
        call_command('loaddata', './rental/fixtures/test_data.json', verbosity=0)
        reservation_report = Reservation.get_reservation_report()
        
        _reservation_report = [
            {
                'id': 1,
                'checkin': datetime.strptime('2022-01-01', self.DATE_FORMAT).date(),
                'checkout': datetime.strptime('2022-01-13', self.DATE_FORMAT).date(),
                'rental__name': 'rental-1',
                'previous_reservation_id': None
            },
            {
                'id': 2,
                'checkin': datetime.strptime('2022-01-20', self.DATE_FORMAT).date(),
                'checkout': datetime.strptime('2022-02-10', self.DATE_FORMAT).date(),
                'rental__name': 'rental-1',
                'previous_reservation_id': 1
            }, 
            {
                'id': 3,
                'checkin': datetime.strptime('2022-02-20', self.DATE_FORMAT).date(),
                'checkout': datetime.strptime('2022-03-10', self.DATE_FORMAT).date(),
                'rental__name': 'rental-1',
                'previous_reservation_id': 2
            }, 
            {
                'id': 4,
                'checkin': datetime.strptime('2022-01-02', self.DATE_FORMAT).date(),
                'checkout': datetime.strptime('2022-01-20', self.DATE_FORMAT).date(),
                'rental__name': 'rental-2', 
                'previous_reservation_id': None
            }, 
            {
                'id': 5, 
                'checkin': datetime.strptime('2022-01-20', self.DATE_FORMAT).date(), 
                'checkout': datetime.strptime('2022-02-11', self.DATE_FORMAT).date(), 
                'rental__name': 'rental-2', 
                'previous_reservation_id': 4
            }
        ]
        self.assertEqual(reservation_report, _reservation_report)
