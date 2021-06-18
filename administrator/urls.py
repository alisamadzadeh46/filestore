
from django.urls import path, include

app_name = 'administrator'

urlpatterns = [
    path('', include('common.urls')),
]
