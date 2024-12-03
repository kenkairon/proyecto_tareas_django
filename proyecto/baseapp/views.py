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
    
