from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

# Create Routing Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('postapi', PostViewSet,
                basename='post')

urlpatterns = [
    path('', include(router.urls)),
]
