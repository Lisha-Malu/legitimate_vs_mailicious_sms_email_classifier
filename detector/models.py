# detector/models.py
from django.db import models

class PredictionLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    message_type = models.CharField(max_length=20)   # 'SMS' or 'Email'
    classification = models.CharField(max_length=50) # 'Spam' / 'Legitimate' / 'Phishing'
    content = models.TextField()
    summary = models.CharField(max_length=255, blank=True)

    def preview(self):
        return (self.content[:200] + '...') if len(self.content) > 200 else self.content

    def _str_(self):
        return f"{self.timestamp} | {self.message_type} | {self.classification}"