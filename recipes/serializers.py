from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import *


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['video', 'title', 'description',
                  'difficulty', 'time_taken', 'save_count', 'theme']
