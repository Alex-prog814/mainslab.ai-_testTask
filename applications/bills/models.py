from django.db import models


class Bill(models.Model):
    client_name = models.CharField(max_length=255)
    client_org = models.CharField(max_length=255)
    bill_num = models.IntegerField()
    bill_sum = models.FloatField()
    date = models.DateField()
    service = models.TextField()
