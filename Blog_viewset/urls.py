from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', include('api.urls')),


]
