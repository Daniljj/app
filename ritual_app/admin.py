from django.contrib import admin
from .models import Category, Product, GalleryImage, CatalogImage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'order')
    list_editable = ('order',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    ordering = ('order',)

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)
    search_fields = ('title',)
    ordering = ('order',)

@admin.register(CatalogImage)
class CatalogImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)
    search_fields = ('title',)
    ordering = ('order',)

admin.site.register(Product)
