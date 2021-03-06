from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path("delete/<str:pk>", views.delete, name="delete"),
    path("", views.login, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout, name="logout")
]