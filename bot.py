from apscheduler.schedulers.blocking import BlockingScheduler
from dotenv import load_dotenv
import os
import requests as r

load_dotenv()

sched = BlockingScheduler()

API_KEY = os.getenv('API_KEY')
print(API_KEY)

@sched.scheduled_job('interval', minutes=20)
def send_req():
	r.get(API_KEY)
	return

sched.start()