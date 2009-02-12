from django.template import Library

register = Library()

def linklist_media_prefix():
    "Returns the string contained in the setting LINKLIST_MEDIA_URL."
    try:
        from django.conf import settings
    except ImportError:
        return ''
    return settings.LINKLIST_MEDIA_URL
linklist_media_prefix = register.simple_tag(linklist_media_prefix)