import django.core.paginator as pag

class Paginator:
    """ Classe para obter model paginado. """
    
    OBJ_PER_PAGE = 3

    def __init__(self, model, request):
        paginator = pag.Paginator(model, self.OBJ_PER_PAGE)
        self.page = paginator.get_page(request.GET.get('page'))

    def getPages(self):
        return self.page
