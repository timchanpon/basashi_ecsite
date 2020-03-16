from django import template

from users.models import CustomUser, ShoppingCart

register = template.Library()


@register.filter
def get_shopping_cart(username):
    user = CustomUser.objects.get(username=username)
    tmp = ShoppingCart.objects.filter(user=user)

    return tmp
