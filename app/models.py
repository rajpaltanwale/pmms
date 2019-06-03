from django.db import models
# Create your models here.
from django.contrib.auth.models import User

from smart_selects.db_fields import ChainedForeignKey

from django.db import connection

class CollegeMaster(models.Model):
    CollegeID = models.AutoField(primary_key=True)
    #Colege_Number = IntegerField()
    CollegeCode = models.CharField(max_length=10, null=True)
    CollegeName = models.CharField(max_length=50, null=True)
    CreatedDate = models.DateTimeField(auto_now_add=True, editable=True)
    ModifiedDate = models.DateTimeField(auto_now=True, editable=True)

    def __str__(self):
   	     return self.CollegeCode 


class ProgramMaster(models.Model):
    ProgramID = models.AutoField(primary_key=True)
    collegeID = models.ForeignKey(CollegeMaster, on_delete=models.CASCADE, null=True)
    ProgramName = models.CharField(max_length=50)
    ProgramAlias = models.CharField(max_length=50)

    def __str__(self):
        return str(self.collegeID) + " - " + self.ProgramName

'''
class DepartmentMaster(models.Model):
    DepartmentID = models.AutoField(primary_key=True)
    collegeID = models.ForeignKey(CollegeMaster, on_delete=models.CASCADE, null=True)
    programID = models.ForeignKey(ProgramMaster, on_delete=models.CASCADE, null=True)    
    DepartmentCode = models.CharField(null=False, max_length=50)
    DepartmentName = models.CharField(null=False, max_length=100)

    def __str__(self):
        return self.DepartmentCode + " - " + self.DepartmentName

'''
class DepartmentMaster(models.Model):
    DepartmentID = models.AutoField(primary_key=True)
    collegeID = models.ForeignKey(CollegeMaster, on_delete=models.CASCADE, null=True)
    programID = ChainedForeignKey(
    ProgramMaster,
    chained_field="collegeID",
    chained_model_field="collegeID",
    show_all=False,
    auto_choose=True,
    sort=True,
    null=True)    
    DepartmentCode = models.CharField(null=False, max_length=50)
    DepartmentName = models.CharField(null=False, max_length=100)

    def __str__(self):
        return str(self.programID) + " - " + self.DepartmentCode

class StreamMaster(models.Model):

    StreamID = models.AutoField(primary_key=True)
    collegeID = models.ForeignKey(CollegeMaster, on_delete=models.CASCADE, null=True)
    programID = ChainedForeignKey(
    ProgramMaster,
    chained_field="collegeID",
    chained_model_field="collegeID",
    show_all=False,
    auto_choose=True,
    sort=True,
    null=True) 
    departmentID = ChainedForeignKey(
    DepartmentMaster,
    chained_field="collegeID",
    chained_model_field="collegeID",
    show_all=False,
    auto_choose=True,
    sort=True,
    null=True)     
    StreamCode = models.CharField(max_length=10, null=True)
    StreamName = models.CharField(max_length=30, null=True)


    def __str__(self):
        return str(self.departmentID) + " - " + str(self.StreamCode)



''' 
    #programID = (ProgramMaster.objects.raw("SELECT * FROM ProgramMaster WHERE DepartmentMaster.collegeID = ProgramMaster.collegeID"))
    #ProgramID = models.ForeignKey(ProgramMaster, on_delete=models.CASCADE, null=True)
    def my_custon_sql(self):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM ProgramMaster WHERE DepartmentMaster.collegeID = ProgramMaster.collegeID")
        row = cursor.fetchall
        return row
''' 