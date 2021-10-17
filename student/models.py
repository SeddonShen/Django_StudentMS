from django.db import models

# Create your models here.
class Student(models.Model):
    num = models.CharField(max_length=7)
    name = models.CharField(max_length=30)
    chinese = models.IntegerField()
    math = models.IntegerField()
    english = models.IntegerField()
    physics = models.IntegerField()
    chemistry = models.IntegerField()
    allscore = models.IntegerField()