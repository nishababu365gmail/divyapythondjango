from pyexpat import model
from django.db.models import Subquery,Count,Prefetch,Sum
from django import forms
from django.forms import ModelForm
from  kittypartyapp.models import( kittyparty,game,invitee,Classes,
inviteepartybridge,gamepartybridge,category,student,studentcourse,course,Class_Student_Bridge)
from django_select2 import forms as select2forms
class studentform(forms.Form):
    jobcarddemand=forms.CharField(max_length=30,min_length=4,strip=True,label="job card")
    choices=(('Male','Male'),('Female','Female'),('Others','Others'))
    studentname=forms.CharField(required=True,max_length=30,min_length=4,strip=True,label="Name")
    studentadharno=forms.CharField(label="Adhar No",max_length=17)    
    studentdob=forms.DateField(label="DOB",widget=forms.DateInput(attrs={'class':"datepicker"}))
    studentgender=forms.ChoiceField(label="Gender",choices=choices)
    # studentcourse=forms.ManyToManyField(course,through="studentcourse",related_name="student")
class flowerform(forms.Form):
    jobcardparts=forms.CharField(max_length=30,min_length=4,strip=True,label="job card")
    choices=(('US','US'),('Russia','Russia'),('Others','Others'))
    flowername=forms.CharField(required=True,max_length=30,min_length=4,strip=True,label="Name")
    flowercolor=forms.CharField(label="Color",max_length=17)    
    
    flowerorigin=forms.ChoiceField(label="Origin",choices=choices)
class jobcardform(forms.Form):
    jobcard= forms.CharField(required=True,max_length=30,min_length=4,strip=True,label="jobcard")
    checkindate=forms.DateField()

class studentclassmodelform(ModelForm):
    d=[]
    @classmethod
    def filteredvalues(cls):
        nisha=Classes.objects.annotate(class_count=Count('class_student_bridge__classname'))
        # classfiltered=[]
        # classfiltered.append(('0','-----'))
        # for item in nisha:
            
        #     if item.max_student>item.class_count:
        #         classfiltered.append((item.class_id,item.class_name))
        # return tuple(classfiltered)
        return nisha
    def __init__(self,*args,**kwargs):
        d=studentclassmodelform.filteredvalues()
        super().__init__(*args,**kwargs)
        # if 'initial' in kwargs:
       
        self.fields['classname']=forms.ModelChoiceField(queryset=d.filter(class_count__lte=0))
    
    class Meta:
        model=Class_Student_Bridge
        fields='__all__'
class studentcourseform(forms.Form):
    # cchoices=course.objects.all().values('courseid','coursename')
    # idlist=[]
    # cnamelist=[]
    input_formats= ['%Y-%m-%d',     
    '%m/%d/%Y',      
    '%m/%d/%y']     
    # for item in cchoices:
    #     idlist.append(item.get("courseid"))
    #     cnamelist.append(item.get("coursename"))
    
    # mychoices= list((zip(idlist,cnamelist)))
    
    student=forms.CharField(required=False,label="Student Name",max_length=17)
    course=forms.ModelChoiceField(queryset=course.objects.all(),label="Course Name",widget=select2forms.Select2Widget(attrs={'class':'select2','width':'50px','theme':'classic'}))
    startdate=forms.DateField(input_formats=input_formats,label="start date",widget=forms.TextInput(attrs={'class':'datepicker','autocomplete':'off'}))
    enddate=forms.DateField(label="end date",widget=forms.TextInput(attrs={'class':'datepicker datepickerclass','autocomplete':'off'}))
    percentageofcompletion=forms.IntegerField(max_value=100,label="per of completion")
    status=forms.CharField(max_length=15,label="status")
    status.widget.attrs.update({'class': 'datepickerclass'})
    percentageofcompletion.widget.attrs.update({'class': 'datepickerclass'})
class kittypartymdlform(ModelForm):
    class Meta:
        model=kittyparty
        fields='__all__'
class gamemdlform(ModelForm):
    class Meta:
        model=game
        fields='__all__' 
class inviteemdlform(ModelForm):
    class Meta:
        model=invitee
        fields='__all__' 
class inviteepartybridgemdlform(ModelForm):
    class Meta:
        model=inviteepartybridge
        fields='__all__' 
class gamepartybridgemdlform(ModelForm):
    class Meta:
        model=gamepartybridge
        fields='__all__' 
class categorymdlform(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        if 'instance' in kwargs:
            self.fields['categoryname'].widget.attrs.update({'class':'special'})
            
    class Meta:
        model= category
        fields='__all__' 
class GameWidget(select2forms.ModelSelect2MultipleWidget):
    search_fields = [
        "gamename__icontains",
        
    ]

class gamepartybridgemdlform2(ModelForm):
    # gameid=forms.ModelChoiceField(
    #         queryset=game.objects.all(),
    #         widget=select2forms.ModelSelect2MultipleWidget(width=60,
    #             queryset=game.objects.all(),
    #             search_fields=['gamename__icontains']
    #         )
    #     )

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)       
        
    class Meta:
        model=gamepartybridge        
        fields=['partyid','gameid']
        widgets = {
            "gameid": select2forms.Select2MultipleWidget(),
            
        }  

class MyForm(forms.Form):
    my_choice = forms.ChoiceField(
widget=select2forms.Select2MultipleWidget(


)
)       
