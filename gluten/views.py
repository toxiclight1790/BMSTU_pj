from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.urls import reverse
from django.views.generic import ListView, DetailView
import json
import requests
from django.core import serializers
from django.views import View
from .forms import *


from .models import Recept, Text, Categor


class IndexView(ListView):
    template_name = 'index.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return "Ok"

def Menu(request):
    menu_list = Categor.objects.values('id', 'title')
    return JsonResponse({'data': list(menu_list)})


def detail(request, categor_id):
    try:
        recepts = Recept.objects.filter(types=categor_id)
        # print(recepts[0].types)
    except Recept.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'recepts.html', {'recepts': recepts})

def CurRec(request, recept_id):
    try:
        data =[]
        data.append(list(Recept.objects.filter(id=recept_id).values()))
        # print(recept.name)
        data.append(list(Text.objects.filter(recept=recept_id).values()))
        
        # recept.append(text)
    except Recept.DoesNotExist:
        raise Http404("Recept does not exist")
    return render(request, 'recept.html', {'recept': data})


class NewRecView(View):    
    def post(self, request):
        print('HERE')
        data=request.POST
        files = request.FILES.getlist('file')

        if request.method == 'POST':
            Name = data['name']
            Types = Categor.objects.get(id=data['types'])
            Description = data['description']
            recept = Recept()
            recept.name = Name
            recept.types = Types
            recept.description = Description
            recept.img = files[0]
            recept.save()
            return HttpResponse(status=201)


# name = models.CharField(default='',max_length=200)
# types = models.ForeignKey(Categor,default=0,on_delete=models.CASCADE)
# description = models.CharField(default='',max_length=200)
# pub_date = models.DateTimeField(default=now,blank=True)
# likes = models.IntegerField(default=0)
# img = models.ImageField(upload_to ='uploads/', default='none.png')