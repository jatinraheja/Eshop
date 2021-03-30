from django.contrib.auth.models import User
from django.views import View
from django.shortcuts import render,redirect
from store.models import Product, Cart


class ProductDetails(View):
    def get(self,request):
        product_id = request.GET['product_id']
        product = Product.get_product_by_id(product_id)
        return render(request,'product_details.html',{'product':product})

    def post(self, request):
        product = request.POST.get('product')
        product_data = Product.get_product_by_id(product)
        cart2 = Cart.get_cart_by_product(product_data, request.user.id)
        remove = request.POST.get('remove')
        size = request.POST.get('size1')
        print(f"product details")
        if cart2:
            quantity2 = Cart.get_product_quantity_by_product(product_data, request.user.id)
            if quantity2:
                if remove:
                    if quantity2 == 1:
                        Cart.delete_by_product(product_data, request.user.id)
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


