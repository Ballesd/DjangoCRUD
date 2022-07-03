from django.http import HttpResponse

#Función vista 
def saludo(request):
    return HttpResponse("Primera pagina ")