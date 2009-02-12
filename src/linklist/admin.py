from django.contrib import admin
from django.http import HttpResponseRedirect
from django.utils.datastructures import MultiValueDictKeyError

from linklist.models import Set, Link
from linklist.lib import move_up, move_down

class LinkAdmin(admin.ModelAdmin):
    change_list_template = 'linklist/link_change_list.html'
    
    ordering = ['link_set']
    # note that position is not exposed anywhere on the front end
    # it should only be editied by the buttons
    fieldsets = ((None,
            {
                'fields':(
                    ('title', 'url'),
                    'html_class',
                    'link_set',
                    'is_live',
                )
            }
        ),
    )
    
    def changelist_view(self, request):
        """
        Custom changelist which recreates some of the django changelist but
        with added shiny up and down buttons for reordering the list
        """
        # if someone pressed one of the up or down buttons
        if request.POST and 'action' in request.POST:
            # work out which page we're dealing with
            link_id = request.POST.get('link_id', None)
            link = Link.objects.get(pk = link_id)
            # did we press up or down?
            if 'up' in request.POST['action'].lower():
                # if up then move the page up and output a suitable message
                move_up(link)
                msg='%s moved up.' % link.title
                request.user.message_set.create(message=msg)
            else:
                # if down then move the page down and output a suitable message
                move_down(link)
                msg='%s moved down.' % link.title
                request.user.message_set.create(message=msg)
            return HttpResponseRedirect(request.path)
        # then get back to the django changelist_view
                
        
        return super(LinkAdmin, self).changelist_view(
            request, extra_context = {
                'passed_title': "bob",
            }
        )
    
class LinkInline(admin.TabularInline):
    "We want the links to be managed as part of a set as well"    
    model = Link
    extra = 1

class SetAdmin(admin.ModelAdmin):
    inlines = [LinkInline]
    list_display = ['title', 'number_of_links']
    
admin.site.register(Link, LinkAdmin)
admin.site.register(Set, SetAdmin)