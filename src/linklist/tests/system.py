from django.test import TestCase

from linklist.tests.common import Common
from linklist.models import Link
from linklist.lib import move_up, move_down

class System(Common):
    "Common system testing properties and methods"
    pass
    
class Links(System):
    "Check the intitial mocks were created"
    
    # sanity check that we really did add 4 links to the list
    def test_number_of_links(self):
        expected = 4        
        actual = len(self.links)
        self.assertEquals(expected,actual,'number of links should be %s, but instead is %s' % (expected,actual))

class PositioningLinks(System):
    "Testing the reordering of links"
    
    # can we move a link in the middle of the list up
    def test_ability_to_move_up(self):
        link = self.links[1]
        
        expected = 2
        actual = link.position
        self.assertEquals(expected,actual,'initial position for second link should be %s, but instead is %s' % (expected,actual))

        move_up(link)

        expected = 1
        actual = link.position
        self.assertEquals(expected,actual,'final position for second link should be %s, but instead is %s' % (expected,actual))
    
    # can we move a link in the middle of the list down
    def test_ability_to_move_down(self):
        link = self.links[1]

        expected = 2
        actual = link.position
        self.assertEquals(expected,actual,'initial position for second link should be %s, but instead is %s' % (expected,actual))

        move_down(link)

        expected = 3
        actual = link.position
        self.assertEquals(expected,actual,'final position for second link should be %s, but instead is %s' % (expected,actual))

    # the interface won't let you do this but better safe than sorry
    def test_that_first_item_cant_be_moved_up(self):
        link = self.links[0]

        expected = 1
        actual = link.position
        self.assertEquals(expected,actual,'initial position for second link should be %s, but instead is %s' % (expected,actual))

        move_up(link)

        expected = 1
        actual = link.position
        self.assertEquals(expected,actual,'final position for second link should be %s, but instead is %s' % (expected,actual))        
        
    # again the interface doesn't provide this option but lets check what happens anyway
    def test_that_last_item_cant_be_moved_down(self):
        link = self.links[3]

        expected = 4
        actual = link.position
        self.assertEquals(expected,actual,'initial position for second link should be %s, but instead is %s' % (expected,actual))

        move_down(link)

        expected = 4
        actual = link.position
        self.assertEquals(expected,actual,'final position for second link should be %s, but instead is %s' % (expected,actual))        

    # test that the first link added got assigned to position 1
    def test_first_link_gets_position_equal_to_one(self):
        link = self.links[0]
        expected = 1
        actual = link.position
        self.assertEquals(expected,actual,'position should be %s, but instead is %s' % (expected,actual))
    
    # test that the attempt to subvert the auto positioning of links failed
    def test_we_ignore_positions_passed_in(self):
        link = self.links[1]
        expected = 2 # it's the second link in the list
        actual = link.position
        self.assertEquals(expected,actual,'position should be %s, but instead is %s' % (expected,actual))