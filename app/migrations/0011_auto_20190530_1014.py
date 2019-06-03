# Generated by Django 2.2.1 on 2019-05-30 10:14

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20190530_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departmentmaster',
            name='ProgramID',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='CollegeID', chained_model_field='CollegeID', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ProgramMaster'),
        ),
    ]
