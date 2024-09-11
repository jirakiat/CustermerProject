from django.db import models

from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_title_name = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    customer_nickname = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=10)
    customer_email = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.customer_name


class CustomerLocation(models.Model):
    customer_location_id = models.AutoField(primary_key=True)
    customer_province = models.CharField(max_length=100)
    customer_district = models.CharField(max_length=100)
    customer_canton = models.CharField(max_length=100)
    customer_postal_number = models.CharField(max_length=10)
    customer_house_number = models.CharField(max_length=10)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # ใช้ customer แทน customer_id

    def __str__(self):
        return f"{self.customer.customer_name} - {self.customer_province}"
