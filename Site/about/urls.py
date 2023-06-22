from django.urls import path
from . import views

urlpatterns = [
    path('helloword/', views.helloword),
    path('', views.paginainicial, name='index'),
    path('menu/historia', views.historia, name='historia'),
    path('menu/aplicacoes', views.aplicacoes, name='aplicacoes'),
    path('menu/funcionamento', views.funcionamento, name='funcionamento'),
    path('menu/objetivo', views.objetivo, name='objetivo'),
    path('menu/problemas', views.problemas, name='problemas'),
    path('menu/Tipos', views.Tipos, name='tipos'),
]
