from django.urls import path
from .views import *

app_name = 'mypages'

urlpatterns = [
    path('recipes/<int:pk>/', RecipeSaveView.as_view()),
]
