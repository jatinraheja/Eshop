from django.views import View
from django.shortcuts import render
from store.models.order import Order
from store.models.customer import Customer
class OrderView(View):
    def get(self,request):
        customer = Customer.objects.get(user=request.user)
        orders = Order.get_orders_by_customer(customer)
        return render(request,'orders.html',{'orders':orders})



