from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from flickr.api.base import views
from flickr.api.base.views import FlickrGroupViewSet

router = DefaultRouter()

router.register(r'flickr_groups', FlickrGroupViewSet, base_name='flickr_group')

urlpatterns = [
    url(r'^', include(router.urls))
]
