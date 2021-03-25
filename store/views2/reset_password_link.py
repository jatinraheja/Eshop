from django.contrib.sites.shortcuts import get_current_site
from django.views import View
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from validate_email import validate_email
from store.models import Customer
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib import messages
class ResetPasswordLink(View):
    def get(self,request,uidb64,token):
        context = {
            'uidb64':uidb64,
            'token':token
        }
        try:
            user_id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=user_id)
            if not PasswordResetTokenGenerator().check_token(user,token):
                message = "Password reset link is invalid now please generate new link"
                return render(request, 'reset_password.html',{'message':message})

            return render(request, 'set_new_password.html',context)

        except DjangoUnicodeDecodeError as identifier:
            context['error'] = 'Something went wrong'
            return render(request, 'set_new_password.html',context)


    def post(self,request,uidb64,token):
        new_password = request.POST['new_password']
        confirm_new_password = request.POST['confirm_new_password']
        error_message = None
        flag = False
        if not new_password:
            flag = True
            messages.error(request,"Password required")
        elif not confirm_new_password:
            flag = True
            messages.error(request, "Please confirm your password")
        elif not new_password == confirm_new_password:
            flag = True
            messages.error(request, "Your password and confirm password does not match")
        elif len(new_password) < 8:
            flag = True
            messages.error(request, "The minimum length of password must be 8 characters")
        context = {
            'uidb64': uidb64,
            'token': token
        }
        if flag:
            return render(request, 'set_new_password.html',context)

        try:
            user_id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=user_id)
            user.set_password(new_password)
            user.save()
            # customer = Customer.objects.get(user=user)
            # new_password = make_password(new_password)
            # customer.password = new_password
            # customer.save()
            return redirect('login')

        except DjangoUnicodeDecodeError as identifier:
            messages.error(request, "Something went wrong")
            return render(request, 'set_new_password.html',context)



