from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("physician/<int:pk>", views.by_physician, name="physician"),
    path("specialty/<int:pk>", views.by_specialty, name="specialty"),
    path("add_physician", views.add_physician, name="add_physician"),
    path("physician/<int:pk>/edit_physician", views.edit_physician, name="edit_physician"),
    path("physician/<int:pk>/delete_physician", views.delete_physician, name="delete_physician"),
    path("auth/login", views.login_user, name="login"),  # AUTHENTICATION
    path("auth/logout", views.logout_user, name="logout"),
    path("auth/register", views.register_user, name="register")
]
