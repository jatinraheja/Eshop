from django.views import View
from django.shortcuts import render,redirect
from store.models.product import Product
from store.models.category import Category
from store.models.cart import Cart
from django.contrib.auth.models import User
class Index(View):
    def get(self,request):
        categories = Category.get_all_category()
        if request.GET.get("category"):
            products = Product.get_all_products_by_category_id(request.GET.get("category"))
        else:
            products = Product.get_all_products()
        cart_size = Cart.get_all_products_by_user(request.user.id)
        data = {}
        data['products'] = products
        data['categories'] = categories
        data['cart_size'] = len(cart_size)
        return render(request, "index.html", data)

    def post(self,request):
        product = request.POST.get('product')
        # cart = request.session.get('cart')
        product_data = Product.get_product_by_id(product)
        cart2 = Cart.get_cart_by_product(product_data,request.user.id)
        remove = request.POST.get('remove')
        size = request.POST.get('size')
        # if cart:
        #     quantity = cart.get(product)
        #     if quantity:
        #         if remove:
        #             if quantity == 1:
        #                 cart.pop(product)
        #             else:
        #                 cart[product] = quantity - 1
        #         else:
        #             cart[product] = quantity + 1
        #
        #     else:
        #         cart[product] = 1
        #
        # else:
        #     cart = {}
        #     cart[product] = 1
        #
        # request.session["cart"] = cart

        if cart2:
            quantity2 = Cart.get_product_quantity_by_product(product_data,request.user.id)
            print(f'Quantity2 {quantity2}')
            if quantity2:
                if remove:
                    if quantity2 == 1:
                        Cart.delete_by_product(product_data,request.user.id)
                        return redirect('/')
                    else:
                        quantity2 = quantity2 - 1
                else:
                    quantity2 = quantity2 + 1
            else:
                quantity2 = 1

            Cart.update_product_quantity_in_cart(cart2, quantity2)

        else:
            user = User.objects.get(email=request.user.email)
            if size:
                cart_object = Cart(user=user,product=product_data, quantity=1,size=size)
                cart_object.save()
                return redirect('cart')
            else:
                cart_object = Cart(user=user,product=product_data, quantity=1)
            cart_object.save()


        return redirect('/')
