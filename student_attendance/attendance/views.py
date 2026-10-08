from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from attendance.models import *
from attendance.serializer import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class AttendenceView(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = AttendenceSerializer
    queryset = Attendence.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["student","date","status"]

class PercentageView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,pk):
        student_id = self.kwargs.get("pk")
        attendence = Attendence.objects.filter(student_id=student_id)
        total = attendence.count()
        present = attendence.filter(status="Present").count()
        absent = attendence.filter(status="Absent").count()
        if total >0:
            percentage = (present/total)*100
        else:
            percentage = 0

        student = Student.objects.get(id=pk)
        return Response(data={
            "student_name" : student.name,
            "student_id":student.id,
            "total_classes":total,
            "present":present,
            "Absent":absent,
            "Percentage":percentage,
        })