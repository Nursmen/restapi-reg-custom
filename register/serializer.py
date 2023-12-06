from rest_framework import serializers
from .models import CustomUser, Task, Photo

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=('name', 'age', 'rank', 'balance')

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields=('name', 'description', 'status')

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Photo
        fields=('name', 'image')