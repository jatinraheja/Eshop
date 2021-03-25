from django.views import View
from django.shortcuts import render,redirect
from store.models.product import Product
from store.models.cart import Cart
from django.contrib.auth.models import User
class Cart_View(View):
    def get(self,request):
        if request.user.is_authenticated:
            cart = Cart.get_cart_by_user_id(request.user.id)
            return render(request,'cart.html',{'Cart':cart})

        else:
            return redirect('homepage')


    def post(self,request):
        remove_product = request.POST.get('remove_product')
        cart = request.POST.get('cart')
        remove = request.POST.get('remove')
        size = request.POST.get('size')

        if remove_product:
            cart_id = request.POST.get('product_to_be_remove')
            Cart.delete_by_id(cart_id)

        elif cart:
            # import pdb;
            # pdb.set_trace()
            cart_object = Cart.get_cart_by_id(cart)
            quantity = cart_object.quantity
            if quantity:
                if remove:
                    if quantity == 1:
                        Cart.delete_by_id(cart)
                        return redirect("cart")
                    else:
                        quantity = quantity - 1
                else:
                    quantity = quantity + 1
                Cart.update_product_quantity_in_cart(cart_object,quantity)
            else:
                Cart.delete_by_id(cart)


        return redirect('cart')



