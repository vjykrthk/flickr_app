from django.core.management.base import BaseCommand, CommandError

KEY = "d0880d905bedbae00abf20023d6f5e6e"
SECRET = "7d2a56d63cfb07cf"

group_ids = ["51035612836@N01", "2464395@N25", "95309787@N00", "41978077@N00"]

format = "json"

FLICKR_BASE_API = "https://api.flickr.com/services/rest/?method={method}&api_key={api_key}&group_id={group_id}&format={}&nojsoncallback=1"

GET_PHOTOS_BY_GROUP_ID_METHOD = "flickr.groups.pools.getPhotos"

GET_PHOTO_INFO_METHOD = "flickr.photos.getInfo"


class Command(BaseCommand):
    help = 'Fetching photos from flickr given group_ids'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        pass