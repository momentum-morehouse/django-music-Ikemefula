from django.shortcuts import render, redirect, get_object_or_404
from .models import Album
from .forms import AlbumForm



# Create your views here.
def list_albums(request):
    albums = Album.objects.all()
    return render(request, "albums/list_albums.html",
                  {"albums": albums})


def add_album(request):
    if request.method == 'GET':
        form = AlbumForm()
    else:
        form = AlbumForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            title = data.get('title')
            artist = data.get('artisrt')
            year_made = data.get('year_made')
            image_url = data.get('image_url')
            artist = Artist.objects.get_or_create(name=artist)
            album = Album.objects.create()

            form.save()
            return redirect(to='list_albums')

    return render(request, "albums/add_albums.html", {"form": form})
    

def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'GET':
        form = AlbumForm(instance=album)
    else:
        form = AlbumForm(data=request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')

    return render(request, "albums/edit_album.html", {
        "form": form,
        "album": album
    })


def delete_album(request, pk):
    albums = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect(to='list_albums')

    return render(request, "albums/delete_albums.html",
                  {"album": album})