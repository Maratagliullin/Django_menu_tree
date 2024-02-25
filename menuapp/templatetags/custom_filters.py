from django import template

register = template.Library()


@register.filter(name='clean_path')
def clean_path(value):
    return value.strip().replace('/', '')
