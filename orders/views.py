from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Dish, DishCategory
from .serializers import DishSerializer, DishCategorySerializer

def menu_list(request):
    categories = DishCategory.objects.filter(parent=None)
    serializer = DishCategorySerializer(categories, many=True)
    return JsonResponse(serializer.data, safe=False)
