from django.views import View
from django.shortcuts import render,redirect
from store.models import Customer,Cart
from django.contrib.auth.hashers import make_password
class Profile(View):
    def get(self,request):
        customer = Customer.get_customer_by_email(request.user.email)
        cart_size = Cart.get_all_products_by_user(request.user.id)
        return render(request,'profile.html',{'customer':customer,'cart_size':len(cart_size)})