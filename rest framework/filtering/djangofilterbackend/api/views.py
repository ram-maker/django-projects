from .Serializers import StudentSerializer
from rest_framework.generics import ListAPIView,CreateAPIView
from .models import Student
# Create your views here.
class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer#define name of the serializer
    filterset_fields=['name','city']