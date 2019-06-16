import json

from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token

from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


from mmcPlanAPI.serializers.profile import CustomerSerializer, Customer, EmployeeSerializer, Employee

GROUP_OBJECTS = {
    'employee': {
        'model': Employee,
        'serializer': EmployeeSerializer
    },
    'management': {
        'model': Employee,
        'serializer': EmployeeSerializer
    },
    'customer': {
        'model': Customer,
        'serializer': CustomerSerializer
    },
}


@api_view(['GET'])
def get_user_profile(request):
    call = request.GET.dict()
    user = Token.objects.get(key=call['userToken']).user
    query = GROUP_OBJECTS[call['group']]['model'].objects.get(id=user.id)
    serializer = GROUP_OBJECTS[call['group']]['serializer'](query, many=False)

    response = serializer.data if serializer is not None else None
    return JsonResponse(response)


@csrf_exempt
def change_user_profile(request):
    call = json.loads(request.body)

    user = Token.objects.get(key=call['userToken']).user

    query = GROUP_OBJECTS[call['group']]['model'].objects.get(id=user.id)

    try:
        GROUP_OBJECTS[call['group']]['model'].objects.update_or_create(**call['form'])
        return JsonResponse({
            'message': 'Reactie is geplaatst',
            'update': True
        })
    except Exception as e:
        return JsonResponse({
            'message': 'Je hebt al gereageerd of alle plekken zijn al bezet',
            'update': False})
