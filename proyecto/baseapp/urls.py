from django.urls import path 
from baseapp.views import ListasPendientes

urlpatterns = [
    path('',ListasPendientes.as_view(), name="pendientes")
]
