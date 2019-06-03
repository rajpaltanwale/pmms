# Generated by Django 2.2.1 on 2019-05-30 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20190530_0505'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramMaster',
            fields=[
                ('ProgramID', models.AutoField(primary_key=True, serialize=False)),
                ('ProgramName', models.CharField(max_length=50)),
                ('ProgramAlias', models.CharField(max_length=50)),
                ('IsActive', models.BooleanField(default=True)),
                ('CreatedBy', models.IntegerField()),
                ('ModifiedBy', models.IntegerField()),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('ModifiedDate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
