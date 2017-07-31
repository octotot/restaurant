from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Dish, DishCategory
from .serializers import DishSerializer, DishCategorySerializer

@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def menu_list(request):
    categories = DishCategory.objects.filter(parent=None)
    serializer = DishCategorySerializer(categories, many=True)
    return JsonResponse(serializer.data, safe=False)
