# Generated by Django 4.2.1 on 2023-05-12 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0004_patient_personalinformations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='personalInformations',
        ),
    ]