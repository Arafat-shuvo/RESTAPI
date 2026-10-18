from django.shortcuts import get_object_or_404
from apiapp.models import BlogModel
from apiapp.serializers import BlogSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class BlogListCreateView(APIView):
    def get(self, request):
        blogs = BlogModel.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response({
            'success': True,
            'message': 'Blog data fetched successfully',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'message': 'Blog data saved successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({
            'success': False,
            'message': 'Blog data not saved',
            'data': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class BlogDetailView(APIView):
    def get(self, request, blog_id):
        blog = get_object_or_404(BlogModel, id=blog_id)
        serializer = BlogSerializer(blog)
        return Response({
            'success': True,
            'message': 'Blog data fetched successfully',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    def put(self, request, blog_id):
        blog = get_object_or_404(BlogModel, id=blog_id)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'message': 'Blog data updated successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)

        return Response({
            'success': False,
            'message': 'Blog data not updated',
            'data': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, blog_id):
        blog = get_object_or_404(BlogModel, id=blog_id)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
