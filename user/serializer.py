from rest_framework import serializers

from recipes.serializers import RecipeSerializer
from theme.serializers import ThemeSerializer
from user.models import User


class UserSerializer(serializers.ModelSerializer):

    saved_themes = ThemeSerializer(many=True)
    saved_recipes = RecipeSerializer(many=True)

    class Meta:
        model = User
        fields = ['nickname', 'saved_themes', 'saved_recipes']
