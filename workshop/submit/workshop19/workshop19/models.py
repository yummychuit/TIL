from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    birthday = models.IntegerField()
    age = models.IntegerField(default=20)
    
    def __str__(self):
        return f'{self.id}: {self.name}'