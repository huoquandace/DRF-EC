from django.utils.translation import gettext_lazy as _
from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers
from users.models import UserData


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserData
        fields = ["id", "email", "name", "password"]

    def create(self, validated_data):
        user = UserData.objects.create(
            email=validated_data["email"], name=validated_data["name"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255, required=True)
    password = serializers.CharField(max_length=128, write_only=True, required=True)


class UpdateUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, required=False)
    email = serializers.EmailField(max_length=100)
    email_verified_at = serializers.CharField(max_length=100, required=False)
    is_admin = serializers.CharField(max_length=100)

    @swagger_serializer_method(serializer_or_field=UserSerializer)
    def update(self, instance, validated_data):
        instance.email = validated_data.get("email", instance.email)
        instance.email_verified_at = validated_data.get(
            "email_verified_at", instance.email_verified_at
        )
        instance.is_admin = validated_data.get("is_admin", instance.is_admin)
        instance.name = validated_data.get("name", instance.name)
        instance.save()

        return instance


class CreateUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, required=False)
    email = serializers.EmailField(max_length=100)
    email_verified_at = serializers.DateTimeField(required=False)
    is_admin = serializers.CharField(max_length=100, required=False)
    password = serializers.CharField(max_length=100)

    @swagger_serializer_method(serializer_or_field=UserSerializer)
    def create(self, validated_data):
        user = UserData.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
        )

        user.name = validated_data.get("name")
        user.email_verified_at = validated_data.get("email_verified_at")
        user.is_admin = validated_data.get("is_admin")
        user.save()

        return user
