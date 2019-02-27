# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Archives(models.Model):
    channel = models.CharField(max_length=50, blank=True, null=True)
    user = models.CharField(max_length=20, blank=True, null=True)
    token = models.CharField(max_length=100, blank=True, null=True)
    file = models.CharField(max_length=100, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    upload_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'archives'


class Circular(models.Model):
    game = models.CharField(max_length=20, blank=True, null=True)
    channel = models.CharField(max_length=20, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'circular'

    def __str__(self):
        return self.title


class IosOrder(models.Model):
    playerid = models.CharField(db_column='playerId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orderid = models.CharField(db_column='orderId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    propprice = models.DecimalField(db_column='propPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    channel = models.CharField(max_length=20, blank=True, null=True)
    rechargetime = models.DateTimeField(db_column='rechargeTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ios_order'


class Order(models.Model):
    playerid = models.CharField(db_column='playerId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orderid = models.CharField(db_column='orderId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    propname = models.CharField(db_column='propName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    propnumber = models.IntegerField(db_column='propNumber', blank=True, null=True)  # Field name made lowercase.
    propprice = models.DecimalField(db_column='propPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    channelcode = models.CharField(db_column='channelCode', max_length=64, blank=True, null=True)  # Field name made lowercase.
    channellabel = models.CharField(db_column='channelLabel', max_length=20, blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    rechargetime = models.DateTimeField(auto_now=True)  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)
    givingtime = models.DateTimeField(auto_now=True)  # Field name made lowercase.
    confirm = models.IntegerField(blank=True, null=True)
    confirmtime = models.DateTimeField(auto_now=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order'

    def __str__(self):
        return self.orderid


class OrderPp(models.Model):
    order_id = models.BigIntegerField(blank=True, null=True)
    billno = models.CharField(max_length=50, blank=True, null=True)
    account = models.CharField(max_length=50, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    app_id = models.IntegerField(blank=True, null=True)
    uuid = models.CharField(max_length=40, blank=True, null=True)
    roleid = models.CharField(max_length=50, blank=True, null=True)
    zone = models.IntegerField(blank=True, null=True)
    rechargetime = models.DateTimeField(db_column='rechargeTime', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)
    givingtime = models.DateTimeField(db_column='givingTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order_pp'
