from django.contrib import admin

from .models import Restaurant, DishCategory, Dish, Order, OrderItem

admin.site.register(DishCategory)
admin.site.register(Dish)
admin.site.register(Order)
admin.site.register(Restaurant)
# Register your models here.
