from attendance.models import Attendence
from rest_framework import serializers

class AttendenceSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source="student.name",read_only=True)
    class Meta:
        model = Attendence
        fields = "__all__"
        read_only_fields = ["id","student_name"]