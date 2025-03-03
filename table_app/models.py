from django.db import models
from django.core.validators import FileExtensionValidator

class TableData(models.Model):
    sheet_name = models.CharField('Название листа', max_length=255)
    file = models.FileField(
        'Excel файл',
        upload_to='excel_files/',
        validators=[FileExtensionValidator(allowed_extensions=['xlsx', 'xls', 'csv', 'ods'])]
    )
    uploaded_at = models.DateTimeField('Дата загрузки', auto_now_add=True)
    data_json = models.JSONField('Данные в JSON', default=dict)

    class Meta:
        verbose_name = 'Данные таблицы'
        verbose_name_plural = 'Данные таблиц'
        ordering = ['-uploaded_at']

    def __str__(self):
        return f"{self.sheet_name} ({self.uploaded_at.strftime('%Y-%m-%d %H:%M')})"

class Filter(models.Model):
    INTERNAL_PURPOSE_CHOICES = [
        ('Ozon', 'Ozon'),
        ('ЯМ', 'ЯМ (Яндекс Маркет)'),
        ('WB', 'WB'),
        ('ПП', 'ПП (Прямые продажи)'),
        ('Другие направления', 'Другие направления'),
        ('(-) ЗК', '(-) ЗК (Затраты Компании)'),
        ('(-) ДБН', '(-) ДБН (Другие бизнес направления)'),
        ('(-) ЛТ', '(-) ЛТ (Личные Траты)'),
        ('(-) ВС', '(-) ВС (Вывод себе на счет)'),
        ('A', 'A (Amazon)'),
        ('ЛД', 'ЛД (личные доходы)'),
        ('(-) Ф', '(-) Ф'),
        ('(-) GB', '(-) GB'),
        ('Переводы', 'Переводы'),
    ]

    contractor = models.CharField('Контрагент', max_length=255, blank=True)
    payment_purpose = models.CharField('Банковское назначение платежа', max_length=255, blank=True)
    internal_purpose = models.CharField(
        'Внутреннее назначение',
        max_length=255,
        choices=INTERNAL_PURPOSE_CHOICES
    )
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Фильтр'
        verbose_name_plural = 'Фильтры'
        ordering = ['-created_at']

    def __str__(self):
        return f"Фильтр: {self.contractor} - {self.internal_purpose}" 