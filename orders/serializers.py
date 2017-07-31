from rest_framework_json_api import serializers
from rest_framework_recursive.fields import RecursiveField
from .models import DishCategory, Dish

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'name', 'price')

class DishCategorySerializer(serializers.ModelSerializer):
    dishes = DishSerializer(many=True)
    subcategories = RecursiveField(allow_null=True, many=True)

    class Meta:
        model = DishCategory
        fields = ('id', 'name', 'dishes', 'subcategories')
