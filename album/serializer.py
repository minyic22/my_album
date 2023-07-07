from rest_framework import serializers
from .models import Image, Tag, ImageTag


class ImageSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Image
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ImageTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageTag
        fields = '__all__'
