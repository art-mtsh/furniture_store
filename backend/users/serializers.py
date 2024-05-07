from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


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
            raise serializers.ValidationError("Користувач з таким email вже існує!")

        # Create the user
        user = User.objects.create_user(**validated_data)
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Клас наслідує TokenObtainPairSerializer
    та перевантажує метод validate
    :return access, refresh
    """

    def validate(self, attrs):
        user_or_email = attrs.get("username")
        password = attrs.get("password")

        # перевіряємо чи використовується email як username

        # якщо поле в форматі email
        if '@' in user_or_email:
            # отримуємо username через email
            username = User.objects.get(email=user_or_email).username

        # якщо поле в форматі str
        else:
            # то це і є username
            username = user_or_email

        # автентифікуємо користувача
        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError("Користувача не знайдено!")

        # перевизначаємо атрибут username
        attrs['username'] = username
        # валідація, отримання JWT зі старшого класу
        data = super().validate(attrs)
        return data
