from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
# from rest_framework.authtoken import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("notes.urls", namespace="notes")),
    path('api/logins/', obtain_jwt_token),
    # path('api/logins/', views.obtain_auth_token)

]
