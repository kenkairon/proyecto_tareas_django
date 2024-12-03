# proyecto_tareas_django
Educativo y de Aprendizaje Personal

---

## Tabla de Contenidos
- [Requisitos](#requisitos)
- [Configuración del Entorno](#configuración-del-entorno)
- [Activación del Entorno](#Activación-del-Entorno)
- [Configuración Inicial](#configuración-inicial)
- [Pasos del Proyecto](#pasos-del-proyecto)
  - [Configuración del Proyecto](#configuración-del-proyecto)
  - [Creación del Superusuario](#Creación-del-Superusuario)
  - [Creación de Vistas y Modelos](#creación-de-vistas-y-modelos)

---
## Requisitos

- Python 3.9 o superior
- Django 4.0 o superior

---
## Configuración del Entorno

1. Crear el entorno virtual:
   ```bash
   python -m venv entorno_virtual 

## Activación del Entorno

2. Activar el entorno virtual:
    ### Windows
    ```bash
    entorno_virtual\Scripts\activate

## Configuración Inicial
## Instalar Django y Guardar dependencias

3. Intalación Django
    ```bash
    pip install django

4. Instalamos la actualizacion de pip
    ```bash
    python.exe -m pip install --upgrade pip

## Guardar las dependencias
5. Instalación dependencias
    ```bash
   pip freeze > requirements.txt

## Pasos del Proyecto
6. Crear el Proyecto
    ```bash
    django-admin startproject proyecto

7. Ingresar al directorio del Proyecto
    ```bash
    cd proyecto

8. Creamos la Aplicación baseapp
    ```bash
    python manage.py startapp baseapp

## Configuración del Proyecto

9. Hacemos Migraciones para que cree las tablas por defecto que tiene django y creando el db.sqlite3
   ```bash 
   python manage.py migrate


10. Conectar el proyecto con la aplicación: Agregar 'baseapp.apps.BaseappConfig', en la lista INSTALLED_APPS dentro del archivo proyecto/settings.py

    ```bash
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'baseapp.apps.BaseappConfig',
    ]
11. En baseapp creamos la urls.py = baseapp/urls.py 
12. Configuramos la views que esta en baseapp/views.py
    ```bash
    from django.shortcuts import render
    from django.http import HttpResponse

    # Create your views here.
    def lista_pendientes(pedido):
        return HttpResponse("listas pendientes")

13. Volvemos baseapp/urls.py llamamos a la función listas_pendientes views. 
    ```bash
    from django.urls import path 
    from . import views

    urlpatterns = [path('',views.lista_pendientes, name="pendientes")]

14. Agregamos la ruta de baseapp.urls al proyecto/urls.py
    ```bash
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('',include('baseapp.urls')),]

15. Hacemos correr el Servidor = y nos dara como resultado lo que contenga la función de listas pendientes
    ```bash
    python manage.py runserver 

16. Generamos el modelo en baseapp/models.py
    ```bash
    from django.db import models
    from django.contrib.auth.models import User

    # Create your models here.
     
    class Tarea(models.Model):
        usuario = models.ForeignKey(User, on_delete=models.CASCADE,
                                    null=True,
                                    blank=True)
        titulo = models.CharField(max_length=200)
        descripcion = models.TextField( null=True,
                                    blank=True)
        completo = models.BooleanField(default=False)
        creado = models.DateTimeField(auto_now_add=True)
        
        def __str__(self):
            return self.titulo
        
        class Meta:
            ordering = ['completo']

17. Creamos la migracion para que nuestra tabla aparezca en la base de datos
    ```bash
    python manage.py makemigrations

18. este comando crea python manage.py makemigrations crea un archivo 0001_initial.py baseapp/migrations/0001_initial.py
    ```bash
    # Generated by Django 5.1.3 on 2024-12-01 04:42
    import django.db.models.deletion
    from django.conf import settings
    from django.db import migrations, models


    class Migration(migrations.Migration):

        initial = True

        dependencies = [
            migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ]

        operations = [
            migrations.CreateModel(
                name='Tarea',
                fields=[
                    ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                    ('titulo', models.CharField(max_length=200)),
                    ('descripcion', models.TextField(blank=True, null=True)),
                    ('completo', models.BooleanField(default=False)),
                    ('creado', models.DateTimeField(auto_now_add=True)),
                    ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ],
                options={
                    'ordering': ['completo'],
                },
            ),
        ]

19. Procedemos hacer la migración donde se veran los datos reflejado en db.sqlite3 y creara baseapp_tarea en la base de datos
    ```bash
    python manage.py migrate 

## Creación del Superusuario

20. Creamos el super usuario 
    ```bash
    python manage.py createsuperuser

21. Creamos permisos para ver las tablas baseapp/admin.py
    ```bash
    from django.contrib import admin
    from .models import Tarea
    # Register your models here.

    admin.site.register(Tarea)

22. Verificamos los permisos http://127.0.0.1:8000/admin para modo de aprendizaje vamos a poner estas credenciales 
    ```bash
    admin 
    admin@gmail.com
    admin1234

23. En la aplicación baseapp/views.py  ListView Este tipo de vista está diseñado específicamente para trabajar con listas de objetos, como datos de un modelo, y simplifica la tarea de renderizar datos en una plantilla.
    ```bash
    from django.views.generic import ListView
    from .models import Tarea

    class ListasPendientes(ListView):
        model = Tarea
        template_name ='tarea_list.html'
        context_object_name = 'tareas'

24. Verificamos  baseapp/urls.py
     ```bash
    from django.urls import path 
    from baseapp.views import ListasPendientes

    urlpatterns = [
        path('',ListasPendientes.as_view(), name="pendientes")
    ]

25. creamos la carpeta templates/baseapp/tarea_list.html
    ```bash
    <h1>Listas Pendientes</h1>

    <table>
        <tr>
            <th>Elementos</th>
        </tr>

        {% for tarea in tareas %}
        <tr>
            <td>{{tarea.titulo}}</td>
        </tr>
        {% empty %}
        <h3>No hay elementos en la lista</h3>
        {% endfor %}
    </table>

26. En la Configuración al proyecto/urls.py agregas el  path('',include('baseapp.urls')),
    ```bash
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('',include('baseapp.urls')),
    ]
27. Vamos a Reconfigurar la Vista baseapp/views.py para agregar la clase DetalleTarea
    ```bash
    from django.views.generic import ListView
    from django.views.generic import DetailView
    from .models import Tarea

    class ListasPendientes(ListView):
        model = Tarea
        template_name ='tarea_list.html'
        context_object_name = 'tareas'
    
    class DetalleTarea(DetailView):
        model = Tarea
        template_name ='baseapp/tarea.html'
        context_object_name = 'tarea'
   

28. Configuramos la urls.py de la aplicación baseapp/urls.py donde van a estar las rutas de la navegación en el navegador 
    http://127.0.0.1:8000/tarea/1

    ```bash
    from django.urls import path 
    from .views import ListasPendientes, DetalleTarea

    urlpatterns = [
        path('',ListasPendientes.as_view(), name="pendientes"),
        path('tarea/<int:pk>', DetalleTarea.as_view(), name="tarea"),

    ]
29. Configuras el templates/tarea.html, estoy enviando desde  baseapp/views.py el  context_object_name = 'tarea' para que se exprese en el templates
    ```bash
    <h1>Tarea: {{tarea}}</h1>

30. Configuramos la vista en baseapp/views.py y agregamos CrearTarea
    ```bash
    from django.views.generic import ListView
    from django.views.generic import DetailView
    from django.views.generic import CreateView
    from django.urls import reverse_lazy
    from .models import Tarea


    class ListasPendientes(ListView):
        model = Tarea
        template_name ='tarea_list.html'
        context_object_name = 'tareas'
    
    class DetalleTarea(DetailView):
        model = Tarea
        template_name ='baseapp/tarea.html'
        context_object_name = 'tarea'
        
    class CrearTarea(CreateView):
        model = Tarea
        fields = '__all__'
        success_url = reverse_lazy('tareas')

31. Configuramos la urls en baseapp/urls.py  http://127.0.0.1:8000/crear-tarea/ 
    ```bash
    from django.urls import path 
    from .views import ListasPendientes, DetalleTarea, CrearTarea

    urlpatterns = [
        path('',ListasPendientes.as_view(), name="tareas"),
        path('tarea/<int:pk>', DetalleTarea.as_view(), name="tarea"),
        path('crear-tarea/', CrearTarea.as_view(), name="crear-tarea"),
    ]
32. Agregamos en el templates/baseapp/tarea_form.html
    ```bash
    <h1>Formulario de Tareas</h1>
    <a href="{% url 'tareas'%}">Volver</a>
    <form method="POST" action="">
        {% csrf_token %}
        {{form.as_p}}
        <input type="submit" value="Enviar">
    </form>

33. baseapp/views.py Agregamos UpdateView y EditarTarea
    ```bash
    from django.views.generic import ListView
    from django.views.generic import DetailView
    from django.views.generic import CreateView, UpdateView
    from django.urls import reverse_lazy
    from .models import Tarea


    class ListasPendientes(ListView):
        model = Tarea
        template_name ='tarea_list.html'
        context_object_name = 'tareas'
    
    class DetalleTarea(DetailView):
        model = Tarea
        template_name ='baseapp/tarea.html'
        context_object_name = 'tarea'
        
    class CrearTarea(CreateView):
        model = Tarea
        fields = '__all__'
        success_url = reverse_lazy('tareas')
        
    class EditarTarea(UpdateView):
        model = Tarea
        fields = '__all__'
        success_url = reverse_lazy('tareas')

 34. Configurar baseapp/urls.py http://127.0.0.1:8000/editar-tarea/1
    ```bash
    from django.urls import path 
    from .views import ListasPendientes, DetalleTarea, CrearTarea, EditarTarea

    urlpatterns = [
        path('',ListasPendientes.as_view(), name="tareas"),
        path('tarea/<int:pk>', DetalleTarea.as_view(), name="tarea"),
        path('crear-tarea/', CrearTarea.as_view(), name="crear-tarea"),
        path('editar-tarea/<int:pk>', EditarTarea.as_view(), name="editar-tarea"),
]

35. templates\baseapp\tarea_list.html agregamos <td><a href="{% url 'editar-tarea' tarea.id %}">Editar</a></td>

    ```bash
    <h1>Listas Pendientes</h1>
    <a href="{% url 'crear-tarea' %}">Crear Nueva Tarea</a>
    <table>
        <tr>
            <th>Elementos</th>
            <th></th>
            <th></th>
        </tr>

        {% for tarea in tareas %}
        <tr>
            <td>{{tarea.titulo}}</td>
            <td><a href="{% url 'tarea' tarea.id %}">Ver</a></td>
            <td><a href="{% url 'editar-tarea' tarea.id %}">Editar</a></td>
        </tr>
        {% empty %}
        <h3>No hay elementos en la lista</h3>
        {% endfor %}
    </table>

36. baseapp/views.py se agrega DeleteView y se crea la clase Eliminar-Tarea

    ```bash
    from django.views.generic import ListView
    from django.views.generic import DetailView
    from django.views.generic import CreateView, UpdateView, DeleteView
    from django.urls import reverse_lazy
    from .models import Tarea


    class ListasPendientes(ListView):
        model = Tarea
        template_name ='tarea_list.html'
        context_object_name = 'tareas'
    
    class DetalleTarea(DetailView):
        model = Tarea
        template_name ='baseapp/tarea.html'
        context_object_name = 'tarea'
        
    class CrearTarea(CreateView):
        model = Tarea
        fields = '__all__'
        success_url = reverse_lazy('tareas')
        
    class EditarTarea(UpdateView):
        model = Tarea
        fields = '__all__'
        success_url = reverse_lazy('tareas')
        
    class EliminarTarea(DeleteView):
        model = Tarea
        template_name ='baseapp/tarea_confirm_delete.html'
        context_object_name = 'tarea'
        success_url = reverse_lazy('tareas')
    
37. Agrego la urls.py baseapp/urls.py  path('eliminar-tarea/<int:pk>', EliminarTarea.as_view(), name="eliminar-tarea"),
    http://127.0.0.1:8000/eliminar-tarea/1

    ```bash
    from django.urls import path 
    from .views import ListasPendientes, DetalleTarea, CrearTarea, EditarTarea, EliminarTarea

    urlpatterns = [
        path('',ListasPendientes.as_view(), name="tareas"),
        path('tarea/<int:pk>', DetalleTarea.as_view(), name="tarea"),
        path('crear-tarea/', CrearTarea.as_view(), name="crear-tarea"),
        path('editar-tarea/<int:pk>', EditarTarea.as_view(), name="editar-tarea"),
        path('eliminar-tarea/<int:pk>', EliminarTarea.as_view(), name="eliminar-tarea"),

    ]

38. en templates/baseapp/tarea_list.html agrego <td><a href="{% url 'eliminar-tarea' tarea.id %}">Eliminar</a></td>
    ```bash
    <h1>Listas Pendientes</h1>
    <a href="{% url 'crear-tarea' %}">Crear Nueva Tarea</a>
    <table>
        <tr>
            <th>Elementos</th>
            <th></th>
            <th></th>
            <th></th>

        </tr>

        {% for tarea in tareas %}
        <tr>
            <td>{{tarea.titulo}}</td>
            <td><a href="{% url 'tarea' tarea.id %}">Ver</a></td>
            <td><a href="{% url 'editar-tarea' tarea.id %}">Editar</a></td>
            <td><a href="{% url 'eliminar-tarea' tarea.id %}">Eliminar</a></td>

        </tr>
        {% empty %}
        <h3>No hay elementos en la lista</h3>
        {% endfor %}
    </table>

39. En templates/baseapp/tarea_confirm_delete.html
    ```bash
    <a href="{% url 'tareas' %}">Volver</a>

    <form method="POST">
        {% csrf_token %}
        <p>Vas a eliminar esta tarea:"{{tarea}}"</p>
        <input type="submit" value="Eliminar">
    </form>

40. templates/baseapp/tarea_list.html creando la lógica del logeo
    ```bash
    {% if request.user.is_authenticated %}
    <p>{{request.user}}</p>
    <a href="">Salir</a>
    {% else%}
    <a href="">Ingresar</a>
    {% endif %}
    <hr>

    <h1>Listas Pendientes</h1>
    <a href="{% url 'crear-tarea' %}">Crear Nueva Tarea</a>
    <table>
        <tr>
            <th>Elementos</th>
            <th></th>
            <th></th>
            <th></th>

        </tr>

        {% for tarea in tareas %}
        <tr>
            <td>{{tarea.titulo}}</td>
            <td><a href="{% url 'tarea' tarea.id %}">Ver</a></td>
            <td><a href="{% url 'editar-tarea' tarea.id %}">Editar</a></td>
            <td><a href="{% url 'eliminar-tarea' tarea.id %}">Eliminar</a></td>

        </tr>
        {% empty %}
        <h3>No hay elementos en la lista</h3>
        {% endfor %}
    </table>

41. Creamos la ruta en baseapp/urls.py y agregamos la ruta  path('login/', logueo.as_view(), name="login"),
    ```bash
    from django.urls import path 
    from .views import ListasPendientes, DetalleTarea, CrearTarea, EditarTarea, EliminarTarea, logueo

    urlpatterns = [
        path('',ListasPendientes.as_view(), name="tareas"),
        path('tarea/<int:pk>', DetalleTarea.as_view(), name="tarea"),
        path('login/', logueo.as_view(), name="login"),
        path('crear-tarea/', CrearTarea.as_view(), name="crear-tarea"),
        path('editar-tarea/<int:pk>', EditarTarea.as_view(), name="editar-tarea"),
        path('eliminar-tarea/<int:pk>', EliminarTarea.as_view(), name="eliminar-tarea"),

    ]
42. en las vistas baseapp/views.py agregamos  from django.contrib.auth.views import LoginView y creamos la Clase logueo
    ```bash
    from django.views.generic import ListView
    from django.views.generic import DetailView
    from django.views.generic import CreateView, UpdateView, DeleteView
    from django.contrib.auth.views import LoginView
    from django.urls import reverse_lazy
    from .models import Tarea

    class logueo(LoginView):
        template_name='baseapp/login.html'
        field= '__all__'
        redirect_authenticated_user = True
        
        def get_success_url(self):
            return reverse_lazy('tareas')

    class ListasPendientes(ListView):
        model = Tarea
        template_name ='tarea_list.html'
        context_object_name = 'tareas'
    
    class DetalleTarea(DetailView):
        model = Tarea
        template_name ='baseapp/tarea.html'
        context_object_name = 'tarea'
        
    class CrearTarea(CreateView):
        model = Tarea
        fields = '__all__'
        success_url = reverse_lazy('tareas')
        
    class EditarTarea(UpdateView):
        model = Tarea
        fields = '__all__'
        success_url = reverse_lazy('tareas')
        
    class EliminarTarea(DeleteView):
        model = Tarea
        template_name ='baseapp/tarea_confirm_delete.html'
        context_object_name = 'tarea'
        success_url = reverse_lazy('tareas')

43. Creamos en templates/baseapp/login.html
    ```bash
    <h1>ingresar</h1>
    <form method="POST">
        {% csrf_token %}
        {{form.as_p}}
        <input type="submit" value="Ingresar">
    </form>

44. Podemos configurar el logout desde la baseapp/urls.py Y Lo configuramos directamente y agregamos path('logout/', LogoutView.as_view(next_page="login"), name="logout" ),

    ```bash
    from django.urls import path 
    from .views import ListasPendientes, DetalleTarea, CrearTarea, EditarTarea, EliminarTarea, logueo
    from django.contrib.auth.views import LogoutView

    urlpatterns = [
        path('',ListasPendientes.as_view(), name="tareas"),
        path('tarea/<int:pk>', DetalleTarea.as_view(), name="tarea"),
        path('login/', logueo.as_view(), name="login"),
        path('logout/', LogoutView.as_view(next_page="login"), name="logout" ),
        path('crear-tarea/', CrearTarea.as_view(), name="crear-tarea"),
        path('editar-tarea/<int:pk>', EditarTarea.as_view(), name="editar-tarea"),
        path('eliminar-tarea/<int:pk>', EliminarTarea.as_view(), name="eliminar-tarea"),
    ]
45. Modificamos en templates/baseapp/tarea_list.html  el boton de Salir con el objetivo de que no tengamos ataques 
    ```bash
    {% if request.user.is_authenticated %}
    <p>{{request.user}}</p>
    <form method="post" action="{% url 'logout' %}">
        {% csrf_token %}
        <button type="submit">Salir</button>
    </form>
    {% else%}
    <a href="{% url 'login' %}">Ingresar</a>
    {% endif %}
    <hr>

    <h1>Listas Pendientes</h1>
    <a href="{% url 'crear-tarea' %}">Crear Nueva Tarea</a>
    <table>
        <tr>
            <th>Elementos</th>
            <th></th>
            <th></th>
            <th></th>

        </tr>

        {% for tarea in tareas %}
        <tr>
            <td>{{tarea.titulo}}</td>
            <td><a href="{% url 'tarea' tarea.id %}">Ver</a></td>
            <td><a href="{% url 'editar-tarea' tarea.id %}">Editar</a></td>
            <td><a href="{% url 'eliminar-tarea' tarea.id %}">Eliminar</a></td>

        </tr>
        {% empty %}
        <h3>No hay elementos en la lista</h3>
        {% endfor %}
    </table>

46. baseapp/views.py, agregamos from django.contrib.auth.mixins import LoginRequiredMixin, vamos agregando a las paginas que quiero restringir menos la de login con el objetivo de poder ingresar usuario y contraseña

    ```bash
    from django.views.generic import ListView
    from django.views.generic import DetailView
    from django.views.generic import CreateView, UpdateView, DeleteView
    from django.contrib.auth.views import LoginView
    from django.contrib.auth.mixins import LoginRequiredMixin
    from django.urls import reverse_lazy
    from .models import Tarea

    class logueo(LoginView):
        template_name='baseapp/login.html'
        field= '__all__'
        redirect_authenticated_user = True
        
        def get_success_url(self):
            return reverse_lazy('tareas')

    class ListasPendientes(LoginRequiredMixin, ListView):
        model = Tarea
        template_name ='tarea_list.html'
        context_object_name = 'tareas'
    
    class DetalleTarea(LoginRequiredMixin, DetailView):
        model = Tarea
        template_name ='baseapp/tarea.html'
        context_object_name = 'tarea'
        
    class CrearTarea(LoginRequiredMixin, CreateView):
        model = Tarea
        fields = '__all__'
        success_url = reverse_lazy('tareas')
        
    class EditarTarea(LoginRequiredMixin,UpdateView):
        model = Tarea
        fields = '__all__'
        success_url = reverse_lazy('tareas')
        
    class EliminarTarea(LoginRequiredMixin,DeleteView):
        model = Tarea
        template_name ='baseapp/tarea_confirm_delete.html'
        context_object_name = 'tarea'
        success_url = reverse_lazy('tareas')
    

47. En proyecto/settings.py agregamos LOGIN_URL = 'login'

    ```bash
        # Internationalization
        # https://docs.djangoproject.com/en/5.1/topics/i18n/

        LANGUAGE_CODE = 'en-us'

        TIME_ZONE = 'UTC'

        USE_I18N = True

        USE_TZ = True

        LOGIN_URL = 'login'

48. baseapp/views.py Este código que esta comentado, cada usuario va tener sus propias tareas 
    ```bash
    from django.views.generic import ListView
    from django.views.generic import DetailView
    from django.views.generic import CreateView, UpdateView, DeleteView
    from django.contrib.auth.views import LoginView
    from django.contrib.auth.mixins import LoginRequiredMixin
    from django.urls import reverse_lazy
    from .models import Tarea

    class logueo(LoginView):
        template_name='baseapp/login.html'
        field= '__all__'
        redirect_authenticated_user = True
        
        def get_success_url(self):
            return reverse_lazy('tareas')

    class ListasPendientes(LoginRequiredMixin, ListView):
        model = Tarea
        template_name ='tarea_list.html'
        context_object_name = 'tareas'
        
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['tareas'] = context['tareas'].filter(usuario=self.request.user) #usuario lo creamos en el modelo
            context['count'] = context['tareas'].filter(completo=False).count()

            return context
    
    class DetalleTarea(LoginRequiredMixin, DetailView):
        model = Tarea
        template_name ='baseapp/tarea.html'
        context_object_name = 'tarea'
        
    class CrearTarea(LoginRequiredMixin, CreateView):
        model = Tarea
        fields = ['titulo', 'descripcion', 'completo'] # para que no muestre todos los campos "usuario"
        success_url = reverse_lazy('tareas')
        
        # Para que las nuevas tareas se le asigne al usuario que este logeado
        def form_valid(self, form):
            form.instance.usuario = self.request.user
            return super(CrearTarea, self).form_valid(form)
        
    class EditarTarea(LoginRequiredMixin,UpdateView):
        model = Tarea
        fields = ['titulo', 'descripcion', 'completo'] # para que no muestre todos los campos "usuario"
        success_url = reverse_lazy('tareas')
        
    class EliminarTarea(LoginRequiredMixin,DeleteView):
        model = Tarea
        template_name ='baseapp/tarea_confirm_delete.html'
        context_object_name = 'tarea'
        success_url = reverse_lazy('tareas')

49. Ingresamos un link o a en templates/baseapp/login.html
    ```bash
    <h1>Ingresar</h1>
    <form method="POST">

        {% csrf_token %}
        {{form.as_p}}
        <input type="submit" value="Ingresar">
    </form>
    <!-- Agregamos un link de registro -->
    <p>No tienes una Cuenta? <a href="">Registrate</a></p>

50. Agregamos en templates/baseapp/registro.html
    ```bash
    <h1>Registrarse</h1>
    <form method="POST">

        {% csrf_token %}
        {{form.as_p}}
        <input type="submit" value="Ingresar">
    </form>
    <!-- Agregamos un link de registro -->
    <p>Ya tienes una Cuenta? <a href="{% url 'login' %}">Ingresa</a></p>

51. Vamos a la vista baseapp/views.py agregamos esta información  y la clase  PaginaRegistro
    from django.views.generic import CreateView, UpdateView, DeleteView, FormView
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib.auth import login

    ```bash
    from django.views.generic import ListView
    from django.views.generic import DetailView
    from django.views.generic import CreateView, UpdateView, DeleteView, FormView
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib.auth import login
    from django.contrib.auth.views import LoginView
    from django.contrib.auth.mixins import LoginRequiredMixin
    from django.urls import reverse_lazy
    from .models import Tarea

    class logueo(LoginView):
        template_name='baseapp/login.html'
        field= '__all__'
        redirect_authenticated_user = True
        
        def get_success_url(self):
            return reverse_lazy('tareas')

    class PaginaRegistro(FormView):
        template_name = 'baseapp/registro.html'
        form_class = UserCreationForm
        redirect_authenticated_user = True
        success_url = reverse_lazy('tareas')

    class ListasPendientes(LoginRequiredMixin, ListView):
        model = Tarea
        template_name ='tarea_list.html'
        context_object_name = 'tareas'
        
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['tareas'] = context['tareas'].filter(usuario=self.request.user) #usuario lo creamos en el modelo
            context['count'] = context['tareas'].filter(completo=False).count()

            return context
    
    class DetalleTarea(LoginRequiredMixin, DetailView):
        model = Tarea
        template_name ='baseapp/tarea.html'
        context_object_name = 'tarea'
        
    class CrearTarea(LoginRequiredMixin, CreateView):
        model = Tarea
        fields = ['titulo', 'descripcion', 'completo'] # para que no muestre todos los campos "usuario"
        success_url = reverse_lazy('tareas')
        
        # Para que las nuevas tareas se le asigne al usuario que este logeado
        def form_valid(self, form):
            form.instance.usuario = self.request.user
            return super(CrearTarea, self).form_valid(form)
        
    class EditarTarea(LoginRequiredMixin,UpdateView):
        model = Tarea
        fields = ['titulo', 'descripcion', 'completo'] # para que no muestre todos los campos "usuario"
        success_url = reverse_lazy('tareas')
        
    class EliminarTarea(LoginRequiredMixin,DeleteView):
        model = Tarea
        template_name ='baseapp/tarea_confirm_delete.html'
        context_object_name = 'tarea'
        success_url = reverse_lazy('tareas')

52. Nos situaremos al baseapp/urls.py e ingresamos la ruta de la página de registro en la urls 
    ```bash
    from django.urls import path 
    from .views import ListasPendientes, DetalleTarea, CrearTarea, EditarTarea, EliminarTarea, logueo, PaginaRegistro
    from django.contrib.auth.views import LogoutView


    urlpatterns = [
        path('',ListasPendientes.as_view(), name="tareas"),
        path('tarea/<int:pk>', DetalleTarea.as_view(), name="tarea"),
        path('registro/', PaginaRegistro.as_view(), name='registro'),
        path('login/', logueo.as_view(), name="login"),
        path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
        path('crear-tarea/', CrearTarea.as_view(), name="crear-tarea"),
        path('editar-tarea/<int:pk>', EditarTarea.as_view(), name="editar-tarea"),
        path('eliminar-tarea/<int:pk>', EliminarTarea.as_view(), name="eliminar-tarea"),

    ]
53. Al tener listo el url, vamos al templates/baseapp/login.html y agregamos la url de direccionamiento <p>No tienes una Cuenta? <a href="{% url 'registro' %}">Registrate</a></p>

    ```bash
    <h1>Ingresar</h1>
    <form method="POST">

        {% csrf_token %}
        {{form.as_p}}
        <input type="submit" value="Ingresar">
    </form>
    <!-- Agregamos un link de registro-->
    <p>No tienes una Cuenta? <a href="{% url 'registro' %}">Registrate</a></p>

54. AL ir al link del registrate sale la información en ingles lo podemos cambiar al español, proyecto/settings.py
    ```bash

    # Internationalization
    # https://docs.djangoproject.com/en/5.1/topics/i18n/

    LANGUAGE_CODE = 'es-cl' # para Chile

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_TZ = True

    LOGIN_URL = 'login'

55. Vamos a la baseapp/views.py vamos agregar la redirección a tareas y llamar a redirect from django.shortcuts import render, redirect
    ```bash
    from django.shortcuts import render, redirect
    from django.views.generic import ListView
    from django.views.generic import DetailView
    from django.views.generic import CreateView, UpdateView, DeleteView, FormView
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib.auth import login
    from django.contrib.auth.views import LoginView
    from django.contrib.auth.mixins import LoginRequiredMixin
    from django.urls import reverse_lazy
    from .models import Tarea

    class logueo(LoginView):
        template_name='baseapp/login.html'
        field= '__all__'
        redirect_authenticated_user = True
        
        def get_success_url(self):
            return reverse_lazy('tareas')

    class PaginaRegistro(FormView):
        template_name = 'baseapp/registro.html'
        form_class = UserCreationForm
        redirect_authenticated_user = True
        success_url = reverse_lazy('tareas')
        
        def form_valid(self, form):
            usuario = form.save()
            if usuario is not None:
                login(self.request, usuario)
            return super(PaginaRegistro,self).form_valid(form)

        
        # Funcion para redireccionar a tareas
        def get(self, *args, **kwargs):
            if self.request.user.is_authenticated:
                return redirect('tareas')
            return super(PaginaRegistro, self).get(*args, **kwargs)

    class ListasPendientes(LoginRequiredMixin, ListView):
        model = Tarea
        template_name ='tarea_list.html'
        context_object_name = 'tareas'
        
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['tareas'] = context['tareas'].filter(usuario=self.request.user) #usuario lo creamos en el modelo
            context['count'] = context['tareas'].filter(completo=False).count()

            return context
    
    class DetalleTarea(LoginRequiredMixin, DetailView):
        model = Tarea
        template_name ='baseapp/tarea.html'
        context_object_name = 'tarea'
        
    class CrearTarea(LoginRequiredMixin, CreateView):
        model = Tarea
        fields = ['titulo', 'descripcion', 'completo'] # para que no muestre todos los campos "usuario"
        success_url = reverse_lazy('tareas')
        
        # Para que las nuevas tareas se le asigne al usuario que este logeado
        def form_valid(self, form):
            form.instance.usuario = self.request.user
            return super(CrearTarea, self).form_valid(form)
        
    class EditarTarea(LoginRequiredMixin,UpdateView):
        model = Tarea
        fields = ['titulo', 'descripcion', 'completo'] # para que no muestre todos los campos "usuario"
        success_url = reverse_lazy('tareas')
        
    class EliminarTarea(LoginRequiredMixin,DeleteView):
        model = Tarea
        template_name ='baseapp/tarea_confirm_delete.html'
        context_object_name = 'tarea'
        success_url = reverse_lazy('tareas')

56. Agregamos en templates/baseapp/tarea_list.html la búsqueda
    ```bash
    {% if request.user.is_authenticated %}
    <p>{{request.user}}</p>
    <form method="post" action="{% url 'logout' %}">
        {% csrf_token %}
        <button type="submit">Salir</button>
    </form>
    {% else%}
    <a href="{% url 'login' %}">Ingresar</a>
    {% endif %}
    <hr>
    <h1>Listas Pendientes</h1>
    <!-- formulario de búsqueda-->
    <form method="GET">
        <input type="text" name="area-buscar">
        <input type="submit" value="Buscar">
    </form>
    <br>
    <a href="{% url 'crear-tarea' %}">Crear Nueva Tarea</a>
    <table>
        <tr>
            <th>Elementos</th>
            <th></th>
            <th></th>
            <th></th>

        </tr>

        {% for tarea in tareas %}
        <tr>
            <td>{{tarea.titulo}}</td>
            <td><a href="{% url 'tarea' tarea.id %}">Ver</a></td>
            <td><a href="{% url 'editar-tarea' tarea.id %}">Editar</a></td>
            <td><a href="{% url 'eliminar-tarea' tarea.id %}">Eliminar</a></td>

        </tr>
        {% empty %}
        <h3>No hay elementos en la lista</h3>
        {% endfor %}
    </table>

57. En la vista configuramos la búsqueda baseapp/views.py
    ```bash
    from django.shortcuts import render, redirect
    from django.views.generic import ListView
    from django.views.generic import DetailView
    from django.views.generic import CreateView, UpdateView, DeleteView, FormView
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib.auth import login
    from django.contrib.auth.views import LoginView
    from django.contrib.auth.mixins import LoginRequiredMixin
    from django.urls import reverse_lazy
    from .models import Tarea

    class logueo(LoginView):
        template_name='baseapp/login.html'
        field= '__all__'
        redirect_authenticated_user = True
        
        def get_success_url(self):
            return reverse_lazy('tareas')

    class PaginaRegistro(FormView):
        template_name = 'baseapp/registro.html'
        form_class = UserCreationForm
        redirect_authenticated_user = True
        success_url = reverse_lazy('tareas')
        
        def form_valid(self, form):
            usuario = form.save()
            if usuario is not None:
                login(self.request, usuario)
            return super(PaginaRegistro,self).form_valid(form)
        
        # Funcion para redireccionar a tareas
        
        def get(self, *args, **kwargs):
            if self.request.user.is_authenticated:
                return redirect('tareas')
            return super(PaginaRegistro, self).get(*args, **kwargs)

    class ListasPendientes(LoginRequiredMixin, ListView):
        model = Tarea
        template_name ='tarea_list.html'
        context_object_name = 'tareas'
        
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['tareas'] = context['tareas'].filter(usuario=self.request.user) #usuario lo creamos en el modelo
            context['count'] = context['tareas'].filter(completo=False).count()
            
            # codigo para hacer la búsqueda
            valor_buscado = self.request.GET.get('area-buscar') or ''
            if valor_buscado:
                context['tareas'] = context['tareas'].filter(titulo__icontains=valor_buscado)
            context['valor_buscado'] = valor_buscado
            return context
    
    class DetalleTarea(LoginRequiredMixin, DetailView):
        model = Tarea
        template_name ='baseapp/tarea.html'
        context_object_name = 'tarea'
        
    class CrearTarea(LoginRequiredMixin, CreateView):
        model = Tarea
        fields = ['titulo', 'descripcion', 'completo'] # para que no muestre todos los campos "usuario"
        success_url = reverse_lazy('tareas')
        
        # Para que las nuevas tareas se le asigne al usuario que este logeado
        def form_valid(self, form):
            form.instance.usuario = self.request.user
            return super(CrearTarea, self).form_valid(form)
        
    class EditarTarea(LoginRequiredMixin,UpdateView):
        model = Tarea
        fields = ['titulo', 'descripcion', 'completo'] # para que no muestre todos los campos "usuario"
        success_url = reverse_lazy('tareas')
        
    class EliminarTarea(LoginRequiredMixin,DeleteView):
        model = Tarea
        template_name ='baseapp/tarea_confirm_delete.html'
        context_object_name = 'tarea'
        success_url = reverse_lazy('tareas')
        





