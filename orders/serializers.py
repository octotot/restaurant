# from rest_framework_json_api import serializers
from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from .models import DishCategory, Dish

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'name', 'price')

# class RecursiveField(serializers.Serializer):
#     def to_representation(self, value):
#         serializer = self.parent.parent.__class__(value, context=self.context)
#         return serializer.data

class DishCategorySerializer(serializers.ModelSerializer):
    dishes = DishSerializer(many=True)
    # subcategories = RecursiveField(many=True)
    subcategories =  RecursiveField(required=False, allow_null=True, many=True)    

    class Meta:
        model = DishCategory
        fields = ('id', 'name', 'dishes', 'subcategories')
