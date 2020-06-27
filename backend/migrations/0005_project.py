# Generated by Django 3.0.7 on 2020-06-27 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20200627_1902'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('project_leader', models.CharField(max_length=255)),
                ('collaborators', models.CharField(max_length=255)),
                ('funding', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('overview', models.TextField()),
            ],
        ),
    ]
