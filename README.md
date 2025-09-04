# Mi Blog Django

Un blog completo desarrollado con Django que incluye sistema de posts, categorías, comentarios y panel de administración.

## 🚀 Características

- ✅ **Sistema de Posts**: Crear, editar y publicar posts
- ✅ **Categorías**: Organizar posts por temas
- ✅ **Comentarios**: Sistema de comentarios para usuarios
- ✅ **Búsqueda**: Buscar posts por título y contenido
- ✅ **Panel de Administración**: Gestión completa del contenido
- ✅ **Diseño Responsive**: Interfaz moderna con Bootstrap 5
- ✅ **Autenticación**: Sistema de usuarios integrado

## 🛠️ Tecnologías Utilizadas

- **Backend**: Django 4.2.24
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Base de Datos**: SQLite
- **Iconos**: Font Awesome
- **Imágenes**: Pillow

## 📋 Requisitos

- Python 3.9+
- Django 4.2.24
- Pillow

## 🚀 Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/tu-usuario/mi_clase_django.git
cd mi_clase_django
```

2. **Crear entorno virtual**
```bash
python3 -m venv venv
source venv/bin/activate  # En macOS/Linux
# o
venv\Scripts\activate     # En Windows
```

3. **Instalar dependencias**
```bash
pip install django Pillow
```

4. **Configurar base de datos**
```bash
python manage.py migrate
```

5. **Crear superusuario**
```bash
python manage.py createsuperuser
```

6. **Ejecutar servidor**
```bash
python manage.py runserver
```

## 🌐 Acceso

- **Blog**: http://127.0.0.1:8000/
- **Panel de Administración**: http://127.0.0.1:8000/admin/

## 📁 Estructura del Proyecto

```
mi_clase_django/
├── blog/                    # Aplicación principal
│   ├── models.py           # Modelos de datos
│   ├── views.py            # Vistas
│   ├── forms.py            # Formularios
│   ├── admin.py            # Panel de administración
│   ├── urls.py             # URLs de la app
│   └── templates/blog/     # Plantillas HTML
├── mi_clase_django/        # Configuración del proyecto
├── static/                 # Archivos estáticos
├── media/                  # Archivos multimedia
└── db.sqlite3             # Base de datos
```

## 🎯 Funcionalidades

### Para Usuarios
- Ver lista de posts
- Leer posts completos
- Buscar posts
- Filtrar por categorías
- Comentar en posts (requiere autenticación)

### Para Autores
- Crear nuevos posts
- Editar posts propios
- Gestionar comentarios

### Para Administradores
- Gestionar todos los posts
- Administrar categorías
- Moderar comentarios
- Acceso completo al panel de administración

## 👨‍💻 Autor

**Nicolas Wagimin Bravo**
- Email: nicolas.wagimin@campusucc.edu.co
- GitHub: [tu-usuario](https://github.com/tu-usuario)

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📞 Soporte

Si tienes alguna pregunta o problema, por favor abre un issue en GitHub o contacta al autor.

---

¡Gracias por usar Mi Blog Django! 🎉
