from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from apiapp.models import *
from apiapp.serializers import *
from rest_framework.response import Response
from rest_framework import status

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

def product_detail_view(request, p_id):
    if request.method == 'GET':
        product_data = ProductModel.objects.get(id=p_id)
        serializer = ProductSerializer(product_data)
        return Response({
            'sucess': True,
            'message': 'Product data fetched successfully',
            'data': serializer.data
        })

@api_view(['GET', 'DELETE', 'PUT'])
def product_details(request, p_id):
    if request.method == 'GET':
        try:
            product_data = ProductModel.objects.get(id=p_id)
            serializer = ProductSerializer(product_data)
        except ProductModel.DoesNotExist:
            return Response({
                'success': False,
                'message': 'Product data not found',
                'data': {}
            })
        return Response({
            'success': True,
            'message': 'Product data fetched successfully',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        try:
            product_data = ProductModel.objects.get(id=p_id)
            product_data.delete()
            return Response({
                'success': True,
                'message': 'Product data deleted successfully',
                'data': {}
            }, status=status.HTTP_204_NO_CONTENT)
        except ProductModel.DoesNotExist:
            return Response({
                'success': False,
                'message': 'Product data not found',
                'data': {}
            }, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        try:
            product_data = ProductModel.objects.get(id=p_id)
        except ProductModel.DoesNotExist:
            return Response({
                'success': False,
                'message': 'Product data not found',
                'data': {}
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'message': 'Product data updated successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'success': False,
                'message': 'Product data not updated',
                'data': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)