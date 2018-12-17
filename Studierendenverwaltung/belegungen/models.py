
# Create your models here.
from django.db import models


class Studierendenliste(models.Model):
    lehrveranstaltung = models.ForeignKey('Lehrveranstaltung', on_delete=models.CASCADE)
    studenten = models.ManyToManyField('Student')

    def __str__(self):
        return "{}, {}".format(self.lehrveranstaltung, self.studenten)


class Student(models.Model):
    matrikel_nr = models.IntegerField(default=0)
    stud_name = models.CharField(max_length=150)
    stud_vorname = models.CharField(max_length=150)

    def __str__(self):
        return "{}, {}, {}".format(self.matrikel_nr, self.stud_name, self.stud_vorname)


class Lehrveranstaltung(models.Model):
    lv_nr = models.IntegerField(default=100)
    lv_name = models.CharField(max_length=200)
    doz_name = models.CharField(max_length=150)
    stud = models.ManyToManyField(Student)
    objects = models.Manager()

    def __str__(self):
        return self.lv_name
