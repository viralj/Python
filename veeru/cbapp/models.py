from django.db import models

# Create your models here.
class CBTransferBTC(models.Model):
    uid = models.IntegerField()
    process_time = models.DateTimeField(auto_now_add=True)
    game = models.CharField(max_length=10)
    amount_amount = models.CharField(max_length=250)
    amount_currency = models.CharField(max_length=10)
    created_at = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    details_subtitle = models.CharField(max_length=250)
    details_title = models.CharField(max_length=250)
    tr_id = models.CharField(max_length=250)
    instant_exchange = models.CharField(max_length=250)
    native_amount_amount = models.CharField(max_length=250)
    native_amount_currency = models.CharField(max_length=250)
    resource = models.CharField(max_length=250)
    resource_path = models.CharField(max_length=250)
    status = models.CharField(max_length=250)
    to_id = models.CharField(max_length=250)
    to_resource = models.CharField(max_length=250)
    to_resource_path = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    updated_at = models.CharField(max_length=250)


class PayOutCreated(models.Model):
    current_month = models.CharField(max_length=20)
    current_year = models.CharField(max_length=20)
    status = models.IntegerField()