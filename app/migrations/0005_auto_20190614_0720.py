# Generated by Django 2.2.1 on 2019-06-14 07:20

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20190614_0707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streammaster',
            name='departmentID',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='programID', chained_model_field='programID', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.DepartmentMaster'),
        ),
    ]
