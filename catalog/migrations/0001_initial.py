# Generated by Django 2.0.2 on 2018-03-09 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BigFootReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_number', models.IntegerField(default=0)),
                ('report_class', models.CharField(max_length=200)),
                ('county', models.CharField(max_length=200)),
                ('season', models.CharField(max_length=200)),
                ('location_details', models.TextField(max_length=1000)),
                ('other_witnesses', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=20)),
                ('observed', models.TextField(max_length=2000)),
                ('time_and_conditions', models.TextField(max_length=1000)),
                ('also_noticed', models.TextField(max_length=1000)),
                ('other_stories', models.TextField(max_length=1000)),
                ('nearest_town', models.CharField(max_length=100)),
                ('nearest_road', models.CharField(max_length=100)),
                ('environment', models.CharField(max_length=500)),
                ('month', models.CharField(max_length=20)),
                ('date', models.CharField(max_length=20)),
                ('a_g_references', models.CharField(max_length=200)),
            ],
        ),
    ]
