from django.contrib import admin

from .models import Restaurant, DishCategory, Dish, Order, OrderItem

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
    ordering = ['name']

@admin.register(DishCategory)
class DishCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent']
    ordering = ['name']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'price', 'time', 'operator', 'restaurant', 'status']
    readonly_fields = ['__str__', 'list_items', 'price', 'time', 'operator', 'restaurant']

    def get_actions(self, request):
        actions = super(OrderAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'city']
    ordering = ['name']
