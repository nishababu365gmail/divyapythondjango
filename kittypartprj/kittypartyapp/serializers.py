from rest_framework import serializers
from kittypartyapp.models import course
class courseserializer(serializers.ModelSerializer):
    class Meta:
        model=course
        fields='__all__'
