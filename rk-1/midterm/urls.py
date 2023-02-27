from django.urls import path
from blogs.views import get_blogs, create_blog, get_blog, update_blog, delete_blog

urlpatterns = [
    path('api/blogs/', get_blogs, name='get_blogs'),
    path('api/blogs/', create_blog, name='create_blog'),
    path('api/blogs/<int:pk>/', get_blog, name='get_blog'),
    path('api/blogs/<int:pk>/', update_blog, name='update_blog'),
    path('api/blogs/<int:pk>/', delete_blog, name='delete_blog'),
]
