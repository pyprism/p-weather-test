from django.test import TestCase
from unittest import mock

from rest_framework.reverse import reverse


class TestWeatherAPI(TestCase):

    def test_get_weather_data(self):
        with mock.patch('weather.views.get_weather_data') as mock_get:
            response_data = {
                "current_temperature": "3.1°C",
                "current_pressure": 1033,
                "current_humidity": 86
            }
            mock_get.return_value = response_data

            response = self.client.get(reverse('get_city_weather'), {'city': 'London'})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), response_data)

    @mock.patch('weather.utils')
    def test_get_current_weather_util(self, mock_utils):
        return_value = {
            "current_temperature": "8.89°C",
            "current_pressure": 1022,
            "current_humidity": 85
        }
        mock_utils.get_weather_data.return_value = return_value
        mock_utils.get_weather_data.called_once_with('Chittagong')
        self.assertEqual(mock_utils.get_weather_data.return_value, return_value)
