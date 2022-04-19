from django import template
from django.utils.html import avoid_wrapping
from django.utils import formats

register = template.Library()

@register.filter
def toBS(txt):
    t = str(txt)
    if t == "Green":
        return "success"
    elif t == "Yellow":
        return "warning"
    elif t == "Red":
        return "danger"
    return "black"
