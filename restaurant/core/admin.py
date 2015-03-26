from django.contrib import admin
from core.models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(MenuItem)
admin.site.register(Table)
admin.site.register(Order)