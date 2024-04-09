from django.db import models


class Car(models.Model):
    FUEL_TYPE_CHOICES = (
        ('GASOLINE', 'GASOLINE'),
        ('ALCOHOL', 'ALCOHOL'),
        ('DIESEL', 'DIESEL')
    )

    CAR_TYPE_CHOICES = (
        ('AUTOMATIC', 'AUTOMATIC'),
        ('MANUAL', 'MANUAL'),
    )

    car_id = models.UUIDField(primary_key=True, null=False, blank=False, auto_created=True)
    brand = models.CharField(max_length=64)
    car_year = models.IntegerField()
    color = models.CharField(max_length=10)
    description = models.TextField(max_length=1024)
    fuel = models.CharField(max_length=10, choices=FUEL_TYPE_CHOICES)
    kilometers = models.DecimalField(decimal_places=2, max_digits=10)
    motor_detail = models.TextField(max_length=256)
    car_type = models.CharField(max_length=10, choices=CAR_TYPE_CHOICES)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    version = models.CharField(max_length=24)
    model = models.CharField(max_length=20, blank=True, null=True)

    photo_car = models.ImageField(upload_to='photos/')
