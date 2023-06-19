from django.urls import path
from . import views

urlpatterns = [
    path('helloword/', views.helloword),
    path('', views.paginainicial, name='index'),
]
