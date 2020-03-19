from django import template

from users.models import CustomUser, ShoppingCart

register = template.Library()


@register.filter
def get_shopping_cart(username):
    user = CustomUser.objects.get(username=username)
    cart_obj_list = ShoppingCart.objects.filter(user=user)

    return cart_obj_list


@register.filter
def calc_total_order_price(username):
    user = CustomUser.objects.get(username=username)
    cart_obj_list = ShoppingCart.objects.filter(user=user)
    total_price = 0
    for cart_obj in cart_obj_list:
        price = cart_obj.post.price
        amt = cart_obj.order_amt
        total_price += price * amt

    return total_price
