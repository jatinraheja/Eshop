from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


class Login(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        error_message = None
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.get(email=email)
        user = auth.authenticate(username=user.username, password=password)
        if user:
            auth.login(request, user)
            request.session['customer_id'] = user.id
            request.session['email'] = user.email
            return redirect('homepage')

        else:
            messages.error(request,"Invalid credentials")
            return render(request, "login.html")


def logout(request):
    request.session.clear()
    auth.logout(request)
    return redirect('login')
