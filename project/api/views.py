from rest_framework import viewsets

from project.api.models import Picture, Profile, Like
from project.api.serializers import PictureSerializer, ProfileSerializer
from rest_framework.response import Response
from project.api.permissions import IsOwnerOrReadOnly
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class PictureViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows pictures to be viewed or edited
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    queryset = Picture.objects.all().select_related('author')
    serializer_class = PictureSerializer


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated, ])
def like_picture(request, pk):
    """
    likes a picture with a certain id
    :param request: http request object
    :param pk: id of the picture that will be liked
    :return: 204 status for successful unlike,
             status 201 + new picture data for successful like.
             404 if picture does not exist.
    """

    picture = get_object_or_404(Picture, pk=pk)
    if Like.objects.filter(person=request.user, picture=picture).count() > 0:
        """
        User has already liked this picture. We un-like the picture.
        """
        Like.objects.filter(person=request.user, picture=picture).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        picture = request.user.like_picture(picture)
        serializer = PictureSerializer(picture, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
