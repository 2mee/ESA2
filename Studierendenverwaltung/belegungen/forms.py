#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'tzoulia'

from django.forms import *
from belegungen.models import *


class ModulwahlForm(ModelForm):
    class Meta:
        model = Lehrveranstaltung
        fields = '__all__'
