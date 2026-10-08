from django.db import models
from students.models import Student
# Create your models here.

class Attendence(models.Model):
    status_choice=[
        ("Present","Present"),
        ("Absent","Absent")
    ]
    student  = models.ForeignKey(Student,on_delete=models.CASCADE,related_name="attendence")
    date = models.DateField()
    status = models.CharField(max_length=30,choices=status_choice)
    #The same student cannot have two attendance records on the same date.
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["student","date"],name="unique_student_attendance")
        ]
    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.status}"
