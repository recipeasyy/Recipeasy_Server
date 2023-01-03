from django.urls import path

from theme.views import ThemeListView, ThemeDetailView

urlpatterns = [
    path('', ThemeListView.as_view(), name="theme_list"),
    path('<int:id>', ThemeDetailView.as_view(), name="theme_detail")
]