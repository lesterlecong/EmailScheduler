from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import datetime

class Email(models.Model):
    sender = models.CharField(max_length=150)
    receiver = models.CharField(max_length=150)
    subject = models.CharField(max_length=300)
    message = models.TextField()
    created_date = models.DateTimeField()
    is_triggered = models.BooleanField(default=False)
    send_schedule_date = models.DateTimeField(blank=True, null=True)


    def save(self):
        self.created_date = datetime.utcnow()
        return super(Email, self).save()

    def __str__(self):
        return self.subject
