from django.shortcuts import render
from students.models import *
from students.serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet
from students.permission import *
# Create your views here.

class StudentView(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSchoolAndAdmin]
    serializer_class = StudentSerializer
    #queryset = Student.objects.all()

    def get_queryset(self):
        if self.request.user.role == "admin":
            return Student.objects.all()
        return Student.objects.filter(user = self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


