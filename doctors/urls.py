from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_medicos, name='lista_medicos'),

    path("/<int:medico_id>/perfil/", views.perfil_medico, name="perfil_medico"),
]

