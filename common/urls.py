from django.urls import path

app_name = 'common'

urlpatterns = [
    path('register', RegisterAPIView.as_view(), name='register'),
]
