from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token

from django.http import JsonResponse
from django.contrib.auth.models import User


from mmcPlanAPI.serializers.profile import CustomerSerializer, Customer, EmployeeSerializer, Employee


@api_view(['GET'])
def get_user_profile(request):
    call = request.GET.dict()
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
    return JsonResponse(response)
