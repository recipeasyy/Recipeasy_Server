from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.status import *
from rest_framework.response import Response

from .serializers import *
from .models import *


# Create your views here.


class RecipeListView(APIView):
    def get(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response({'message': '레시피 목록 조회 성공', 'data': serializer.data}, status=HTTP_200_OK)


class RecipeDetailView(APIView):
    def get(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        serializer = RecipeDetailSerializer(recipe)
        return Response({'message': '레시피 상세 조회 성공', 'data': serializer.data}, status=HTTP_200_OK)
