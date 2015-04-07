from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *

# this view is called at the base URL (front page)
def index(request):
	all_menu_items = MenuItem.objects.all()
	categories = Category.objects.all()
	context = {'all_menu_items': all_menu_items, 'categories': categories}
	return render(request, 'index.html', context)


# this is the waiter index where a waiter can view their tables
def waiter_index(request):
	# if the waiter is not logged in, we need to redirect them to the login index
	# this is a terrible idea for a regular website, completely insecure
	if ("logged_in" not in request.COOKIES): 
		return redirect('/waiter/login/')

	# todo: make this render to a template, provide logout links
	return HttpResponse("logged in as %s" % Employee.objects.get(pk=request.COOKIES['uid']))

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
	return render(request, 'login.html', context)