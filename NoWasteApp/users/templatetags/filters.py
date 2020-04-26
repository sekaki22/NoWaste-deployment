from django import template

register = template.Library()

@register.filter(name = 'cut')
def cut (value, arg):
    """
    This cuts out specific element from a string determined by arg (Everthing equal to arg will be cut of)
    """

    return value.replace(arg, '')
