
# Create your views here.

from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from .models import Lehrveranstaltung, Student


def index(request):  # Liste der verfügbaren Module
    lehrveranstaltungen = Lehrveranstaltung.objects.order_by('lv_name')
    context = {'page_title': 'Liste angebotener Lehrveranstaltungen',
               'lehrveranstaltungen': lehrveranstaltungen, }
    return render(request, 'belegungen/index.html', context)


def modul_detail(request, lv_id):  # zeigt welche Matrikelnummern zugehörig sind und zählt sie zusammen
    lv = get_object_or_404(Lehrveranstaltung, pk=lv_id)  # statt einen try block zu verwenden
    # lv = Lehrveranstaltung.objects.order_by('lv_name')
    # student = get_object_or_404(Student, pk=id)
    student = Student.objects.order_by('stud_name')
    return render(request, 'belegungen/modul_detail.html', {'page_title': lv.lv_name, 'lv': lv, 'student': student, })


def modulwahl(request):  # Belegungsseite für Module
    lv = Lehrveranstaltung()
    l_veranstaltungen = Lehrveranstaltung.objects.order_by('lv_name')
    # Prüfung ob das Formular schon abgeschickt wurde
    if request.method == 'POST':
        # Formular wurde abgeschickt
        form = ModulwahlForm(request.POST, instance=lv)
        if form.is_valid():
            auswahl = form.save(commit=False)
            auswahl.save()
            messages.success(request, u'Auswahl wurde gespeichert.')
            # 'Speichern erfolgt' ausgeben
            return HttpResponseRedirect(reverse('belegungen/index.html'))
        else:
            # Fehlermeldung
            messages.error(request, u'Eingabe konnte nicht gespeichert werden, bitte versuchen sie es erneut.')
            pass
    else:
        form = ModulwahlForm(instance=lv)
    return render(request, 'belegungen/modulwahl.html', {'page_title': 'Modulwahl', 'form': form,
                                                         'modul': l_veranstaltungen, })


    # try:
    #     selected_modul = Lehrveranstaltung.stud.student_set.get(pk=request.POST['modul'])
    # except(KeyError, Lehrveranstaltung.DoesNotExist):
    #     return render(request, 'belegungen/modulwahl.html',
    #                   {'lv': lv, 'error_message': "Bitte wählen Sie eine Lehrveranstaltung aus."})
    # else:
    #     selected_modul.lv_name += 1
    #     selected_modul.save()
    #     return HttpResponseRedirect(reverse('belegungen:results', args=(lv.id,)))


def student_detail(request, stud_id):  # zeigt Name, Vorname & Matrikelnummer und welche Kurse gewählt wurden
    stud = get_object_or_404(Student, pk=stud_id)  # statt einen try block zu verwenden
    # studi = Student.objects.order_by('stud_name')
    lv = Lehrveranstaltung.objects.order_by('lv_name')
    return render(request, 'belegungen/student_detail.html',
                  {'page_title': 'Student', 'name': stud.stud_name, 'vorname': stud.stud_vorname,
                   'matrikel': stud.matrikel_nr, 'studi': stud, 'lv': lv, })


def studenten_liste(request, pk=None):
    # anzeigen oder hinzufügen
    studi = Student.objects.order_by('stud_name')
    if pk == None:
        student = Student()
        page_title = "Studenten"
    else:
        student = get_object_or_404(Student, pk=pk)
        page_title = "Bearbeiten"

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Gespeichert')
            return HttpResponseRedirect(reverse('belegungen/studenten_liste'))
        else:
            messages.error(request, "Es ist ein Fehler aufgetreten!")
    else:
        form = StudentForm(instance=student)
        return render(request, 'belegungen/studenten_liste.html',
                      {'page_title': page_title, 'form': form, 'student': studi, })


# def studenten_verwalten(request, pk=None):
#     # anzeigen , löschen, ändern
#     studi = Student.objects.order_by('stud_name')
#     if pk == pk:
#         student = Student()
#         page_title = "Details bearbeiten"
#     else:
#         student = get_object_or_404(Student, pk=pk)
#         page_title = "Keine Daten vorhanden"
#
#     # if request.method == 'POST':
#     #     form = StudentForm(request.POST, instance=student)
#     #     if form.is_valid():
#     #         form.save()
#     #         messages.success(request, 'Gespeichert')
#     #         return HttpResponseRedirect(reverse('belegungen/studierendenListe'))
#     #     else:
#     #         messages.error(request, "Es ist ein Fehler aufgetreten!")
#     # else:
#     #     form = StudentForm(instance=student)
#     #     return render(request, 'belegungen/studenten_liste.html',
#     #                   {'page_title': page_title, 'form': form, 'student': student})
#     return render(request, 'belegungen/studenten_liste.html',
#                       {'page_title': page_title, 'student': studi, })


def results(request):
    lv = Lehrveranstaltung.objects.order_by('lv_name')
    # lv = get_object_or_404(Lehrveranstaltung, pk=id)
    # belegungsanzahl = 0
    counter = 0
    lv_details = Lehrveranstaltung.objects.order_by(pk=id)
    studi = Lehrveranstaltung.stud.count()
    for l in lv_details:
        for s in studi:
            counter = studi(s)
        print(counter(l))

    # for l in belegungen:
    #     count += 1
    #     belegungsanzahl = count(l)
    #     return str(belegungsanzahl)

    return render(request, 'belegungen/results.html', {'page_title': 'Belegungen pro Lehrveranstaltung',
                                                       'lehrveranstaltungen': lv,
                                                       'counter': counter, 'student': studi, })

