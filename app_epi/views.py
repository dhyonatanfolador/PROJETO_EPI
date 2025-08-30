from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse


# Create your views here.
def index(request):
    return render(request, "app_epi/global/index.html")


def logina(request):
    return render(request, "app_epi/pages/login.html")


def inicio(request):
    return render(request, "app_epi/pages/inicio.html")


def sobre(request):
    return render(request, "app_epi/pages/sobre.html")


def Colaboradores(request):
    return HttpResponse("Método não suportado.")


def Equipamentos(request):
    return render(request, "app_epi/pages/sobre.html")


def Usuarios(request):
    return render(request, "app_epi/pages/sobre.html")


def Emprestimos(request):
    return render(request, "app_epi/pages/sobre.html")


def logins(request):
    error = None

    if request.method == "POST":
        # Detecta se é JSON ou form normal
        if request.content_type == "application/json":
            try:
                data = json.loads(request.body)
            except json.JSONDecodeError:
                return JsonResponse({"status": "error", "message": "JSON inválido"})
            email = data.get("email")
            password = data.get("password")

        # Autenticação Django
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            if (
                request.headers.get("x-requested-with") == "XMLHttpRequest"
                or request.content_type == "application/json"
            ):
                return JsonResponse({"status": "success", "message": "Login ok"})

        else:
            error = "Usuário ou senha incorretos."

            # Para fetch → JSON
            if (
                request.headers.get("x-requested-with") == "XMLHttpRequest"
                or request.content_type == "application/json"
            ):
                return JsonResponse({"status": "error", "message": error})

    # Se GET ou erro → volta pro template de login
    return render(request, "app_epi/pages/login.html", {"error": error})
