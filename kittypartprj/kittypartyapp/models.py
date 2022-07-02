from django.db import models
from django.db.models import Subquery,Count,Prefetch,Sum
class Classes(models.Model):
    class_id=models.IntegerField(primary_key=True,auto_created=True)
    class_name=models.CharField(max_length=40,null=False,blank=False,unique=True)
    min_age=models.IntegerField(null=False,blank=False)
    max_age=models.IntegerField(null=False,blank=False)
    max_student=models.IntegerField(null=False,blank=False)
    class_fee=models.IntegerField(null=False,blank=False)
    def __str__(self):
        return self.class_name
class StudentDivya(models.Model):
    student_id=models.IntegerField(primary_key=True,auto_created=True)
    gender=(("Female","Female"),("Male","Male"))
    student_name=models.CharField(max_length=40,null=False,blank=False)
    student_dob=models.DateField(null=True,blank=True,verbose_name="Date of Birth")
    student_gender=models.CharField(max_length=10,choices=gender,verbose_name='Gender')
    guardian_name=models.CharField(max_length=40,null=False,blank=False)
    contact_no=models.CharField(max_length=20,unique=True,null=False,blank=False,verbose_name="Contact Number")
    def __str__(self):
        return self.student_name

class Class_Student_Bridge(models.Model):
    
    cs_bridgeid=models.IntegerField(primary_key=True,auto_created=True)
    classname=models.ForeignKey(Classes, on_delete=models.PROTECT,null=True,blank=True,related_name="class_student_bridge")
    student=models.ForeignKey(StudentDivya,on_delete=models.PROTECT,null=True,blank=True,related_name="class_student_bridge")
    def __str__(self):
        return f"{self.student} {self.classname}"
    
    # def filteredvalues():
    #     nisha=Classes.objects.annotate(class_count=Count('class_student_bridge__classname'))
    #     classfiltered=[]
    #     for item in nisha:
    #         if item.max_student>item.class_count:
    #             classfiltered.append(item)
    # d=filteredvalues()
class kittyparty(models.Model):
    partyid=models.IntegerField(primary_key=True,auto_created=True)
    partyname=models.CharField(max_length=50)
    partydate=models.DateField()
    partyvenue=models.CharField(max_length=50)
    def __str__(self):
        return self.partyname
class category(models.Model):
    categoryid=models.IntegerField(primary_key=True,auto_created=True)
    categoryname=models.CharField(max_length=50,verbose_name='Category')
    def __str__(self):
        return self.categoryname
class game(models.Model):
    gameid=models.IntegerField(primary_key=True,auto_created=True)
    gamename=models.CharField(max_length=50)  
    def __str__(self):
        return self.gamename
class menu(models.Model):
    menuid=models.IntegerField(auto_created=True,primary_key=True)
    menuname=models.CharField(max_length=50)
    categoryid=models.ForeignKey(category,on_delete=models.RESTRICT,default=1)
    def __str__(self):
        return f"{self.menuname} {self.categoryid}"
    
class menupartybridge(models.Model):
    partyid=models.ForeignKey(kittyparty,on_delete=models.PROTECT)
    menuid=models.ForeignKey(menu,on_delete=models.RESTRICT) 
    def __str__(self):
        return f"{self.partyid} {self.menuid}"
     
class invitee(models.Model):
    inviteeid=models.IntegerField(primary_key=True,auto_created=True)
    inviteename=models.CharField(max_length=50)  
    def __str__(self):
        return self.inviteename

class gamepartybridge(models.Model):
    partyid=models.ForeignKey(kittyparty,on_delete=models.PROTECT)
    gameid=models.ForeignKey(game,on_delete=models.CASCADE)                       
    def __str__(self):
        return f"{self.partyid} {self.gameid}"    
class inviteepartybridge(models.Model):
    partyid=models.ForeignKey(kittyparty,on_delete=models.PROTECT,related_name="party")
    inviteeid=models.ForeignKey(invitee,on_delete=models.CASCADE,related_name="invitee")                       
    def __str__(self):
        return f"{self.partyid} {self.inviteeid}" 
class course(models.Model):
    courseid=models.IntegerField(primary_key=True,auto_created=True)
    coursename=models.CharField(max_length=30,verbose_name="Course Name")
    coursefee=models.PositiveIntegerField()
    courselevel=models.CharField(max_length=30,verbose_name="Level")
    courseyear=models.PositiveIntegerField()
    def __str__(self):
        return self.coursename
class student(models.Model):
    studentid=models.IntegerField(primary_key=True,auto_created=True)
    studentname=models.CharField(verbose_name="Name",max_length=50)        
    studentadharno=models.CharField(verbose_name="Adhar No",max_length=17)    
    studentdob=models.DateField(verbose_name="DOB")
    studentgender=models.CharField(max_length=10,verbose_name="Gender")
    studentcourse=models.ManyToManyField(course,through="studentcourse",related_name="student")
    def __str__(self):
        return self.studentname
class studentcourse(models.Model):
    scid=models.IntegerField(primary_key=True,auto_created=True)
    student=models.ForeignKey(student,related_name="student_course",null=True,on_delete=models.SET_NULL)
    course=models.ForeignKey(course,related_name="student_course",null=True,on_delete=models.SET_NULL)
    startdate=models.DateField(verbose_name="start date")
    enddate=models.DateField(verbose_name="end date")
    percentageofcompletion=models.PositiveSmallIntegerField(verbose_name="per of completion")
    status=models.CharField(max_length=15,verbose_name="status")
    def __str__(self):
        return f"{self.student.studentname} {self.course.coursename}"
