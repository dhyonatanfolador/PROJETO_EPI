from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
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
    email = None
    password = None

    if request.method == "POST":
        # Requisição JSON (fetch)
        if request.content_type == "application/json":
            try:
                import json
                data = json.loads(request.body)
                email = data.get("email")
                password = data.get("password")
            except json.JSONDecodeError:
                return JsonResponse({"status": "error", "message": "JSON inválido"})

        # Requisição de formulário HTML
        elif request.content_type == "application/x-www-form-urlencoded":
            email = request.POST.get("email")
            password = request.POST.get("password")

        # Autenticação
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)

            # Resposta para requisição AJAX ou JSON
            if request.headers.get("x-requested-with") == "XMLHttpRequest" or request.content_type == "application/json":
                return JsonResponse({"status": "success", "message": "Login ok"})

            # Redirecionamento padrão
            return redirect("inicio")

        else:
            error = "Usuário ou senha incorretos."

            # Resposta para requisição AJAX ou JSON
            if request.headers.get("x-requested-with") == "XMLHttpRequest" or request.content_type == "application/json":
                return JsonResponse({"status": "error", "message": error})

    # GET ou erro → renderiza template
    return render(request, "app_epi/pages/login.html", {"error": error})
