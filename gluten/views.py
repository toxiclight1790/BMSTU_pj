from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.views.generic import ListView, DetailView
import json
from django.core import serializers



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
        print(recepts)
    except Recept.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'recepts.html', {'recepts': recepts})



# def results(request, recept_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % recept_id)

# def vote(request, recept_id):
#     return HttpResponse("You're voting on question %s." % recept_id)