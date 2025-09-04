from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # URLs principales
    path('', views.post_list, name='post_list'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    
    # URLs para crear y editar posts
    path('crear/', views.post_create, name='post_create'),
    path('editar/<slug:slug>/', views.post_edit, name='post_edit'),
    
    # URLs para categorías
    path('categorias/', views.categoria_list, name='categoria_list'),
    path('categoria/<int:categoria_id>/', views.categoria_detail, name='categoria_detail'),
]
