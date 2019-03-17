import requests
import json
import datetime
from sqlalchemy.sql import func

api_key = ''

url = f'http://developer.itsmarta.com/RealtimeTrain/RestServiceNextTrain/GetRealtimeArrivals?apikey={api_key}'
response = requests.get(url)

if response.status_code == 401 or response.status_code == 403:
        raise Exception('Your API key seems to be invalid.')


if response.status_code == 200:
	data = json.loads(response.text)
	print(data)




#parse the event_time
event_time = datetime.datetime.strptime(event_time, '%m/%d/%Y %I:%M:%S %p')



#parse the next arrival time
next_arrival = datetime.datetime.strptime(event_time, '%I:%M:%S %p')





