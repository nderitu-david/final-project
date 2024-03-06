from django import template
import math
register =  template.Library()

@register.simple_tag
def call_sellprice(price,Discount):
    if Discount is None or Discount is 0:
        return price
    sellprice = price
    sellprice  = price - (price * Discount/100)
    return math.floor(sellprice)