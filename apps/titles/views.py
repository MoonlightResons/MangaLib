from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from .serializer import MangaCreateSerializer, MangaDetailsSeralizer
from .models import Manga
# from apps.users.permisions import
from django.shortcuts import get_object_or_404


class MangaCreateView(APIView):
    def post(self, request):
        serializer = MangaCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MangaDetailView(APIView):
    def get(self, request, id):
        manga = get_object_or_404(Manga, id=id)
        serializer = MangaDetailsSeralizer(manga)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, id):
        manga = Manga.objects.get(id=id)
        serializer = MangaDetailsSeralizer(manga, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        manga = Manga.objects.get(id=id)
        manga.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
