from django.urls import path
from . import views

app_name="perfil"
urlpatterns = [
    path('p1/', views.perfil_uno,name = 'p1'),
    path('p2/', views.perfil_dos,name = 'p2'),
]