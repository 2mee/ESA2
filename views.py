
# Create your views here.

from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Lehrveranstaltung, Student


def index(request):  # Liste der verfügbaren Module
    lehrveranstaltungen = Lehrveranstaltung.objects.order_by('lv_name')
    context = {'lehrveranstaltungen': lehrveranstaltungen, }
    return render(request, 'belegungen/index.html', context)


def modul_detail(request, lv_id):  # zeigt welche Matrikelnummern zugehörig sind und zählt sie zusammen
    lv = get_object_or_404(Lehrveranstaltung, pk=lv_id)  # statt einen try block zu verwenden
    return render(request, 'belegungen/modul_detail.html', {'lv': lv})


def modulwahl(request, lv_id):  # Belegungsseite für Module
    # latest_lehrveranstaltungen = Lehrveranstaltung.objects.order_by('lv_name')
    # context = {'latest_lehrveranstaltungen': latest_lehrveranstaltungen, }
    # return render(request, 'belegungen/modul_detail.html', context)

    try:
        selected_modul = lv.student_set.get(pk=request.POST['modul'])
    except(KeyError, Lehrveranstaltung.DoesNotExist):
        return render(request, 'belegungen/modulwahl.html',
                      {'lv': lv, 'error_message': "Bitte wählen Sie eine Lehrveranstaltung aus."})
    else:
        selected_modul.lv_name += 1
        selected_modul.save()
        return HttpResponseRedirect(reverse('belegungen:results', args=(lv.id,)))


# def student_detail(request, stud_id):  # zeigt Name, Vorname & Matrikelnummer und welche Kurse gewählt wurden
#     studi = get_object_or_404(Student, pk=stud_id)  # statt einen try block zu verwenden
#     modul = Lehrveranstaltung.objects.order_by('lv_name')
#     return render(request, 'belegungen/student_detail.html', {'studi': studi, 'modul': modul})


def results(request, lv_id):
    lv = get_object_or_404(Lehrveranstaltung, pk=lv_id)
    return render(request, 'belegungen/results.html', {'lv': lv})


def belegungsanzahl(request, count):  # Übersicht aller Belegungen
    # lv = get_object_or_404(Lehrveranstaltung, pk=lv_id)
    belegungen = Lehrveranstaltung.objects.All()
    for l in belegungen:
        count += 1
        return count(l)
    return HttpResponseRedirect(reverse('belegungen:results', args=(count,)))
