from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

from .models import CustomUser, Photo, Task
from .serializer import DataSerializer, PhotoSerializer, TaskSerializer

# Create your views here.
@api_view(['GET'])
def getData(request):
    app = CustomUser.objects.all()
    serializer = DataSerializer(app, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postData(request):
    serializer = DataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getPhoto(request):
    app = Photo.objects.all()
    serializer = PhotoSerializer(app, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postPhoto(request):
    serializer = PhotoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getTask(request):
    app = Task.objects.all()
    serializer = TaskSerializer(app, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postTask(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)