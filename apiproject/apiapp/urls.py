from django.urls import path
from apiapp.views import student_details, student_view

urlpatterns = [
    path('students/', student_view, name='student_view'),
    path('students/<int:student_id>/', student_details, name='student_details'),
]
