from django.contrib.auth.models import User
from django.views import View
from django.shortcuts import render,redirect
from store.models import Product, Cart
from django.contrib import messages

class ProductDetails(View):
    def get(self,request):
        product_id = request.GET['product_id']
        product = Product.get_product_by_id(product_id)
        cart_size = Cart.get_all_products_by_user(request.user.id)
        return render(request,'product_details.html',{'product':product,'cart_size':len(cart_size)})

    def post(self, request):
        size = request.POST.get('size1')
        product = request.POST.get('product')
        product_data = Product.get_product_by_id(product)
        if not size:
            messages.error(request, "Please select the size.")
            return render(request, 'product_details.html', {'product': product_data})

        cart2 = Cart.get_cart_by_product(product_data, request.user.id,size)
        remove = request.POST.get('remove')


        if cart2:
            quantity2 = Cart.get_product_quantity_by_product(product_data, request.user.id,size)
            if quantity2:
                if remove:
                    if quantity2 == 1:
                        Cart.delete_by_product(product_data, request.user.id,size=size)
                        return redirect('product_details')
                    else:
                        quantity2 = quantity2 - 1
                else:
                    quantity2 = quantity2 + 1
            else:
                quantity2 = 1

            Cart.update_product_quantity_in_cart(cart2, quantity2)

        else:
            user = User.objects.get(email=request.user.email)
            cart_object = Cart(user=user, product=product_data, quantity=1, size=size)
            cart_object.save()


        return redirect('cart')


