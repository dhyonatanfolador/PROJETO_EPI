from django.shortcuts import render


# Create your views here.
def Relatorio(request):
    return render(request, "app_relatorio/pages/relatorio.html")
