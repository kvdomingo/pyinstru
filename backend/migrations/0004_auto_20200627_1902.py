# Generated by Django 3.0.7 on 2020-06-27 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20200627_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='suffix',
            field=models.CharField(blank=True, max_length=16),
        ),
        migrations.AlterField(
            model_name='member',
            name='middle_name',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
