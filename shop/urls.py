from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .apps import ShopConfig
from .views import ShopNodeViewSet, ProductViewSet

app_name = ShopConfig.name

router = DefaultRouter()
router.register(r'nodes', ShopNodeViewSet, basename='nodes')
router.register(r'product', ProductViewSet, basename='product')

urlpatterns = [

    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
] + router.urls
