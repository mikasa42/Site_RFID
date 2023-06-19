from django.shortcuts import render
from django.http import HttpResponse


def helloword(request):
    return HttpResponse('Hello word')


def paginainicial(request):
    return render(request, 'home/index.html')
