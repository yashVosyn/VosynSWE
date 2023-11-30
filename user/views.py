from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"user/index.html")

def signup(request):
    return HttpResponse("hello this is signup page")
        