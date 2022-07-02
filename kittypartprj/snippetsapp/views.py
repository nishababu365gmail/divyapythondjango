from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Snippet,Flower
from .serializers import SnippetSerializer,FlowerSerializer

# @csrf_exempt
@api_view(['GET'])
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)
@api_view(['GET'])
def flower_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        flowers = Flower.objects.all()
        serializer = FlowerSerializer(flowers, many=True)
        
        return Response(serializer.data)
@api_view(['GET','POST','PUT','PATCH'])

def editflower(request,flowerid):
    flowerinstance=Flower.objects.get(id=flowerid)
    if request.method=="GET":
     flowerinstance=Flower.objects.get(id=flowerid)
     serializer=FlowerSerializer(flowerinstance)     
     return Response(serializer.data)
    elif request.method=='PATCH':
     print('maaaaaaaaaaaaaaaaaa')
     data = JSONParser().parse(request)
     serializer=FlowerSerializer(flowerinstance,data)     
     
     if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
@api_view(['POST'])
def snippet_save(request):
    
    if request.method=="POST":
        serisnippet=SnippetSerializer(data=request.data)       
        
        if serisnippet.is_valid():
           serisnippet.save()
           return Response(status=status.HTTP_201_CREATED)
        else:
           return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
@api_view(['POST'])
def flower_save(request):    
    if request.method=="POST":
        serisnippet=FlowerSerializer(data=request.data)  
        serisnippet.is_valid()
        print(serisnippet.errors)
        if serisnippet.is_valid():
           serisnippet.save()
           return Response(status=status.HTTP_201_CREATED)
        else:
           return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


