from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token

from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from mmcPlanAPI.serializers.jobs import JobSerializer, Job
from mmcPlanAPI.serializers.profile import CustomerSerializer, Customer, EmployeeSerializer, Employee


class JobViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer


@api_view(['GET', 'POST'])
def get_user_profile(request):
    call = request.data
    user = Token.objects.get(key=call['userToken']).user
    query = User.objects.get(id=user.id)
    serializer = None

    if call['group'] == 'employee':
        query = Employee.objects.get(id=user.id)
        serializer = EmployeeSerializer(query, many=False)

    if call['group'] == 'customer':
        query = Customer.objects.get(id=user.id)
        serializer = CustomerSerializer(query, many=False)

    response = serializer.data if serializer is not None else None
    print(response)
    return JsonResponse(response)


@api_view(['GET', 'POST'])
def authenticate_user(request):
    """
    :param request:
    :return:
    """
    call = request.data
    user = User.objects.filter(email=call['username'])
    if len(user) == 1:
        call['username'] = user[0].username

    if authenticate(**call) is not None:
        user = User.objects.get(username=call['username'])
        token, create = Token.objects.get_or_create(user=user)
        response = {
            'userToken': token.key,
            'group': user.groups.first().name
        }
        print(response)
        return JsonResponse(response)

    # auth failed return error
    return JsonResponse({'error': True})

