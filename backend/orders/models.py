from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from items.models import *


class OrderTotal(models.Model):
    related_user = models.ForeignKey(User, verbose_name='Користувач', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, verbose_name='Телефон', default=0)
    order_number = models.IntegerField(verbose_name='Код')

    items = models.JSONField(verbose_name='Товари', default=None)
    order_sum = models.FloatField(verbose_name='Сума', default=None)
    payment_type = models.CharField(max_length=50, verbose_name='Тип оплати', default='Готівка')
    promocode = models.CharField(max_length=50, verbose_name='Промокод', blank=True, null=True)
    status = models.CharField(verbose_name='Статус', default='В обробці')

    region = models.CharField(verbose_name='Область', default=None)
    location = models.CharField(verbose_name='Населений пункт', default=None)
    warehouse = models.IntegerField(verbose_name='Склад', default=None)

    order_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата замовлення')

    def __str__(self):
        return self.related_user.username

    class Meta:
        db_table = 'order_total'
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"
        ordering = ['related_user']


class OrderCart(models.Model):
    related_user = models.ForeignKey(User, verbose_name='Користувач', on_delete=models.CASCADE)
    related_item = models.ForeignKey(Items, verbose_name='Товар', on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='Код замовлення')
    soft_body = models.ForeignKey(ItemSoftBody, verbose_name='Оздоблення', on_delete=models.SET_NULL, null=True, blank=True)
    hard_body = models.ForeignKey(ItemHardBody, verbose_name='Корпус', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.related_user.username

    class Meta:
        db_table = 'order_cart'
        verbose_name = "Корзина"
        verbose_name_plural = "Корзини"
        ordering = ['related_user']
