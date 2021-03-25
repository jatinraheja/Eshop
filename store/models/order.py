import datetime

from store.models import Product
from store.models import Customer
from django.db import models

class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=50,default='',blank=True)
    phone = models.CharField(max_length=50,default='',blank=True)
    price = models.IntegerField()
    date = models.DateField(default=datetime.datetime.today())
    status = models.BooleanField(default=False)

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')


