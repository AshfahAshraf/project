from django.urls import path
from .import views
urlpatterns = [
              path('seller_home',views.seller_home,name="seller_home")


]