from rest_framework import serializers
from recipes.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):

    id = serializers.SerializerMethodField()
    steps = serializers.SerializerMethodField()

    def get_id(self, obj):
        return obj.external_id

    def get_steps(self, obj):
        return obj.steps

    class Meta:
        model = Recipe
        fields = ('id', 'ingredients', 'name', 'steps')
