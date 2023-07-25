from rest_framework import serializers

from .models import Recipe, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta():
        model = Tag
        fields = (
            'id',
            'name',
            'url',
        )

class RecipeListSerializer(serializers.ModelSerializer):
    class Meta():
        model = Recipe
        fields = (
            'user',
            'name',
            'ingredients',
            'url',
            'get_thumbnail',
            'option',
        )

class RecipeDetailedSerializer(serializers.ModelSerializer):
    pass