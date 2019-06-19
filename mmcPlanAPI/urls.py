from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'jobs', views.JobViewSet)
router.register(r'agenda', views.AgendaViewSet, basename='agenda')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('auth/', views.authenticate_user),
    path('user-profile/', views.get_user_profile),
    path('job-applicants/', views.apply_on_job),
    path('add-agenda-item/', views.add_agenda_item),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]