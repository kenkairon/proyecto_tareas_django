from django.urls import path 
from .views import ListasPendientes, DetalleTarea, CrearTarea, EditarTarea

urlpatterns = [
    path('',ListasPendientes.as_view(), name="tareas"),
    path('tarea/<int:pk>', DetalleTarea.as_view(), name="tarea"),
    path('crear-tarea/', CrearTarea.as_view(), name="crear-tarea"),
    path('editar-tarea/<int:pk>', EditarTarea.as_view(), name="editar-tarea"),
]
