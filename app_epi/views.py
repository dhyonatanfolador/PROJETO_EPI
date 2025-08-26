from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "app_epi/partial/index.html")

def inicio(request):
    return render(request, "app_epi/partial/inicio.html")

def sobre(request):
    return render(request, "app_epi/partial/sobre.html")
