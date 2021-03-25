from store.models import Product
from django.db import models
from django.contrib.auth.models import User
class Cart(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    size = models.IntegerField(default=0)

    @staticmethod
    def get_cart_by_product(product,user_id):
        cart = Cart.objects.filter(product=product,user=user_id)
        if cart:
            return cart[0]
        else:
            return None

    @staticmethod
    def get_all_products_by_user(user_id):
        return Cart.objects.filter(user = user_id)

    @staticmethod
    def get_product_quantity_by_product(product,user_id):
        cart = Cart.objects.filter(product=product,user=user_id)
        if cart:
            print(f'cart quantity {cart[0].get_quantity()}')
            return cart[0].get_quantity()
        else:
            return None

    @staticmethod
    def delete_by_product(product,user_id):
        Cart.objects.filter(product=product,user=user_id).delete()

    @staticmethod
    def delete_by_id(cart_id):
        Cart.objects.filter(id=cart_id).delete()


    @staticmethod
    def update_product_quantity_in_cart(cart,quantity):
        cart.set_cart_quantity(quantity)
        cart.save()

    @staticmethod
    def get_cart_by_id(cart_id):
        return Cart.objects.filter(id=cart_id)[0]

    @staticmethod
    def get_cart_by_user_id(user_id):
        if user_id:
            return Cart.objects.filter(user=user_id)
        else:
            return None

    def set_cart_quantity(self,quantity):
        self.quantity = quantity


    def get_quantity(self):
        return self.quantity








