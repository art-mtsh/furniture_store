from django.contrib.auth.models import User
from rest_framework import serializers
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    # визначаємо поля, задаємо параметр не-відображення пароля при GET
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password']

        # в поля username є вбудована unique валідація, в email - немає
        # в поля email є вбудована email валідація
        extra_kwargs = {
            'password': {'write_only': True},
            'username': {'required': False},
            'email': {'required': True},
        }

    # перевантаження методу create, повернення інфо при GET
    def create(self, validated_data):
        email = validated_data.get('email')

        # Якщо не вказано username: username = email
        if validated_data.get('username') is None:
            validated_data['username'] = validated_data.get('email')
        # інфо по юзерам доступне в pg:auth_user

        # перевірка чи є такий email
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email already exists")

        # Create the user
        user = User.objects.create_user(**validated_data)
        return user
