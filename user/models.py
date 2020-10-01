from django.db import models

class User(models.Model):
    user_no     = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=50, null=False)
    email       = models.EmailField(max_length=255, null=False)
    password    = models.CharField(max_length=50, null=False)
    is_deleted  = models.BooleanField(default=False)
    created_at  = models.DateTimeField(auto_now_add=True)
    last_access = models.DateTimeField(auto_now=True)

    class Meta:
        db_table='users'

class UserShippingDetail(models.Model):
    user_shipping_detail_no = models.AutoField(primary_key=True)
    user_id                 = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    receiver                = models.CharField(max_length=50, null=True)
    phone_number            = models.CharField(max_length=50, null=True)
    address                 = models.CharField(max_length=500, null=True)
    additional_address      = models.CharField(max_length=100, null=True)
    zip_code                = models.CharField(max_length=10, null=True)

    class Meta:
        db_table='user_shipping_details'
