from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.views import View
from django.shortcuts import render,redirect
from validate_email import validate_email
from store.models import Customer
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib import messages
from EShop import settings
class ResetPassword(View):
    def get(self,request):
        return render(request,'reset_password.html')

    def post(self,request):
        email = request.POST['email']
        if not validate_email(email):
            messages.error(request,"Please enter a valid email")
            return render(request,'reset_password.html')

        user = User.objects.filter(email=email)
        if user:
            current_site = get_current_site(request)
            email_subject = "[Reset your password]"
            message = render_to_string('reset_password_form_link.html',{
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user[0].pk)),
                'token': PasswordResetTokenGenerator().make_token(user[0])})

            email_message = EmailMessage(
                email_subject,
                message,
                settings.EMAIL_HOST_USER,
                [email]

            )
            email_message.send()
            messages.info(request,"Reset Password email has been sent")
            return render(request,'reset_password.html')

        else:
            messages.error(request,"No user with this email id is present")
            return render(request, 'reset_password.html')

