
from django import template

register = template.Library()

@register.filter
def lower(value):
	return value.lower()

@register.filter
def upper(value):
	return value.upper()

class UpperNode(template.Node):
	def __init__(self, nodelist):
		self.nodelist = nodelist

	def render(self, context):
		output = self.nodelist.render(context)
		return output.upper()

@register.tag('upper')
def do_upper(parser, token):
	nodelist = parser.parse(('endupper',))
	parser.delete_first_token()
	return UpperNode(nodelist)

@register.simple_tag
def current_time():
	from datetime import datetime
	return datetime.now()

