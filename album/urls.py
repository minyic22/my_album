from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ImageViewSet, TagViewSet, ImageTagViewSet

simple_router = SimpleRouter()
simple_router.register('image', ImageViewSet, basename='image')
simple_router.register('tag', TagViewSet, basename='tag')
simple_router.register('image-tag', ImageTagViewSet, basename='image-tag')

urlpatterns = [
              ] + simple_router.urls
