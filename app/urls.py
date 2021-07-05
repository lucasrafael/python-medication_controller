
from django.contrib import admin
from django.urls import path

from .views import marca, categoria, medicamento, usuario

urlpatterns = [
    # Inicial
    path('', medicamento.listarMedicamentos),

    # Marca
    path('marca/list', marca.listarMarcas, name='listar-marcas'),
    path('marca/new', marca.criarMarca, name='nova-marca'),
    path('marca/edit/<int:id>', marca.editarMarca, name='editar-marca'),
    path('marca/delete/<int:id>', marca.removerMarca, name='remover-marca'),
    path('marca/show/<int:id>', marca.mostrarMarca, name='mostrar-marca'),
    path('marca/show/delete/<int:id>', marca.mostrarMarca, name='mostrar-marca'),
    path('marca/<int:id>/medicamentos', marca.mostrarMedicamentos, name='mostrar-marca-med'),

    # Categoria
    path('categoria/list', categoria.listarCategorias, name='listar-categorias'),
    path('categoria/new', categoria.criarCategoria, name='nova-categoria'),
    path('categoria/edit/<int:id>', categoria.editarCategoria, name='editar-categoria'),
    path('categoria/delete/<int:id>', categoria.removerCategoria, name='remover-categoria'),
    path('categoria/show/<int:id>', categoria.mostrarCategoria, name='mostrar-categoria'),
    path('categoria/show/delete/<int:id>', categoria.mostrarCategoria, name='mostrar-categoria'),
    path('categoria/<int:id>/medicamentos', categoria.mostrarMedicamentos, name='mostrar-categoria-med'),

    # Medicamentos
    path('medicamento/list', medicamento.listarMedicamentos, name='listar-medicamentos'),
    path('medicamento/new', medicamento.criarMedicamento, name='nova-medicamento'),
    path('medicamento/edit/<int:id>', medicamento.editarMedicamento, name='editar-medicamento'),
    path('medicamento/delete/<int:id>', medicamento.removerMedicamento, name='remover-medicamento'),
    path('medicamento/show/<int:id>', medicamento.mostrarMedicamento, name='mostrar-medicamento'),
    path('medicamento/show/delete/<int:id>', medicamento.mostrarMedicamento, name='mostrar-medicamento'),

    # Usuário
    path('usuario/login', usuario.loginUsuario, name='login-usuario'),
    path('usuario/new', usuario.criarUsuario, name='criar-usuario'),
    path('usuario/logout', usuario.logoutUsuario, name='logout-usuario')
]