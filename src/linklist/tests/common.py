from django.test import TestCase
from django.template import Context, Template

from linklist.models import Set, Link

class Common(TestCase):
    "Common assertions for this test suite as well as mock objects for testing"
    
    # register tag libraries we want to test
    tag_libraries = ['render_link_list',]
    
    def setUp(self):        
        
        self.sets = []
        set1 = Set(title="footer")
        set1.save()
        
        self.links = []
        # a pretty normal link
        link1 = Link(title="Home",url="/",html_class="",link_set_id="1",is_live=True,position="")
        link1.save()
        # a link trying to bypass the position ordering by setting the position attribute
        link2 = Link(title="About",url="/about",html_class="",link_set_id="1",is_live=True,position="10")
        link2.save()
        # a non-live link
        link3 = Link(title="Contact",url="/contact",html_class="",link_set_id="1",is_live=False,position="")
        link3.save()
        # a link with an html_class attribute
        link4 = Link(title="External",url="http://google.com",html_class="external",link_set_id="1",is_live=True,position="")
        link4.save()

        self.links.append(link1)
        self.links.append(link2)
        self.links.append(link3)
        self.links.append(link4)
        
    # get rid of all the links
    def tearDown(self):
        Link.objects.all().delete()
        self.links=None
        
    # a handful of customer assertions
    def assert_contains(self, needle, haystack):
        return self.assert_(needle in haystack, "Content should contain `%s' but doesn't:\n%s" % (needle, haystack))

    def assert_doesnt_contain(self, needle, haystack):
        return self.assert_(needle not in haystack, "Content should not contain `%s' but does:\n%s" % (needle, haystack))
        
    def assert_equal(self, *args, **kwargs):
        return self.assertEqual(*args, **kwargs)

    def assert_not_equal(self, *args, **kwargs):
        return not self.assertEqual(*args, **kwargs)
        
    def assert_render(self, expected, template, **kwargs):
        self.assert_equal(expected, self.render(template, **kwargs))

    def assert_doesnt_render(self, expected, template, **kwargs):
        self.assert_not_equal(expected, self.render(template, **kwargs))

    def assert_render_contains(self, expected, template, **kwargs):
        self.assert_contains(expected, self.render(template, **kwargs))

    def assert_render_doesnt_contain(self, expected, template, **kwargs):
        self.assert_doesnt_contain(expected, self.render(template, **kwargs))

    def render(self, template, **kwargs):
        template = "".join(["{%% load %s %%}" % lib for lib in self.tag_libraries]) + template
        return Template(template).render(Context(kwargs)).strip()