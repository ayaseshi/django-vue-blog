from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from drf_spectacular.utils import extend_schema

from .serializers import CredentialsSerializer

class LoginView(APIView):
    @extend_schema(
        request=CredentialsSerializer,
        tags=["User"]
    )
    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Incorrect login or password.'})

class RegisterView(APIView):
    @extend_schema(
        request=CredentialsSerializer,
        tags=["User"]
    )
    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')
    
        if User.objects.filter(username=username).exists():
            return Response({'error': 'User with the given username already exists.'})

        user = User.objects.create_user(username=username, password=password)

        if user is not None:
            token = Token.objects.create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'There was a problem during registration.'})