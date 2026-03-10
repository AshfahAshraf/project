from django.urls import re_path,path
from .import views
urlpatterns = [
    #register and login page
      path("",views.index,name='register'),
      #email otp
      path("send-otp",views.send_otp,name="send_otp"),
      path("verify-otp",views.verify_otp,name="verify_otp"),
      path("reset-password",views.reset_password,name="reset_password"),

      re_path('^terms_conditons',views.terms_conditon,name='terms_conditons'),
      re_path('^privacy_policy$',views.privacy_policy,name='privacy_policy'),
      re_path("^navbar$",views.navbar,name="navbar"),
      re_path("^footer$",views.footer,name="footer"),
      re_path('^home$',views.home,name="home"),
      re_path('^about_us$',views.aboutus,name="about_Us"),
      re_path('^contact$',views.contact,name='contact'),
      re_path('^cart',views.cart,name="cart"),
      re_path('^wishlist',views.wishlist,name="wishlist"),
      re_path('^faq$',views.faq,name="faq"),
      re_path('^return_refund$',views.return_refund,name="return_refund"),
      re_path('^shipping_info$',views.shipping_info,name="shipping_info"),
      re_path('^my_account$',views.my_account,name="my_account"),
      re_path('^order$',views.order,name="order"),
      re_path('^seller_home$',views.seller_home,name="seller_home"),
      re_path('^artisan_register$',views.artisan_register,name="artisan_register"),




 ]