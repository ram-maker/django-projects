from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
# http -f POST  http://127.0.0.1:8000/studentapi/ name=Badri roll=10 city=pokhari  'Authorization:Token cec074a0696031fcd835a8f4984b76f99f1f2c2e'