from django.urls import path, include
from .views import *

app_name = 'administrator'

urlpatterns = [
    path('', include('common.urls')),
    path('ambassadors', AmbassadorAPIView.as_view(), name='ambassadors'),
    path('products', ProductGenericAPIView.as_view(), name='products'),
    path('products/<str:pk>', ProductGenericAPIView.as_view(), name='products'),
]
