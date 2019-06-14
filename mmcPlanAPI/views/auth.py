from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


@csrf_exempt
def authenticate_user(request):
    """
    :param request:
    :return:
    """
    call = json.loads(request.body)
    user = User.objects.filter(email=call['username'])
    if len(user) == 1:
        call['username'] = user[0].username

    if authenticate(username=call['username'], password=call['password']) is not None:
        user = User.objects.get(username=call['username'])
        token, create = Token.objects.get_or_create(user=user)
        response = {
            'userToken': token.key,
            'group': user.groups.first().name
        }
        return JsonResponse(response)

    # auth failed return error
    return JsonResponse({'error': call})
