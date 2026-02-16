from django.urls import re_path
from .import views
urlpatterns = [
    re_path("^$",views.index),
    re_path("^navbar$",views.navbar,name="navbar"),
    re_path("^footer$",views.footer,name="footer"),
      re_path('^home$',views.home,name="home")
 ]