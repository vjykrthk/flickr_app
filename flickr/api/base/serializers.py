from rest_framework import serializers

from FlickrApp.settings import REST_FRAMEWORK as app_settings

from flickr.models import FlickrGroup, FlickrPhoto

class FlickrGroupSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    count = serializers.SerializerMethodField()

    def get_count(self, obj):
        return obj.flickr_photos.count()

    class Meta:
        model = FlickrGroup
        fields = ('flickr_id', 'name', 'owner', 'count')


class FlickGroupPhotoSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()
    ownername = serializers.SerializerMethodField()

    def get_owner(self, obj):
        return obj.flickrphotoowner.nsid

    def get_ownername(self, obj):
        return obj.flickrphotoowner.realname

    class Meta:
        model = FlickrPhoto
        fields = (
            'flickr_id', 'owner', 'secret', 'server', 'farm', 'ownername', 'title', 'ispublic', 'isfriend', 'isfamily',
            'dateuploaded')


class FlickrGroupDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    photos = serializers.SerializerMethodField()

    def get_photos(self, obj):
        page = self.context.get('request').query_params.get('page', 1)
        page_size = app_settings.get('PAGE_SIZE')
        start = (page -1) * page_size
        return FlickGroupPhotoSerializer(obj.flickr_photos.all()[start:page_size], many=True).data

    class Meta:
        model = FlickrGroup
        fields = ('flickr_id', 'name', 'owner', 'photos')
