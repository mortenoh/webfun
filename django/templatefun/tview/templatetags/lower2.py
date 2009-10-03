
from django import template

register = template.Library()

@register.filter
def lower2(value):
	return value.lower()

