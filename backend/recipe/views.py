from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Tag, Recipe
from .serializers import TagSerializer, RecipeListSerializer

@api_view(['GET'])
def get_tags(request):
    tag_list = Tag.objects.all()
    serializer = TagSerializer(tag_list, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_recipes(request):
    recipe_list = Recipe.objects.all()
    serializer = RecipeListSerializer(recipe_list, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_recipes_by_page(request):
    page = int(request.GET.get('page'))
    records_per_page = 6
    start_index = (page - 1) * records_per_page
    end_index = page * records_per_page

    recipe_list = Recipe.objects.all()[start_index:end_index]
    serializer = RecipeListSerializer(recipe_list, many=True)
    return Response(serializer.data)