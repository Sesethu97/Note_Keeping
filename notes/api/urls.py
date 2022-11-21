from django.urls import path
from .views import (
    HomeAPIView,
    RegisterAPIView,
    SettingsAPIView,
    AddAPIView,
    DetailAPIView,
    UpdateAPIView
)
from . import views



urlpatterns = [
    path("homes/", HomeAPIView.as_view(), name="home"),
    path("registers/", RegisterAPIView.as_view(), name="auth_register"),
    path("setting/", SettingsAPIView.as_view(), name="auth_settings"),
    path("adds/", AddAPIView.as_view(), name="auth_add"),
    path("detail/<int:id>/", DetailAPIView.as_view(), name="auth_details"),
    path("updates/<int:id>/", UpdateAPIView.as_view(), name="auth_update"),

]
