from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Create your views here.

def function_view(request):
    return HttpResponse('response from function view')


class ExampleClassBased(View):
    def get(self, request):
        return HttpResponse('response from class based view')


class ExampleView(View):
    def get(self, request):
        return render(request, 'example.html', {'list': "123"})


class VarExampleView(View):
    def get(self, request):
        return render(request, 'var_example.html', {'my_var': '03.11.2017'})