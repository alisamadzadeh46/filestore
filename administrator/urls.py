from django.urls import path, include
from .views import *

app_name = 'administrator'

urlpatterns = [
    path('', include('common.urls')),
    path('ambassadors', AmbassadorAPIView.as_view(), name='ambassadors'),
]
