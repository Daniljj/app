from django.shortcuts import render
from .models import Category, Product, GalleryImage, CatalogImage

def home(request):
    categories = Category.objects.all()
    gallery_images = GalleryImage.objects.all()
    catalog_images = CatalogImage.objects.all()
    return render(request, 'ritual_app/home.html', {
        'categories': categories,
        'gallery_images': gallery_images,
        'catalog_images': catalog_images
    })

def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=category)
    return render(request, 'ritual_app/category.html', {
        'category': category,
        'products': products
    })

def services(request):
    return render(request, 'ritual_app/services.html')

def contacts(request):
    return render(request, 'ritual_app/contacts.html')
