from django.db import models


class Customer(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    phone = models.CharField(max_length=13)
    age = models.IntegerField()

    class Meta:
        db_table = "customers"
