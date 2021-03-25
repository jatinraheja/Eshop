from django.views import View
from django.shortcuts import redirect
from store.models.product import Product
from store.models.order import Order
from store.models.order import Customer
from store.models.cart import Cart
class CheckOut(View):
    def post(self,request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        cart_objects = Cart.get_all_products_by_user(request.user.id)
        for cart in cart_objects:
            order = Order(address=address,
                          phone = phone,
                          customer=Customer.objects.get(user = request.user),
                          quantity = cart.quantity,
                          product = cart.product,
                          price = cart.product.price
                          )
            order.save()
        Cart.objects.all().delete()
        return redirect('cart')
