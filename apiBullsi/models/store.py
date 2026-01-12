from django.db import models

class Store(models.Model):
    id = models.AutoField(primary_key=True)
    name  = models.CharField(max_length=100, unique=True, null=False)
    address = models.CharField( max_length=255, null=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.IntegerField(null=False)

    def __str__(self):
        return self.name
