from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    if isinstance(dictionary, dict):
        return dictionary.get(key)
    return None  # ou "" se preferir exibir vazio

@register.filter
def to(value, arg):
    return range(value, arg + 1)
