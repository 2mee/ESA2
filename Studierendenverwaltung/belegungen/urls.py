#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'tzoulia'

from django.urls import path
from . import views

app_name = 'belegungen'
urlpatterns = [                  # urlpatterns += [] auch möglich
    # 127.0.0.1:8000/belegungen/
    path('', views.index, name='index'),

    # 127.0.0.1:8000/belegungen/2/
    path('<int:lv_id>/', views.modul_detail, name='modul_detail'),
    path('modulwahl/', views.modulwahl, name='modulwahl'),

    # 127.0.0.1:8000/belegungen/studenten
    path('studenten/', views.studenten_liste, name='studenten_liste'),
    path('studenten/<int:stud_id>/', views.student_detail, name='student_detail'),
    path('studenten/<int:stud_id>/studenten_verwalten/', views.studenten_verwalten, name='student_verwalten'),
    path('studenten/studenten_verwalten/', views.studenten_verwalten, name='studenten_verwalten'),

    # 127.0.0.1:8000/belegungen/results
    path('results/', views.results, name='results'),

]

