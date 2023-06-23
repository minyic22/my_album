from rest_framework.routers import SimpleRouter
from .views import UserViewSet

simple_router = SimpleRouter()
simple_router.register('', UserViewSet, basename='user')

urlpatterns = [] + simple_router.urls
