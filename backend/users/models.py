from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from items.models import *


def validate_phone_number(value):
    if not value.isdigit():
        raise ValidationError("Phone number must contain only digits.")


class UserBio(models.Model):
    related_user = models.OneToOneField(User, verbose_name='Користувач', on_delete=models.CASCADE, null=True)
    phone = models.CharField(verbose_name='Телефон', max_length=20, validators=[validate_phone_number], null=True)
    birth_date = models.DateField(verbose_name='Дата народження', null=True)

    def __str__(self):
        return self.related_user.username

    class Meta:
        db_table = 'user_bio'
        verbose_name = "Деталі користувача"
        verbose_name_plural = "Деталі користувача"
        ordering = ['related_user']


class UserFavorites(models.Model):
    related_user = models.ForeignKey(User, verbose_name='Користувач', on_delete=models.CASCADE)
    related_item = models.ForeignKey(Items, verbose_name='Товар', on_delete=models.CASCADE)

    def __str__(self):
        return self.related_user.username

    class Meta:
        db_table = 'user_favorites'
        verbose_name = "Обране"
        verbose_name_plural = "Обрані"
        ordering = ['related_user']
        unique_together = ('related_user', 'related_item')
