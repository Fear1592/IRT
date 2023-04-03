from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название категории')
    image = models.ImageField(upload_to='category/', verbose_name='Изображение категории')

    class Meta:
        ordering = ['id']
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец поста')
    name = models.CharField(max_length=155, verbose_name='Название товара')
    choice_cat = models.CharField(max_length=155, verbose_name='Название подкатегорий',
                                  blank=True, null=True)
    specifications = models.TextField(max_length=555, verbose_name='Характеристики', blank=True, null=True)
    equipment = models.TextField(max_length=555, verbose_name='Комплектация', blank=True, null=True)
    # images = models.ManyToManyField(Images, blank=True,
    #                                 verbose_name='Все изображения товара',
    #                                 related_name="images")
    # videos = models.ManyToManyField(Videos, blank=True,
    #                                 verbose_name='Все видео товара',
    #                                 related_name="videos")
    category = models.ForeignKey(Category,
                                 verbose_name='Категория товара',
                                 on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False, verbose_name='Опбуликовано')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')
    price = models.PositiveIntegerField(verbose_name='Цена товара')

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return str(self.name)


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт', related_name='images')
    image = models.ImageField(upload_to='image/', verbose_name='Общие изображения товаров')

    class Meta:
        ordering = ['id']
        verbose_name = "Изображения товара"
        verbose_name_plural = "Изображения товаров"

    def __str__(self):
        return str(self.image)


class Videos(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт', related_name='videos')
    video = models.FileField(upload_to='video/', verbose_name='Общие видео товаров')

    class Meta:
        ordering = ['id']
        verbose_name = "Видео товара"
        verbose_name_plural = "Видео товаров"

    def __str__(self):
        return str(self.video)


class Choices(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт', related_name='choices')
    name = models.CharField(max_length=150, verbose_name='Имя типа товара цвет/вкус')
    in_stock = models.BooleanField(default=True, verbose_name='В наличии')
    count = models.PositiveIntegerField(default=0, verbose_name='Колличество товара')
    image = models.ImageField(upload_to='choices/', verbose_name='Изображение категории')

    class Meta:
        ordering = ['id']
        verbose_name = "Разновидность товара"
        verbose_name_plural = "Разновидности товаров"

    def __str__(self):
        return self.name
