from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
# @api_view()
#For GET
# def hello_world(request):
#     return Response({"msg":"This is GET request implemented"})
#For POST
# @api_view(['POST'])
# def hello_world(request):
#     if request.method=="POST":
#         print(request.data)
#         return Response({"msg":"This is POST implemented"})
#For POST and GET
@api_view(['GET','POST'])
def hello_world(request):
    if request.method == 'GET':
        return Response({"msg":"This is GET method implemented"})
    if request.method=="POST":
        print(request.data)
        return Response({"msg":"This is POST implemented",'data':request.data})
    