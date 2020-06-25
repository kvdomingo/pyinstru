# Generated by Django 3.0.7 on 2020-06-25 17:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20200626_0150'),
    ]

    operations = [
        migrations.AddField(
            model_name='award',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='award',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
