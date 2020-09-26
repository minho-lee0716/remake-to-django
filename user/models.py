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
