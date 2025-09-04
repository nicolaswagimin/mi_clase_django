from django.contrib import admin
from django.utils.html import format_html
from .models import Post, Categoria, Comentario


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'fecha_creacion', 'post_count']
    list_filter = ['fecha_creacion']
    search_fields = ['nombre', 'descripcion']
    readonly_fields = ['fecha_creacion']
    
    def post_count(self, obj):
        return obj.post_set.count()
    post_count.short_description = 'Posts'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'categoria', 'estado', 'fecha_publicacion', 'comentario_count']
    list_filter = ['estado', 'categoria', 'fecha_creacion', 'fecha_publicacion']
    search_fields = ['titulo', 'contenido', 'resumen']
    prepopulated_fields = {'slug': ('titulo',)}
    readonly_fields = ['fecha_creacion', 'fecha_actualizacion']
    date_hierarchy = 'fecha_publicacion'
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('titulo', 'slug', 'autor', 'categoria')
        }),
        ('Contenido', {
            'fields': ('resumen', 'contenido', 'imagen_destacada')
        }),
        ('Configuración', {
            'fields': ('estado', 'fecha_publicacion')
        }),
        ('Metadatos', {
            'fields': ('fecha_creacion', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )
    
    def comentario_count(self, obj):
        return obj.comentarios.count()
    comentario_count.short_description = 'Comentarios'
    
    def save_model(self, request, obj, form, change):
        if not change:  # Si es un nuevo post
            obj.autor = request.user
        super().save_model(request, obj, form, change)


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['post', 'autor', 'fecha_creacion', 'activo', 'contenido_preview']
    list_filter = ['activo', 'fecha_creacion', 'post__categoria']
    search_fields = ['contenido', 'autor__username', 'post__titulo']
    readonly_fields = ['fecha_creacion']
    date_hierarchy = 'fecha_creacion'
    
    def contenido_preview(self, obj):
        return obj.contenido[:50] + '...' if len(obj.contenido) > 50 else obj.contenido
    contenido_preview.short_description = 'Contenido'
    
    actions = ['aprobar_comentarios', 'desaprobar_comentarios']
    
    def aprobar_comentarios(self, request, queryset):
        queryset.update(activo=True)
        self.message_user(request, f'{queryset.count()} comentarios aprobados.')
    aprobar_comentarios.short_description = 'Aprobar comentarios seleccionados'
    
    def desaprobar_comentarios(self, request, queryset):
        queryset.update(activo=False)
        self.message_user(request, f'{queryset.count()} comentarios desaprobados.')
    desaprobar_comentarios.short_description = 'Desaprobar comentarios seleccionados'


# Personalizar el título del admin
admin.site.site_header = "Administración del Blog"
admin.site.site_title = "Blog Admin"
admin.site.index_title = "Panel de Administración"