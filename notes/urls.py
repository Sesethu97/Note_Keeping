from django.urls import path
from . import views
import django.contrib.auth.views as auth_views

app_name = "notes"

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="notes/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="notes/logout.html"),
        name="logout",
    ),
    path("home/", views.home, name="home"),
    path("update/<int:id>/", views.update, name="update"),
    path("details/<int:id>/", views.note_details, name="details"),
    path("importantId/<int:id>/", views.important, name="important_id"),
    path("important_note/", views.important_note, name="important_note"),

    path("add/", views.add, name="add"),
    path("register/", views.register, name="register"),
    path("settings/", views.settings, name="settings"),
    path("delete/<int:id>/", views.delete, name="delete"),
]
