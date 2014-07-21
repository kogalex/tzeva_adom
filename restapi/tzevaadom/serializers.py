from models import Area, City, Alarm
from rest_framework import serializers


class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ('url', 'name', 'area')

class AreaSerializer(serializers.HyperlinkedModelSerializer):
    cities = CitySerializer(many=True)
    class Meta:
        model = Area
        fields = ('url', 'name', 'time_to_run', 'cities', 'alarms')

class CitySmallSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ('name',)

class AreaSmallSerializer(serializers.HyperlinkedModelSerializer):
    cities = CitySmallSerializer(many=True)
    class Meta:
        model = Area
        fields = ('id', 'name', 'time_to_run', 'cities')


class AlarmSerializer(serializers.HyperlinkedModelSerializer):
    area = AreaSmallSerializer()
    class Meta:
        model = Alarm
        fields = ('url', 'started', 'area')