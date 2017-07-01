"""warsztaty URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from album.views import HomeView, AddPhotoView, ListPhotoView, FavPhotoView
from warsztaty import settings
from album.views import UnFavPhotoView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^add_photo', AddPhotoView.as_view(), name="add_photo"),
    url(r'^list_photos', ListPhotoView.as_view(), name="list_photos"),
    url(r'^fav_photo/(?P<photo_id>(\d+))', FavPhotoView.as_view(), name="fav_photo"),
    url(r'^unfav_photo/(?P<photo_id>(\d+))', UnFavPhotoView.as_view(), name="unfav_photo"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
