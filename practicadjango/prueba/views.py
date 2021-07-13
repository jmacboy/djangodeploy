from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.template import loader

from prueba.forms import PersonaForm
from prueba.models import Persona


def holamundo(request):
    return HttpResponse('Index de prueba')


def detalle_persona(request, persona_id):
    return HttpResponse('Mandaste la persona: ' + str(persona_id))


def personas_list(request):
    lista_personas = Persona.objects.all()
    template = loader.get_template('prueba/lista.html')
    context = {
        'lista_personas': lista_personas
    }
    return HttpResponse(
        template.render(context, request)
    )


def personas_create(request):
    if request.method == 'POST':
        # Insert
        form = PersonaForm(request.POST)
        if form.is_valid():
            # nombres = form.cleaned_data['nombres']
            # apellidos = form.cleaned_data['apellidos']
            # ciudad = form.cleaned_data['ciudad']
            # edad = form.cleaned_data['edad']
            # fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            # genero = form.cleaned_data['genero']
            # email = form.cleaned_data['email']
            # obj_persona = Persona()
            # obj_persona.nombres = nombres
            # obj_persona.apellidos = apellidos
            # obj_persona.ciudad = ciudad
            # obj_persona.fecha_nacimiento = fecha_nacimiento
            # obj_persona.edad = edad
            # obj_persona.genero = genero
            # obj_persona.email = email
            # obj_persona.save()
            form.save()
            return HttpResponseRedirect('/prueba/personas')
    else:
        form = PersonaForm()
    return render(request, 'prueba/form.html', {'form': form})


def personas_update(request, persona_id):
    obj_persona = Persona.objects.filter(pk=persona_id).first()
    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=obj_persona)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/prueba/personas')
    else:
        form = PersonaForm(instance=obj_persona)
    return render(request, 'prueba/form.html', {'form': form})


def personas_delete(request, persona_id):
    obj_persona = Persona.objects.filter(pk=persona_id).first()
    obj_persona.delete()
    return HttpResponseRedirect('/prueba/personas')
