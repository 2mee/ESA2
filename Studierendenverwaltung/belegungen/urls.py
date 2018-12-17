#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'tzoulia'

from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'belegungen'
urlpatterns = [                  # urlpatterns += [] auch möglich
    # 127.0.0.1:8000/belegungen/
    path('', views.index, name='index'),
    # 127.0.0.1:8000/belegungen/2/
    path('<int:lv_id>/', views.modul_detail, name='modul_detail'),
    path('<int:lv_id>/', views.modulwahl, name='modulwahl'),
    # path('student_detail/', views.student_detail, name='student_detail'),
    # 127.0.0.1:8000/belegungen/results
    path('results/', views.results, name='results'),
    # 127.0.0.1:8000/belegungen/belegungsanzahl
    path('belegungsanzahl/', views.belegungsanzahl, name='belegungsanzahl'),

]
