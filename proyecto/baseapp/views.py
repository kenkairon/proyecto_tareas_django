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
    
