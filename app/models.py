from django.db import models

# Create models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=50,unique=True,null=False,blank=False)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']

class Marca(models.Model):
    nome = models.CharField(max_length=30,unique=True,null=False,blank=False)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']

class Medicamento(models.Model):
    nome =  models.CharField(max_length=50,unique=True,null=False,blank=False)
    descricao = models.CharField(max_length=100,null=False,blank=False)
    prescricao = models.CharField(max_length=200,null=True,blank=True)
    validade = models.DateField(null=False,blank=False)
    quantidade = models.IntegerField(null=False,blank=False)

    marca = models.ForeignKey(Marca,
            on_delete=models.SET_NULL,
            blank=False,
            null=True
    )
    categoria = models.ForeignKey(Categoria,
            on_delete=models.SET_NULL,
            blank=False,
            null=True
    )

    def __str__(self):
        return self.nome

    class Meta:
        """ O símbolo '-' que antecede informa que a ordenação é decrescente. """
        ordering = ['-validade']

