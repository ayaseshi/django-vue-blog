from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Tag
from .serializers import Tagserializer

@api_view(['GET'])
def get_tags(request):
    tag_list = Tag.objects.all()
    serializer = Tagserializer(tag_list, many=True)
    return Response(serializer.data)