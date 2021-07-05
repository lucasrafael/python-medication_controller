from django import forms

from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from datetime import datetime

from ..models import Marca, Categoria, Medicamento
from ..forms import MedicamentoForm
from ..util.page import Paginator


#################
## Medicamento ##
#################
URL_MEDICAMENTO_LIST = '/medicamento/list'

VIEW_MEDICAMENTO_EDIT = 'medicamento/editar.html'
VIEW_MEDICAMENTO_LIST = 'medicamento/listar.html'

def listarMedicamentos(request):
    if request.method == 'POST':
        nome = MedicamentoForm(request.POST).data.get('nome')
        if nome is not None:
            medicamentos = Medicamento.objects.filter(nome__startswith=nome)
            pages = Paginator(medicamentos, request).getPages()

            return render(request, VIEW_MEDICAMENTO_LIST, { 'nome': nome, 'medicamentos': pages })

        return redirect(URL_MEDICAMENTO_LIST)

    else:
        medicamentos = Medicamento.objects.all()
        pages = Paginator(medicamentos, request).getPages()

        return render(request, VIEW_MEDICAMENTO_LIST, { 'medicamentos': pages })

def mostrarMedicamento(request, id):
    medicamento = Medicamento.objects.get(pk=id);
    
    return render(request, 'medicamento/show.html', { 'medicamento' : medicamento, 'isToDelete': request.path.find("delete") > 0 })

@login_required
def criarMedicamento(request):
    if request.method == 'POST':
        try:
            MedicamentoForm(request.POST).save()
            messages.add_message(request, messages.INFO, _('medicamento.inserido'))

            return redirect(URL_MEDICAMENTO_LIST)

        except Exception as err:
            messages.add_message(request, messages.ERROR, err)

    marcas = Marca.objects.all()
    categorias = Categoria.objects.all()

    return render(request, VIEW_MEDICAMENTO_EDIT, {'form': MedicamentoForm(request.POST), 'marcas': marcas, 'categorias': categorias})

@login_required
def editarMedicamento(request, id):
    medicamento = Medicamento.objects.get(pk=id)
    if request.method == 'POST':
        try:
            MedicamentoForm(request.POST, instance=medicamento).save()        
            messages.add_message(request, messages.INFO, _('medicamento.alterado'))

            return redirect(URL_MEDICAMENTO_LIST)

        except Exception as err:
            messages.add_message(request, messages.ERROR, err)

    marcas = Marca.objects.all()
    categorias = Categoria.objects.all()

    return render(request, VIEW_MEDICAMENTO_EDIT, {
        'form' : MedicamentoForm(instance=medicamento), 
        'medicamento' : medicamento,
        'marcas': marcas, 
        'categorias': categorias
    })

@login_required
def removerMedicamento(request, id):
    try:
        Medicamento.objects.get(pk=id).delete()
        messages.add_message(request, messages.INFO, _('medicamento.excluido'))
    
    except Exception as err:
        messages.add_message(request, messages.ERROR, err)

    return redirect(URL_MEDICAMENTO_LIST)
