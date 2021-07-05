from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from ..models import Categoria
from ..forms import CategoriaForm
from ..util.page import Paginator


###############
## Categoria ##
###############
URL_CATEGORIA_LIST = '/categoria/list'

VIEW_CATEGORIA_EDIT = 'categoria/editar.html'
VIEW_CATEGORIA_LIST = 'categoria/listar.html'

def listarCategorias(request):
    if request.method == 'POST':
        nome = CategoriaForm(request.POST).data.get('nome')
        if nome:
            categorias = Categoria.objects.filter(nome__startswith=nome)
            pages = Paginator(categorias, request).getPages()

            return render(request, VIEW_CATEGORIA_LIST, { 'nome': nome, 'categorias': pages })

        return redirect(URL_CATEGORIA_LIST)

    else:
        categorias = Categoria.objects.all()
        pages = Paginator(categorias, request).getPages()

        return render(request, VIEW_CATEGORIA_LIST, { 'categorias': pages })

def mostrarCategoria(request, id):
    categoria = Categoria.objects.get(pk=id);
    
    return render(request, 'categoria/show.html', { 'categoria' : categoria, 'isToDelete': request.path.find("delete") > 0 })

def mostrarMedicamentos(request, id):
    categoria = Categoria.objects.get(pk=id);
    medicamentos = categoria.medicamento_set.all()

    return render(request, 'categoria/medicamentos.html', { 'categoria' : categoria, 'medicamentos': medicamentos })

@login_required
def criarCategoria(request):
    if request.method == 'POST':
        try:
            CategoriaForm(request.POST).save()
            messages.add_message(request, messages.INFO, _('categoria.inserida'))

            return redirect(URL_CATEGORIA_LIST)

        except Exception as err:
            messages.add_message(request, messages.ERROR, err)

    return render(request, VIEW_CATEGORIA_EDIT, {'form': CategoriaForm(request.POST)})

@login_required
def editarCategoria(request, id):
    categoria = Categoria.objects.get(pk=id)
    if request.method == 'POST':
        try:
            CategoriaForm(request.POST, instance=categoria).save()
            messages.add_message(request, messages.INFO, _('categoria.alterada'))

            return redirect(URL_CATEGORIA_LIST)

        except Exception as err:
            messages.add_message(request, messages.ERROR, err)

    return render(request, VIEW_CATEGORIA_EDIT, {
        'form' : CategoriaForm(instance=categoria), 
        'categoria' : categoria
    })

@login_required
def removerCategoria(request, id):
    try:
        Categoria.objects.get(pk=id).delete()
        messages.add_message(request, messages.INFO, _('categoria.excluida'))

    except Exception as err:
        messages.add_message(request, messages.ERROR, err)

    return redirect(URL_CATEGORIA_LIST)
