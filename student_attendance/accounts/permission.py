from rest_framework.permissions import BasePermission

class IsSchoolAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff == True

class IsStudentAndAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ["student","admin"]