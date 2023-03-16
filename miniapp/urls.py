from django.urls import path
from .views import *


urlpatterns = [
    path('user', user),
    path('shop', shop),
    path('signup', userreg),
    path('signupp', shopreg),
    path('verify/<auth_token>', verify),
    path('', index),
    path('profile/<username>/<id>/',profile),
    path('product_upload/<int:id>',upload_product),
    path('editshopuser/<int:id>',editshop),
    path('display',productdisplay),
    path('editproduct/<int:id>',editproduct),
    path('user_profile/<username>/<id>/',userprofile),
    path('edituser/<int:id>', edituser),
    path('cart/<int:id>/<iid>/',cart),
    path('cartdisplay/<iid>',cartdisplay),
    path('cartdelete/<int:id>/<iid>',cartdelete),
    path('buy/<int:id>/',buy),
    path('nav', nav),
    path('demo', demo),
    path('address', address),
    path('placed', orderplaced),

]