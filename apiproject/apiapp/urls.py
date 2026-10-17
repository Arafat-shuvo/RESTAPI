from django.urls import path
from apiapp.views import *

urlpatterns = [
    path('products/', product_view, name='product_view'),
]