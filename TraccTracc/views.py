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
        "album": contact
    })


def delete_album(request, pk):
    albums = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect(to='list_albums')

    return render(request, "albums/delete_albums.html",
                  {"album": album})


























    






def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'GET':
        form = NoteForm()
    return render(request, "contacts/contact_detail.html", {"contact": contact, "form":form})

def add_note(request, contact_pk):
    contact = get_object_or_404(Contact, pk=contact_pk)
    if request.method == 'POST':
        form = NoteForm(data=request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.contact = contact
            note.save()
            return redirect(to='contact_detail', pk=contact_pk)

    return render(request, "contacts/contact_detail.html", {"form": form})
    













