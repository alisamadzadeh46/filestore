from django.urls import path, include

from .views import ProductFrontendAPIView, ProductBackendAPIView, LinkAPIView, StatsAPIView, RankingsAPIView

app_name = 'ambassador'

urlpatterns = [
    path('', include('common.urls')),
    path('products/frontend', ProductFrontendAPIView.as_view(), name='product_frontend'),
    path('products/backend', ProductBackendAPIView.as_view(), name='product_backend'),
    path('links', LinkAPIView.as_view(), name='links'),
    path('stats', StatsAPIView.as_view(), name='stats'),
    path('rankings', RankingsAPIView.as_view(), name='rankings'),
]
