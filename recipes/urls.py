from django.urls import path

from django.http import HttpResponse

from recipes.views import *

urlpatterns = [
    path('home/', home),
    path('sobre/', sobre),
    path('contato/', contato)
]