from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    is_active = models.BooleanField(verbose_name='Активна', default=True)

    class Meta:  # для отображения в админке имя таблицы
        verbose_name = 'Категория товаров'
        verbose_name_plural = 'Категории товаров'

    def __str__(self):
        return self.name


class ProductType(models.Model):
    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    is_active = models.BooleanField(verbose_name='Активна', default=True)

    class Meta:
        verbose_name = 'Тип материала товаров'
        verbose_name_plural = 'Тип материалов товаров'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='Категория товара')
    type = models.ForeignKey(ProductType, on_delete=models.ForeignKey, verbose_name='Материал')
    name = models.CharField(verbose_name='Название товара', max_length=128)
    image = models.ImageField(verbose_name='Расположение фото', upload_to='foto_product',
                              blank=True)  # upload_to папк куда загрузится фото при добавлении товара и указания фото
    # удалить кр. описание если не понадобится
    short_desc = models.CharField(verbose_name='краткое описание товара', max_length=60, blank=True)
    description = models.TextField(verbose_name='описание товара', blank=True)
    price = models.DecimalField(verbose_name='цена товара', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)
    is_active = models.BooleanField(verbose_name='Активна', default=True)

    class Meta:  # для отображения в админке имя таблицы
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f"{self.name} ({self.category.name})"
