from django.test import TestCase
from todoitem.views import get_index
from django.core.urlresolvers import resolve

# Basic Test - addition
class SimpleTest(TestCase):
    def test_adding_something_simple(self):
        self.assertEqual( 1 + 2, 3 )
 
    def test_adding_something_isnt_equal(self):
        self.assertNotEqual( 1 + 2, 4 )
        
