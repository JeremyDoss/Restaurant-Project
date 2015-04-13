
from django.test import TestCase
from django.core.urlresolvers import reverse
from decimal import *

from .models import *

class MenuTests(TestCase):
    def setUp(self):
        menu_item=MenuItem(
            name = "Pepperoni Pizza",
            category = Category.objects.create(parent=Category.objects.create(parent=None, name="Entrees"), name="Pizzas"),
            times_ordered = 5,
            price = 11.99,
            description = "Tomato Sauce, Pepperoni, and Mozzarella Cheese",
            calories = 850,
            sodium_mg = 250,
            fat_grams= 350
        )
        ingredient = []
        ingredient.append(Ingredient.objects.create(name="Pepperoni"))
        ingredient.append(Ingredient.objects.create(name="Tomato Sauce"))
        ingredient.append(Ingredient.objects.create(name="Mozzarella Cheese"))
        menu_item.save()
        menu_item.ingredients.add(ingredient[0])
        menu_item.ingredients.add(ingredient[1])
        menu_item.ingredients.add(ingredient[2])
        menu_item.save()

    def test_menu_item_name(self):
        item = MenuItem.objects.get(name="Pepperoni Pizza")
        self.assertEqual(item.name, "Pepperoni Pizza")

    def test_menu_item_description(self):
        item = MenuItem.objects.get(name="Pepperoni Pizza")
        self.assertEqual(item.description, "Tomato Sauce, Pepperoni, and Mozzarella Cheese")

    def test_menu_item_price(self):
        item = MenuItem.objects.get(name="Pepperoni Pizza")
        self.assertEqual(item.price, Decimal("11.99"))

"""
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


class PostTests(TestCase):
	def setUp(self):
		# add a table
		table = Table()
		table.save()

		manager = Employee(name='Matt', is_manager=True, passkey=1234)
		manager.save()

		waiter_user = Employee(name='Jill', is_manager=False, passkey=101)
		waiter_user.save()
		waiter = Waiter(employee=waiter_user)
		waiter.save()
		waiter.tables.add(table)
		waiter.save()

		cook_user = Employee(name='Jack', is_manager=False, passkey=0)
		cook_user.save()
		cook = Cook(employee=cook_user)
		cook.save()

	def test_waiter_login(self):
		response = self.client.post('/waiter/login/', {'passkey': '101'})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], 'http://testserver/waiter/')
		self.assertEqual(self.client.cookies['logged_in'].value, 'yes')

	def test_cook_login(self):
		response = self.client.post('/kitchen/login/', {'passkey': '0'})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], 'http://testserver/kitchen/')
		self.assertEqual(self.client.cookies['logged_in'].value, 'yes')
"""
