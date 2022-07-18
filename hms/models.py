from django.db import models

# Create your models here.


class data(models.Model):
    firstName = models.CharField(max_length=122)
    lastName = models.CharField(max_length=122)
    age = models.CharField(max_length=122)
    sex = models.CharField(max_length=122)
    disease = models.CharField(max_length=122)
    phoneNumber = models.CharField(max_length=122)
    bloodGroup = models.CharField(max_length=122)
    doctorsName = models.CharField(max_length=122)

    def __str__(self):
        return self.firstName
