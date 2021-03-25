from django.views import View
from django.shortcuts import render,redirect
from store.models import Customer
from django.contrib.auth.hashers import make_password,check_password
class ChangePassword(View):
    def get(self,request):
        return render(request,'change_password.html')

    def post(self,request):
        error_message = None
        password = request.POST["password"]
        new_password = request.POST["new_password"]
        confirm_password = request.POST["confirm_password"]
        data={}
        data['password'] = password
        data['new_password'] = new_password
        data['confirm_password'] = confirm_password
        customer = Customer.get_customer_by_email(request.user.email)
        flag = check_password(password,customer.user.password)
        if not password:
            error_message = "Please enter your original password"
        elif not new_password:
            error_message = "Please enter new password"
        elif not confirm_password:
            error_message = "Please confirm your new password"
        elif not confirm_password == new_password:
            error_message = "Your password and confirm password does not match"
        elif len(new_password) < 8:
            error_message = "The minimum length of password must be 8 characters"
        elif flag:
            request.user.set_password(new_password)
            request.user.save()
            return redirect('logout')
        else:
            error_message = "Please enter correct original password"

        if error_message:
            return render(request, "change_password.html", {'error': error_message,'data':data})



