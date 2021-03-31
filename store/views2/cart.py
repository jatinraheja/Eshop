from django.views import View
from django.shortcuts import render,redirect
from store.models.cart import Cart
class Cart_View(View):
    def get(self,request):
        if request.user.is_authenticated:
            cart = Cart.get_cart_by_user_id(request.user.id)
            cart_size = Cart.get_all_products_by_user(request.user.id)
            return render(request,'cart.html',{'Cart':cart,'cart_size':len(cart_size)})

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



