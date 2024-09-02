from .models import Tipo

def tipo(request):
    tipos = Tipo.objects.all()
    
    context = {
        'Tipos': tipos
    }
    return context