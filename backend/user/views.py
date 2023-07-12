from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    else:
        return Response({'error': 'Nieprawidłowe dane logowania.'})

@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Użytkownik o podanej nazwie już istnieje.'})

    user = User.objects.create_user(username=username, password=password)

    if user is not None:
        token = Token.objects.create(user=user)
        return Response({'token': token.key})
    else:
        return Response({'error': 'Wystąpił problem podczas rejestracji.'})