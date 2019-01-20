
# Create your views here.

from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from .models import Lehrveranstaltung, Student


def index(request):  # Liste der verfügbaren Module
    lehrveranstaltungen = Lehrveranstaltung.objects.order_by('lv_name')
    return render(request, 'belegungen/index.html', {'lehrveranstaltungen': lehrveranstaltungen, })


def modul_detail(request, lv_id):  # zeigt welche Matrikelnummern zugehörig sind und zählt sie zusammen
    lv = get_object_or_404(Lehrveranstaltung, pk=lv_id)  # statt einen try block zu verwenden
    # lv = Lehrveranstaltung.objects.order_by('lv_name')
    # student = get_object_or_404(Student, pk=id)
    student = Student.objects.order_by('stud_name')
    return render(request, 'belegungen/modul_detail.html', {'page_title': lv.lv_name, 'lv': lv, 'student': student, })


def modul_verwalten(request, pk=None):
    lehrveranstaltungen = Lehrveranstaltung.objects.order_by('lv_name')
    if pk == None:
        lv = Lehrveranstaltung()
        page_title = 'Lehrveranstaltung hinzufügen'
    else:
        lv = get_object_or_404(Lehrveranstaltung, pk=pk)
        page_title = 'Lehrveranstaltung bearbeiten'

    if request.method == 'POST':
        form = ModulwahlForm(request.POST, instance=lv)
        if form.is_valid():
            form.save()
            messages.success(request, 'Gespeichert')
            return HttpResponseRedirect(reverse('belegungen:index'))
        else:
            messages.error(request, 'Es ist ein Fehler aufgetaucht!')
    else:
        form = ModulwahlForm(instance=lv)

    return render(request, 'belegungen/modul_verwalten.html', {'page_title': page_title, 'form': form, 'lv': lehrveranstaltungen})


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
            # Mitteilung über erfolgte Speicherung
            messages.success(request, 'Auswahl wurde gespeichert.')

            return HttpResponseRedirect(reverse('belegungen/index.html'))
        else:
            # Fehlermeldung
            messages.error(request, 'Eingabe konnte nicht gespeichert werden, bitte versuchen sie es erneut.')
            pass
    else:
        form = ModulwahlForm(instance=lv)
    return render(request, 'belegungen/modulwahl.html', {'page_title': 'Modulwahl', 'form': form,
                                                         'modul': l_veranstaltungen, })


def modul_entfernen(request, pk):
    modul = get_object_or_404(Lehrveranstaltung, pk=pk)
    if request.method == 'POST':
        modul.delete()
        messages.success(request, 'Die Lehrveranstaltung wurde gelöscht')
        return redirect('belegungen:modulList')
    return render(request, 'belegungen/modul_entfernen.html', {'modul': modul, })


def student_detail(request, stud_id):  # zeigt Name, Vorname & Matrikelnummer und welche Kurse gewählt wurden
    stud = get_object_or_404(Student, pk=stud_id)
    lv = Lehrveranstaltung.objects.order_by('lv_name')
    if request.method == 'POST':
        messages.info(request, 'Der Student wurde aus der Datenbank entfernt.')
        # return student_entfernen(request, pk='stud_id')
        return render(request, 'belegungen/student_detail.html', {'pk': stud.pk, })
    else:
        return render(request, 'belegungen/student_detail.html',
                      {'page_title': 'Student', 'name': stud.stud_name, 'vorname': stud.stud_vorname,
                       'matrikel': stud.matrikel_nr, 'studi': stud, 'lv': lv, 'pk': stud.pk, })


def studenten_liste(request):
    # anzeigen aller Studenten
    studi = Student.objects.order_by('stud_name')  # benötigt um die Studenten aufzulisten
    return render(request, 'belegungen/studenten_liste.html', {'page_title': 'Studenten', 'studi': studi, })


def studenten_verwalten(request):
    # anzeigen, ändern
    studi = Student.objects.order_by('stud_name')
    page_title = "Student hinzufügen"
    student = Student()

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        # Bei Gültigkeit der Formulardaten speichern und bestätigen
        if form.is_valid():
            form.save()
            messages.success(request, 'Gespeichert')
            return HttpResponseRedirect(reverse('belegungen:studenten_liste'))
        # sonst Fehlermeldung
        else:
            messages.error(request, "Es ist ein Fehler aufgetreten!")
    # liegen keine Daten vor, Formular zur Verfügung stellen
    else:
        page_title = "Student bearbeiten"
        form = StudentForm(instance=student)

        # return studenten_verwalten(request, pk=None)

    return render(request, 'belegungen/studenten_verwalten.html',
                  {'page_title': page_title, 'form': form, 'student': studi, })


def student_entfernen(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student wurde gelöscht')
        return redirect('belegungen:studenten_liste')
    return render(request, 'belegungen/student_entfernen.html', {'student': student, })
