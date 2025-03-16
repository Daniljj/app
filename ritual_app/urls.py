from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('services/', views.services, name='services'),
    path('contacts/', views.contacts, name='contacts'),
]
