from rest_framework import viewsets

from recipes.models import Recipe
from recipes.serializers import RecipeSerializer


class RecipeViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    lookup_field = 'external_id'
