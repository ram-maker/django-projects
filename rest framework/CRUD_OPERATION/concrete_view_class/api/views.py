from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView

class StudentListCreate(ListCreateAPIView):
    queryset=Student.objects.all()#define name of the model
    serializer_class=StudentSerializer#define name of the serializer
class StudentReadUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()#define name of the model
    serializer_class=StudentSerializer#define name of the serializer
class StudentList(ListAPIView):
    queryset=Student.objects.all()#define name of the model
    serializer_class=StudentSerializer#define name of the serializer
class StudentCreate(CreateAPIView):
    queryset=Student.objects.all()#define name of the model
    serializer_class=StudentSerializer#define name of the serializer

class StudentRead(RetrieveAPIView):
    queryset=Student.objects.all()#define name of the model
    serializer_class=StudentSerializer#define name of the serializer

class StudentUpdate(UpdateAPIView):
    queryset=Student.objects.all()#define name of the model
    serializer_class=StudentSerializer#define name of the serializer

class StudentDestroy(DestroyAPIView):
    queryset=Student.objects.all()#define name of the model
    serializer_class=StudentSerializer#define name of the serializer

