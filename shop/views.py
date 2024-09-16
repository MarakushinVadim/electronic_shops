from rest_framework import viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from .models import ShopNode, Product
from .serializers import ShopNodeSerializer, ProductSerializer


class ShopNodeViewSet(viewsets.ModelViewSet):
    queryset = ShopNode.objects.all()
    serializer_class = ShopNodeSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('country',)

    def update(self, request, *args, **kwargs):
        """Запрет обновления поля 'Задолженность перед поставщиком в API интерфейсе'"""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if 'debt' in request.data:
            request.data.pop('debt')
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def get_queryset(self):
        queryset = super().get_queryset()
        country = self.request.query_params.get('country')
        if country:
            queryset = queryset.filter(country=country)
        return queryset


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
