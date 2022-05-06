from django.db import models
from . import constants as SV
from . import messages as MSG
from datetime import datetime, timedelta
from twilio.rest import Client

# Create your models here.
class Basemodel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Meeting(Basemodel):
    title = models.CharField(max_length=255)
    mettingId = models.CharField(max_length=255)
    passcode = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    content = models.TextField(null=True)
    messageSID = models.CharField(max_length=255, blank=True)

    def save(self):
        account_sid = SV.TWILIO_ACCOUNT_SID
        auth_token = SV.TWILIO_AUTH_TOKEN
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=MSG.METTING_MESSAGE.format(
                TOPIC=self.title, 
                DATE=self.date, 
                TIME=self.time, 
                URL=self.url, 
                METTINGID=self.mettingId,
                CONTENT=content, 
                PASSCODE=self.passcode
                ),
            from_=MSG.SMS_FROM,
            to='+918980145007'
        )
        self.messageSID = message.sid
        return super(Meeting, self).save()
