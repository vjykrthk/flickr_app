from django.db import models


class FlickrGroup(models.Model):
    flickr_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    owner = models.ForeignKey('auth.User', related_name='flickr_groups', on_delete=models.CASCADE)


class FlickrPhoto(models.Model):
    flickr_id = models.CharField(max_length=200)
    secret = models.CharField(max_length=200, null=True, blank=True)
    server = models.CharField(max_length=100, null=True, blank=True)
    farm = models.IntegerField(null=True, blank=True)
    dateuploaded = models.DateTimeField(null=True, blank=True)
    isfavorite = models.NullBooleanField()
    license = models.IntegerField(null=True, blank=True)
    safety_level = models.IntegerField(null=True, blank=True)
    rotation = models.IntegerField(null=True, blank=True)
    originalsecret = models.CharField(max_length=200, null=True, blank=True)
    originalformat = models.CharField(max_length=50, null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    ispublic = models.NullBooleanField()
    isfriend = models.NullBooleanField()
    isfamily = models.NullBooleanField()
    views = models.IntegerField(null=True, blank=True)
    editability = models.TextField(null=True, blank=True, default='{}')
    publiceditability = models.TextField(null=True, blank=True, default='{}')
    usage = models.TextField(null=True, blank=True, default='{}')
    comments = models.IntegerField(null=True, blank=True)
    people = models.TextField(null=True, blank=True, default='{}')
    geoperms = models.TextField(null=True, blank=True, default='{}')
    media = models.CharField(max_length=200, null=True, blank=True)
    flickr_group = models.ForeignKey('FlickrGroup', related_name='flickr_photos', on_delete=models.CASCADE)

    @property
    def owner(self):
        return self.flickr_group.owner


class FlickrPhotoDate(models.Model):
    posted = models.DateTimeField(null=True, blank=True)
    taken = models.DateTimeField(null=True, blank=True)
    takengranularity = models.IntegerField(null=True, blank=True)
    takenunknown = models.IntegerField(null=True, blank=True)
    lastupdate = models.DateTimeField(null=True, blank=True)
    flickr_photo = models.OneToOneField('FlickrPhoto', on_delete=models.CASCADE)


class FlickrPhotoOwner(models.Model):
    nsid = models.CharField(max_length=200)
    username = models.CharField(max_length=200, null=True, blank=True)
    realname = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    iconserver = models.IntegerField(null=True, blank=True)
    iconfarm = models.IntegerField(null=True, blank=True)
    path_alias = models.CharField(max_length=200, null=True, blank=True)
    flickr_photo = models.OneToOneField('FlickrPhoto', on_delete=models.CASCADE)


class FlickrPhotoNote(models.Model):
    flickr_id = models.CharField(max_length=200)
    photo_id = models.CharField(max_length=100, null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    authorname = models.CharField(max_length=200, null=True, blank=True)
    authorrealname = models.CharField(max_length=200, null=True, blank=True)
    authorispro = models.NullBooleanField()
    authorisdeleted = models.NullBooleanField()
    dimesions = models.TextField(null=True, blank=True, default='{}')
    content = models.TextField(null=True, blank=True)
    flickr_photo = models.ForeignKey('FlickrPhoto', related_name='notes', on_delete=models.CASCADE)


class FlickrPhotoTag(models.Model):
    flickr_id = models.CharField(max_length=200)
    author = models.CharField(max_length=200, null=True, blank=True)
    authorname = models.CharField(max_length=200, null=True, blank=True)
    raw = models.CharField(max_length=200, null=True, blank=True)
    content = models.CharField(max_length=200, null=True, blank=True)
    machine_tag = models.IntegerField(null=True, blank=True)
    flickr_photos = models.ManyToManyField('FlickrPhoto', related_name='tags')


class FlickrPhotoLocation(models.Model):
    latitude = models.DecimalField(max_digits=50, decimal_places=30, null=True, blank=True)
    longitude = models.DecimalField(max_digits=50, decimal_places=30, null=True, blank=True)
    accuracy = models.IntegerField(null=True, blank=True)
    context = models.IntegerField(null=True, blank=True)
    neighbourhood = models.TextField(null=True, blank=True, default='{}')
    locality = models.TextField(null=True, blank=True, default='{}')
    county = models.TextField(null=True, blank=True, default='{}')
    region = models.TextField(null=True, blank=True, default='{}')
    country = models.TextField(null=True, blank=True, default='{}')
    place_id = models.CharField(max_length=200, null=True, blank=True)
    woeid = models.CharField(max_length=200, null=True, blank=True)
    flickr_photo = models.OneToOneField('FlickrPhoto', on_delete=models.CASCADE)


class FlickrPhotoUrl(models.Model):
    type = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    flickr_photo = models.ForeignKey('FlickrPhoto', related_name='urls', on_delete=models.CASCADE)
