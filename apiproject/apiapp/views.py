from rest_framework import generics
from apiapp.serializers import BlogSerializer
from apiapp.models import BlogModel

class blogListAPI(generics.listAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer


class BlogGetAPI(generics.RetrieveAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer

class BlogIndividual(generics.RetrieveAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer

class CourseViewSet(Model)