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
