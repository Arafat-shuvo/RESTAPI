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
        return Response({
            'sucess': True,
            'message': 'Product data fetched successfully',
            'data': serializer.data
        })

    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'message': 'Product data saved successfully',
                'data': serializer.data
            })
        else:
            return Response({
                'success': False,
                'message': 'Product data not saved',
                'data': serializer.errors
            })