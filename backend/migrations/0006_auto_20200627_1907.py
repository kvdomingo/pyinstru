# Generated by Django 3.0.7 on 2020-06-27 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateField(blank=True),
        ),
    ]