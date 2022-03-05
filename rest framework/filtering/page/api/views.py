from .Serializers import StudentSerializer
from rest_framework.generics import ListAPIView,CreateAPIView
from .models import Student
from .mypaginations import MyPageNumberPagination
# Create your views here.
class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer#define name of the serializer
    pagination_class= MyPageNumberPagination