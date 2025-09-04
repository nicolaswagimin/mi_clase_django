from django import forms
from .models import Post, Comentario


class PostForm(forms.ModelForm):
    """Formulario para crear y editar posts"""
    
    class Meta:
        model = Post
        fields = ['titulo', 'slug', 'contenido', 'resumen', 'categoria', 'estado', 'imagen_destacada']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título del post'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'url-del-post'
            }),
            'contenido': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
                'placeholder': 'Contenido del post...'
            }),
            'resumen': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Resumen breve del post...'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-control'
            }),
            'estado': forms.Select(attrs={
                'class': 'form-control'
            }),
            'imagen_destacada': forms.FileInput(attrs={
                'class': 'form-control'
            })
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Hacer que el campo slug sea opcional
        self.fields['slug'].required = False
        self.fields['resumen'].required = False


class ComentarioForm(forms.ModelForm):
    """Formulario para comentarios"""
    
    class Meta:
        model = Comentario
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Escribe tu comentario aquí...'
            })
        }
