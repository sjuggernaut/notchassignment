from django.db import models
import uuid
from datetime import datetime


class Event(models.Model):
    """
    Model for Event
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    createdAt = models.IntegerField()
    email = models.EmailField(max_length=45)
    environment = models.CharField(max_length=15)
    component = models.CharField(max_length=15)
    message = models.TextField()
    data = models.TextField()

    def get_created_date(self):
        """
        Convert epoch timestamp to date format
        :return:
        """
        created_date_str = datetime.utcfromtimestamp(self.createdAt).strftime('%m-%d-%Y')
        return datetime.strptime(created_date_str, "%m-%d-%Y").date()
