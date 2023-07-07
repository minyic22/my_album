from rest_framework.routers import SimpleRouter
from .views import UserViewSet, signup
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

simple_router = SimpleRouter()
simple_router.register('', UserViewSet, basename='user')

urlpatterns = [
                  path('signup/', signup, name='signup'),
                  path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
              ] + simple_router.urls

