# Generated by Django 2.1.4 on 2018-12-14 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('belegungen', '0002_remove_lehrveranstaltung_stud'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studierendenliste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lehrveranstaltung', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='belegungen.Lehrveranstaltung')),
                ('studenten', models.ManyToManyField(to='belegungen.Student')),
            ],
        ),
    ]
