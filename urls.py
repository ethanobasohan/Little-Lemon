from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'reservations', views.ReservationViewSet)
router.register(r'inventory', views.InventoryItemViewSet)
router.register(r'menu', views.MenuItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
