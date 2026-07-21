from django.db import models

class Student(models.Model):

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    registration_number = models.CharField(max_length=30, unique=True)

    programme = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    def __str__(self):
        return self.first_name