from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Entity
from django.template import loader
from user_ver import user_ver
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.             ENTITY VIEW

def list(request):
    user_ver(request, False)
    context = {'entity_list': Entity.objects.all(), 'admin': False }
    return render(request, 'entity/list.html', context)

def detail(request, entity_id):
    user_ver(request, False)
    context = {'entity': get_object_or_404(Entity, id = entity_id)}
    return render(request, 'entity/detail.html', context)

def search(request):
    user_ver(request, False)
    input = request.POST['search_input']
    context = {'entity_list': Entity.objects.filter(name__icontains = input), 'admin': False, 'search': True}
    return render(request, 'entity/list.html', context)


#ADMIN

def admin_entity_list(request):
    user_ver(request, True)
    context = {'entity_list': Entity.objects.all(), 'admin': True}
    return render(request, 'entity/list.html', context)


def edit_entity(request, entity_id):
    user_ver(request, True)
    if int(entity_id) != 0:
        context = {'entity': get_object_or_404(Entity, id = entity_id), 'entityid': int(entity_id)}
    else:
        context = {'entityid': 0}
    return render(request, 'entity/edit_create_entity.html', context)

def edit_entity_save(request, entity_id):
    user_ver(request, True)
    
    if int(entity_id) == 0:
        a = Entity()
    else:
        a = Entity.objects.get(id = entity_id)
    
    a.name = request.POST['name']
    a.description = request.POST['description']
    a.address = request.POST['address']
    a.photolink = request.POST['photolink']
    a.officallink = request.POST['officallink']

    a.save()

    if entity_id == 0:
        return HttpResponseRedirect(reverse('adminentitylist', args=()))
    else:
        return HttpResponseRedirect(reverse('editentity', args=(entity_id,)))

def adminsearch(request):
    user_ver(request, True)
    input = request.POST['search_input']
    context = {'entity_list': Entity.objects.filter(name__icontains = input), 'admin': True, 'search': True}
    return render(request, 'entity/list.html', context)

def review(request, entity_id):
    user_ver(request, False)
    entity = Entity.objects.get(id = entity_id)
    comment = request.POST['commentbox']
    try:
        selected = request.POST['review']
    except MultiValueDictKeyError:
        selected = '0'

    if (selected == 'Good' or selected == 'Bad'):
        if(selected == 'Good'):
            entity.positive_review += 1
        else:
            entity.negative_review += 1
        entity.save()

    if comment:
        pass

    return HttpResponseRedirect(reverse('detail', args=(entity_id,)))


