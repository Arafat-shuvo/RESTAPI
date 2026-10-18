from django.urls import path
from apiapp.views import BlogDetailView, BlogListCreateView

urlpatterns = [
    path('blogs/', BlogListCreateView.as_view(), name='blog_view'),
    path('blogs/<int:blog_id>/', BlogDetailView.as_view(), name='blog_details'),
]
