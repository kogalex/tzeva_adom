# -*- coding: utf8 -*-

import json, requests, time

cities_json = open('output.json')

data = json.load(cities_json)

fixtures = []
time_map = {u"45 שניות": 45, u"30 שניות":30, u"3 דקות":180, u"דקה":60, u"-1":1, u"מיידי":1, u"דקה וחצי":90, u"15 שניות":15}


for k, v in data.items():
    area = {
        "model": "tzevaadom.area",
        "pk": int(k),
        "fields": {
            "name": v['fullname'],
            "time_to_run": time_map[v['time']],
        }
    }
    cities = [{
        "model": "tzevaadom.city",
        "pk": city,
        "fields": {
            "area": int(k),
        }
    } for city in v['cities']]
    fixtures.append(area)
    fixtures.extend(cities)

fp = open('fixtures.json', 'w')
json.dump(fixtures, fp)
