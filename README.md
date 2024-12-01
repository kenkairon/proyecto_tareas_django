# proyecto_tareas_python
Educativo y de Aprendizaje Personal

---

## Tabla de Contenidos
- [Requisitos](#requisitos)
- [Configuración del Entorno](#configuración-del-entorno)
- [Activación del Entorno](#Activación-del-Entorno)
- [Configuración Inicial](#configuración-inicial)
- [Pasos del Proyecto](#pasos-del-proyecto)
  - [Configuración del Proyecto](#configuración-del-proyecto)
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

## Configuración del Proyecto

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


   
