# Register your models here.

from django.contrib import admin
from .models import Lehrveranstaltung, Student

admin.site.register(Lehrveranstaltung)
admin.site.register(Student)

