from django.urls import path
from .views import TeamCreateView, TeamMemberRequestVIew, TeamDetailView


urlpatterns = [
    path('create/', TeamCreateView.as_view(), name='team-crete'),
    path('<int:id>/request/', TeamMemberRequestVIew.as_view(), name='team-member-request'),
    path('<int:id>/detail', TeamDetailView.as_view(), name='team-detail')
]