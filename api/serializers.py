from rest_framework import serializers
from .models import  ImgFile

class ImgFileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=ImgFile
        fields=['img']