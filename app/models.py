from django.db import models
# Create your models here.
from django.contrib.auth.models import User

from smart_selects.db_fields import ChainedForeignKey




class CollegeMaster(models.Model):
    CollegeID = models.AutoField(primary_key=True)
    #Colege_Number = IntegerField()
    CollegeCode = models.CharField(max_length=10, null=True)
    CollegeName = models.CharField(max_length=50, null=True)
    CreatedDate = models.DateTimeField(auto_now_add=True, editable=True)
    ModifiedDate = models.DateTimeField(auto_now=True, editable=True)

    def __str__(self):
   	     return str(self.CollegeID) + " - " + self.CollegeCode 


class ProgramMaster(models.Model):
    ProgramID = models.AutoField(primary_key=True)
    collegeID = models.ForeignKey(CollegeMaster, on_delete=models.CASCADE, null=True)
    ProgramName = models.CharField(max_length=50)
    ProgramAlias = models.CharField(max_length=50)
    NumberOfSemester = models.IntegerField(null=True)

    def __str__(self):
        return  str(self.collegeID) + " - " +str(self.ProgramID) + " - " + self.ProgramName



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
        return str(self.programID) + " - " + str(self.DepartmentID) + " - " + self.DepartmentCode

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
        return str(self.departmentID) + " - " + str(self.StreamID) + " - " + str(self.StreamCode)
'''
class Signup(models.Model):  
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
    streamID = ChainedForeignKey(
    StreamMaster,
    chained_field="collegeID",
    chained_model_field="collegeID",
    show_all=False,
    auto_choose=True,
    sort=True,
    null=True,
    blank=True)
    student_Enrollment = models.IntegerField(null=True)
    first_Name = models.CharField(max_length=15, null=True)
    #middle_Name = models.CharField(max_length=15, blank=True, null=False)
    last_Name = models.CharField(max_length=20, null=True)
    emailID= models.CharField(max_length=45, null=True)
  #  DerivedUserFrom = models.IntegerField(choices=((1, 'Student'), (2, 'Internal Faculty'), (3, 'External Faculty')))
'''
class Signup(models.Model):      
    first_Name = models.CharField(max_length=15, null=True)
    #middle_Name = models.CharField(max_length=15, blank=True, null=False)
    last_Name = models.CharField(max_length=20, null=True)
    student_Enrollment = models.IntegerField(null=True)
    Branch = models.CharField(max_length=15, null=True)
    semester = models.IntegerField(null=True)
    emailID= models.CharField(max_length=45, null=True)
  #  DerivedUserFrom = models.IntegerField(choices=((1, 'Student'), (2, 'Internal Faculty'), (3, 'External Faculty')))

    class Meta:
        abstract = True


    def __str__(self):
        return str(self.first_Name) + " " + str(self.last_Name) + " - " +  str(self.Branch) + " - semester - " + str(self.semester)
        
class SignupMaster(Signup):
    pass

'''
class SignupMaster(models.Model):
    StudentID = models.AutoField(primary_key=True)    
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
    streamID = ChainedForeignKey(
    StreamMaster,
    chained_field="collegeID",
    chained_model_field="collegeID",
    show_all=False,
    auto_choose=True,
    sort=True,
    null=True,
    blank=True)
    student_Enrollment = models.IntegerField(null=True)
    first_Name = models.CharField(max_length=15, null=True)
    middle_Name = models.CharField(max_length=15, blank=True)
    last_Name = models.CharField(max_length=20, null=True)
    emailID= models.CharField(max_length=45, null=True)
  #  DerivedUserFrom = models.IntegerField(choices=((1, 'Student'), (2, 'Internal Faculty'), (3, 'External Faculty')))

    def __str__(self):
        if str(self.streamID) == "None":
            return str(self.departmentID) + " - " + str(self.student_Enrollment) 
        else:
            return str(self.streamID) + " - " + str(self.student_Enrollment)
'''
class LoginMaster(models.Model):
    UserID = models.AutoField(primary_key=True)
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
    chained_field="programID",
    chained_model_field="programID",
    show_all=False,
    auto_choose=True,
    sort=True,
    null=True)    
    streamID = ChainedForeignKey(
    StreamMaster,
    chained_field="departmentID",
    chained_model_field="departmentID",
    show_all=False,
    auto_choose=True,
    sort=True,
    blank=True,
    null=True)
    studentID = ChainedForeignKey(
    SignupMaster,
    chained_field="departmentID",
    chained_model_field="departmentID",
    show_all=False,
    auto_choose=True,
    sort=True,
    blank=True,
    null=True)
    LoginID = models.CharField(max_length=50)
    Password = models.CharField(max_length=200)
  #  DerivedUserFrom = models.IntegerField(choices=((1, 'Student'), (2, 'Internal Faculty'), (3, 'External Faculty')))

    def __str__(self):
        return str(self.LoginID)

class FileMaster(models.Model):
    UserID = models.AutoField(primary_key=True)
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
    chained_field="programID",
    chained_model_field="programID",
    show_all=False,
    auto_choose=True,
    sort=True,
    null=True)    
    streamID = ChainedForeignKey(
    StreamMaster,
    chained_field="departmentID",
    chained_model_field="departmentID",
    show_all=False,
    auto_choose=True,
    sort=True,
    blank=True,
    null=True)
    studentID = ChainedForeignKey(
    SignupMaster,
    chained_field="departmentID",
    chained_model_field="departmentID",
    show_all=False,
    auto_choose=True,
    sort=True,
    blank=True,
    null=True)
    pdf1 = models.FileField(upload_to='app/upload')
    pdf2 = models.FileField(upload_to='app/upload')
    pdf3 = models.FileField(upload_to='app/upload')
    pdf4 = models.FileField(upload_to='app/upload')
    
    def __str__(self):
        return str(self.studentID)

class ProjectTypeMaster(models.Model):
    ProjectTypeID= models.AutoField(primary_key=True)
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
    chained_field="programID",
    chained_model_field="programID",
    show_all=False,
    auto_choose=True,
    sort=True,
    null=True)    
    streamID = ChainedForeignKey(
    StreamMaster,
    chained_field="departmentID",
    chained_model_field="departmentID",
    show_all=False,
    auto_choose=True,
    sort=True,
    blank=True,
    null=True)
    InSemester = models.IntegerField(choices=((1, 1), (2, 2), (3, 3)))  
    ProjectType = models.CharField(max_length=20, null=True)

    def __str__(self):
        return str(self.departmentID) + " - " + str(self.StreamCode) + " - " + self.ProjectType  






