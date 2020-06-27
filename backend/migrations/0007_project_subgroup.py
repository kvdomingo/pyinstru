# Generated by Django 3.0.7 on 2020-06-27 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20200627_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='subgroup',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='backend.Subgroup', to_field='code'),
            preserve_default=False,
        ),
    ]
