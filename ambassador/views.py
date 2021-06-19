import math, random, time, string

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from common.authentication import JWTAuthentication
from common.serializers import UserSerializer
from .serializer import ProductSerializer, LinkSerializer
from core.models import Product, Link, Order, User
from django.core.cache import cache


class ProductFrontendAPIView(APIView):
    @method_decorator(cache_page(60 * 60 * 2, key_prefix='products_frontend'))
    def get(self, _):
        time.sleep(2)
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductBackendAPIView(APIView):
    pass


class LinkAPIView(APIView):
    pass


class StatsAPIView(APIView):
    pass


class RankingsAPIView(APIView):
    pass
