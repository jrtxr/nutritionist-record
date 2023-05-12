# Generated by Django 4.2.1 on 2023-05-12 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('dateBirth', models.DateTimeField(blank=True, max_length=100)),
                ('maritalStatus', models.CharField(blank=True, default='', max_length=50)),
                ('IntestinalTransit', models.CharField(blank=True, default='', max_length=50)),
                ('escalaBristol', models.IntegerField(blank=True)),
                ('sleepQuality', models.CharField(blank=True, default='', max_length=100)),
                ('Weight', models.FloatField(blank=True)),
                ('height', models.FloatField(blank=True)),
                ('UrinaryStaining', models.IntegerField(blank=True)),
                ('genre', models.CharField(blank=True, default='', max_length=20)),
                ('profession', models.CharField(blank=True, default='', max_length=50)),
                ('clinicalHistory', models.TextField(blank=True, default='', max_length=100)),
                ('objective', models.TextField(blank=True, default='', max_length=100)),
            ],
        ),
    ]