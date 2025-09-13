from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

# Create your views here.
def logina(request):
    return render(request, "app_account/pages/login.html")


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
            return redirect("home")

        else:
            error = "Usuário ou senha incorretos."

            # Resposta para requisição AJAX ou JSON
            if request.headers.get("x-requested-with") == "XMLHttpRequest" or request.content_type == "application/json":
                return JsonResponse({"status": "error", "message": error})

    # GET ou erro → renderiza template
    return render(request, "app_accont/pages/login.html", {"error": error})
