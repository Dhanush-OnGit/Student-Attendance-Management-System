from rest_framework import serializers
from accounts.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id","username","password","email","phone","role"]
        read_only_fields = ["id","role"]
    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)