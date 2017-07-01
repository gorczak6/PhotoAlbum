from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView

from album.models import Photo


class HomeView(View):

    def get(self, request):
        return render(request, "home.html")


class AddPhotoView(CreateView):
    model = Photo
    fields = ['image']
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddPhotoView, self).form_valid(form)


class ListPhotoView(View):

    def get(self, request):

        photos = Photo.objects.all()
        ctx = {"photos": photos}

        return render(request, "list_photos.html", ctx)


class FavPhotoView(View):

    def get(self, request, photo_id):
        photo = Photo.objects.get(pk=photo_id)
        photo.fav.add(request.user.id)

        return redirect("/list_photos")

class UnFavPhotoView(View):

    def get(self, request, photo_id):
        photo = Photo.objects.get(pk=photo_id)
        photo.fav.remove(request.user.id)

        return redirect("/list_photos")
