
from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.index,name='home'),
    path('shop',views.shop,name='shop'),
    path('blog',views.blog,name='blog'),
    path('checkout/<int:id>',views.checkout,name='checkout'),
    path('cart/<int:id>',views.cart,name='cart'),

]
