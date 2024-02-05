from django.db import models
from apps.teams.models import Translators_Team


class Tags(models.Model):
    tag_name = models.CharField(max_length=55)

    def __str__(self):
        return self.tag_name


class Genres(models.Model):
    genre_name = models.CharField(max_length=55)

    def __str__(self):
        return self.genre_name


class Format(models.Model):
    format_name = models.CharField(max_length=55)

    def __str__(self):
        return self.format_name


class Title_status(models.Model):
    t_status = models.CharField(max_length=55)

    def __str__(self):
        return self.t_status


class Translate_status(models.Model):
    trans_status = models.CharField(max_length=55)

    def __str__(self):
        return self.trans_status


class Age_content(models.Model):
    age_cont = models.CharField(max_length=55)

    def __str__(self):
        return self.age_cont


class Chapter_Permissions(models.Model):
    chapter_permissions = models.CharField(max_length=55)

    def __str__(self):
        return self.chapter_permissions


class Type(models.Model):
    manga_type = models.CharField(max_length=55)

    def __str__(self):
        return self.manga_type


class Manga(models.Model):
    image = models.ImageField(upload_to='manga_img')
    background = models.ImageField(upload_to='manga_img')
    original_name = models.CharField(max_length=255)
    russian_name = models.CharField(max_length=255)
    english_name = models.CharField(max_length=255)
    another_name = models.CharField(max_length=255)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    realise_year = models.IntegerField()
    author = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    genres = models.ManyToManyField(Genres)
    tags = models.ManyToManyField(Tags)
    release_format = models.ManyToManyField(Format)
    translators = models.ForeignKey(Translators_Team, on_delete=models.CASCADE, blank=True)
    title_status = models.ForeignKey(Title_status, on_delete=models.CASCADE)
    translate_status = models.ForeignKey(Translate_status, on_delete=models.CASCADE)
    age_content = models.ForeignKey(Age_content, on_delete=models.CASCADE)
    permissions_for_chapter = models.ForeignKey(Chapter_Permissions, on_delete=models.CASCADE)
    link_for_original = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.english_name


class Chapter(models.Model):
    manga_page = models.FileField(upload_to="chapters")
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
