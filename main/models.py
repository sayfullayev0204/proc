from django.db import models
from django.contrib.auth.models import User

class Tashkilot(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Tuman(models.Model):
    tashkilot = models.ForeignKey(Tashkilot, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Mahalla(models.Model):
    tuman = models.ForeignKey(Tuman, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Xizmatlar(models.Model):
    mahalla = models.ForeignKey(Mahalla, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Axoli(models.Model):
    xizmat = models.ForeignKey(Xizmatlar, on_delete=models.CASCADE)
    mahalla = models.ForeignKey(Mahalla, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=225)
    status = models.CharField(max_length=225)
    discreption = models.TextField()
    passport = models.CharField(max_length=255)
    

    def __str__(self):
        return self.name
