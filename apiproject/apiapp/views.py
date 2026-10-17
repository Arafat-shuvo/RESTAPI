from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from apiapp.models import *
from apiapp.serializers import *
from rest_framework.response import Response


@api_view(['GET'])
def product_view(request):
    if request.method == 'GET':
        product_data = ProductModel.objects.all()
        serializer = ProductSerializer(product_data, many=True)
        return Response(serializer.data)