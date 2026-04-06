from django.conf.urls import url, include
from rest_framework import routers
from project.api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'pictures', views.PictureViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'pictures/(?P<pk>[0-9]+)/like$', views.like_picture)
]
