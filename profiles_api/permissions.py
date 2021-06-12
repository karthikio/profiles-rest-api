from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    # users can update only their own profile
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    # users can update only their own status
    def has_object_permission(self, request, view, obj):
        #checks the user is updating their own status
        if request.method.in permissions.SAFE_METHODS:
            return True

        #if the user_profile instance id == req.user.id ... that return true... and allows the user
        return obj.user_profile.id == request.user.id
