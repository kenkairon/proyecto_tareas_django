from django.urls import path 
from .views import ListasPendientes, DetalleTarea

urlpatterns = [
    path('',ListasPendientes.as_view(), name="pendientes"),
    path('tarea/<int:pk>', DetalleTarea.as_view(), name="tarea"),

]
