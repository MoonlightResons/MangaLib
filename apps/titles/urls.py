from django.urls import path
from .views import MangaCreateView, MangaDetailView

urlpatterns = [
    path('create/', MangaCreateView.as_view(), name='manga-create'),
    path('<int:id>/detail/', MangaDetailView.as_view(), name='manga-detail'),
]
