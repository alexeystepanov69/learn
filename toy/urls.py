from django.urls import path, include
from rest_framework import routers
from toy.views import FloorViewSet

router = routers.DefaultRouter()
router.register('floor', FloorViewSet)

urlpatterns = [
    path('', include(router.urls))
]