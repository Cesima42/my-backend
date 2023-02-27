from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogSerializer

@api_view(['GET'])
def get_blogs(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_blog(request):
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_blog(request, id):
    blog = get_object_or_404(Blog, pk=id)
    serializer = BlogSerializer(blog)
    return Response(serializer.data)

@api_view(['PUT'])
def update_blog(request, id):
    blog = get_object_or_404(Blog, pk=id)
    serializer = BlogSerializer(blog, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_blog(request, id):
    blog = get_object_or_404(Blog, pk=id)
    blog.delete()
    return Response(status=204)
