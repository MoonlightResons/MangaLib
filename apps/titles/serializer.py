from rest_framework import serializers
from .models import Manga, Genres, Tags, Format


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ('genre_name',)


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('tag_name',)


class FormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Format
        fields = ('format_name',)


class MangaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = "__all__"


class MangaDetailsSeralizer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    tags = TagsSerializer(many=True)
    release_format = FormatSerializer(many=True)

    class Meta:
        model = Manga
        fields = "__all__"
