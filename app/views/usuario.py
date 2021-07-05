from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

from ..forms import UsuarioLoginForm, UsuarioCriarForm


#############
## Usuario ##
#############
def logoutUsuario(request):

	logout(request)

	return redirect("/")

def loginUsuario(request):

    if request.method == 'POST':

        form = UsuarioLoginForm(request.POST)
        if form.is_valid():
        
            user = authenticate(request, username=form.cleaned_data['login'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                
                return redirect("/")

            else:
                if request.user.is_authenticated:
                    logout(request)

                messages.add_message(request, messages.WARNING,  _('usuario.invalido'))

    else:
         form = UsuarioLoginForm()

    return render(request, 'usuario/login.html', { 'form': form })


def criarUsuario(request):

    if request.method == 'POST':

        form = UsuarioCriarForm(request.POST)
        try:
            if form.is_valid():

                username = form.cleaned_data['login']
                password = form.cleaned_data['password']
                password_confirm = form.cleaned_data['password_confirm']
                first_name = form.cleaned_data['nome']
                email = form.cleaned_data['email']

                if password != password_confirm:
                    raise AttributeError(_('usuario.senha.diferente'))

                User.objects.create_user(
                    username=username,
                    password=password,
                    first_name=first_name,
                    email=email
                )
                messages.add_message(request, messages.INFO, _('usuario.cadastrado'))
                return redirect("/")

        except Exception as err:
            messages.add_message(request, messages.WARNING, err)

    else:
         form = UsuarioCriarForm()

    return render(request, 'usuario/criar.html', { 'form': form })
