from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from weather.utils import get_weather_data


class CityWeather(APIView):

    def get(self, request):
        city = request.GET.get('city', None)
        if city:
            city_weather = get_weather_data(city)
            if city_weather:
                return Response(city_weather, status=status.HTTP_200_OK)
        return Response({"error": "City was not found"}, status=status.HTTP_404_NOT_FOUND)
