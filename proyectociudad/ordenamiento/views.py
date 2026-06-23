from django.shortcuts import render, redirect
from ordenamiento.models import Parroquia
from ordenamiento.forms import ParroquiaForm

def listar_parroquias(request):
    parroquias = Parroquia.objects.all()
    informacion_template = {'parroquias': parroquias, 'numero_parroquias': len(parroquias)}
    return render(request, 'listar_parroquias.html', informacion_template)

def crear_parroquia(request):
    if request.method == 'POST':
        formulario = ParroquiaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(listar_parroquias)
    else:
        formulario = ParroquiaForm()
    diccionario = {'formulario': formulario}
    return render(request, 'crear_parroquia.html', diccionario)

def editar_parroquia(request, id):
    parroquia = Parroquia.objects.get(pk=id)
    if request.method == 'POST':
        formulario = ParroquiaForm(request.POST, instance=parroquia)
        if formulario.is_valid():
            formulario.save()
            return redirect(listar_parroquias)
    else:
        formulario = ParroquiaForm(instance=parroquia)
    diccionario = {'formulario': formulario}
    return render(request, 'editar_parroquia.html', diccionario)
