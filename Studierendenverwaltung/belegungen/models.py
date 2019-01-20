# Lehrveranstaltungen können angelegt, angezeigt, gelöscht und geändert werden.
# Studierende können angelegt, angezeigt, gelöscht und geändert werden.
# Studierende können sich für Lehrveranstaltungen einschreiben.
# Je Lehrveranstaltung wird die Liste der eingeschriebenen Studierenden angezeigt.

# Create your models here.
from django.db import models


class Student(models.Model):
    matrikel_nr = models.IntegerField(default=None)
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




