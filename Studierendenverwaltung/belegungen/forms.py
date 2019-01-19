#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'tzoulia'

from django.forms import *
from belegungen.models import *


class ModulwahlForm(ModelForm):
    class Meta:
        model = Lehrveranstaltung
        labels = {
            'lv_nr': 'Nummer Lehrveranstaltung',
            'lv_name': 'Name Lehrveranstaltung',
            'doz_name': 'Name des Dozenten',
        }
        fields = ['lv_nr', 'lv_name']


class StudentForm(ModelForm):
    class Meta:
        model = Student
        labels = {
            'matrikel_nr': 'Matrikelnummer',
            'stud_name': 'Name',
            'stud_vorname': 'Vorname',
        }
        fields = ['matrikel_nr', 'stud_name', 'stud_vorname']
