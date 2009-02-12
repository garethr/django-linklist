from django.db import models

class Link(models.Model):
    """
    Links for link list
    
    Links represent nodes in a given one dimensional list of links.
    Originally designed for building a simple footer navigation list
    this could be extended for use in other places where a list of links
    is required.
    """
    title = models.CharField(max_length=64)
    is_live = models.BooleanField(default=True)
    position = models.IntegerField(default=0)
    url = models.URLField(verify_exists=False, max_length=255, 
        help_text='Must be a valid URL')
    html_class = models.CharField(max_length=100, blank=True, null=True,
        help_text="Specify a class attribute to be assigned to the list item.")
    link_set = models.ForeignKey('Set', verbose_name="Set")
        
    def __str__(self):
        "User friendly output when printing an object"
        return self.title
        
    def save(self, force_insert=False, force_update=False):
        "Overridden save method which deals with reordering"
        # check to see if we're dealing with a new link
        if not self.id:
            # if we are we need to make sure we put it in the right position
            try:
                # get the last link
                link_set = self.link_set
                last_link = Link.objects.filter(link_set=link_set).order_by("-position")[0]
                # then increment the position counter
                self.position = last_link.position+1
            # if this is the first link in the list their are no other links
            except IndexError:
                # so set the position to 1
                self.position = 1
        super(Link, self).save(force_insert, force_update)
   
class Set(models.Model):
    "A named grouping of links which can be displayed via a template tag"
    title = models.CharField(max_length=100, 
        help_text = "Used to display a list of links like so {% load render_link_list %} {% render_link_list \"{title}\" %}")

    def number_of_links(self):
        "Method for use in the admin to display number of related links"
        return Link.objects.filter(link_set=self).count()

    def __str__(self):
        "User friendly output when printing an object"
        return self.title