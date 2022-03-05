from .Serializers import StudentSerializer
from rest_framework.generics import ListAPIView,CreateAPIView
from .models import Student
from rest_framework.filters import OrderingFilter
# Create your views here.
class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer#define name of the serializer
    filter_backends=[OrderingFilter]
    ordering_fields=['name']#for executing specific field ordering