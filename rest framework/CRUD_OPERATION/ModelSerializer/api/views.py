from functools import partial
from django.shortcuts import render
import requests
import io
from requests.api import post
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.serializers import Serializer
from .Serializers import StudentSerializer
from django.http import HttpResponse, JsonResponse
from .models import Student
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
# Create your views here.
def req(request):
    if request.method == 'GET':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id',None)
        if id is not None:
            stu=Student.objects.get(id=id)
            serialized_data=StudentSerializer(stu)
            json_data = JSONRenderer().render(serialized_data.data)
            return HttpResponse(json_data,content_type='application/json')
        stu=Student.objects.all()
        serialized_data=StudentSerializer(stu,many=True)
        json_data = JSONRenderer().render(serialized_data.data)
        return HttpResponse(json_data,content_type='application/json')
    if request.method == 'POST':
        json_data=request.body
        stream= io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serialized_data=StudentSerializer(data=pythondata)
        if serialized_data.is_valid():
            serialized_data.save()
            res={'msg':'Post implemented'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serialized_data.errors)
        return HttpResponse(json_data,content_type='application/json')
    if request.method == 'PUT':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id') 
        stu=Student.objects.get(id=id)
        serialized_data=StudentSerializer(stu,data=pythondata,partial=True)
        if serialized_data.is_valid():
            serialized_data.save()
            res={'msg':'data Updated!!'} 
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')     
        json_data=JSONRenderer.render(serialized_data.errors)
        return HttpResponse(json_data,content_type='application/json')                                                  
    if request.method == 'DELETE':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        res={'msg':'data deleted'}
        # json_data=JSONRenderer().render(res)
        # return HttpResponse(json_data,content_type='application/json') 
        return JsonResponse(res,safe=False)




