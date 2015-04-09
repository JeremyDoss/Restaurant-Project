from django.test import TestCase
from .models import *

# Create your tests here.
class MenuTests(TestCase):
	# these are mainly just placeholder tests. actual tests of the models will need to be different
	# but as an example, this inserts a MenuItem and verifies that it got inserted properly by checking that
	# the name returns what we expect, and the category is what we expect when we query the database
	def setUp(self):
		cat = Category.objects.create(parent=None, name='Entrees')
		ing = Ingredient.objects.create(name="Potatoes")
		item = MenuItem(name='Soup', category=cat, times_ordered=0, price=5.99, description="Test description", 
			calories=100, sodium_mg=1000, fat_grams=150)
		item.save()
		item.ingredients.add(ing)
		item.save()

	def test_menu_item_name(self):
		item = MenuItem.objects.get(name='Soup')
		self.assertEqual(item.name, 'Soup')

	def test_menu_item_category(self):
		item = MenuItem.objects.get(name='Soup')
		self.assertEqual(item.category.name, 'Entrees')

	def test_top_category(self):
		item = MenuItem.objects.get(name='Soup')
		self.assertEqual(item.top_level_category().name, 'Entrees')

class ViewTests(TestCase):
	def setUp(self):
		cat = Category.objects.create(parent=None, name='Entrees')
		ing = Ingredient.objects.create(name="Potatoes")
		item = MenuItem(name='Soup', category=cat, times_ordered=0, price=5.99, description="Test description", 
			calories=100, sodium_mg=1000, fat_grams=150)
		item.save()
		item.ingredients.add(ing)
		item.save()

	# these will test the various views we've configured
	# for now, this verifies that the index gives us the HTTP OK status code 200
	def test_index(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
		# also make sure our view is actually executing, so we check a variable that is filled by it
		self.assertTrue('all_menu_items' in response.context)
		# and finally, make sure that all_menu_items actually has what it's supposed to have in it
		# which in this case is the single Soup item we added above
		self.assertEqual([item.name for item in response.context['all_menu_items']], ['Soup'])

