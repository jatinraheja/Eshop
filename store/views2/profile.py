from django.views import View
from django.shortcuts import render,redirect
from store.models import Customer
from django.contrib.auth.hashers import make_password
class Profile(View):
    def get(self,request):
        print(f'user email  {request.user.email}')
        customer = Customer.get_customer_by_email(request.user.email)
        print(f'customer {customer}')
        return render(request,'profile.html',{'customer':customer})