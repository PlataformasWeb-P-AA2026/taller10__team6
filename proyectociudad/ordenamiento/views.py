<<<<<<< HEAD
def listar_barrios(request):
    barrios = Barrio.objects.all()
    return render(request, 'listar_barrios.html', {'barrios': barrios})

def crear_barrio(request):
    if request.method == 'POST':
        form = BarrioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_barrios')
    else:
        form = BarrioForm()
    return render(request, 'crear_barrio.html', {'form': form, 'titulo': 'Crear Barrio'})

def editar_barrio(request, id):
    b = Barrio.objects.get(pk=id)
    if request.method == 'POST':
        form = BarrioForm(request.POST, instance=b)
        if form.is_valid():
            form.save()
            return redirect('listar_barrios')
    else:
        form = BarrioForm(instance=b)
    return render(request, 'editar_barrio.html', {'form': form, 'titulo': 'Editar Barrio'})

def listar_parroquias(request): 
    parroquias = Parroquia.objects.all()
    return render(request, 'listar_parroquias.html', {'parroquias': parroquias})

def crear_parroquia(request):
    if request.method == 'POST':
        form = ParroquiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_parroquias')
    else:
        form = ParroquiaForm()
    return render(request, 'formulario.html', {'form': form, 'titulo': 'Crear Parroquia'})

def editar_parroquia(request, id):
    p = Parroquia.objects.get(pk=id)
    if request.method == 'POST':
        form = ParroquiaForm(request.POST, instance=p)
        if form.is_valid():
            form.save()
            return redirect('listar_parroquias')
    else:
        form = ParroquiaForm(instance=p)
    return render(request, 'formulario.html', {'form': form, 'titulo': 'Editar Parroquia'})
=======
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
>>>>>>> 1d0228d99bf39a117dbc4e2a6bf5261526b7ec2e
