from email_scheduler_app.models import Email
from datetime import datetime
from django.utils import timezone
import pytz
from .email_sender import send_email

def check_email():
    print("Check email")
    emails = Email.objects.filter(is_triggered=False)
    utc=pytz.UTC
    for email in emails:
        if email.send_schedule_date.replace(tzinfo=utc) <= datetime.now().replace(tzinfo=utc):
            print("Sending email with subject:", email.subject)
            result = send_email(email)
            if result == 0:
                email.is_triggered = True
                email.save()
        #print(email.send_schedule_date)
