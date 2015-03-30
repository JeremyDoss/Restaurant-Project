from django.db import models

# Create your models here.

# category
# this can be a main category or a sub category
class Category(models.Model):
	parent = models.ForeignKey('self', null=True)
	name = models.CharField(max_length=100)

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
	ingredients = models.ManyToManyField(Ingredient) # this will be used to remove items with ingredients that are out of stock from listing
	category = models.ForeignKey(Category)
	nutritional_info = models.URLField()
	is_vegetarian = models.BooleanField(default=False)

	ALLERGY_TYPES = (
		("PEANUT", 'Peanuts'),
		("GLUTEN", 'Gluten'),
	)
	allergens = models.CharField(max_length=10, choices=ALLERGY_TYPES)


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
	status = models.CharField(max_length=2, choices=STATUS_TYPES)
	prev_status = models.CharField(max_length=2, choices=STATUS_TYPES) # so we can revert from e.g. "Need refill"

	def __str__(self):
		return "Table %i" % self.id



# orders
# Order number, table, list of menu items
class Order(models.Model):
	#order_number = models.AutoField() # auto increments 
	table = models.ForeignKey(Table)
	menu_items = models.ManyToManyField(MenuItem)
	date = models.DateTimeField(auto_now_add=True)
	STATUS_TYPES = (
		("OP", "Open"),
		("CL", "Closed"),
		("RD", "Ready to be served")
	)
	status = models.CharField(max_length=2, choices=STATUS_TYPES)

	def __str__(self):
		return "Order %i" % self.id


# feedback
class Feedback(models.Model):
	order = models.ForeignKey(Order)
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

# these could be implemented as boolean fields in the Employee class, but
# this way, if there are specific things we need to store for waiters or cooks
# this makes it easier
class Waiter(models.Model):
	employee = models.ForeignKey(Employee)
	tables = models.ManyToManyField(Table)

class Cook(models.Model):
	employee = models.ForeignKey(Employee)