from django.urls import path
from apiapp.views import *

urlpatterns = [
    path('products/', product_view, name='product_view'),
    path('products/<int:p_id>/', product_details, name='product_details'),
]