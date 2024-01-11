from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_user, name="login"),
    path("logout", views.logout_user, name="logout"),
    path("register", views.register_user, name="register"),
    path("physician/<int:pk>", views.by_physician, name="physician"),
    path("specialty/<int:pk>", views.by_specialty, name="specialty"),
]
