from rest_framework.routers import DefaultRouter
from .views import (ArtistAPIViewSet, AlbomAPIViewSet, SongAPIViewSET)
from django.urls import path, include

router = DefaultRouter()
router.register(r'songs', SongAPIViewSET)
router.register(r'artists', ArtistAPIViewSet)
router.register(r'alboms', AlbomAPIViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]