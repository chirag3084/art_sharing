from rest_framework import serializers

from project.api.models import Profile, Picture, Status


class PictureSerializer(serializers.HyperlinkedModelSerializer):
    likes = serializers.SerializerMethodField()
    author = serializers.PrimaryKeyRelatedField(read_only=True,
                                                default=serializers.CurrentUserDefault())

    class Meta:
        model = Picture
        fields = ('id',
                  'title',
                  'image',
                  'description',
                  'upload_date',
                  'last_modified',
                  'author',
                  'url',
                  'likes')

    def get_likes(self, obj: Picture) -> int:
        """
        Returns the amount of likes this Picture has received.
        :param obj: Picture
        :return: int
        """
        return obj.likes.count()


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(min_length=8, trim_whitespace=True, write_only=True)

    class Meta:
        model = Profile
        fields = ('id',
                  'url',
                  'username',
                  'email',
                  'password',
                  'groups',
                  'birthday',
                  'bio',
                  'likes',
                  'followers')

    def create(self, validated_data):
        user = Profile.objects.create_user(validated_data['username'], validated_data['email'],
                                           password=validated_data['password'])
        return user

    def update(self, instance, validated_data):
        # TODO
        # user = Profile.objects.filter(id=instance.id).update()

        user = super().update(instance, validated_data)
        user.set_password(validated_data['password'])
        return user


class StatusSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = Status
        fields = ('id',
                  'author',
                  'text',
                  'date_created')
