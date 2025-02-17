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



