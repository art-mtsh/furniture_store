from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class RoomType(models.Model):
    """
    Тип кімнати:
    - офісні меблі
    - передпокій,
    - вітальня
    - спальня
    """

    title = models.CharField(max_length=150, db_index=True, verbose_name="Тип кімнати")

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'item_room_type'
        verbose_name = "Тип кімнати"
        verbose_name_plural = "Типи кімнат"
        ordering = ['title']

    # def get_absolute_url(self):
    #     return reverse('category', kwargs={'category_id': self.pk})


class ItemCategory(models.Model):
    """
    Категорія:
    - шафи
    - комоди
    - ліжка
    - столи
    """

    title = models.CharField(max_length=150, db_index=True, verbose_name="Категорія")
    room = models.ForeignKey(RoomType, verbose_name='Тип кімнати', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'item_category'
        verbose_name = "Категорія об'єкта"
        verbose_name_plural = "Категорії об'єкта"
        ordering = ['title']

    # def get_absolute_url(self):
    #     return reverse('category', kwargs={'category_id': self.pk})


class Manufacturer(models.Model):
    """
    Інформація про виробника.
    """

    title = models.CharField(max_length=150, db_index=True, verbose_name="Виробник")
    about = models.TextField(blank=True, verbose_name='Інформація')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'item_manufacturer'
        verbose_name = "Виробник"
        verbose_name_plural = "Виробники"
        ordering = ['title']


class ItemCollection(models.Model):
    """
    Інформація про колекцію.
    """

    title = models.CharField(max_length=150, db_index=True, verbose_name="Колекція")
    manufacturer = models.ForeignKey(Manufacturer, verbose_name='Виробник', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'item_collection'
        verbose_name = "Колекція"
        verbose_name_plural = "Колекції"
        ordering = ['title']


class Items(models.Model):
    """
    Інформація про об'єкт. Це кінцева картка товару
    """

    title = models.CharField(max_length=150, verbose_name='Назва товару', blank=False)
    article_code = models.IntegerField(verbose_name='Артикул', unique=True, blank=False)
    price = models.FloatField(verbose_name='Ціна, ГРН')
    description = models.TextField(blank=True, verbose_name='Опис товару')
    upholstery_material = models.CharField(max_length=150, verbose_name='Наповнення', blank=True, null=True)
    upholstery_capacity = models.IntegerField(verbose_name='Щільність набивки', blank=True, null=True)
    d_length = models.IntegerField(verbose_name='Загальна довжина', blank=True)
    d_width = models.IntegerField(verbose_name='Загальна ширина', blank=True)
    d_height = models.IntegerField(verbose_name='Загальна висота', blank=True)
    dimension_in_use_length = models.IntegerField(verbose_name='Корисна довжина', blank=True)
    dimension_in_use_width = models.IntegerField(verbose_name='Корисна ширина', blank=True)
    dimension_in_use_height = models.IntegerField(verbose_name='Загальна висота', blank=True)
    counter_claw = models.BooleanField(verbose_name='Захист від кігтів', default=False)
    avaliability = models.BooleanField(verbose_name='В наявності', default=True)
    in_stock = models.IntegerField(verbose_name='Кількість на складі', default=1)

    manufacturer = models.ForeignKey(Manufacturer, verbose_name='Виробник', on_delete=models.SET_NULL, null=True)  # виробник
    collection = models.ForeignKey(ItemCollection, verbose_name='Колекція', on_delete=models.SET_NULL, null=True)  # колекція
    item_category = models.ForeignKey(ItemCategory, verbose_name='Категорія', on_delete=models.SET_NULL, null=True)  # категорія
    room_type = models.ForeignKey(RoomType, verbose_name='Тип кімнати', on_delete=models.SET_NULL, null=True)  # тип кімнати

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Створено')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Відредаговано')
    is_published = models.BooleanField(default=True, verbose_name='Статус публікації')

    # def get_absolute_url(self):
    #     return reverse('view_news', kwargs={'news_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'item_items'
        verbose_name = "Товар"
        verbose_name_plural = "Товари"
        ordering = ['room_type', 'item_category', 'title']


class ItemColour(models.Model):
    """
    Інформація про колір товару.
    """

    title = models.CharField(max_length=150, db_index=True, verbose_name="Колекція")
    item = models.ForeignKey(Items, verbose_name='Товар', on_delete=models.SET_NULL, null=True)  # товар
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Семпл кольору', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'item_colours'
        verbose_name = "Колір"
        verbose_name_plural = "Кольори"
        ordering = ['title']


class ItemMaterial(models.Model):
    """
    Інформація про матеріал.
    """
    title = models.CharField(max_length=150, db_index=True, verbose_name="Матеріал")
    item = models.ForeignKey(Items, verbose_name='Товар', on_delete=models.SET_NULL, null=True)  # товар
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Семпл дерева', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'item_material'
        verbose_name = "Матеріал"
        verbose_name_plural = "Матеріали"
        ordering = ['title']


class ItemPhoto(models.Model):
    """
    Фотографії товару.
    """
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото товару", blank=True)
    item = models.ForeignKey(Items, verbose_name='Товар', on_delete=models.CASCADE, null=True)  # товар

    class Meta:
        db_table = 'item_photo'
        verbose_name = "Фото"
        verbose_name_plural = "Фото"
        ordering = ['item']


def validate_even(value):
    if value > 5 or value < 0:
        raise ValidationError(
            _("%(value)s not a valid rating!"), params={"value": value},
        )


class ItemReview(models.Model):
    """
    Відгуки про товар.
    """

    item = models.ForeignKey(Items, verbose_name='Товар', on_delete=models.PROTECT, null=True, related_name='get_news')
    first_name = models.CharField(max_length=150, verbose_name="Ім'я", blank=False)
    second_name = models.CharField(max_length=150, verbose_name='Прізвище', blank=False)
    review = models.TextField(blank=True, verbose_name='Відгук')
    rating = models.IntegerField(verbose_name='Оцінка товару', blank=False, validators=[validate_even])
    review_usefulness_counter = models.IntegerField(verbose_name='Корисність відгуку', default=0)

    def __str__(self):
        return self.item.title

    class Meta:
        db_table = 'item_review'
        verbose_name = "Відгук"
        verbose_name_plural = "Відгуки"
        ordering = ['item']
