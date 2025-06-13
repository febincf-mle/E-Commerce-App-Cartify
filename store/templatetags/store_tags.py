from django import template


register = template.Library()

@register.filter
def add_value(value, arg):
    return value + arg