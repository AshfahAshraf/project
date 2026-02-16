from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "register.html")

def navbar(request):
    return render(request,"navbar.html")

def footer(request):
    return render(request,"footer.html")

def home(request):
    return render(request ,"Home.html")