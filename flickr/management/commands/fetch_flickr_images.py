from datetime import datetime

from django.core.management.base import BaseCommand
import requests

from flickr.models import FlickrGroup, FlickrPhoto, FlickrPhotoDate, FlickrPhotoOwner, FlickrPhotoTag, \
    FlickrPhotoLocation, FlickrPhotoUrl

KEY = "d0880d905bedbae00abf20023d6f5e6e"
SECRET = "7d2a56d63cfb07cf"

FLICKR_BASE_API = "https://api.flickr.com/services/rest/"

GET_PHOTOS_BY_GROUP_ID_METHOD = "flickr.groups.pools.getPhotos"

GET_PHOTO_INFO_METHOD = "flickr.photos.getInfo"


def get_datetime_from_epoch(epoch_time_str):
    return datetime.fromtimestamp(int(epoch_time_str)) if epoch_time_str else None


def flickr_str_dt(str_dt):
    return datetime.strptime(str_dt, '%Y-%m-%d %H:%M:%S') if str_dt else None


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

    @staticmethod
    def get_photos_by_id_params(photo_id, secret):
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
                photo_detail = res.json()['photo']
                flickr_photo = FlickrPhoto(
                    flickr_id=photo_detail['id'],
                    secret=photo_detail.get('secret'),
                    server=photo_detail.get('server'),
                    farm=photo_detail.get('farm'),
                    dateuploaded=get_datetime_from_epoch(photo_detail['dateuploaded']),
                    isfavorite=bool(photo_detail['isfavorite']),
                    license=photo_detail.get('license'),
                    safety_level=photo_detail.get('safety_level'),
                    rotation=photo_detail.get('rotation'),
                    originalsecret=photo_detail.get('originalsecret'),
                    originalformat=photo_detail.get('originalformat'),
                    title=photo_detail.get('title', {}).get('_content'),
                    description=photo_detail.get('description', {}).get('_content'),
                    ispublic=bool(photo_detail.get('visibility', {}).get('ispublic')),
                    isfriend=bool(photo_detail.get('visibility', {}).get('isfriend')),
                    isfamily=bool(photo_detail.get('visibility', {}).get('isfamily')),
                    views=int(photo_detail.get('views')) if 'views' in photo_detail else None,
                    editability=photo_detail.get('editability', '{}'),
                    publiceditability=photo_detail.get('publiceditability', '{}'),
                    usage=photo_detail.get('usage', '{}'),
                    comments=photo_detail.get('comments', {}).get('_content'),
                    notes=photo_detail.get('notes', '{}'),
                    people=photo_detail.get('people', '{}'),
                    geoperms=photo_detail.get('geoperms', '{}'),
                    media=photo_detail.get('photo'),
                    flickr_group=group
                )

                flickr_photo.save()

                flickr_photo_date = FlickrPhotoDate(
                    posted=get_datetime_from_epoch(photo_detail.get('dates', {}).get('posted')),
                    taken=flickr_str_dt(photo_detail.get('dates', {}).get('taken')),
                    takengranularity=photo_detail.get('dates', {}).get('takengranularity'),
                    takenunknown=photo_detail.get('dates', {}).get('takenunknown'),
                    lastupdate=get_datetime_from_epoch(photo_detail.get('dates', {}).get('lastupdate')),
                    flickr_photo=flickr_photo
                )

                flickr_photo_date.save()

                flickr_photo_owner = FlickrPhotoOwner(
                    nsid=photo_detail.get('owner', {}).get('nsid'),
                    username=photo_detail.get('owner', {}).get('username'),
                    realname=photo_detail.get('owner', {}).get('realname'),
                    location=photo_detail.get('owner', {}).get('location'),
                    iconserver=photo_detail.get('owner', {}).get('iconserver'),
                    iconfarm=photo_detail.get('owner', {}).get('iconfarm'),
                    path_alias=photo_detail.get('owner', {}).get('path_alias'),
                    flickr_photo=flickr_photo
                )

                flickr_photo_owner.save()

                for tag in photo_detail['tags']['tag']:
                    flickr_photo_tag = FlickrPhotoTag(
                        flickr_id=tag.get('id'),
                        author=tag.get('author'),
                        authorname=tag.get('authorname'),
                        raw=tag.get('raw'),
                        content=tag.get('_content'),
                        machine_tag=tag.get('machine_tag')
                    )
                    flickr_photo_tag.save()
                    flickr_photo_tag.flickr_photos.add(flickr_photo)

                flickr_photo_location = FlickrPhotoLocation(
                    latitude=photo_detail.get('location', {}).get('latitude'),
                    longitude=photo_detail.get('location', {}).get('longitude'),
                    accuracy=photo_detail.get('location', {}).get('accuracy'),
                    context=photo_detail.get('location', {}).get('context'),
                    neighbourhood=photo_detail.get('location', {}).get('neighbourhood'),
                    locality=photo_detail.get('location', {}).get('locality', '{}'),
                    county=photo_detail.get('location', {}).get('county', '{}'),
                    region=photo_detail.get('location', {}).get('region', '{}'),
                    country=photo_detail.get('location', {}).get('country', '{}'),
                    place_id=photo_detail.get('location', {}).get('place_id'),
                    woeid=photo_detail.get('location', {}).get('woeid'),
                    flickr_photo=flickr_photo
                )
                flickr_photo_location.save()

                for url in photo_detail['urls']['url']:
                    flickr_photo_url = FlickrPhotoUrl(
                        type=url.get('type'),
                        content=url.get('_content'),
                        flickr_photo=flickr_photo
                    )
                    flickr_photo_url.save()
