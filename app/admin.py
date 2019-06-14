from django.contrib import admin


# Object Level permisiions
from guardian.admin import GuardedModelAdmin

from import_export import resources

from import_export.admin import ImportExportModelAdmin

# Register your models here.
from . models import *
 #mymodels=[CollegeMaster,]
 


class SomeModelAdmin(GuardedModelAdmin):
	pass
@admin.register(CollegeMaster,  ProgramMaster, DepartmentMaster, StreamMaster, LoginMaster, SignupMaster, FileMaster)
class ViewAdmin(ImportExportModelAdmin):
	exclude = ('id', )

