from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

