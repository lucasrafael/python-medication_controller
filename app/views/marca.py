from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from ..models import Marca
from ..forms import MarcaForm
from ..util.page import Paginator


###########
## Marca ##
###########
URL_MARCA_LIST = '/marca/list'

VIEW_MARCA_EDIT = 'marca/editar.html'
VIEW_MARCA_LIST = 'marca/listar.html'

def listarMarcas(request):
    if request.method == 'POST':
        nome = MarcaForm(request.POST).data.get('nome')
        if nome:
            marcas = Marca.objects.filter(nome__startswith=nome)
            pages = Paginator(marcas, request).getPages()

            return render(request, VIEW_MARCA_LIST, { 'nome': nome, 'marcas': pages })

        return redirect(URL_MARCA_LIST)

    else:
        marcas = Marca.objects.all()
        pages = Paginator(marcas, request).getPages()

        return render(request, VIEW_MARCA_LIST, { 'marcas': pages })

def mostrarMarca(request, id):
    marca = Marca.objects.get(pk=id)
    
    return render(request, 'marca/show.html', { 'marca' : marca, 'isToDelete': request.path.find("delete") > 0 })

def mostrarMedicamentos(request, id):
    marca = Marca.objects.get(pk=id)
    medicamentos = marca.medicamento_set.all()
    
    return render(request, 'marca/medicamentos.html', { 'marca': marca, 'medicamentos': medicamentos })

@login_required
def criarMarca(request):
    if request.method == 'POST':
        try:
            MarcaForm(request.POST).save()
            messages.add_message(request, messages.INFO, _('marca.inserida'))

            return redirect(URL_MARCA_LIST)

        except Exception as err:
            messages.add_message(request, messages.ERROR, err)

    return render(request, VIEW_MARCA_EDIT, {'form': MarcaForm(request.POST)})

@login_required
def editarMarca(request, id):
    marca = Marca.objects.get(pk=id)
    if request.method == 'POST':        
        try:
            MarcaForm(request.POST, instance=marca).save()
            messages.add_message(request, messages.INFO, _('marca.alterada'))

            return redirect(URL_MARCA_LIST)

        except Exception as err:
            messages.add_message(request, messages.ERROR, err)

    return render(request, VIEW_MARCA_EDIT, {
        'form' : MarcaForm(instance=marca), 
        'marca' : marca
    })

@login_required
def removerMarca(request, id):
    try:
        Marca.objects.get(pk=id).delete()
        messages.add_message(request, messages.INFO, _('marca.excluida'))

    except Exception as err:
        messages.add_message(request, messages.ERROR, err)

    return redirect(URL_MARCA_LIST)
