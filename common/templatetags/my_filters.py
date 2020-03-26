from django import template

from ..models import SiteSettings
from users.models import CustomUser, ShoppingCart

register = template.Library()


@register.filter
def get_shopping_cart(pk):
    user = CustomUser.objects.get(pk=pk)
    cart_obj_list = ShoppingCart.objects.filter(user=user)

    return cart_obj_list


@register.filter
def calc_total_order_price(pk):
    user = CustomUser.objects.get(pk=pk)
    cart_obj_list = ShoppingCart.objects.filter(user=user)
    total_price = 0
    for cart_obj in cart_obj_list:
        price = cart_obj.post.price
        amt = cart_obj.order_amt
        total_price += price * amt

    return total_price


@register.filter
def get_site_settings(true):
    site_settings = SiteSettings.objects.get(is_selected=true)

    return site_settings
