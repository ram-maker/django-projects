from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .Serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
# Create your views here.
def student_create(request):
    if request.method == 'POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        Serialized_data=StudentSerializer(data=python_data)
        if Serialized_data.is_valid():
            Serialized_data.save()
            res={'msg':'Data has been inserted'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')


