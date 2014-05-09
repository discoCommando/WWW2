from django.template import Library

register = Library()

@register.filter
def minus( value, arg ):
	return value - arg
	
