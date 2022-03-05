from .Serializers import StudentSerializer
from rest_framework.generics import ListAPIView,CreateAPIView
from .models import Student
from rest_framework.filters import SearchFilter
# Create your views here.
class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer#define name of the serializer
    filter_backends=[SearchFilter]
    search_fields=['=name']
    # search_fields=['=name']#the search contnet must have same name as registered in  database else return False