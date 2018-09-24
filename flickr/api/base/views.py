from django.shortcuts import render, get_list_or_404, get_object_or_404

# Create your views here.
from rest_framework import viewsets

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from FlickrApp.permissions import IsOwner
from flickr.api.base.serializers import FlickrGroupSerializer, FlickrGroupDetailSerializer, FlickrPhotoSerializer
from flickr.models import FlickrGroup, FlickrPhoto


class FlickrGroupViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated, IsOwner,)
    queryset = FlickrGroup.objects.all()

    def list(self, request, *args, **kwargs):
        user = self.request.user
        flickr_groups = self.get_queryset().filter(owner=user)
        serializer = FlickrGroupSerializer(flickr_groups, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        flickr_group = self.get_object()
        serializier = FlickrGroupDetailSerializer(flickr_group, context={'request': self.request})
        return Response(serializier.data)


class FlickrPhotoViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated, IsOwner,)
    queryset = FlickrPhoto.objects.all()
    serializer_class = FlickrPhotoSerializer

    def list(self, request, *args, **kwargs):
        flick_group_id = self.request.query_params.get('group')
        flickr_group = get_object_or_404(FlickrGroup, id=flick_group_id)
        self.check_object_permissions(self.request, flickr_group)
        serializer = FlickrGroupDetailSerializer(flickr_group, context={'request': self.request})
        return Response(serializer.data)
