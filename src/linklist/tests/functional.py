from django.test import TestCase
from django.test.client import Client

from linklist.tests.common import Common

class Functional(Common):
    "Common functional testing properties and methods"
    pass

class TemplateTags(Functional):
    "The app only reners it's content via a template tag so best test that"

    # check all the live links are output by the tag
    def test_live_links_render_in_tag(self):
        self.assert_render_contains('Home', "{% render_link_list \"footer\" %}")
        self.assert_render_contains('About', "{% render_link_list \"footer\" %}")
        self.assert_render_contains('External', "{% render_link_list \"footer\" %}")

    # check the non live link isn't present in the tag
    def test_not_live_links_dont_render_in_tag(self):
        self.assert_render_doesnt_contain('Contact', "{% render_link_list \"footer\" %}")

    # lets make the non-live link live and check it now appears
    def test_change_to_live_causes_link_to_render_in_tag(self):
        link = self.links[2]
        link.is_live = 1
        link.save()
        self.assert_render_contains('Contact', "{% render_link_list \"footer\" %}")

    # does the class name get added to the output   
    def test_html_class_attribute_outputs_value(self):
        self.assert_render_contains('external', "{% render_link_list \"footer\" %}")