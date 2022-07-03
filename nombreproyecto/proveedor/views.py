from tkinter import EW
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Proveedor
from .forms import ProveedorForm
# Create your views here.

def inicio(request):
    return render(request, 'pages/inicio.html')

def index(request):
    return render(request, 'pages/index.html')

def proveedor(request):
    proveedors = Proveedor.objects.all()
    return render(request, 'proveedores/index.html', {'proveedors':proveedors})

def crear_proveedor(request):
    formulario = ProveedorForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('proveedor')

    return render(request, 'proveedores/crear.html', {'formulario':formulario})

def editar_proveedor(request, id):
    proveedor = Proveedor.objects.get(id=id)
    formulario = ProveedorForm(request.POST or None, request.FILES or None, instance=proveedor)
    if (formulario.is_valid() and request.POST):
        formulario.save()
        return redirect('proveedor')

    return render(request, 'proveedores/editar.html', {'formulario':formulario})

def borrar_proveedor(request,id):
    proveedor = Proveedor.objects.get(id = id)
    proveedor.delete()
    return redirect('proveedor')