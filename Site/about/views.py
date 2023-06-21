from django.shortcuts import render
from django.http import HttpResponse


def helloword(request):
    return HttpResponse('Hello word')


def paginainicial(request):
    return render(request, 'home/index.html')

def historia(request):
    return render(request, 'home/historia.html')

def aplicacoes(request):
    return render(request, 'home/aplicacoes.html')
def funcionamento(request):
    return render(request, 'home/funcionamento.html')
def objetivo(request):
    return render(request, 'home/objetivo.html')
def problemas(request):
    return render(request, 'home/problemas.html')
def Tipos(request):
    return render(request, 'home/Tipos.html')
