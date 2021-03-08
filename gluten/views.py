from django.http import HttpResponse, Http404, JsonResponse, HttpResponseRedirect
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
    except Recept.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'recepts.html', {'recepts': recepts})
def CurRec(request, recept_id):
    try:
        data =[]
        data.append(list(Recept.objects.filter(id=recept_id).values()))
        data.append(list(Text.objects.filter(recept=recept_id).values()))
        data.append(list(Comment.objects.filter(recept=recept_id).values().order_by('-pub_date')))
        
    except Recept.DoesNotExist:
        raise Http404("Recept does not exist")
    return render(request, 'recept.html', {'recept': data})

def add_text(id, data):
    for i in data:
        print(id, i)

class NewRecView(View):    
    def post(self, request):
        print('HERE_rec')
        data=request.POST
        files = request.FILES.getlist('file')

        if request.method == 'POST':
            Name = data['name']
            Types = Categor.objects.get(id=data['types'])
            Description = data['description']
            Components = json.loads(data['text'])
            recept = Recept()
            recept.name = Name
            recept.types = Types
            recept.comp = Components
            recept.description = Description
            if files != []:
                recept.img = files[0]
            recept.save()
            # add_text(recept.id, text)
            return HttpResponse(status=201)

class NewComView(View):    
    def post(self, request, recept_id):
        print('HERE_com')
        data=request.POST
        Text = data['text']
        # files = request.FILES
        # print(files)
        if request.method == 'POST':
            rec = Recept.objects.get(id=recept_id)
            comment = Comment()
            comment.recept = rec
            comment.comment_text = Text
            # if files != []:
                # comment.img = files[0]
            comment.save()
            # return HttpResponse(status=201)
            return redirect('/recept/'+str(recept_id)+'/')
        else:
            return HttpResponse(status=999)

def DelRec(request, recept_id):
    print('HERE_del_rec')
    try:
        rec = Recept.objects.get(id=recept_id)
        rec.delete()
        return HttpResponseRedirect("/")   
    except Recept.DoesNotExist:
        raise Http404("Recept does not exist")
 