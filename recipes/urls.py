from django.urls import path
from .views import *

app_name = 'recipes'

urlpatterns = [
    path('list/', RecipeListView.as_view()),
]
