from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
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
        user_or_email = attrs.get("username")
        password = attrs.get("password")

        if '@' in user_or_email:
            username = User.objects.get(email=user_or_email).username
        else:
            username = user_or_email

        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError("Користувача не знайдено!")

        # перевизначаємо атрибут username, бо при логіні по email (якщо username != email) - ми не отримаємо токен
        attrs['username'] = username
        data = super().validate(attrs)
        return data
