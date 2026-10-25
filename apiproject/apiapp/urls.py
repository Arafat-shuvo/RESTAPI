class BlogModel(model)

urlpatterns = [
    path('blogs/', BlogListCreateView.as_view(), name='blog_view'),
    path('blogs/<int:blog_id>/', BlogDetailView.as_view(), name='blog_details'),
    path('students/', RedirectView.as_view(url='/api/blogs/', permanent=False), name='student_api_redirect'),
]
