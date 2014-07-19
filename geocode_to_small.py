# -*- coding: utf8 -*-

import json, requests, time

cities_json = open('city_geocode.json')

CITY_LIST = json.load(cities_json)

cities_to_geocode = {}

for k, v in CITY_LIST.items():
    if v['status'] == 'OK':
        try:
            cities_to_geocode[k] = v['results'][0]['geometry']['location']
        except Exception:
            raise

fp = open('city_geocode_small.json', 'w')
json_s = json.dumps(cities_to_geocode, ensure_ascii=False).encode('utf8')
fp.write(json_s)
