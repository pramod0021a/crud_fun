from django.db import models


class Student(models.Model):
   name = models.CharField(max_length=100)
   age = models.PositiveIntegerField()
   location = models.CharField(max_length=200)

   def __str__(self):
      return str(self.name)