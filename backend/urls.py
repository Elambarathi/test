# ecommerce_backend/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet
from products.views import ProductDeleteView

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/products/<int:pk>/', ProductDeleteView.as_view(), name='product-delete'),
    
]
