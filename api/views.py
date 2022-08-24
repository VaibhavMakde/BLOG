from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import PostSerializer
from blog import models


class PostViewSet(viewsets.ViewSet):
    # list all post
    def list(self, request):
        all_post = models.Post.objects.all()
        serializer = PostSerializer(all_post, many=True)
        return Response(serializer.data)

    # retire single post
    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            post = models.Post.objects.get(id=pk)
            serializer = PostSerializer(post)
            return Response(serializer.data)

    # create post
    def create(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'DATA CREATED !!!!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        id = pk
        post = models.Post.objects.get(pk=id)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        id = pk
        post = models.Post.objects.get(pk=id)
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'})
        return Response(serializer.errors)

    def destroy(self, request, pk):
        id = pk
        post = models.Post.objects.get(pk=id)
        post.delete()
        return Response({'msg': 'Data Deleted !!!!'})
