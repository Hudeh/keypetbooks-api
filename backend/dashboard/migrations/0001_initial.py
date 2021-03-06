# Generated by Django 3.1.7 on 2021-03-06 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CsvModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iso_code', models.CharField(blank=True, max_length=50, null=True)),
                ('continent', models.CharField(blank=True, max_length=50, null=True)),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('total_cases', models.IntegerField(blank=True, null=True)),
                ('new_cases', models.IntegerField(blank=True, null=True)),
                ('total_deaths', models.IntegerField(blank=True, null=True)),
                ('new_deaths', models.IntegerField(blank=True, null=True)),
                ('new_deaths_smoothed', models.IntegerField(blank=True, null=True)),
                ('total_cases_per_million', models.FloatField(blank=True, null=True)),
                ('new_cases_per_million', models.FloatField(blank=True, null=True)),
                ('new_cases_smoothed_per_million', models.FloatField(blank=True, null=True)),
                ('total_deaths_per_million', models.FloatField(blank=True, null=True)),
                ('new_deaths_per_million', models.FloatField(blank=True, null=True)),
                ('new_deaths_smoothed_per_million', models.FloatField(blank=True, null=True)),
                ('new_cases_smoothed', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
