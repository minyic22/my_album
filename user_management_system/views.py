import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from .serializer import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@csrf_exempt
@require_http_methods(['POST'])
def signup(request):
    print(request.user)
    if request.method == 'POST':
        userDict = json.loads(request.body)
        print(userDict, type(userDict))
        serializer = UserSerializer(data=userDict)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'User created successfully'}, status=201)
        else:
            return JsonResponse({'message': serializer.errors}, status=400)


