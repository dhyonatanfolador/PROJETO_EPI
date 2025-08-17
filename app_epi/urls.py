from django.urls import path
from app_epi.views import home, about

urlpatterns = [
    path('', home),
    path('about/', about),
]