from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from recipes.models import Recipe
from recipes.serializers import RecipeSerializer
from theme.models import Theme, ThemeType
from theme.serializers import ThemeSerializer, ThemeTypeSerializer

class ThemeListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        theme_types = ThemeType.objects.all()
        theme_types_serializer = ThemeTypeSerializer(theme_types, many=True)
        theme_list = Theme.objects.all()
        theme_list_serializer = ThemeSerializer(theme_list, many=True)
        return Response({"Theme Types": theme_types_serializer.data, "Themes": theme_list_serializer.data},
                        status=status.HTTP_200_OK)


class ThemeDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        theme = get_object_or_404(Theme, id=id)
        serializer = ThemeSerializer(theme)

        return Response({"theme": serializer.data}, status=status.HTTP_200_OK)

