from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from FlickrApp.permissions import IsOwner
from flickr.api.base.serializers import FlickrGroupSerializer, FlickrGroupDetailSerializer
from flickr.models import FlickrGroup


@api_view(['GET'])
def api_root(request, format=None):
    return Response({})


class FlickrGroupViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FlickrGroupSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def get_queryset(self):
        user = self.request.user
        return FlickrGroup.objects.filter(owner=user)

    def retrieve(self, request, *args, **kwargs):
        flickr_group = self.get_object()
        serializier = FlickrGroupDetailSerializer(flickr_group, context={'request': self.request})
        return Response(serializier.data)
