from rest_framework import serializers

from .models import Recipe, Tag

class Tagserializer(serializers.ModelSerializer):
    class Meta():
        model = Tag
        fields = (
            'id',
            'name',
            'url',
        )