"""
URL configuration for student_attendance project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts.views import *
from students.views import *
from attendance.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("student-signin",SignIn,basename="student-signin")
router.register("admin-signup",AdminSignUp,basename="admin-signup")
router.register("student-login",StudentLoginView,basename="student-login")
router.register('admin-login',AdminLoginView,basename="admin-login")

router.register('student',StudentView,basename="student")
router.register('attendence',AttendenceView,basename="attendence")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('percentage/<int:pk>/',PercentageView.as_view())
]+ router.urls
