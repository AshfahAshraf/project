from django.urls import re_path
from .import views
urlpatterns = [
    re_path("^$",views.index),
    re_path("^navbar$",views.navbar,name="navbar"),
    re_path("^footer$",views.footer,name="footer"),
      re_path('^home$',views.home,name="home"),
      re_path('^about_us$',views.aboutus,name="about_Us"),
      re_path('^contact$',views.contact,name='contact'),
      re_path('^cart',views.cart,name="cart"),

 ]