# Generated by Django 2.2.1 on 2019-06-14 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_signupmaster_middle_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signupmaster',
            name='collegeID',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='signupmaster',
            name='departmentID',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='signupmaster',
            name='programID',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='signupmaster',
            name='streamID',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
