from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

# category
# this can be a main category or a sub category
class Category(models.Model):
	parent = models.ForeignKey('self', null=True, blank=True)
	name = models.CharField(max_length=100)

	class Meta:
		verbose_name_plural = "categories"
	def __str__(self):
		if self.parent:
			return "%s (parent: %s)" % (self.name, self.parent.name)
		return self.name

# ingredient
class Ingredient(models.Model):
	name = models.CharField(max_length=100)
	in_stock = models.BooleanField(default=True)

	# this is how you make it show its name in the admin interface
	def __str__(self):
		return self.name

# menu item
# Name, image, price, description, warnings, ingredients, category, nutritional info (image?)
class MenuItem(models.Model):
	name = models.CharField(max_length=200)
	times_ordered = models.IntegerField() # for measuring popularity
	price = models.DecimalField(decimal_places=2, max_digits=5)
	description = models.TextField()
	image = models.URLField(blank=True)
	ingredients = models.ManyToManyField(Ingredient) # this will be used to remove items with ingredients that are out of stock from listing
	category = models.ForeignKey(Category)
	nutritional_info = models.URLField(blank=True)
	calories = models.IntegerField()
	fat_grams = models.IntegerField()
	sodium_mg = models.IntegerField()
	is_vegetarian = models.BooleanField(default=False)
	in_stock = models.BooleanField(default=True)

	ALLERGY_TYPES = (
		("NONE", 'None'),
		("PEANUT", 'Peanuts'),
		("GLUTEN", 'Gluten'),
	)
	allergens = models.CharField(max_length=10, choices=ALLERGY_TYPES, default=ALLERGY_TYPES[0][0])

	# recursive function to find the top level category for this item
	def top_level_category(self, prev=None):
		if prev == None: 
			prev = self.category
		
		if self.category.parent == None:
			return self.category
		elif prev.parent == None:
			return prev
		else:
			return self.top_level_category(prev.parent)

	def __str__(self):
		return "%s (%s)" % (self.name, self.category.name)


# tables
class Table(models.Model):
	#table_number = models.AutoField()
	
	STATUS_TYPES = (
		("OP", "Open"),
		("OC", "Occupied"),
		("NR", "Need refill"),
		("NA", "Need assistance"),
		("PL", "Order placed"),
	)
	status = models.CharField(max_length=2, choices=STATUS_TYPES, default=STATUS_TYPES[0][0])
	prev_status = models.CharField(max_length=2, choices=STATUS_TYPES, default=STATUS_TYPES[0][0]) # so we can revert from e.g. "Need refill"

	def __str__(self):
		return "Table %i" % self.id



# orders
# Order number, table, list of menu items
class Order(models.Model):
	#order_number = models.AutoField() # auto increments 
	table = models.ForeignKey(Table)
	menu_items = models.ManyToManyField(MenuItem)
	date = models.DateTimeField(auto_now_add=True, default=timezone.now)
	STATUS_TYPES = (
		("OP", "Open"),
		("CL", "Closed"),
		("RD", "Ready to be served")
	)
	status = models.CharField(max_length=2, choices=STATUS_TYPES, default=STATUS_TYPES[0][0])

	def __str__(self):
		return "Order %i" % self.id


# feedback
class Feedback(models.Model):
	order = models.ForeignKey(Order)
	rating = models.IntegerField()
	message = models.TextField()

# invoice
class Invoice(models.Model):
	order = models.ForeignKey(Order)
	subtotal = models.DecimalField(decimal_places=2, max_digits=10)
	tax = models.DecimalField(decimal_places=2, max_digits=5)
	tip = models.DecimalField(decimal_places=2, max_digits=5)
	comped = models.BooleanField(default=False)
	total = models.DecimalField(decimal_places=2, max_digits=10)
	# I think we should only be concerned with the split in the interface
	# but for the sake of completeness, I'll add this
	split_ways = models.IntegerField()
	# the split is recorded in the Split model

class Split(models.Model):
	invoice = models.ForeignKey(Invoice)
	amount = models.DecimalField(decimal_places=2, max_digits=10)

class Employee(models.Model):
	name = models.CharField(max_length=512)
	is_manager = models.BooleanField(default=False)
	passkey = models.IntegerField()

	def __str__(self):
		if self.is_manager:
			return "%s (manager)" % self.name
		else: return self.name

# these could be implemented as boolean fields in the Employee class, but
# this way, if there are specific things we need to store for waiters or cooks
# this makes it easier
class Waiter(models.Model):
	employee = models.ForeignKey(Employee)
	tables = models.ManyToManyField(Table)

	def __str__(self):
		return self.employee.name

class Cook(models.Model):
	employee = models.ForeignKey(Employee)
	current_orders = models.ManyToManyField(Order, blank=True)

	def __str__(self):
		return self.employee.name

