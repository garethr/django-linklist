from django import template

from linklist.models import Set, Link

register = template.Library()

@register.inclusion_tag('linklist/_link_list.html')
def render_link_list(requested_link_set):
    "Render a list of links as an unordered list"
    try:
        link_set = Set.objects.filter(title=requested_link_set)[0]
        links = Link.objects.filter(link_set=link_set.id,is_live=True).order_by("position")
    except IndexError:
        links = []
    return {
        "links" : links,
    }