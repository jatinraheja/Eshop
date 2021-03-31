from django.views import View
from django.shortcuts import render,redirect
from store.models import Customer
from django.contrib.auth.models import User
class EditProfile(View):
    def get(self,request):
        customer = Customer.get_customer_by_email(request.user.email)
        return render(request,'edit_profile.html',{'customer':customer})

    def post(self,request):
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        phone = request.POST["phone"]
        data = {}
        data['first_name'] = first_name
        data['last_name'] = last_name
        data['username'] = username
        data['phone'] = phone
        customer = Customer.get_customer_by_email(request.user.email)
        error_message = None
        if not first_name:
            error_message = "first name required"
        elif not last_name:
            error_message = "last name required"
        elif not username:
            error_message = "username required"
        elif customer.user.username != username:
            if User.objects.filter(username=username).exists():
                error_message = "Username already taken"

        elif customer.phone != int(phone):
            if Customer.objects.filter(phone=phone).exists():
                error_message = "Account with this phone no already present"
        if error_message:
            return render(request,'edit_profile.html',{'error':error_message,'customer':data})
        else:
            user = User.objects.filter(username=request.user.username)[0]
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.save(update_fields=['first_name','last_name','username'])
            customer.phone = phone
            customer.save()
            return redirect('profile')





