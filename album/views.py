from rest_framework.viewsets import ModelViewSet
from .models import Image, Tag, ImageTag
from .serializer import ImageSerializer, TagSerializer, ImageTagSerializer


class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ImageTagViewSet(ModelViewSet):
    queryset = ImageTag.objects.all()
    serializer_class = ImageTagSerializer
