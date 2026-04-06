from django.db import models
from django.contrib.auth.models import User, AbstractUser


# TODO from django.core.files.storage import FileSystemStorage
# TODO fs = FileSystemStorage(location='/media/photos')


class Profile(AbstractUser):
    birthday = models.DateField(blank=True, null=True)
    bio = models.CharField(max_length=128, blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False)

    def like_picture(self, pic):
        Like.objects.create(person=self, picture=pic)
        return pic


class Picture(models.Model):
    title = models.CharField(max_length=32, blank=False)
    image = models.ImageField()  # TODO storage = fs
    description = models.TextField(default="", blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    author = models.OneToOneField(Profile, on_delete=models.CASCADE)
    likes = models.ManyToManyField(
        Profile,
        through='Like',
        through_fields=('picture', 'person'),
        related_name='likes')


class Like(models.Model):
    person = models.ForeignKey(Profile)
    picture = models.ForeignKey(Picture)
    timestamp = models.DateTimeField(auto_now_add=True)


class Status(models.Model):
    author = models.OneToOneField(Profile, on_delete=models.CASCADE)
    text = models.TextField(blank=False, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
