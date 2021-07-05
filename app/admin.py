from django.contrib import admin

from .models import Marca, Categoria, Medicamento

# Register models here.

admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Medicamento)