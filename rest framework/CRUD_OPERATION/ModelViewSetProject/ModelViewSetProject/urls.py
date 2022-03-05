from xml.etree.ElementInclude import include
from django import views
from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
router= DefaultRouter()#Router Object
#Register Studentviewsert with ROuter
router.register('studentapi',views.StudentViewSet,basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
]
