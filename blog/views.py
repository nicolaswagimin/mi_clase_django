from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Post, Categoria, Comentario
from .forms import PostForm, ComentarioForm


def post_list(request):
    """Vista para listar todos los posts publicados"""
    posts = Post.objects.filter(estado='publicado')
    
    # Búsqueda
    query = request.GET.get('q')
    if query:
        posts = posts.filter(
            Q(titulo__icontains=query) |
            Q(contenido__icontains=query) |
            Q(resumen__icontains=query)
        )
    
    # Filtro por categoría
    categoria_id = request.GET.get('categoria')
    if categoria_id:
        posts = posts.filter(categoria_id=categoria_id)
    
    # Paginación
    paginator = Paginator(posts, 6)  # 6 posts por página
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    
    # Obtener todas las categorías para el filtro
    categorias = Categoria.objects.all()
    
    context = {
        'posts': posts,
        'categorias': categorias,
        'query': query,
        'categoria_id': categoria_id,
    }
    return render(request, 'blog/post_list.html', context)


def post_detail(request, slug):
    """Vista para mostrar el detalle de un post"""
    post = get_object_or_404(Post, slug=slug, estado='publicado')
    comentarios = post.comentarios.filter(activo=True)
    
    # Formulario para comentarios
    if request.method == 'POST':
        comentario_form = ComentarioForm(request.POST)
        if comentario_form.is_valid():
            comentario = comentario_form.save(commit=False)
            comentario.post = post
            comentario.autor = request.user
            comentario.save()
            messages.success(request, 'Tu comentario ha sido agregado.')
            return redirect('blog:post_detail', slug=post.slug)
    else:
        comentario_form = ComentarioForm()
    
    # Posts relacionados (misma categoría)
    posts_relacionados = Post.objects.filter(
        categoria=post.categoria,
        estado='publicado'
    ).exclude(id=post.id)[:3]
    
    context = {
        'post': post,
        'comentarios': comentarios,
        'comentario_form': comentario_form,
        'posts_relacionados': posts_relacionados,
    }
    return render(request, 'blog/post_detail.html', context)


@login_required
def post_create(request):
    """Vista para crear un nuevo post"""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            messages.success(request, 'Tu post ha sido creado exitosamente.')
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = PostForm()
    
    context = {
        'form': form,
        'title': 'Crear Nuevo Post'
    }
    return render(request, 'blog/post_form.html', context)


@login_required
def post_edit(request, slug):
    """Vista para editar un post existente"""
    post = get_object_or_404(Post, slug=slug, autor=request.user)
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu post ha sido actualizado exitosamente.')
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    
    context = {
        'form': form,
        'title': 'Editar Post',
        'post': post
    }
    return render(request, 'blog/post_form.html', context)


def categoria_list(request):
    """Vista para mostrar todas las categorías"""
    categorias = Categoria.objects.all()
    context = {
        'categorias': categorias
    }
    return render(request, 'blog/categoria_list.html', context)


def categoria_detail(request, categoria_id):
    """Vista para mostrar posts de una categoría específica"""
    categoria = get_object_or_404(Categoria, id=categoria_id)
    posts = Post.objects.filter(categoria=categoria, estado='publicado')
    
    # Paginación
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    
    context = {
        'categoria': categoria,
        'posts': posts
    }
    return render(request, 'blog/categoria_detail.html', context)