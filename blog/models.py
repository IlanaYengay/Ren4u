from django.db import models
from django.contrib.auth.models import AbstractUser


class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=455)
    image = models.ImageField(upload_to='blogs')
    date = models.DateField()

    def __str__(self):
        return self.title


class Feedback(models.Model):
    CHOICES = (
        ('male', 'Мужчина'),
        ('female', 'Женщина')

    )
    text = models.CharField(max_length=500)
    gender = models.CharField(choices=CHOICES, max_length=6)
    name = models.CharField(max_length=20)
    profession = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Callback(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


class CarMake(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Car(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    bio = models.TextField()
    model = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='cars')

    def __str__(self):
        return f"{self.year} {self.make.name} {self.model}"

