from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("physician/<int:pk>", views.by_physician, name="physician"),
    path("specialty/<int:pk>", views.by_specialty, name="specialty"),

    path("add_physician", views.add_physician, name="add_physician"),

    path("login", views.login_user, name="login"),  # AUTHENTICATION
    path("logout", views.logout_user, name="logout"),
    path("register", views.register_user, name="register"),
]
