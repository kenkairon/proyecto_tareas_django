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
    
