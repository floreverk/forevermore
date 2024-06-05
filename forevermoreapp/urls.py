from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('AeroplaneCemetery', views.AeroplaneCemetery),
    path('AbeeleAerodromeMilitaryCemetery', views.AbeeleAerodromeMilitaryCemetery),
    path('AdinkerkeMilitaryCemetery', views.AdinkerkeMilitaryCemetery),
    path('AncreBritishCemetery', views.AncreBritishCemetery),
]
