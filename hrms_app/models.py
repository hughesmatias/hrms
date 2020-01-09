from django.db import models

# Create your models here.
class Person(models.Model):
  firstName = models.CharField(max_length=30)
  lastName = models.CharField(max_length=30)

  def __str__(self):
    return self.firstName + " " + self.lastName