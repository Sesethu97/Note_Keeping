from django.urls import path, include
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
    path("important/<int:id>/", views.importants, name="importants"),
    path("importantslist/", views.importantslist, name="importantslist"),

    path("add/", views.add, name="add"),
    path("register/", views.register, name="register"),
    path("settings/", views.settings, name="settings"),
    path("delete/<int:id>/", views.delete, name="delete"),


    # API routes
    path("api/", include("notes.api.urls"))
]
