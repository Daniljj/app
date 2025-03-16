from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название категории")
    slug = models.SlugField(unique=True, verbose_name="URL-идентификатор")
    description = models.TextField(blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to='categories/', blank=True, verbose_name="Изображение")
    order = models.IntegerField(default=0, verbose_name="Порядок отображения")

    class Meta:
        ordering = ['order']
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=255, blank=True)  # Заменили ImageField на CharField
    
    def __str__(self):
        return self.name

class GalleryImage(models.Model):
    title = models.CharField(max_length=200, blank=True, verbose_name="Название", help_text="При отсутствии названия будет сгенерировано автоматически")
    image = models.ImageField(upload_to='gallery/', verbose_name="Изображение")
    order = models.IntegerField(default=0, verbose_name="Порядок")

    class Meta:
        ordering = ['order']
        verbose_name = "Изображение галереи"
        verbose_name_plural = "Изображения галереи"

    def save(self, *args, **kwargs):
        if not self.title:
            # Сохраняем сгенерированное название в базу
            existing_count = GalleryImage.objects.count()
            self.title = f"Изображение {existing_count + 1}"
        super().save(*args, **kwargs)

    def __str__(self):
        if not self.title:
            # Генерируем название для существующих записей без названия
            return f"Изображение {self.order or self.id or 0}"
        return self.title

class CatalogImage(models.Model):
    title = models.CharField(max_length=200, blank=True, verbose_name="Название")
    image = models.ImageField(upload_to='catalog/', verbose_name="Изображение")
    order = models.IntegerField(default=0, verbose_name="Порядок")

    class Meta:
        ordering = ['order']
        verbose_name = "Изображение каталога"
        verbose_name_plural = "Изображения каталога"

    def save(self, *args, **kwargs):
        if not self.title:
            self.title = f"Каталог {self.order or 0 + 1}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
