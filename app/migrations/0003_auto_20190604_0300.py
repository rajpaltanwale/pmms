# Generated by Django 2.2.1 on 2019-06-04 03:00

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190604_0259'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignupMaster',
            fields=[
                ('StudentID', models.AutoField(primary_key=True, serialize=False)),
                ('student_Enrollment', models.IntegerField(null=True)),
                ('first_Name', models.CharField(max_length=15, null=True)),
                ('middle_Name', models.CharField(blank=True, max_length=15)),
                ('last_Name', models.CharField(max_length=20, null=True)),
                ('emailID', models.CharField(max_length=45, null=True)),
                ('collegeID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.CollegeMaster')),
                ('departmentID', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='collegeID', chained_model_field='collegeID', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.DepartmentMaster')),
                ('programID', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='collegeID', chained_model_field='collegeID', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ProgramMaster')),
                ('streamID', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='collegeID', chained_model_field='collegeID', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.StreamMaster')),
            ],
        ),
        migrations.AddField(
            model_name='loginmaster',
            name='studentID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.SignupMaster'),
        ),
    ]
