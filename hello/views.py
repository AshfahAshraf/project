from django.shortcuts import render,redirect
from .models import * 
from django.db.models import Q

# email
import random
from django.core.mail import send_mail

# contact
from django.contrib import messages
from .models import Complaint

# Create your views here.


def index(request):

    if request.method == 'POST':

        #REGISTER
        if "register" in request.POST:
            username = request.POST["textUsername"]
            email_phone = request.POST["textEmailPhone"]
            password = request.POST["textPassword"]
            confirm_password = request.POST["textConfirmPassword"]

            if password != confirm_password:
                print("passwords do not match")
                return render(request,"register.html")
        
            email = None
            phone_number = None

            if "@" in email_phone:
                email = email_phone
            else:
                phone_number = email_phone

            reg = User(Username =username,
                       Email =email,
                       Phone_Number =phone_number,
                       Password = password
            ) 
            reg.save()


        #LOGIN

        elif "login" in request.POST:
            email_phone = request.POST["textEmailPhone"]  # email or phone
            password = request.POST["textPassword"]

            try:
                user = User.objects.get(
                    Q(Email = email_phone) | Q(Phone_Number = email_phone),
                    Password =password
                )

                request.session["user"] = user.id
                return redirect("home")
            except User.DoesNotExist:
                print("invalid login")
        

    return render(request, "register.html")
########
#email 

# send otp 

def send_otp(request):

    if request.method == "POST":
        email = request.POST["email"]


        #check if email exists
        if not User.objects.filter(Email=email).exists():
            return render(request, "send_otp.html",{"error": "Email not registered"})

        otp = str(random.randint(100000, 999999))

        #store in session instead of database
        request.session['email'] = email
        request.session['otp'] =otp

        send_mail(
            "Password Reset OTP",
            f"Your OTP is {otp}",
            "yourgmail@gmail.com",
            [email],
            fail_silently=False,
        )

        

        return redirect("verify_otp")
    
    return render(request, "send_otp.html")


#verify otp

def verify_otp(request):

    if request.method == "POST":
        user_otp = request.POST["otp"]
       


        if user_otp == request.session.get("otp_verifedwokring?"):
            request.session["otp_verifed"] =True
            return redirect("reset_password")
           
        else:
           return render(request, "verify_otp.html", {"error": "Invalid OTP"})

    return render(request, "verify_otp.html")


#reset password

def reset_password(request):

    if not request.session.get("otp_verified"):
        return redirect("send_otp")

    if request.method == "POST":
        new_password = request.POST["newPassword"]
        email = request.session.get("email")

        user = User.objects.get(Email=email)
        user.Password = new_password
        user.save()

        return redirect("register")
    
    return render(request,"reset_password.html")
#########
def terms_conditon(request):
    return render(request, "terms_conditon.html")

def privacy_policy(request):
    return render(request,"privacy_policy.html")

def navbar(request):
    return render(request,"navbar.html")

def footer(request):
    return render(request,"footer.html")

def home(request):
    return render(request ,"Home.html")

def aboutus(request):
    return render(request, "aboutUs.html")

def contact(request):

    if request.method =="POST":

        fullname = request.POST["fullname"]
        email = request.POST["email"]
        phonenumber = request.POST["phonenumber"]
        orderid = request.POST["orderid"]
        productname =request.POST["productname"]
        issue_type = request.POST["issue_type"]
        description = request.POST["description"]
        product_image = request.FILES["product_image"]


        Complaint.objects.create(
            Fullname =fullname,
            Email = email,
            Phonenumber = phonenumber,
            Orderid = orderid,
            Productname = productname,
            Issue_type = issue_type,
            Product_image = product_image,
            Description = description
        )

        #confirmation email
        send_mail(
            "Complaint Received",
            f"Hello  {fullname},\n\nYour complaint has been received successfully. Our support team will contact you soon.\n\nThank you,",
            "supoort@yourwebsite.com",
            [email],
            fail_silently=False
        )

        messages.success(request,"Complaint submitted successfully!")

        return redirect("contact")

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

def artisan_register(request):
    return render(request,"artisan_register.html")
