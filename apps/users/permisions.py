from rest_framework import permissions


class AnnonPermission(permissions.BasePermission):
    message = 'You are arledy authenticated'

    def has_permission(self, request, view):
        return not request.user.is_authenticated


class UserProfileOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.mangauser == request.mangauser


class TeamOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.team_owner == request.user
