from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from sematext import log_engine


class ItemRoomType(models.Model):
    """
    Тип кімнати. Унікальні.
    """

    title = models.CharField(max_length=150, unique=True, verbose_name="Тип кімнати")

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'item_room_type'
        verbose_name = "Тип кімнати"
        verbose_name_plural = "Типи кімнат"
        ordering = ['title']


class ItemCategory(models.Model):
    """
    Категорія.
    """

    title = models.CharField(max_length=150, db_index=True, verbose_name="Категорія")
    room = models.ForeignKey(ItemRoomType, verbose_name='Тип кімнати', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'item_category'
        verbose_name = "Категорія об'єкта"
        verbose_name_plural = "Категорії об'єкта"
        ordering = ['title']


class ItemManufacturer(models.Model):
    """
    Виробник. Унікальні.
    """

    title = models.CharField(max_length=150, unique=True, verbose_name="Виробник")
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
    manufacturer = models.ForeignKey(ItemManufacturer, verbose_name='Виробник', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'item_collection'
        verbose_name = "Колекція"
        verbose_name_plural = "Колекції"
        ordering = ['title']


class Items(models.Model):
    """
    Інформація про об'єкт.
    """

    title = models.CharField(max_length=150, verbose_name='Назва', blank=False)
    price = models.FloatField(verbose_name='Ціна')
    article_code = models.IntegerField(verbose_name='Артикул', unique=True, blank=False)
    description = models.TextField(blank=True, verbose_name='Опис')
    colour = models.CharField(max_length=150, verbose_name='Колір', blank=True)
    avaliability = models.BooleanField(verbose_name='В наявності', default=True)
    in_stock = models.IntegerField(verbose_name='На складі', default=1)

    length = models.IntegerField(verbose_name='Довжина', blank=True)
    width = models.IntegerField(verbose_name='Висота', blank=True)
    height = models.IntegerField(verbose_name='Висота', blank=True)
    form = models.CharField(max_length=50, verbose_name='Форма')

    item_category = models.ForeignKey(ItemCategory, verbose_name='Категорія', on_delete=models.SET_NULL, null=True)  # категорія
    collection = models.ForeignKey(ItemCollection, verbose_name='Колекція', on_delete=models.SET_NULL, null=True)  # колекція

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Створено')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Відредаговано')
    is_published = models.BooleanField(default=True, verbose_name='Статус')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'item_items'
        verbose_name = "Товар"
        verbose_name_plural = "Товари"
        ordering = ['item_category', 'title']


class ItemMaterials(models.Model):
    """
    Усі матеріали.
    """

    material_type = models.CharField(max_length=50, verbose_name='Тип матеріалу', blank=False)
    manufacturer = models.CharField(max_length=100, verbose_name='Виробник матеріалу', blank=False)
    title = models.CharField(max_length=150, verbose_name='Назва матеріалу', blank=False)
    colour = models.CharField(max_length=50, verbose_name='Колір матеріалу', blank=False)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Семпл кольору', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'item_materials'
        verbose_name = "Матеріали"
        verbose_name_plural = "Матеріали"
        ordering = ['material_type', 'manufacturer', 'title']


class ItemHardBody(models.Model):
    """
    Матеріали корпусу.
    """
    related_item = models.ForeignKey(Items, verbose_name='Товар', on_delete=models.CASCADE)

    body_material = models.ForeignKey(ItemMaterials, verbose_name='Корпус', on_delete=models.SET_NULL, null=True, related_name='body_material')
    facade_material = models.ForeignKey(ItemMaterials, verbose_name='Фасад', on_delete=models.SET_NULL, null=True, related_name='facade_material')
    tabletop_material = models.ForeignKey(ItemMaterials, verbose_name='Стільниця', on_delete=models.SET_NULL, null=True, related_name='tabletop_material')

    # def __str__(self):
    #     return self.related_item.title

    class Meta:
        db_table = 'item_hard_body'
        verbose_name = "Корпус"
        verbose_name_plural = "Корпуси"
        ordering = ['related_item']


class ItemSoftBody(models.Model):
    """
    М'які матеріали.
    """
    related_item = models.ForeignKey(Items, verbose_name='Товар', on_delete=models.CASCADE)

    sleep_place = models.CharField(max_length=100, verbose_name='Спальне місце')
    sleep_size = models.CharField(max_length=100, verbose_name='Спальне місце ДхШ')
    springs_type = models.CharField(max_length=100, verbose_name='Пружини')
    linen_niche = models.BooleanField(verbose_name='Ніша д.білизни')
    mechanism = models.CharField(max_length=100, verbose_name='Механізм')
    filler = models.CharField(max_length=100, verbose_name='Наповнення')
    counter_claw = models.BooleanField(verbose_name='Антикіготь')
    armrests = models.CharField(max_length=100, verbose_name='Підлокітники')
    max_weight = models.IntegerField(verbose_name='Макс. навантаження')
    upholstery_material = models.ForeignKey(ItemMaterials, verbose_name='Оббивка', on_delete=models.SET_NULL, null=True)
    other = models.CharField(max_length=150, verbose_name='Інше')

    # def __str__(self):
    #     return self.related_item.title

    class Meta:
        db_table = 'item_soft_body'
        verbose_name = "М'який матеріал"
        verbose_name_plural = "М'які матеріали"
        ordering = ['related_item']


class ItemPhoto(models.Model):
    """
    Фотографії товару.
    """

    def item_photo_upload_path(instance, filename):
        category = instance.related_item.item_category
        item_id = instance.related_item_id
        return f"items/{category}/{item_id}/{filename}"

    related_item = models.ForeignKey(Items, verbose_name='Товар', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=item_photo_upload_path, verbose_name="Фото товару", blank=True)

    class Meta:
        db_table = 'item_photo'
        verbose_name = "Фото"
        verbose_name_plural = "Фото"
        ordering = ['related_item']


def validate_even(value):
    if value > 5 or value < 0:
        raise ValidationError(
            _("%(value)s not a valid rating!"), params={"value": value},
        )


class ItemReview(models.Model):
    """
    Відгуки про товар.
    """
    related_item = models.ForeignKey(Items, verbose_name='Товар', on_delete=models.CASCADE)

    first_name = models.CharField(max_length=150, verbose_name="Ім'я", blank=False)
    second_name = models.CharField(max_length=150, verbose_name='Прізвище', blank=False)
    review = models.TextField(blank=True, verbose_name='Відгук')
    rating = models.IntegerField(verbose_name='Оцінка товару', blank=False, validators=[validate_even])
    review_usefulness_counter = models.IntegerField(verbose_name='Корисність відгуку', default=0)

    # def __str__(self):
    #     return self.related_item.title

    class Meta:
        db_table = 'item_review'
        verbose_name = "Відгук"
        verbose_name_plural = "Відгуки"
        ordering = ['related_item']
