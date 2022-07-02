from django.forms import formset_factory
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from .serializers import HeroSerializer
from .models import Hero
from .forms import kunjamu
from django.forms import formset_factory
def kunjamuview(request):
      template_name='myapiapp/frmset.html'
      kunjamuformset=formset_factory(kunjamu,extra=2)
      kunjamuformsetobj=kunjamuformset()
      return render(request,template_name=template_name,context={'forms':kunjamuformsetobj})
@api_view(['GET','POST'])
def SayHello(request):
    if request.method=="GET": 
      # heroname=request.data.get('name')
      # heroobj=Hero.objects.get(name=heroname)
      # serhero=HeroSerializer(heroobj)
      # return Response({'Object':serhero})    
       return Response({'message':'hello maaaniii'})
    elif request.method=="POST":
      seri=HeroSerializer(data=request.data)
      if seri.is_valid():
          seri.save()
          return Response({'message':'data saved'})
      else:
          return Response({'message':'data not saved'})        

    elif request.method=="PUT":
        
        heroname=request.data.get('name')
        heroobj=Hero.objects.get(name=heroname)
        serhero=HeroSerializer(heroobj,data=request.data)
        if serhero.is_valid():
          serhero.save()
          return Response({'Object':serhero})
        else:
           return Response({'message':'data not saved'})
@api_view(['GET','PUT'])   
def update_items(request, name):
  if request.method=='GET':          
    item = Hero.objects.get(name=name)
    print(item.pk)
    seri=HeroSerializer(item)
    return Response({'obj':seri.data})
  elif request.method=='PUT':
    item = Hero.objects.get(name=name)        
    data = HeroSerializer(instance=item, data=request.data)
  
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)             


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer
