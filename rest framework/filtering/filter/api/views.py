from .Serializers import StudentSerializer
from rest_framework.generics import ListAPIView,CreateAPIView
from .models import Student
# Create your views here.
class StudentList(ListAPIView):
    # queryset=Student.objects.filter(passby="hanamo")#lists only those data that has been passed by hanamo
    queryset=Student.objects.all()
    serializer_class=StudentSerializer#define name of the serializer
    def get_queryset(self):
        user=self.request.user
        return Student.objects.filter(passby=user)
class StudentCreate(CreateAPIView):
    queryset=Student.objects.all()#define name of the model
    serializer_class=StudentSerializer#define name of the serializer    