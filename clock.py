from datetime import datetime
from proj import sendMessage

from apscheduler.schedulers.blocking import BlockingScheduler

sendMessage()
def job_function():
    sendMessage()

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(job_function, 'interval', hours=2)

sched.start()