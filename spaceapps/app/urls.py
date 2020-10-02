from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("home", views.mainPage, name = "mainPage"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    #API ROUTES
    path("getPosts/<str:name>", views.getPosts, name="getPosts"),
    path("sendPost", views.sendPost, name="sendPost"),
    path("getCategories", views.getCategories, name="getCategories"),
    path("currentUser", views.currentUser, name="currentUser"),
    path("like/<int:post_id>", views.like, name="like"),
    path("profile/<int:user_id>/<str:type>", views.follow_users, name="follow_users"),
    path("follow/<int:user_id>", views.follow, name="follow"),
    path("getArticles", views.getArticles, name = "getArticles")


    
]