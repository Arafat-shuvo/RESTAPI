from django.db import models

# Create your models here.

class CourseCatagory(models>model):
    category_name = models.CharField(max_length = 100, null =True)
    description = models.TextField(null = True)


    def __str__(self):
        return f'{self.category_name}'


class SubjectModel(models.Model):
    name = models.models.CharField( max_length=50)
    catagory = models.TextField(null=True)
    description = models.TextField(max_length=100)
    teacher_name = models.CharField(max_length=100, null=True)
    credit = models.PositiveBigIntegerField(null = True)

    def __str__(self):
        return f'{self.name}'

    




class BlogModel(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title











                                                                       