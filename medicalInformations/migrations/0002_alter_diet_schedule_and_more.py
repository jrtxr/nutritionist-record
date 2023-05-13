# Generated by Django 4.2.1 on 2023-05-12 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalInformations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diet',
            name='schedule',
            field=models.TimeField(blank=True, default='', max_length=50),
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='restrictions',
        ),
        migrations.AddField(
            model_name='medicalinformation',
            name='restrictions',
            field=models.ManyToManyField(to='medicalInformations.restriction'),
        ),
    ]
