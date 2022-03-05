from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.throttling import ScopedRateThrottle

class StudentList(ListAPIView):
    queryset=Student.objects.all()#define name of the model
    serializer_class=StudentSerializer#define name of the serializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='viewstu'
class StudentCreate(CreateAPIView):
    queryset=Student.objects.all()#define name of the model
    serializer_class=StudentSerializer#define name of the serializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='modify'
class StudentRead(RetrieveAPIView):
    queryset=Student.objects.all()#define name of the model
    serializer_class=StudentSerializer#define name of the serializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='viewstu'
class StudentUpdate(UpdateAPIView):
    queryset=Student.objects.all()#define name of the model
    serializer_class=StudentSerializer#define name of the serializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='modify'
class StudentDestroy(DestroyAPIView):
    queryset=Student.objects.all()#define name of the model
    serializer_class=StudentSerializer#define name of the serializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='modify'