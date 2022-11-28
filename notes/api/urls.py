from django.urls import path
from .views import (
    HomeAPIView,
    RegisterAPIView,
    SettingsAPIView,
    AddAPIView,
    DetailAPIView,
    UpdateAPIView,
    DeleteAPIView,
    ImportantsAPIView,
    ImportantListsAPIView,
    # LogInAPIView,
)
from . import views


urlpatterns = [
    path("homes/", HomeAPIView.as_view(), name="auth_homes"),
    path("registers/", RegisterAPIView.as_view(), name="auth_register"),
    path("setting/", SettingsAPIView.as_view(), name="auth_settings"),
    path("adds/", AddAPIView.as_view(), name="auth_add"),
    path("detail/<int:id>/", DetailAPIView.as_view(), name="auth_details"),
    path("updates/<int:id>/", UpdateAPIView.as_view(), name="auth_update"),
    path("deleted/<int:id>/", DeleteAPIView.as_view(), name="auth_delete"),
    path("importants/<int:id>/", ImportantsAPIView.as_view(), name="auth_importants"),
    path(
        "importantlists/",
        ImportantListsAPIView.as_view(),
        name="auth_importantLists",
    ),
    # path("logins/",LogInAPIView.as_view(),name="auth_login" ),

]
