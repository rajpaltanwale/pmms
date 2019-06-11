# Generated by Django 2.2.1 on 2019-06-11 03:26

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CollegeMaster',
            fields=[
                ('CollegeID', models.AutoField(primary_key=True, serialize=False)),
                ('CollegeCode', models.CharField(max_length=10, null=True)),
                ('CollegeName', models.CharField(max_length=50, null=True)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('ModifiedDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentMaster',
            fields=[
                ('DepartmentID', models.AutoField(primary_key=True, serialize=False)),
                ('DepartmentCode', models.CharField(max_length=50)),
                ('DepartmentName', models.CharField(max_length=100)),
                ('collegeID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.CollegeMaster')),
            ],
        ),
        migrations.CreateModel(
            name='ProgramMaster',
            fields=[
                ('ProgramID', models.AutoField(primary_key=True, serialize=False)),
                ('ProgramName', models.CharField(max_length=50)),
                ('ProgramAlias', models.CharField(max_length=50)),
                ('collegeID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.CollegeMaster')),
            ],
        ),
        migrations.CreateModel(
            name='StreamMaster',
            fields=[
                ('StreamID', models.AutoField(primary_key=True, serialize=False)),
                ('StreamCode', models.CharField(max_length=10, null=True)),
                ('StreamName', models.CharField(max_length=30, null=True)),
                ('collegeID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.CollegeMaster')),
                ('departmentID', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='collegeID', chained_model_field='collegeID', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.DepartmentMaster')),
                ('programID', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='collegeID', chained_model_field='collegeID', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ProgramMaster')),
            ],
        ),
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
        migrations.CreateModel(
            name='LoginMaster',
            fields=[
                ('UserID', models.AutoField(primary_key=True, serialize=False)),
                ('LoginID', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=200)),
                ('collegeID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.CollegeMaster')),
                ('departmentID', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='programID', chained_model_field='programID', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.DepartmentMaster')),
                ('programID', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='collegeID', chained_model_field='collegeID', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ProgramMaster')),
                ('streamID', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='departmentID', chained_model_field='departmentID', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.StreamMaster')),
                ('studentID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.SignupMaster')),
            ],
        ),
        migrations.AddField(
            model_name='departmentmaster',
            name='programID',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='collegeID', chained_model_field='collegeID', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ProgramMaster'),
        ),
    ]
