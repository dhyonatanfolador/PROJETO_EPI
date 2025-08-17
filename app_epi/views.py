from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "app_epi/partial/index.html")

def home(request):
    return render(request, "app_epi/partial/home.html")

def about(request):
    return render(request, "app_epi/partial/about.html")
