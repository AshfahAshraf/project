from django.shortcuts import render,redirect
from .models import * 
from django.db.models import Q

# email
import random
from django.core.mail import send_mail

# contact
from django.contrib import messages

#cart
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
@login_required
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

def home(request):                #
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

########## cart

def cart_view(request):

    cart_items= []
    total_price = 0
    total_items = 0

    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)

   

    for item in cart_items:
        total_price += item.product.offer_price * item.quantity
        total_items += item.quantity

    context = {
        "cart_items": cart_items,
        "total_price": total_price,
        "total_items": total_items
    }

    return render(request,"cart.html", context)

# add product to cart

def add_to_cart(request, product_id):

    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(
        user= request.user,
        product =product
    )
    if not created:
        cart_item.quantity +=1
        cart_item.save()
    return redirect("cart")

# remove product from cart

def remove_from_cart(request, cart_id):
    item =get_object_or_404(Cart, id=cart_id, user=request.user)
    item.delete()

    return redirect("cart")

# increase_quantity

def increase_quantity(request, cart_id):
    item = get_object_or_404(Cart, id=cart_id, user=request.user)

    if item.quantity < item.product.Quantity: 
        item.quantity +=1
        item.save()

    return redirect("cart")


# decrease_quantity 

def decrease_quantity(request, cart_id):
    item = get_object_or_404(Cart, id=cart_id, user=request.user)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()

    return redirect("Cart")


################


# wishlist

# add product to wishlist

def add_to_wishlist(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    Wishlist.objects.get_or_create(
        user=request.user,
        product=product
    )

    return redirect("wishlist")

# wislist page view

def wishlist_view(request):


    if request.user.is_authenticated:
        wishlist_items = Wishlist.objects.filter(user=request.user)
    else:
        wishlist_items = []
    context ={
        "wishlist_items": wishlist_items
    }

    return render(request, "wishlist.html",context)

# remove from wishlist

def remove_wishlist(request, wishlist_id):
    item = get_object_or_404(Wishlist, id=wishlist_id, user=request.user)

    item.delete()

    return redirect("wishlist")

# move wishlist item to cart

def wishlist_to_cart(request, wishlist_id):
    wishlist_item = get_object_or_404(
        Wishlist,
        id=wishlist_id,
        user =request.user)

    product = wishlist_item.product

    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    wishlist_item.delete()

    return redirect("wishlist")
#########

def faq(request):
    return render(request,'faq.html')

def return_refund(request):
    return render(request,"return_refund.html")


def shipping_info(request):
    return render(request,"shipping_info.html")

def my_account(request):

    user_id = request.session.get("user_id")

  

    # if not user_id:
    #     return redirect("register")


    user = User.objects.filter(id=user_id).first()

    # if not user:
    #     request.session.flush()
    #     return redirect("register")

    if request.method == "POST":

        user.Username = request.POST["username"]
        user.email = request.POST["email"]
        user.phone_number = request.POST["phone_number"] 

        user.save()   


    orders = Order.objects.filter(user=user).order_by("-order_date")[:3]

    address = Address.objects.filter(user =user).first()


    context = {
        "user": user,
        "orders": orders,
        "address": address
    }
    return render(request,"my_account.html", context)

def order(request):
    return render(request,"order.html")

def seller_home(request):
    return render(request,"seller_home.html")

def artisan_register(request):
    return render(request,"artisan_register.html")

def change_password(request):
    return render(request, "change_password.html")

def address(request):
    return render(request, "address.html")

def logout_view(request):
    request.session.flush()
    return redirect("/")