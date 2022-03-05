from xml.etree.ElementInclude import include
from django import views
from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from api.auth import CustomAuthToken
router= DefaultRouter()#Router Object
#Register Studentviewsert with ROuter
router.register('studentapi',views.StudentViewSet,basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
    # path('gettoken/',obtain_auth_token)#for obtaining token from http
    path('gettoken/',CustomAuthToken.as_view())#url for exposing endpoint, separate auth.py file was created
]
#Use http POST http://127.0.0.1:8000/gettoken/ username="superuser" password="superuser"  for endpoints
