from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render

# Create your views here.



class bendi_view(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')
