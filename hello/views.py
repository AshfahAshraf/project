from django.shortcuts import render,redirect
from .models import * 
from django.db.models import Q

# email
import random
from django.core.mail import send_mail



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

#email 

# send otp 

def send_otp(request):

    if request.method == "POST":
        email = request.POST["email"]

        otp = str(random.randint(100000, 999999))

        EmailOTP.objects.create(email =email, otp =otp)

        send_mail(
            "Password Reset OTP",
            f"Your OTP is {otp}",
            "yourgmail@gmail.com",
            [email],
            fail_silently=False,
        )

        request.session['email'] = email

        return redirect("verify_otp")
    
    return render(request, "send_otp.html")


#verify otp

def verify_otp(request):

    if request.method == "POST":
        user_otp = request.POST["otp"]
        email = request.session.get("email")

        otp_record = EmailOTP.objects.filter(email=email, otp=user_otp).first()

        if otp_record:
            request.session["otp_verified"] = True
            otp_record.delete()
            return redirect("reset_password")
        else:
            print("invalid OTP")

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