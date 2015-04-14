from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import *

# Create your tests here.

class MenuTests(TestCase):
	# these are mainly just placeholder tests. actual tests of the models will need to be different
	# but as an example, this inserts a MenuItem and verifies that it got inserted properly by checking that
	# the name returns what we expect, and the category is what we expect when we query the database
	def setUp(self):
		cat = Category.objects.create(parent=None, name='Entrees')
		subcat = Category.objects.create(parent=cat, name="Soups")
		ing = Ingredient.objects.create(name="Potatoes")
		item = MenuItem(name='Soup', category=subcat, times_ordered=0, price=5.99, description="Test description",
			calories=100, sodium_mg=1000, fat_grams=150)
		item.save()
		item.ingredients.add(ing)
		item.save()
		table = Table()
		table.save()
		order = Order(table=table, status='OP')
		order.save()
		order.menu_items.add(item)
		order.save()

	def test_order_table_number(self):
		order = Order.objects.get(pk=1)
		self.assertEqual(order.table.id, 1)

	def test_order_number(self):
		ordr = Order.objects.get(pk=1)
		self.assertEqual(ordr.id, 1)

	def test_order_time(self):
		order = Order.objects.get(pk=1)
		self.assertEqual(order.time, "") #checks for empty string

	def test_order_status_open(self):
		order = Order.objects.get(pk=1)
		order.status='OP'
		self.assertEqual(order.status, "OP")

	def test_order_status_occupied(self):
		order = Order.objects.get(pk=1)
		order.status='OC'
		self.assertEqual(order.status, "OC")

	def test_order_status_need_refill(self):
		order = Order.objects.get(pk=1)
		order.status='NR'
		self.assertEqual(order.status, "NR")

	def test_order_status_need_assistance(self):
		order = Order.objects.get(pk=1)
		order.status='NA'
		self.assertEqual(order.status, "NA")

	def test_order_status_order_placed(self):
		order = Order.objects.get(pk=1)
		order.status='PL'
		self.assertEqual(order.status, "PL")

	def test_order_status_contains_items(self):
		order = Order.objects.get(pk=1)
		self.assertEqual(order.status, "OP")

	def test_waiter_has_orders(self):
		order = Order.objects.get(pk=1)
		self.assertEqual(waiter.name, "Jill" == hasOrder )

	def test_order_has_waiter(self):
		order = Order.objects.get(pk=1)
		self.assertEqual(order.waiter, "jill")

	def test_game_win(self):
		table = Objects.game.get(pk=1)
		self.assertEqual(table.win == 1)

	def test_game_false(self):
		table = Objects.game.get(pk=1)
		self.assertEqual(table.win == 0)

	def test_game_table_split_to_one(self):
		order = Order.objects.get(pk=1)
		self.assertEqual(table.check.1.hasItems == true)

	def test_game_table_split_to_two(self):
		order = Order.objects.get(pk=2)
		self.assertEqual(table.check.2.hasItems == true)

	def test_game_table_split_to_three(self):
		order = Order.objects.get(pk=3)
		self.assertEqual(table.check.3 == true)

	def test_game_table_split_to_four(self):
		order = Order.objects.get(pk=4)
		self.assertEqual(table.check.4.hasItems == true)

	def test_game_table_split_one_hasPaid(self):
		order = Order.objects.get(pk=1)
		self.assertEqual(table.check.1.hasPaid == true)

	def test_game_table_split_two_hasPaid(self):
		order = Order.objects.get(pk=1)
		self.assertEqual(table.check.2.hasPaid == true)

	def test_game_table_split_three_hasPaid(self):
		order = Order.objects.get(pk=1)
		self.assertEqual(table.check.3.hasPaid == true)

	def test_game_table_split_four_hasPaid(self):
		order = Order.objects.get(pk=1)
		self.assertEqual(table.check.4.hasPaid == true)
