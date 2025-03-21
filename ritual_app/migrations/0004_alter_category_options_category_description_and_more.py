# Generated by Django 5.0.2 on 2025-03-15 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ritual_app', '0003_alter_galleryimage_options_alter_galleryimage_image_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['order'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='categories/', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='category',
            name='order',
            field=models.IntegerField(default=0, verbose_name='Порядок отображения'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='URL-идентификатор'),
        ),
    ]
