from django.db import models

# Create your models here.

class User(models.Model):
    Name = models.CharField(max_length=200)
    Username =models.CharField(max_length=250)
    Email =models.EmailField(unique=True,null=True, blank=True)
    Phone_Number = models.CharField(max_length=20,null=True,blank=True)
    Address =models.CharField(max_length=200)
    Password = models.CharField(max_length=250)

    def __str__(self):
        return self.Username
    
class Product(models.Model):
     artisan = models.ForeignKey(Artisan, on_delete=models.CASCADE)
     Product_name = models.CharField(max_length=200)
     Actual_price = models.CharField(max_length=20)
     Quantity = models.IntegerField()
     Offer_price = models.CharField(max_length=10)
     Description = models.TextField()

     def __str__(self):
          return self.Product_name

class Cart(models.Model):
     user =models.ForeignKey(User, on_delete=models.CASCADE)
     product=models.ForeignKey(Product, on_delete=models.CASCADE)
     quantity = models.IntegerField(default=1)
     

class Wishlist(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
          

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product =models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_date = models.DateField(auto_now_add=True)

class Artisan(models.Model):  
     huio

class Complaint(models.Model):
     
     Fullname =models.CharField(max_length=100)
     Email =models.EmailField()
     Phonenumber = models.CharField(max_length=15)
     Orderid = models.CharField(max_length=50)
     Productname = models.CharField(max_length=100)
     Issue_type = models.CharField(max_length=100)
     Product_image =models.ImageField(upload_to="complaints/",null=True, blank=True)
     Description = models.TextField()
     created_at =models.DateTimeField(auto_now_add=True)


     def __str__(self):
          return self.Fullname

         