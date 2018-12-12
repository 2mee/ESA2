
# Create your models here.
from django.db import models


class Lehrveranstaltung(models.Model):
    lv_nr = models.IntegerField(default=100)
    lv_name = models.CharField(max_length=200)
    doz_name = models.CharField(max_length=150)
    stud = models.ForeignKey('Student', on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.lv_name


class Student(models.Model):
    matrikel_nr = models.IntegerField(default=0)
    stud_name = models.CharField(max_length=150)
    stud_vorname = models.CharField(max_length=150)
    lv = models.ForeignKey(Lehrveranstaltung, on_delete=models.CASCADE)

    def __str__(self):
        return self.stud_name

