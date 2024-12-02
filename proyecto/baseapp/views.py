from django.views.generic import ListView
from .models import Tarea


class ListasPendientes(ListView):
    model = Tarea
    template_name ='tarea_list.html'
    context_object_name = 'tareas'
  

