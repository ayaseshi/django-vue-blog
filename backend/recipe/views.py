from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import Tag, Recipe
from .serializers import TagSerializer, RecipeSerializer

@extend_schema(tags=["Tag"])
class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

@extend_schema(tags=["Recipe"])
class RecipeViewSet(ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipePaginationView(APIView):
    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='page',
                required=True,
                type=int,
            ),
        ],
        tags=["Recipe"]
    )
    def get(self, request, *args, **kwargs):
        page = int(request.GET.get('page'))
        records_per_page = 6
        start_index = (page - 1) * records_per_page
        end_index = page * records_per_page

        recipe_list = Recipe.objects.all()[start_index:end_index]
        serializer = RecipeSerializer(recipe_list, many=True)
        return Response(serializer.data)