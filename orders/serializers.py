from django.contrib.auth.models import User
from rest_framework_json_api import serializers
from rest_framework_recursive.fields import RecursiveField
from .models import Restaurant, DishCategory, Dish, Order, OrderItem, STATUS_CHOICES


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'name', 'price')

class DishCategorySerializer(serializers.ModelSerializer):
    dishes = DishSerializer(many=True)
    subcategories = RecursiveField(allow_null=True, many=True)

    class Meta:
        model = DishCategory
        fields = ('name', 'dishes', 'subcategories')

class OrderItemSerializer(serializers.ModelSerializer):
    dish = serializers.PrimaryKeyRelatedField(queryset=Dish.objects.all())
    class Meta:
        model = OrderItem
        fields = ('dish', 'count')

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    restaurant = serializers.PrimaryKeyRelatedField(queryset=Restaurant.objects.all())
    operator = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Order
        fields = ('restaurant', 'items', 'operator')

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        price = 0
        for item in items_data:
            price += item['dish'].price * item['count']
        validated_data['price'] = price
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order
