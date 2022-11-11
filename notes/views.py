from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect, HttpResponseRedirect

# Create your views here.

from .models import Note
from .forms import NoteCreationForm, NoteUpdateForm, AccountSettingsForm


def index(request):
    return render(request, "notes/index.html")


def home(request):
    context = {"notes": Note.objects.all()}
    return render(request, "notes/home.html", context)


def register(request):
    form = AccountSettingsForm()

    if request.method == "POST":
        form = AccountSettingsForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Account Created successfully")
            return redirect("notes:login")

    context = {"form": form}
    return render(request, "notes/register.html", context)


def add(request):
    notes = Note.objects.all()
    form = NoteCreationForm()

    if request.method == "POST":
        form = NoteCreationForm(request.POST)

        if form.is_valid():
            note_obj = form.save(commit=False)
            note_obj.author = request.user
            note_obj.save()

            return redirect("notes:home")

    context = {"notes": notes, "form": form}
    return render(request, "notes/add.html", context)


def settings(request):

    user = request.user

    form = AccountSettingsForm(instance=user)

    if request.method == "POST":
        user.username = request.POST["username"]
        user.first_name = request.POST["first_name"]
        user.last_name = request.POST["last_name"]

        user.save()

        messages.success(request, "Account Updated Successfully")

        return redirect("notes:settings")
    context = {"form": form, "user": user}
    return render(request, "notes/setting.html", context)


def logout(request):
    return render(request, "notes/logout.html")


def note_details(request, id):
    notes = Note.objects.get(id=id)
    context = {'notes': notes}
    return render(request, "notes/note_details.html", context)




def important(request, id):
    note_important  = get_object_or_404(Note, id=id)
    if note_important.importance.filter(id=request.user.id).exists():
        note_important.importance.remove(request.user)
    else:
        note_important.importance.add(request.user)
    return HttpResponseRedirect(post.get_absolute_url())

    

    
def update(request, id):
    note_to_update = Note.objects.get(id=id)
    form = NoteUpdateForm(instance=note_to_update)

    if request.method == "POST":
        form = NoteUpdateForm(request.POST)

        if form.is_valid():
            note_to_update.title = form.cleaned_data["title"]
            note_to_update.description = form.cleaned_data["description"]

            note_to_update.save()

            return redirect("notes:home")

    context = {"note": note_to_update, "form": form}
    return render(request, "notes/update.html", context)


def delete(request, id):
    note_to_delete = Note.objects.get(id=id)

    note_to_delete.delete()

    return redirect("notes:home")
