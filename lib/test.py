import requests, logging, time, json

# create logger with 'spam_application'
logger = logging.getLogger('log')
logger.setLevel(logging.INFO)
# create file handler which logs even debug messages
fh = logging.FileHandler('reqs.log')
fh.setLevel(logging.INFO)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(message)s')
#fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

prev = None

while True:
	try:
		r = requests.get('http://www.oref.org.il/WarningMessages/alerts.json', timeout=1)
		j = r.json()
		current = json.dumps(j, ensure_ascii=False).encode('utf8')
		if prev != current:
			logger.info(current)
			prev = current

		time.sleep(1)
	except Exception, e:
		logger.error(e)
		time.sleep(1)