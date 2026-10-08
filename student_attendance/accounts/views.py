from django.shortcuts import render
from accounts.serializer import UserSerializer
from rest_framework.viewsets import ViewSet
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from accounts.models import *
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from accounts.permission import *
# Create your views here.

class SignIn(ViewSet):
    def create(self,request):
        dserializer = UserSerializer(data=request.data)
        if dserializer.is_valid():
            dserializer.save()
            return Response(data=dserializer.data,status=status.HTTP_201_CREATED)
        return Response(data=dserializer.errors,status=status.HTTP_400_BAD_REQUEST)

class AdminSignUp(ViewSet):
    def create(self,request):
        dserializer = UserSerializer(data=request.data)
        if dserializer.is_valid():
            user = dserializer.save()
            user.role = "admin"
            user.is_superuser = True
            user.is_staff = True
            user.save()
            return Response(data={
                "msg":"Admin is created succefully",
                "user_id":user.id,
                "user_name":user.username,
                "user_role":user.role
            },status=status.HTTP_201_CREATED)
        return Response(data=dserializer.errors,status=status.HTTP_401_UNAUTHORIZED)

class StudentLoginView(ViewSet):
    def create(self,request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username,password=password)
        if user and user.role == "student":
            token,created = Token.objects.get_or_create(user=user)
            return Response({"msg":"user login succesfull","token":token.key,"user_id":user.id,"username":user.username,"user_role":user.role,"created":created},
                            status=status.HTTP_202_ACCEPTED
            )
        return Response({"msg":"Invalid username or password.The user is not a student"},status=status.HTTP_401_UNAUTHORIZED)

class AdminLoginView(ViewSet):
    def create(self,request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username,password=password)
        if user and user.is_staff == True:
            token,created = Token.objects.get_or_create(user=user)
            return Response(data={
                "msg":"Admin login in",
                "token":token.key,
                "created":created,
                "user_name":user.username,
                "user_id":user.id,
                "user_role":user.role
            },status=status.HTTP_201_CREATED)
        return Response(data={"msg":"error on logged in,The user is not a admin"},status=status.HTTP_401_UNAUTHORIZED)

class DeleteAccount(ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def destroy(self,request,pk):
        user_id = self.kwargs.get("pk")
        user = CustomUser.objects.get(id=user_id)
        if request.user.role == "student" and user_id != request.user:
            return Response(data={"ou can delete only your own account"},status=status.HTTP_401_UNAUTHORIZED)

        user.delete()
        return Response(data={"msg":"The account deleted succesfully"},status=status.HTTP_202_ACCEPTED)
        
        