import json

from rest_framework import serializers

from FlickrApp.settings import REST_FRAMEWORK as app_settings

from flickr.models import FlickrGroup, FlickrPhoto, FlickrPhotoOwner, FlickrPhotoDate, FlickrPhotoLocation, \
    FlickrPhotoTag, FlickrPhotoNote, FlickrPhotoUrl


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
            'id', 'flickr_id', 'owner', 'secret', 'server', 'farm', 'ownername', 'title', 'ispublic', 'isfriend',
            'isfamily',
            'dateuploaded')


class FlickrGroupDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    photos = serializers.SerializerMethodField()

    def get_photos(self, obj):
        page = self.context.get('request').query_params.get('page', 1)
        page_size = app_settings.get('PAGE_SIZE')
        start = (int(page) - 1) * page_size
        end = start + page_size
        return FlickGroupPhotoSerializer(obj.flickr_photos.all()[start:end], many=True).data

    class Meta:
        model = FlickrGroup
        fields = ('flickr_id', 'name', 'owner', 'photos')


class FlickrPhotoOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlickrPhotoOwner
        fields = ('nsid', 'username', 'realname', 'location', 'iconserver', 'iconfarm', 'path_alias')


class FlickrPhotoDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlickrPhotoDate
        fields = ('posted', 'taken', 'takengranularity', 'takenunknown', 'lastupdate')


class FlickrPhotoLocationSerializer(serializers.ModelSerializer):
    neighbourhood = serializers.SerializerMethodField()
    locality = serializers.SerializerMethodField()
    county = serializers.SerializerMethodField()
    region = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()

    def get_neighbourhood(self, obj):
        return json.loads(obj.neighbourhood)

    def get_locality(self, obj):
        return json.loads(obj.locality)

    def get_county(self, obj):
        return json.loads(obj.county)

    def get_region(self, obj):
        return json.loads(obj.region)

    def get_country(self, obj):
        return json.loads(obj.country)

    class Meta:
        model = FlickrPhotoLocation
        fields = ('latitude', 'longitude', 'accuracy', 'context',
                  'neighbourhood', 'locality', 'county',
                  'region', 'country', 'place_id', 'woeid'
                  )


class FlickrPhotoNoteSerializer(serializers.ModelSerializer):
    dimensions = serializers.SerializerMethodField()

    def get_dimensions(self, obj):
        return json.loads(obj.dimesions)

    class Meta:
        model = FlickrPhotoNote
        fields = ('flickr_id', 'photo_id', 'author', 'authorname',
                  'authorrealname', 'authorispro', 'authorisdeleted', 'dimensions', 'content')


class FlickrPhotoTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlickrPhotoTag
        fields = ('flickr_id', 'author', 'authorname', 'raw', 'content', 'machine_tag')


class FlickrPhotoUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlickrPhotoUrl
        fields = ('type', 'content')


class FlickrPhotoSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()
    visibility = serializers.SerializerMethodField()
    dates = serializers.SerializerMethodField()
    editability = serializers.SerializerMethodField()
    publiceditability = serializers.SerializerMethodField()
    usage = serializers.SerializerMethodField()
    notes = serializers.SerializerMethodField()
    people = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    urls = serializers.SerializerMethodField()
    geoperms = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()

    def get_owner(self, obj):
        return FlickrPhotoOwnerSerializer(obj.flickrphotoowner).data

    def get_visibility(self, obj):
        return {
            'ipublic': obj.ispublic,
            'isfriend': obj.isfriend,
            'isfriend': obj.isfriend
        }

    def get_dates(self, obj):
        return FlickrPhotoDateSerializer(obj.flickrphotodate).data

    def get_geoperms(self, obj):
        return json.loads(obj.geoperms)

    def get_location(self, obj):
        return FlickrPhotoLocationSerializer(obj.flickrphotolocation).data

    def get_editability(self, obj):
        return json.loads(obj.editability)

    def get_publiceditability(self, obj):
        return json.loads(obj.publiceditability)

    def get_usage(self, obj):
        return json.loads(obj.usage)

    def get_notes(self, obj):
        return FlickrPhotoNoteSerializer(obj.notes, many=True).data

    def get_people(self, obj):
        return json.loads(obj.people)

    def get_tags(self, obj):
        return FlickrPhotoTagSerializer(obj.tags, many=True).data

    def get_urls(self, obj):
        return FlickrPhotoUrlSerializer(obj.urls, many=True).data

    class Meta:
        model = FlickrPhoto
        fields = (
            'id', 'flickr_id', 'secret', 'server', 'farm', 'title', 'isfavorite',
            'license', 'safety_level', 'rotation', 'originalsecret', 'originalformat',
                                                                     'dateuploaded', 'owner', 'description',
            'visibility', 'dates', 'views', 'geoperms', 'location',
            'editability', 'publiceditability', 'usage', 'comments', 'notes', 'people', 'tags', 'urls', 'media'

        )
