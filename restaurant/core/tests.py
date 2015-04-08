from django.test import TestCase
from .models import *

# Create your tests here.
class MenuTests(TestCase):
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

class ViewTests(TestCase):
	# these will test the various views we've configured
	# for now, this verifies that the index gives us the HTTP OK status code 200
	def test_index(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)