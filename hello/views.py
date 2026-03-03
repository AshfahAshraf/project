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

def aboutus(request):
    return render(request, "aboutUs.html")

def contact(request):
    return render(request,"contact.html")

def cart(request):
    return render (request,"cart.html")

def wishlist(request):
    return render(request,"wishlist.html")

def faq(request):
    return render(request,'faq.html')

def return_refund(request):
    return render(request,"return_refund.html")


def shipping_info(request):
    return render(request,"shipping_info.html")

def my_account(request):
    return render(request,"my_account.html")

def order(request):
    return render(request,"order.html")

def seller_home(request):
    return render(request,"seller_home.html")