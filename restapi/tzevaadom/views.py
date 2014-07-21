from rest_framework import viewsets
from serializers import AlarmSerializer, AreaSerializer, CitySerializer
from models import Area, City, Alarm


class AreaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class CityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = City.objects.all()
    serializer_class = CitySerializer


class AlarmViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Alarm.objects.all()
    serializer_class = AlarmSerializer

