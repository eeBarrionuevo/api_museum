from django.urls import path, include
from .views import ArtistViewSet
from rest_framework import routers


router = routers.DefaultRouter()

router.register('artists', ArtistViewSet)


urlpatterns = [
  path('', include(router.urls))  
]




