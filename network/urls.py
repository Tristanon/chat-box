
from django.urls import path

from . import views

urlpatterns = [
    # create path for index 
    path("", views.index, name="index"),

    # create path for login, logout, registration
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    # create path for post
    path("post", views.post, name="post"),

    # create path for profile
    path("profile/<int:user_id>", views.profile, name="profile"),

    # create path for follow, unfollow
    path("follow", views.follow, name="follow"),
    path("unfollow", views.unfollow, name="unfollow"),
    path("following", views.following, name="following"),

    # Edit path
    path("edit/<int:post_id>", views.edit, name="edit"),

    # add Like and remove Like
    path("add_like/<int:post_id>", views.add_like, name="add_like"),
    path("remove_like/<int:post_id>", views.remove_like, name="remove_like"),
]
