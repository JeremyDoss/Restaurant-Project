from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json
import logging


from .models import *

class Counter:
    count = 0

    def increment_and_return(self):
    	self.count += 1
    	return self.count

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    def double(self):
        self.count *= 2

def get_employee_from_uid(uid):
	emp = Employee.objects.get(pk=uid)
	return emp

def logout(request):
	if ("logged_in" in request.COOKIES):
		response = redirect('/')
		response.delete_cookie('logged_in')
		return response
	return redirect('/')

def logout_redirect(request, redir):
	if ("logged_in" in request.COOKIES):
		response = redirect('/' + redir)
		response.delete_cookie('logged_in')
		return response
	return redirect('/' + redir)

# this view is called at the base URL (front page)
def index(request):
	all_menu_items = MenuItem.objects.all()
	categories = Category.objects.all()
	context = {'all_menu_items': all_menu_items, 'categories': categories, 'counter': Counter()}
	return render(request, 'index.html', context)


# this is the kitchen index where the kitchen staff can view kitchen stuff
def kitchen_index(request):
	# if the kitchen is not logged in, we need to redirect them to the login index
	# this is a terrible idea for a regular website, completely insecure
	if ("logged_in" not in request.COOKIES): 
		return redirect('/kitchen/login/')

	user = get_employee_from_uid(request.COOKIES['uid'])
	if user.is_manager or len(user.cook_set.all()) > 0:
		# get incoming (unclaimed) orders
		unclaimed_orders = Order.objects.filter(cook__isnull=True, status="OP")
		
		if user.is_manager:
			associated_orders = Order.objects.filter(status="OP", cook__isnull=False)
		else:
			associated_orders = Order.objects.filter(cook__employee=user)
		context = {'unclaimed_orders': unclaimed_orders, 'associated_orders': associated_orders, 'user': user}
		#return HttpResponse("YO MANAGER OR COOK")
		return render(request, 'kitchen.html', context)

	else:
		return HttpResponse('Access denied for user "%s"' % (user.name))

def kitchen_login(request):
	# if we're already logged in, there's no reason to be here
	if ("logged_in" in request.COOKIES):
		return redirect('/kitchen/')

	# check if we're coming here via the form
	if (request.method == 'POST'):
		try:
			# the passkey form will POST to this same URL, so we need to check if that's set
			# and query the database for the user whose passkey matches, if any
			user = Employee.objects.get(passkey=request.POST['passkey'])
			response = redirect('/kitchen/')
			response.set_cookie('logged_in', 'yes')
			response.set_cookie('uid', user.id)
			return response
		except Employee.DoesNotExist:
			user = None
			# user does not exist, handle that
			return redirect('/kitchen/login/')

	# we need to render the login template
	#return HttpResponse("Display login form")
	context = {}
	return render(request, 'kitchen_login.html', context)

# this is the waiter index where a waiter can view their tables
def waiter_index(request):
	# if the waiter is not logged in, we need to redirect them to the login index
	# this is a terrible idea for a regular website, completely insecure
	if ("logged_in" not in request.COOKIES): 
		return redirect('/waiter/login/')

	# todo: make this render to a template, provide logout links
	#return HttpResponse("logged in as %s" % Employee.objects.get(pk=request.COOKIES['uid']))
	user = get_employee_from_uid(request.COOKIES['uid'])
	if user.is_manager:
		tables = Table.objects.all()
	else:
		try:
			waiter = Waiter.objects.get(employee=user)
			tables = waiter.tables.all()
		except Waiter.DoesNotExist:
			return HttpResponse("Access denied.")
		except AttributeError:
			return HttpResponse("You have no tables.")
	context = {'tables': tables, 'user': user}
	return render(request, 'waiter.html', context)

def waiter_login(request):
	# if we're already logged in, there's no reason to be here
	if ("logged_in" in request.COOKIES):
		return redirect('/waiter/')

	# check if we're coming here via the form
	if (request.method == 'POST'):
		try:
			# the passkey form will POST to this same URL, so we need to check if that's set
			# and query the database for the user whose passkey matches, if any
			user = Employee.objects.get(passkey=request.POST['passkey'])
			response = redirect('/waiter')
			response.set_cookie('logged_in', 'yes')
			response.set_cookie('uid', user.id)
			return response
		except Employee.DoesNotExist:
			user = None
			# user does not exist, handle that
			return redirect('/waiter/login/')

	# we need to render the login template
	#return HttpResponse("Display login form")
	context = {}
	return render(request, 'waiter_login.html', context)

def waiter_set_status(request):
	# POST['action'] contains the action
	logger = logging.getLogger(__name__)

	tables = []
	if 'tables[]' in request.POST:
		tables = request.POST.getlist('tables[]')

	action = request.POST['action']
	for table in tables:
		tbl = Table.objects.get(pk=table)
		if action == "open":
			tbl.status = "OP"
			tbl.prev_status = "OP"
		elif action == "occupied":
			tbl.prev_status = tbl.status
			tbl.status = "OC"
		elif action == "refill":
			if tbl.status == "NR":
				tbl.status = tbl.prev_status
		elif action == "assistance":
			if tbl.status == "NA":
				tbl.status = tbl.prev_status
		elif action == "comp":
			try:
				order = tbl.order_set.get()
				invoice = order.invoice_set.get()
				invoice.comped = True
				invoice.total = 0.00
				invoice.save()
			except (Order.DoesNotExist, Invoice.DoesNotExist):
				pass
		tbl.save()

	return HttpResponse(json.dumps({'status': 'OK', 'action_was': request.POST['action'], 'tables_were': tables}))

def kitchen_claim(request):
	if (request.method == 'POST'):
		user = get_employee_from_uid(request.COOKIES['uid'])
		try:
			cook = Cook.objects.get(employee=user)
			orderid = request.POST['orderID']
			order = Order.objects.get(pk=orderid)
			cook.current_orders.add(order)
			cook.save()
		except Cook.DoesNotExist:
			pass
	return HttpResponse("OK")

def kitchen_ready(request):
	if (request.method == 'POST'):
		user = get_employee_from_uid(request.COOKIES['uid'])
		try:
			cook = Cook.objects.get(employee=user)
			orderid = request.POST['orderID']
			order = Order.objects.get(pk=orderid)
			order.prev_status = order.status
			order.status = "RD"
			order.save()
		except Cook.DoesNotExist:
			pass
	return HttpResponse("OK")

def standby(request):
	return render(request, 'standby.html', {})

def kitchen_items(request):
	context = {}
	return render(request, 'items.html', context)
