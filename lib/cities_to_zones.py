# -*- coding: utf8 -*-
import json, requests

cities_json = open('cities.js')

CITY_LIST = json.load(cities_json)

from collections import defaultdict

cities_by_code = defaultdict(list)

for v in CITY_LIST:
    cities_by_code[v['value']].append(v['label'])

codes = cities_by_code.keys()

details_by_area_id = {}

for code in codes:
    r = requests.get('http://www.oref.org.il/Shared/Ajax/GetAreaName.aspx?lang=he&area=%s' % code)
    response_text = r.text.strip('\r\n')
    name, time_to_run = (v.strip('\r\n~') for v in response_text.split('\r\n'))
    print name
    area_id = [int(v) for v in name.split() if v.isdigit() or v == '-1']
    if len(area_id) > 1 or not area_id:
        print area_id
        raise 'whoops'
    else:
        area_id = area_id[0]

    details = {'fullname': name,
               'time': time_to_run,
               'cities': cities_by_code[code]
    }
    details_by_area_id[area_id] = details

    print details

fp = open('output.json', 'w')
json_s = json.dumps(details_by_area_id, ensure_ascii=False, sort_keys=True,
                    indent=4, separators=(',', ': ')).encode('utf8')
fp.write(json_s)
