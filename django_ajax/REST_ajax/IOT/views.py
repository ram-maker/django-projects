from django.shortcuts import render
from .forms import UserRegistration
# Create your views here.
def home(request):
    form=UserRegistration()
    return render(request,'pages/home.html',{'form':form})