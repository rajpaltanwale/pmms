from django.contrib import admin


# Object Level permisiions
from guardian.admin import GuardedModelAdmin



# Register your models here.
from . models import CollegeMaster,  ProgramMaster, DepartmentMaster, StreamMaster, LoginMaster, SignupMaster, FileMaster
 #mymodels=[CollegeMaster,]



class SomeModelAdmin(GuardedModelAdmin):
	pass

admin.site.register(CollegeMaster, SomeModelAdmin)
admin.site.register(ProgramMaster, SomeModelAdmin)
admin.site.register(DepartmentMaster, SomeModelAdmin)
admin.site.register(StreamMaster, SomeModelAdmin)
admin.site.register(LoginMaster, SomeModelAdmin)
admin.site.register(SignupMaster, SomeModelAdmin)
admin.site.register(FileMaster, SomeModelAdmin)
#admin.site.register(mymodels)