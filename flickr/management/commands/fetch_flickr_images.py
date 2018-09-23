from django.core.management.base import BaseCommand, CommandError
import requests

from flickr.models import FlickrGroup

KEY = "d0880d905bedbae00abf20023d6f5e6e"
SECRET = "7d2a56d63cfb07cf"

FLICKR_BASE_API = "https://api.flickr.com/services/rest/"

GET_PHOTOS_BY_GROUP_ID_METHOD = "flickr.groups.pools.getPhotos"

GET_PHOTO_INFO_METHOD = "flickr.photos.getInfo"


class Command(BaseCommand):
    help = 'Fetching photos from flickr given group_ids'

    def get_photos_by_group_id_params(self, group_id):
        return {
            "method": GET_PHOTOS_BY_GROUP_ID_METHOD,
            "api_key": KEY,
            "group_id": group_id,
            "format": "json",
            "nojsoncallback": 1,
            "per_page": 30
        }

    def get_photos_by_id_params(self, photo_id, secret):
        return {
            "method": GET_PHOTO_INFO_METHOD,
            "api_key": KEY,
            "photo_id": photo_id,
            "secret": secret,
            "format": "json",
            "nojsoncallback": 1
        }

    def handle(self, *args, **options):
        groups = FlickrGroup.objects.all()
        for group in groups:
            group_params = self.get_photos_by_group_id_params(group.flickr_id)
            res = requests.get(FLICKR_BASE_API, params=group_params)
            photos = res.json()['photos']['photo']
            for photo in photos:
                photos_params = self.get_photos_by_id_params(photo['id'], photo['secret'])
                res = requests.get(FLICKR_BASE_API, params=photos_params)
                res.json()['photo']
                import pdb; pdb.set_trace()


