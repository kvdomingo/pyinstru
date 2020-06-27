# Generated by Django 3.0.7 on 2020-06-27 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='honorific',
            field=models.CharField(blank=True, max_length=16),
        ),
        migrations.AddField(
            model_name='member',
            name='middle_name',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
    ]
