from django.db import models
from django.contrib.auth.models import User
class Customer(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    phone = models.IntegerField()

    @staticmethod
    def get_customer_by_email(email):
        try:
            user = User.objects.get(email=email)
            customer =  Customer.objects.filter(user=user)
            return customer[0]
        except:
            return False



