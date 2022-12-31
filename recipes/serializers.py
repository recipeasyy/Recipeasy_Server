from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import *


class RequiredIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequiredIngredient
        fields = ['name', 'quantity', 'substitute', 'emoji']


class RequiredIngredientSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequiredIngredient
        fields = ['name']


class AdditionalIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalIngredient
        fields = ['name', 'quantity', 'substitute', 'emoji']


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ['name']


class RecipeSequenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeSequence
        fields = ['order', 'short_desc', 'long_desc', 'image']


class RecipeSerializer(serializers.ModelSerializer):
    required_ingredients = RequiredIngredientSimpleSerializer(
        many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ['video', 'title', 'time_taken',
                  'save_count', 'required_ingredients', 'theme']


class RecipeDetailSerializer(serializers.ModelSerializer):
    required_ingredients = RequiredIngredientSerializer(
        many=True, read_only=True)
    additional_ingredients = AdditionalIngredientSerializer(
        many=True, read_only=True)
    equipments = EquipmentSerializer(many=True, read_only=True)
    recipe_sequences = RecipeSequenceSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ['title', 'description', 'difficulty', 'time_taken', 'save_count',
                  'required_ingredients', 'additional_ingredients', 'equipments', 'recipe_sequences']