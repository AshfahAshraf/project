from django.urls import re_path
from .import views
urlpatterns = [
      re_path("^$",views.index,name='register'),
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

 ]