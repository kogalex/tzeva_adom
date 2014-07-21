# -*- coding: utf8 -*-

import json, requests, time

cities_json = open('cities.js')

CITY_LIST = json.load(cities_json)




cities = [v['label'] for v in CITY_LIST]


cities_to_geocode = {}

for city in cities:
    r = requests.get(u'https://maps.googleapis.com/maps/api/geocode/json?address=%s, ישראל' % city)

    response = r.json()
    cities_to_geocode[city] = response
    print response

    time.sleep(0.1)

fp = open('city_geocode.json', 'w')
json_s = json.dumps(cities_to_geocode, ensure_ascii=False, sort_keys=True,
                    indent=4, separators=(',', ': ')).encode('utf8')
fp.write(json_s)
