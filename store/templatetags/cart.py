from django import template
from store.models.cart import Cart
register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product,user_id):
    cart = Cart.objects.filter(user=user_id,product=product)
    if cart:
        return True
    else:
        return False

@register.filter(name='cart_quantity')
def cart_quantity(product,user_id):
    cart = Cart.objects.filter(product=product,user=user_id)
    return cart[0].quantity

@register.filter(name='product_total_price')
def product_total_price(product,user_id):
    return product.price * cart_quantity(product,user_id)

@register.filter(name='total_cart_price')
def total_cart_price(Cart,user_id):
    sum = int(0)
    for cart in Cart:
        sum += product_total_price(cart.product,user_id)
    return sum