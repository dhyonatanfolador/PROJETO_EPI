from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "app_epi/global/index.html")

def inicio(request):
    return render(request, "app_epi/pages/inicio.html")

def sobre(request):
    return render(request, "app_epi/pages/sobre.html")
