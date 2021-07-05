from django import forms
from django.forms.widgets import Textarea
from django.utils import translation

from .models import Marca, Categoria, Medicamento

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = [ 'nome' ]
        widgets = {
            'nome': forms.TextInput(attrs={
                'size': '30',
                'required': 'True',
                'class': "form-control",
                'placeholder': "Nome"
            })
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = [ 'nome' ]
        widgets = {
            'nome': forms.TextInput(attrs={
                'size': '50',
                'required': 'True',
                'class': "form-control",
                'placeholder': "Nome"
            })
        }

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento

        #[ 'nome', 'descricao', 'prescricao', 'validade', 'quantidade' ]
        fields = '__all__'

        extraClass = 'date_pt-BR' if translation.get_language() == 'pt-BR' else 'date_en'

        widgets = {
            'nome': forms.TextInput(attrs={
                'size': '50',
                'required': 'True',
                'class': "form-control",
                'placeholder': "Nome"
            }),
            'descricao': forms.TextInput(attrs={
                'size': '100',
                'required': 'True',
                'class': "form-control",
                'placeholder': "Descricao"
            }),
            'prescricao': forms.Textarea(attrs={
                'style': 'resize:vertical',
                'size': '200',
                'rows': '4', 
                'cols': '50', 
                'class': "form-control",
                'placeholder': "Prescricao"
            }),
            'validade': forms.DateInput(attrs={
                'size': '50',
                'required': 'True',
                'class': "form-control " + extraClass,
                'placeholder': "Validade"
            }),
            'quantidade': forms.TextInput(attrs={
                'required': 'True',
                'class': "form-control 3d_number",
                'placeholder': "Quantidade"
            })
        }

class UsuarioLoginForm(forms.Form):
    login = forms.CharField(required=True, label='Login', widget=forms.TextInput(attrs={
                'required': 'True',
                'class': "form-control",
                'placeholder': "Informe seu login"
    }))
    password = forms.CharField(required=True, label='Senha', widget=forms.PasswordInput(attrs={
                'required': 'True',
                'class': "form-control",
                'placeholder': "Informe sua senha",
                'type': "password"
    }))

class UsuarioCriarForm(UsuarioLoginForm):
    password_confirm = forms.CharField(required=True, label='Conf. Senha', widget=forms.PasswordInput(attrs={
                'required': 'True',
                'class': "form-control",
                'placeholder': "Informe novamente a senha",
                'autocomplete': "new-password",
                'type': "password"
    }))
    nome = forms.CharField(required=True, label='Nome', widget=forms.TextInput(attrs={
                'required': 'True',
                'class': "form-control",
                'placeholder': "Informe seu nome"
    }))
    email = forms.CharField(required=True, label='Email', widget=forms.TextInput(attrs={
                'required': 'True',
                'class': "form-control",
                'placeholder': "Informe seu email"
    }))
