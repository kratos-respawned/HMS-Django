from django.db import models

# Create your models here.
class data(models.Model):
    name=models.CharField(max_length=122)
    sex=models.CharField(max_length=122)
    doctor_name=models.CharField(max_length=122)
    disease=models.CharField(max_length=122)
    age=models.CharField(max_length=122)
    blood_group=models.CharField(max_length=122)
    mail=models.CharField(max_length=122)
    def __str__(self):
        return self.name 