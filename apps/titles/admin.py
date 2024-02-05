from django.contrib import admin
from .models import (Manga, Title_status, Tags, Format, Genres,
                     Translate_status, Chapter_Permissions, Age_content,
                     Type, Chapter)


admin.site.register(Manga)
admin.site.register(Translate_status)
admin.site.register(Title_status)
admin.site.register(Tags)
admin.site.register(Format)
admin.site.register(Genres)
admin.site.register(Chapter_Permissions)
admin.site.register(Age_content)
admin.site.register(Type)
admin.site.register(Chapter)
