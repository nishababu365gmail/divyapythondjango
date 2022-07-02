from dataclasses import fields
from msilib import text
from numpy import require
from rest_framework import serializers
from snippetsapp.models import Snippet,Flower, LANGUAGE_CHOICES, STYLE_CHOICES
class FlowerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Flower
        fields='__all__'
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Snippet
        exclude=('id','language','style')
#     id=serializers.IntegerField(read_only=True)
#     title=serializers.CharField(required=False,max_length=100,allow_blank=True)
#     code=serializers.CharField(style={'base_template':'textarea.html'})
#     linenos=serializers.BooleanField(required=None)
#     style=serializers.ChoiceField(choices=STYLE_CHOICES)
#     language=serializers.ChoiceField(choices=LANGUAGE_CHOICES)
# def create(self,**validated_data):
#     return Snippet.objects.create(**validated_data)
# def update(self,instance,validated_data):
#     instance.title=validated_data.get('title',instance.title)
#     instance.code=validated_data.get('code',instance.code)
#     instance.linenos=validated_data.get('linenos',instance.linenos)
#     instance.style=validated_data.get('style',instance.style)
#     instance.language=validated_data.get('language',instance.language)
#     instance.save()
#     return instance