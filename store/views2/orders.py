from django.views import View
from django.shortcuts import render
from store.models.order import Order
from store.models.customer import Customer
from store.models.cart import Cart
class OrderView(View):
    def get(self,request):
        customer = Customer.objects.get(user=request.user)
        orders = Order.get_orders_by_customer(customer)
        cart_size = Cart.get_all_products_by_user(request.user.id)
        return render(request,'orders.html',{'orders':orders,'cart_size':len(cart_size)})



