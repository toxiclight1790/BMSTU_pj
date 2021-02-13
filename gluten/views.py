from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader

from .models import Recept, Text


def index(request):
    latest_recept_list = Recept.objects.order_by('-pub_date')[:5]
    template = loader.get_template('index.html')
    context = {
        'latest_recept_list': latest_recept_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, recept_id):
    recept = get_object_or_404(Recept, pk=recept_id)
    return render(request, 'detail.html', {'recept': recept})




# def results(request, recept_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % recept_id)

# def vote(request, recept_id):
#     return HttpResponse("You're voting on question %s." % recept_id)