from itertools import count
from telnetlib import STATUS
from django.http import JsonResponse
from django.http.response import HttpResponse
import pandas as pd
import requests
from django.shortcuts import render
from django.db.models import Subquery,Count,Prefetch,Sum
from django.forms import (modelformset_factory,
inlineformset_factory, formset_factory)
from django.contrib.auth.decorators import login_required


    

from kittypartyapp.models import(kittyparty,gamepartybridge,
inviteepartybridge,game,invitee,category,menupartybridge,menu,
student,studentcourse,course,StudentDivya,Class_Student_Bridge,Classes
)
from kittypartyapp.forms import (kittypartymdlform,
gamepartybridgemdlform2,MyForm,studentform,
studentcourseform,flowerform,jobcardform,
categorymdlform,studentclassmodelform)
from kittypartyapp.serializers import courseserializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

from itertools import chain
def multformdemanddisplay(request):
    template_name='kittypartyapp/multformdemand.html'
    if request.method=='GET':
        # template_name='kittypartyapp/multformdemand.html'
        # return render(request,template_name=template_name)
        jbcardno=request.GET.get('demandjobcard')
        # jbcardno=request.GET.get('demandjobcard1')
        print('i am from maani')
        studentformset=formset_factory(studentform,extra=2)
        studentformsetobj=studentformset(initial=[{'jobcarddemand':jbcardno}])
        template_name='kittypartyapp/multformdemand.html'
        return render(request,template_name=template_name,context={'jobcard':jbcardno,'formset':studentformsetobj})
    elif request.method=='POST':
        jbcardno=request.POST.get('demandjobcard')
        print('i am from post maani')
        studentformset=formset_factory(studentform,extra=2)
        studentformsetobj=studentformset(request.POST)
        for item in studentformsetobj:
            print(item)
        template_name='kittypartyapp/multformdemand.html'
        return render(request,template_name=template_name,context={'jobcard':jbcardno,'formset':studentformsetobj})

def multformpartsdisplay(request):
    template_name='kittypartyapp/multformparts.html'
    if request.method=='GET':
        
        # template_name='kittypartyapp/multformparts.html'
        # return render(request,template_name=template_name)
        print('i am from vava')
        jbcardno=request.GET.get('partsjobcard')
        flowerformset=formset_factory(flowerform,extra=2)
        flowerformsetobj=flowerformset()
        template_name='kittypartyapp/multformparts.html'
        return render(request,template_name=template_name,context={'jobcard':jbcardno,'formset':flowerformsetobj})
    elif request.method=='POST':
        print('formset parts')
        print('i am from vava')
        jbcardno=request.POST.get('partsjobcard')
        flowerformset=formset_factory(flowerform,extra=2)
        flowerformsetobj=flowerformset(request.POST)
        for item in flowerformsetobj:
            print(item)
        template_name='kittypartyapp/multformparts.html'
        return render(request,template_name=template_name,context={'jobcard':jbcardno,'formset':flowerformsetobj})
def multformedit(request,jobcard):
    template_name='kittypartyapp/multipleforms.html'
    if request.method=='GET': 
        jbcardno=jobcard
        return render(request,template_name=template_name,context={'jobcard':jbcardno})
def multform(request):
    template_name='kittypartyapp/multipleforms.html'
    if request.method=='GET': 
        jbcardno=request.GET.get('demandjobcard') 
        
        jobcardformset=formset_factory(jobcardform,extra=0)
        jobcardformsetobj=jobcardformset(initial=[{'jobcard':jbcardno}])
       
        # if request.GET.get('maaniname')=='maani':
        #     jbcardno=request.GET.get('demandjobcard')
        #     print('i am from maani')
        #     studentformset=formset_factory(studentform,extra=2)
        #     studentformsetobj=studentformset()
        #     template_name='kittypartyapp/multformdemand.html'
        return render(request,template_name=template_name,context={'jobcard':jbcardno,'formset':jobcardformsetobj})
        # elif request.GET.get('vavaname')=='vava':
        #     print('i am from vava')
        #     jbcardno=request.GET.get('partsjobcard')
        #     flowerformset=formset_factory(flowerform,extra=2)
        #     flowerformsetobj=flowerformset()
        #     template_name='kittypartyapp/multformparts.html'
        #     return render(request,template_name=template_name,context={'jobcard':jbcardno,'formset':flowerformsetobj})
    else:
        jbcardno=request.POST.get('form-0-jobcard') 
        print(request.POST)
        jobcardformset=formset_factory(jobcardform,extra=0)

        jobcardformsetobj=jobcardformset(request.POST)
        jbcardno=request.POST.get('form-0-jobcard')
        return render(request,template_name=template_name,context={'jobcard':jbcardno,'formset':jobcardformsetobj})
    # return render(request,template_name=templatename)

def concatenatequeryset(request):
    partylist=kittyparty.objects.filter(partyid=1).values('partyname','partyvenue')
    gamelist=game.objects.filter(gameid=1).values('gamename','gameid')
    
    result_list = list(chain(partylist, gamelist))
    return JsonResponse(result_list,safe=False)
@login_required
def my_view(request):
    pass
def callapifromview(request):
    template_name='kittypartyapp/GetValuesFromApi.html'
    r=requests.get('https://api.github.com/events')
    print(r)
    jsonstring=r.json()
    return render(request,template_name,context={'json':jsonstring})

def coursesertrial(request):
    courselist=course.objects.all()
    courseser=courseserializer(courselist,many=True)
    return JsonResponse(courseser.data,safe=False)
@api_view(['GET','POST'])
def coursesertrialwithdec(request):
    if request.method=="GET":        
        courselist=course.objects.all()
        courseser=courseserializer(courselist,many=True)
        return Response(courseser.data)
    elif request.method=="POST":
        courseinstance=courseserializer(data=request.data)
        if courseinstance.is_valid():
            courseinstance.save()
            return Response(data=courseinstance.data) 

def grasshopper(request):  
    
    nisha=Classes.objects.annotate(class_count=Count('class_student_bridge__classname'))
    classfiltered=[]
    for item in nisha:
        if item.max_student>item.class_count:
            classfiltered.append(item)
    
    print(classfiltered)
    partyobj=kittyparty.objects.get(partyname='Xmas')
    menulist=menupartybridge.objects.filter(partyid=partyobj)
    myform= studentclassmodelform()
    if request.method=="GET":
        context={'menulist':menulist,'entelist':myform}
        return render (request,'kittypartyapp/menucategorywiselist.html',context)
    # nisha=Classes.objects.filter(max_student__lte=Subquery(Class_Student_Bridge.objects.annotate(numberof_class=Count('classname'))))
def mycategorywisemenulist(request):
    partyobj=kittyparty.objects.get(partyname='Xmas')
    menulist=menupartybridge.objects.filter(partyid=partyobj)
    if request.method=="GET":

        context={'menulist':menulist}
        return render (request,'kittypartyapp/menucategorywiselist.html',context)

def myselect2(request):
    myform=gamepartybridgemdlform2()
    if request.method=="GET":
        context={'myform':myform}
        return render (request,'kittypartyapp/gamewithselect2.html',context)
    elif request.method=="POST":
        print(myform.errors)
        print(request.POST)    

        myform=gamepartybridgemdlform2(request.POST)
        if myform.is_valid():
            print('hello nisha')
            print(myform)
        context={'myform':myform}
        return render (request,'kittypartyapp/gamewithselect2.html',context)
@login_required
def kittypartylist(request):
    partylist=kittyparty.objects.all()
    if request.method=="GET":
        
        mydict=[{'name':'nisha','age':4,'adhar':1234},{'name':'babu','age':3,'adhar':9900}]
        context={'partylist':partylist,'mydict':mydict}
        return render(request,'kittypartyapp/kittypartylist.html',context)
                
def editkittypartyinvitee(request,partyid=None):
     party=kittyparty.objects.get(partyid=partyid)
     partymodelform=kittypartymdlform(instance=party)
     inviteeformset=inlineformset_factory(kittyparty,inviteepartybridge,fields=('inviteeid',),can_delete=True)       
     if request.method=="GET":
        myinviteeformset=inviteeformset(instance=party)
        return render(request,'kittypartyapp/KittyPartyInvitee.html',{'myform':partymodelform,'inviteeform':myinviteeformset})
     elif request.method=="POST":
        myinviteeformset=inviteeformset(request.POST,instance=party) 
        if myinviteeformset.is_valid():
              instances= myinviteeformset.save(commit=False) 
              for instance in instances:
                  instance.partyid=party
                  instance.save()
     return render(request,'kittypartyapp/KittyPartyInvitee.html',{'myform':partymodelform,'inviteeform':myinviteeformset})

def kittypartyinvitee(request):
    party=kittypartymdlform()
    inviteeformset=inlineformset_factory(kittyparty,inviteepartybridge,fields=('inviteeid',),can_delete=True)
    if request.method=="GET":
        myinviteeformset=  inviteeformset()
        return render(request,'kittypartyapp/KittyPartyInvitee.html',{'myform':party,'inviteeform':myinviteeformset})      
    else:
        party=kittypartymdlform(request.POST)
        if party.is_valid():
            party.save()
            lastpartyid=kittyparty.objects.last()
            myinviteeformset=inviteeformset(request.POST)
            partyinstance=kittyparty.objects.get(partyid=lastpartyid.partyid)
            if myinviteeformset.is_valid():
              instances= myinviteeformset.save(commit=False) 
              for instance in instances:
                  instance.partyid=partyinstance
                  
                  instance.save()
            return render(request,'kittypartyapp/KittyPartyInvitee.html',{'myform':party,'inviteeform':myinviteeformset})      
        return render(request,'kittypartyapp/KittyPartyInvitee.html',{'myform':party,'inviteeform':myinviteeformset})          
def kittypartydef(request):
    party=kittypartymdlform()
    gameformset=inlineformset_factory(kittyparty,gamepartybridge,fields=('gameid',),can_delete=True)
    inviteeformset=inlineformset_factory(kittyparty,inviteepartybridge,fields=('inviteeid',),can_delete=True)
    if request.method=="GET":
        myformset=gameformset()
        myinviteeformset=inviteeformset()
        return render(request,'kittypartyapp/KittyParty.html',{'myform':party,'formset':myformset,"inviteeformset":myinviteeformset})
    elif request.method=="POST":               
        party=kittypartymdlform(request.POST)
        
        if party.is_valid():
            party.save()     
            latestpartyid = kittyparty.objects.last() 
            print(latestpartyid.partyid)  
            myformset=gameformset(request.POST)
            
            myinviteeformset=inviteeformset(request.POST)
            myparty=kittyparty.objects.get(partyid=latestpartyid.partyid)
            if myformset.is_valid():
                instances=myformset.save(commit=False)
                for instance in instances:
                    instance.partyid=myparty
                    instance.save() 
            if myinviteeformset.is_valid():
                instances=myinviteeformset.save(commit=False)
                for instance in instances:
                    instance.partyid=myparty
                    instance.save()            
            return render(request,'kittypartyapp/KittyParty.html',{'myform':party,'formset':myformset,"inviteeformset":myinviteeformset})        
    return render(request,'kittypartyapp/KittyParty.html',{'myform':party,'formset':myformset,"inviteeformset":myinviteeformset})    
    
def editkittyparty(request,parampartyid=None):
 party=kittyparty.objects.get(partyid=parampartyid)
 partymdlform=kittypartymdlform(instance=party)
 gameformset=inlineformset_factory(kittyparty,gamepartybridge,fields=('gameid',))
 inviteeformset=inlineformset_factory(kittyparty,inviteepartybridge,fields=('inviteeid',))
 if request.method=="GET":
     myformset=gameformset(instance=party)            
     myinviteeformset=inviteeformset(instance=party)
     print(party)
     return render(request,'kittypartyapp/KittyParty.html',{'myform':partymdlform,'formset':myformset,"inviteeformset":myinviteeformset})

def queryview(request):
    templatename='kittypartyapp/myquery.html'
    #Display partyname which does not have invitees assigned
    # partyidlist=kittyparty.objects.all().values_list('partyid')
    # inviteeassignedpartylist=inviteepartybridge.objects.all().values_list('partyid')
    # difflist=partyidlist.difference(inviteeassignedpartylist)
    # partynamelist=kittyparty.objects.filter(partyid__in=difflist).values_list('partyname')
    #End of Display partyname which does not have invitees assigned

    #Display list of invitees common to two different parties
    # partyobjvd=kittyparty.objects.get(partyname='Vijayadasmi')
    # partyobjonam=kittyparty.objects.get(partyname='Onam')
    # vdlist=inviteepartybridge.objects.filter(partyid=partyobjvd).values_list('inviteeid')    
    # onamist=inviteepartybridge.objects.filter(partyid=partyobjonam).values_list('inviteeid')    
    # commonlist=vdlist.intersection(onamist)
    # namelist=invitee.objects.filter(inviteeid__in=commonlist).values_list('inviteename')
    #End of Display list of invitees common to two different parties
    #Display list of invitees who are not in the party for Vijayadasmi
    # partyobj=kittyparty.objects.get(partyname='Vijayadasmi')
    # list=inviteepartybridge.objects.filter(partyid=partyobj).values_list('inviteeid')
    # difflist=invitee.objects.exclude(inviteeid__in=list)
    #End of Display list of invitees who are not in the party for Vijayadasmi
    #Display list of game name assigned for a party.this way we can find out the invitees also
    # partyobj=kittyparty.objects.get(partyname='Vishu')
    # list=gamepartybridge.objects.filter(partyid=partyobj).values_list('gameid')
    # gamesforaparty=game.objects.filter(gameid__in=list)
    #End of display list of game name assigned for a party
    #Display a list of party which does not have games assigned
    # list= gamepartybridge.objects.select_related('partyid').all().values_list('partyid__partyid').distinct()    
    # difflist=kittyparty.objects.exclude(partyid__in=list)
    #End of display a list of party which does not have games assigned
    bridgelist=menupartybridge.objects.all().order_by('partyid__partyname')
    # context={'mylist':partynamelist}
    context={'mylist':bridgelist}
    return render(request,templatename,context)
def CreateCategory(request):
    categorymdlfrm=categorymdlform()
    template_name='kittypartyapp/Category.html'
    if request.method=='GET':    
        context={'Title':'Category','myform':categorymdlfrm}
        return render(request,template_name,context)
    elif request.method=='POST':
        categorymdlfrm=categorymdlform(request.POST)
        if categorymdlfrm.is_valid():
           categorymdlfrm.save()
           context={'Title':'Category Saved','myform':categorymdlfrm}
           return render(request,template_name,context)
    context={'Title':'Category Not Saved','myform':categorymdlfrm}
    return render(request,template_name,context) 

def CategoryList(request):
    template_name='kittypartyapp/CategoryList.html'
    catlist=category.objects.all() 
    context={'Title':'Category List','mylist':catlist}
    return render(request,template_name,context) 
def EditCategory(request,catid=None):
    categoryobject=category.objects.get(categoryid=catid)
    categorymdlfrm=categorymdlform(instance=categoryobject)
    template_name='kittypartyapp/Category.html'
    if request.method=='GET':    
        context={'Title':'Category','myform':categorymdlfrm}
        return render(request,template_name,context)
    elif request.method=='POST':
        categoryobject=category.objects.get(categoryid=catid)
        categorymdlfrm=categorymdlform(request.POST,instance=categoryobject)
        if categorymdlfrm.is_valid():
           categorymdlfrm.save()
           context={'Title':'Category Saved','myform':categorymdlfrm}
           return render(request,template_name,context)
    context={'Title':'Category Not Saved','myform':categorymdlfrm}
    return render(request,template_name,context) 
def KittyPartyGame(request):
    partylist=kittyparty.objects.all()
    if request.method=="GET":
        context={'partylist':partylist}
        return render(request,'kittypartyapp/KittyPartygamelist.html',context)

def AddKittyPartyGame(request,partyid=None):
    partygameformset= inlineformset_factory(kittyparty,gamepartybridge,fields=('gameid',))
    mypartygameformset=partygameformset()
    kittypartyobj=kittyparty.objects.get(partyid=partyid)
    kittypartyobjform=kittypartymdlform(instance=kittypartyobj)
    if request.method=="GET":  
       
        context={'formset':mypartygameformset,'kittypartyform':kittypartyobjform}
        return render(request,'kittypartyapp/KittyPartygameform.html',context)
    if request.method=="POST":
        partyobjecttosave=kittyparty.objects.get(partyid=partyid)
        formset= partygameformset(request.POST,instance=partyobjecttosave)
        if formset.is_valid():
           
           instances=formset.save(commit=False)
           
           for instance in instances:
               
               myid=gamepartybridge.objects.filter(gameid=instance.gameid)
               
               if myid.count()==0:
                    instance.partyid=partyobjecttosave
                    instance.save()

        context={'formset':formset,'kittypartyform':kittypartyobjform}
        return render(request,'kittypartyapp/KittyPartygameform.html',context)
    return render(request,'kittypartyapp/KittyPartygameform.html',context)    
def AddStudentWithForm(request):
    if request.method=="GET":
        studentformobj=studentform()
        context={'formobj':studentformobj}
        return render(request,'kittypartyapp/CreateStudent.html',context)
    else:
        studentformobj=studentform(request.POST)
        context={'formobj':studentformobj}
        if studentformobj.is_valid():
            studentobj=student()
            studentobj.studentname=studentformobj.cleaned_data["studentname"]
            studentobj.studentadharno=studentformobj.cleaned_data["studentadharno"]
            studentobj.studentdob=studentformobj.cleaned_data["studentdob"]
            studentobj.studentgender=studentformobj.cleaned_data["studentgender"]
            studentobj.save()
            context={'formobj':studentformobj}
            return render(request,'kittypartyapp/CreateStudent.html',context)
    return render(request,'kittypartyapp/CreateStudent.html',context)
def AddCourseWithFormset(request):
    studentobj=student.objects.get(studentid=2)
    studentcourseformset=formset_factory(studentcourseform,extra=1,can_delete=True,max_num=5,min_num=1)
    if request.method=="GET":    
         
        studentcourseformsetobj=studentcourseformset(initial=[{'student':studentobj.studentname}])
        context={'scformsetobj':studentcourseformsetobj}
        return render(request,'kittypartyapp/StudentCourseFormset.html',context) 
    if request.method=="POST":
        studentcourseformsetobj=studentcourseformset(request.POST)
        print(studentcourseformsetobj.errors)
        print('nisha babu')
        if studentcourseformsetobj.is_valid():
            studentcourseform.student= studentobj
            for objform in studentcourseformsetobj:
                studentcourseobj=studentcourse()
                
                studentcourseobj.student=studentobj
                
                # courseobj=course.objects.get(courseid=objform.cleaned_data["course"])
                if objform.cleaned_data["DELETE"]!=True:
                    print(objform)
                    studentcourseobj.course=objform.cleaned_data["course"]
                    studentcourseobj.startdate= objform.cleaned_data["startdate"]
                    studentcourseobj.enddate=objform.cleaned_data["enddate"]
                    studentcourseobj.percentageofcompletion=objform.cleaned_data["percentageofcompletion"]            
                    studentcourseobj.status=objform.cleaned_data["status"]
                    studentcourseobj.save()
            context={'scformsetobj':studentcourseformsetobj}
            return render(request,'kittypartyapp/StudentCourseFormset.html',context)
        context={'scformsetobj':studentcourseformsetobj}
        return render(request,'kittypartyapp/StudentCourseFormset.html',context) 

def manaytomanyexample(request):
    template_name=''
    # list=studentcourse.objects.filter(student__studentname__exact='Vava')
    list=student.objects.filter(student_course__status="Break")
    list=student.objects.filter(student_course__course=course.objects.get(coursename='BSc Maths'))
    print(list)
    return HttpResponse("hello")
def regroupexample1(request):
    # template_name='kittypartyapp/regroupdivya.html'
    template_name='kittypartyapp/matrixsample.html' 
    if request.method=="GET":      
    
       return render(request,template_name)
    else:
        print(request.POST)
        hiddenval=request.POST.getlist('name')
        for item in hiddenval:
            print(item)
        return render(request,template_name)
    
def regroupexample(request):
    # template_name='kittypartyapp/regroupdivya.html' 
    template_name='kittypartyapp/matrixsample.html' 
    cities = [
    {'name': 'Mumbai', 'population': '200', 'country': 'India','Region':'North India'},
    {'name': 'Puna', 'population': '400', 'country': 'India','Region':'North India'},
    {'name': 'Guhawati', 'population': '500', 'country': 'India','Region':'North India'},
    {'name': 'Surat', 'population': '200', 'country': 'India','Region':'Central India'},
    {'name': 'Kanpur', 'population': '340', 'country': 'India','Region':'Central India'},
     {'name': 'Vareli', 'population': '200', 'country': 'India','Region':'Central India'},
    {'name': 'Nilgiri', 'population': '550', 'country': 'India','Region':'South India'},
    {'name': 'Kolkatta', 'population': '320', 'country': 'India','Region':'South India'},
    {'name': 'Connecticut', 'population': '200', 'country': 'USA','Region':'South America'},
    {'name': 'New York', 'population': '2000', 'country': 'USA','Region':'South America'},
    {'name': 'Miami', 'population': '2000', 'country': 'USA','Region':'South America'},
    {'name': 'Bahama', 'population': '33', 'country': 'USA','Region':'Middle America'},
] 

    
    cities2=[
    {'date': '2020-02-03', 'supplier': 'supp1', 'invoice': 'inv1','taxper':4,'cgst':12,'sgst':12,'taxableamt':120},
    {'date': '2020-02-03', 'supplier': 'supp1', 'invoice': 'inv1','taxper':4,'cgst':23,'sgst':23,'taxableamt':340},
    {'date': '2020-02-03', 'supplier': 'supp1', 'invoice': 'inv1','taxper':9,'cgst':23,'sgst':23,'taxableamt':34},
    {'date': '2020-02-03', 'supplier': 'supp2', 'invoice': 'inv2','taxper':9,'cgst':42,'sgst':42,'taxableamt':340},
    {'date': '2020-02-03', 'supplier': 'supp2', 'invoice': 'inv2','taxper':5,'cgst':120,'sgst':120,'taxableamt':670},
    {'date': '2020-02-03', 'supplier': 'supp2', 'invoice': 'inv2','taxper':5,'cgst':56,'sgst':56,'taxableamt':90},
    {'date': '2020-02-03', 'supplier': 'supp2', 'invoice': 'inv2','taxper':2,'cgst':78,'sgst':78,'taxableamt':12},
    {'date': '2020-02-03', 'supplier': 'supp2', 'invoice': 'inv2','taxper':2,'cgst':66,'sgst':66,'taxableamt':33},
    {'date': '2020-02-03', 'supplier': 'supp3', 'invoice': 'inv3','taxper':4,'cgst':12,'sgst':12,'taxableamt':600},
    {'date': '2020-02-03', 'supplier': 'supp3', 'invoice': 'inv3','taxper':1,'cgst':89,'sgst':89,'taxableamt':100},
    {'date': '2020-02-03', 'supplier': 'supp3', 'invoice': 'inv3','taxper':1,'cgst':76,'sgst':76,'taxableamt':33},
    {'date': '2020-02-03', 'supplier': 'supp4', 'invoice': 'inv4','taxper':5,'cgst':398,'sgst':398,'taxableamt':209},

    ]

    
    divyalist=[[5, '52500.000', '1250.000', '1250.000', '0.000'],
[17, '292500.000', '21250.000', '21250.000', '0.000'],
[4, '14560.000', '280.000', '280.000', '0.000'],
[17, '2340.000', '170.000', '170.000', '0.000'],
[4, '8320.000', '160.000', '160.000', '0.000'],
[5, '157500.000', '3750.000', '3750.000', '0.000'],
[17, '2340.000', '170.000', '170.000', '0.000'],
[4, '1664000.000', '32000.000', '32000.000', '0.000'],
[5, '84000.000', '2000.000', '2000.000', '0.000'],
[4, '2080.000', '40.000', '40.000', '0.000'],
[4, '208000.000', '4000.000', '4000.000', '0.000'],
[5, '6300.000', '150.000', '150.000', '0.000'],
[4, '12480.000', '240.000', '240.000', '0.000'],
[5, '26250.000', '625.000', '625.000', '0.000'],
[17, '9828.000', '714.000', '714.000', '0.000'],
[4, '20800.000', '400.000', '400.000', '0.000'],
[17, '23400.000', '1700.000', '1700.000', '0.000']]
    list_4=[]
    list_5=[]
    list_17=[]

    for item in divyalist:
        # print(item)
        if item[0]==4:
            list_4.append(item)
        elif item[0]==5:
            list_5.append(item)
        elif item[0]==17:
            list_17.append(item)
    # print(list_4)
    # print('**********************')
    # print(list_5)
    # print('**********************')
    # print(list_17)
    # print('**********************')
    #return HttpResponse('')
    

    list_main=[]
    list_main.append(list_4)
    list_main.append(list_5)
    list_main.append(list_17)
    pd.DataFrame(list_main)
    # return HttpResponse(myres)
    context={'listmain':list_main}
    return render(request,template_name,context)