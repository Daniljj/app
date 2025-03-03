from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_file, name='upload_file'),
    path('filters/', views.apply_filters, name='apply_filters'),
    path('filters/list/', views.filters_list, name='filters_list'),
    path('filters/delete/<int:filter_id>/', views.delete_filter, name='delete_filter'),
    path('report/generate/', views.generate_report, name='generate_report'),
    path('report/download/', views.download_report, name='download_report'),
    path('tables/', views.tables_list, name='tables_list'),
    path('tables/<int:table_id>/delete/', views.delete_table, name='delete_table'),
    path('tables/<int:table_id>/append/', views.append_to_table, name='append_to_table'),
] 