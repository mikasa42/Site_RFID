from django.urls import path
from . import views

urlpatterns = [
    path('helloword/', views.helloword),
    path('', views.paginainicial, name='index'),
    path('historia/', views.historia),
    path('aplicacoes/', views.aplicacoes),
    path('funcionamento/', views.funcionamento),
    path('objetivo/', views.objetivo),
    path('problemas/', views.problemas),
    path('Tipos/', views.Tipos),
]
