from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Dish, DishCategory
from .serializers import DishSerializer, DishCategorySerializer

def index(request):
    return HttpResponse("Hello, world. You're at the orders index.")

def dishes_list(request):
    dishes = Dish.objects.all()
    serializer = DishSerializer(dishes, many=True)
    return JsonResponse(serializer.data, safe=False)

def categories_list(request):
    categories = DishCategory.objects.all()
    serializer = DishCategorySerializer(categories, many=True)
    return JsonResponse(serializer.data, safe=False)
