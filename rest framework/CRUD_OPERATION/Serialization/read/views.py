# from django.Json.response import JsonResponse
from django.shortcuts import render
from rest_framework import serializers
from .serializers import StudentSerializer
from .models import Student
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
# Create your views here.
# for model object
def student_detail(request,pk):
    stu=Student.objects.get(id=pk)
    serializer=StudentSerializer(stu)
    return JsonResponse(serializer.data)
# for query set
def student_list(request):
    stu=Student.objects.all()
    serializer=StudentSerializer(stu, many=True)
    return JsonResponse(serializer.data,safe=False)



