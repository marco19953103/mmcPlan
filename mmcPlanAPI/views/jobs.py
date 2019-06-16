import json

from rest_framework import viewsets
from rest_framework.authtoken.models import Token

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from mmcPlanAPI.serializers.jobs import JobSerializer, Job, JobApplicant
from jobs.models import Position


class JobViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer


@csrf_exempt
def apply_on_job(request):
    if request.GET:
        call = request.GET.dict()
        return JsonResponse({'Error': call})

    call = json.loads(request.body)
    user = Token.objects.get(key=call['userToken']).user
    job = Job.objects.get(pk=call['job'])
    position = Position.objects.get(description=call['position'])

    try:
        JobApplicant.objects.create(job=job, employee_id=user.id, position=position)
        return JsonResponse({
            'message': 'Reactie is geplaatst',
            'created': True
        })
    except Exception as e:
        return JsonResponse({
            'message': 'Je hebt al gereageerd of alle plekken zijn al bezet',
            'created': False})
