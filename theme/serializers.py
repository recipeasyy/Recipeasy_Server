from rest_framework import serializers

from theme.models import Theme, ThemeType


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ["id", "title", "description", "recipe_count", "duration", "tips", "theme_type"]


class ThemeTypeSerializer(serializers.ModelSerializer):
    themes = ThemeSerializer(many=True)

    class Meta:
        model = ThemeType
        fields = ["id", "title", "themes"]




