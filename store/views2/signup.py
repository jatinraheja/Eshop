import re
from django.views import View
from django.shortcuts import render,redirect
from store.models import Customer
from  django.core.validators import validate_email
from django.contrib.auth.models import User
class Signup(View):
    def get(self,request):
        return render(request,'signup.html')

    def post(self,request):
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        data = {}
        data['first_name'] = first_name
        data['last_name'] = last_name
        data['username'] = username
        data['email']   = email
        data['phone']  = phone
        error_message = self.validateCode(data,password1,password2)
        data['error'] = error_message
        if error_message:
            return render(request,'signup.html',data)

        else:
           user = User.objects.create_user(first_name=first_name, username=username, email=email, password=password1,
                                            last_name=last_name)
           user.save()
           customer = Customer(user=user,phone=phone)
           customer.save()
           return redirect("login")

    def validateCode(self,data,password1,password2):
        error_message = None
        if not data['first_name']:
            error_message = "first name required"
        elif not data['last_name']:
            error_message = "last name required"
        elif not data['username']:
            error_message = "username required"
        elif not data['email']:
            error_message = "email required"
        elif not password1:
            error_message = "Password required"
        elif not password2:
            error_message = "Please confirm your password"
        elif not re.search('^[a-zA-z]*$', data['first_name']):
            error_message = 'First Name can only have alpha characters'
        elif  not re.search('^[a-zA-z]*$',data['last_name']):
                error_message = 'Last Name can only have alpha characters'
        elif len(data['phone']) != 10:
            error_message = "Phone Number must have 10 digits"
        elif not password1 == password2:
            error_message = "Your password and confirm password does not match"
        elif len(password1) < 8:
            error_message = "The minimum length of password must be 8 characters"
        elif User.objects.filter(username = data['username']).exists():
            error_message = "Username already taken"
        elif User.objects.filter(email = data['email']).exists():
            error_message = "Account with this email id already present"
        else:
            try:
                validate_email(data['email'])
            except:
                error_message = "Invalid email id.Please enter valid email id"

        return error_message
