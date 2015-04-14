
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
            fat_grams= 350,
            is_vegetarian = True,
            allergens="GLUTEN"
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

    def test_menu_item_calories(self):
        item = MenuItem.objects.get(name="Pepperoni Pizza")
        self.assertEqual(item.calories, 850)

    def test_menu_item_sodium_mg(self):
        item = MenuItem.objects.get(name="Pepperoni Pizza")
        self.assertEqual(item.sodium_mg, 250)

    def test_menu_item_fat_grams(self):
        item = MenuItem.objects.get(name="Pepperoni Pizza")
        self.assertEqual(item.fat_grams, 350)

    def test_menu_item_times_ordered(self):
        item = MenuItem.objects.get(name="Pepperoni Pizza")
        self.assertEqual(item.times_ordered, 5)

    def test_menu_item_allergens(self):
        item = MenuItem.objects.get(name="Pepperoni Pizza")
        self.assertEqual(item.allergens, "GLUTEN")

    def test_menu_item_vegetarian(self):
        item = MenuItem.objects.get(name="Pepperoni Pizza")
        self.assertEqual(item.is_vegetarian, True)

    def test_menu_item_ingredients(self):
        item = MenuItem.objects.get(name="Pepperoni Pizza")
        lst = ["Pepperoni", "Tomato Sauce", "Mozzarella Cheese"]
        lst_ = [x.name for x in item.ingredients.all()]
        self.assertEqual(lst, lst_)
