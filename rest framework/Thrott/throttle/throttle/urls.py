from xml.etree.ElementInclude import include
from django import views
from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView 

router= DefaultRouter()#Router Object
#Register Studentviewsert with ROuter
router.register('studentapi',views.StudentViewSet,basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('gettoken/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('auth/',include('rest_framework.urls',namespace='rest_framework'))
    ]
