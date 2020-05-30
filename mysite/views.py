from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json
from . import models


# Create your views here.
def index(request):
    return render(request, 'Todo.html', locals())


def get_json(request):
    m = dict()
    msgMap = models.Msg.objects.get(mapKey='msgMap')
    activateMap = models.Msg.objects.get(mapKey='activateMap')
    completedMap = models.Msg.objects.get(mapKey='completedMap')
    m.update({msgMap.mapKey: msgMap.mapValue})
    m.update({activateMap.mapKey: activateMap.mapValue})
    m.update({completedMap.mapKey: completedMap.mapValue})

    return JsonResponse(m)


def set_json(request):
    msgMApValue = request.POST.get('msgMap')
    # activateMapValue = request.POST.get('activateMap')
    # completedMapValue = request.POST.get('completedMap')
    models.Msg.objects.filter(mapKey='msgMap').update(mapValue=msgMApValue)
    # models.Msg.objects.filter(mapKey='activateMap').update(mapValue=activateMapValue)
    # models.Msg.objects.filter(mapKey='completedMap').update(mapValue=completedMapValue)
    return HttpResponse('set_json')
