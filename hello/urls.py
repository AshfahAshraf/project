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

      #cart
      path('cart',views.cart_view,name="cart"),
      path("add-to-cart/<int:product_id>/",views.add_to_cart, name="add_to_cart"),
      path("remove-cart/<int:cart_id>/",views.remove_from_cart, name="remove_cart"),
      path("increase/<int:cart_id>/",views.increase_quantity, name="inreases"),
      path('decrease/<int:cart_id>/',views.decrease_quantity, name="decrease"),

    #wishlist
      path("wishlist/",views.wishlist_view, name="wishlist"),
      path("add-wishlist/<int:product_id>/",views.add_to_wishlist,name="add_wishlist"),
      path('remove-wishlist/<int:wishlist_id>/',views.remove_wishlist,name="remove_wishlist"),
      path("wishlist-to-cart/<int:wishlist_id>/",views.wishlist_to_cart,name='wishlist_to_cart'),


      re_path('^faq$',views.faq,name="faq"),
      re_path('^return_refund$',views.return_refund,name="return_refund"),
      re_path('^shipping_info$',views.shipping_info,name="shipping_info"),
      re_path('^my_account$',views.my_account,name="my_account"),
      re_path('^order$',views.order,name="order"),
      re_path('^seller_home$',views.seller_home,name="seller_home"),
      re_path('^artisan_register$',views.artisan_register,name="artisan_register"),




 ]