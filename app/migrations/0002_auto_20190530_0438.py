# Generated by Django 2.2.1 on 2019-05-30 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collegemaster',
            name='CreatedBy',
        ),
        migrations.RemoveField(
            model_name='collegemaster',
            name='ModifiedBy',
        ),
    ]
