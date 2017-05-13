from django import template

register = template.Library()


@register.filter
def get_color(properties, status):
    return properties['statuses'][status]['color_class']