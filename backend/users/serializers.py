from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import *


class UserSerializer(serializers.ModelSerializer):
    # визначаємо поля, задаємо параметр не-відображення пароля при GET
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password']

        # в поля username є вбудована unique валідація, в email - немає
        # в поля email є вбудована email валідація
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True},
            'password': {'write_only': True},
            'username': {'required': False},
        }

    # якщо settings.AUTH_PASSWORD_VALIDATORS не перевіряє
    def validate_password(self, value):
        try:
            validate_password(value)
        except serializers.ValidationError as e:
            raise serializers.ValidationError(e.messages)
        return value

    # перевантаження методу create, повернення інфо при GET
    def create(self, validated_data):
        email = validated_data.get('email')

        # Якщо не вказано username: username = email
        if validated_data.get('username') is None:
            validated_data['username'] = validated_data.get('email')
        # інфо по юзерам доступне в pg:auth_user

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Користувач з таким email вже існує!")

        user = User.objects.create_user(**validated_data)
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    При реєстрації поле username є необов'язковим. Якщо воно відсутнє username = email.

    Цей клас відповідає за логін і видачу токена сесії. Він перевіряє чи введено email чи username,
    перевіряє наявність такого користувача і видає JWT токен.

    Клас наслідує TokenObtainPairSerializer та перевантажує метод validate

    :return access, refresh
    """

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        try:
            user = User.objects.get(username=username)
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError("291")
        except User.DoesNotExist:
            raise serializers.ValidationError("290")

        return super().validate(attrs)


class UserFavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFavorites
        fields = ['related_user', 'related_item']
        read_only_fields = ('related_user',)
        order_by = ['related_item']


class UserInfoSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='related_user.email', read_only=True)
    first_name = serializers.CharField(source='related_user.first_name', read_only=True)
    last_name = serializers.CharField(source='related_user.last_name', read_only=True)

    class Meta:
        model = UserBio
        fields = ['email',
                  'first_name',
                  'last_name',
                  'phone',
                  'birth_date',
                  ]
