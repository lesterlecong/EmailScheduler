from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from email_updater import email_update


def start():
    print("Start scheduler")

    scheduler = BackgroundScheduler()
    scheduler.add_job(email_update.check_email, 'interval', minutes=1)
    scheduler.start()
