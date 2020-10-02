from django.shortcuts import render
from django.http import HttpResponse
import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("mainPage"))
    return render(request, "app/index.html")

def home(request):
    return render(request, "app/home.html")

@csrf_exempt
def login_view(request):
    
    if request.method == "POST":

        data = json.loads(request.body)

        username = data.get("username", "")
        password = data.get("password", "")

        user = authenticate(request, username=username,password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({"message": "Loged in"}, status = 201)  # I didn't return HttpResponseRedirect because fetch calls do not accept such returns
        else:
            return JsonResponse({"message": "Invalid username or Password"})

    else:
        pass


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["name"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        
        if password != confirmation:
            return JsonResponse({"message": "Password unmatches confirmation!"})

        # Attempt to create new user
        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
        except IntegrityError:
            return JsonResponse({"message": "Username/email/password already taken"})
        login(request, user)
        return HttpResponseRedirect(reverse("mainPage"))  # got to main page
    else:
        pass

def getPosts(request, name):
    if name == 'profile':
        posts = request.user.posts.all()
    elif name == 'following':  # followings of request.user
        followings = Follow.objects.filter(follower=request.user)
        posts = followings.posts.all()
    elif name == 'followers':
        followers = Follow.objects.filter(followee=request.user)
        posts = followers.posts.all()
    elif name == 'all':
        posts = Post.objects.all()
    else:
        category = Category.objects.get(name=name)
        posts = category.posts.all()

    return JsonResponse([post.serialize() for post in posts], safe=False)


@csrf_exempt
@login_required(login_url="/login")
def sendPost(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    data = json.loads(request.body)

    description = data['description']
    category_name = data['category']
    category = Category.objects.get(name=category_name)

    video = data['video']

    post = Post(owner=request.user, description=description, date_created=datetime.datetime.now(), category=category,
                video=video)

    post.save()

    return JsonResponse({"message": "Post Sent successfully"}, status=201)


def getCategories(request):
    categories = Category.objects.all()
    return JsonResponse([category.serialize() for category in categories], safe=False)


@login_required(login_url="/login")
def currentUser(request):
    return JsonResponse(request.user.serialize())


@login_required(login_url="/login")
@csrf_exempt
def like(request, post_id):
    """
        Like and unlike + sending in JSON Format the outcome:
        - is_liked to represent the state liked/unliked
        - like_count
    """

    if request.method != "PUT":
        return JsonResponse({"error": "PUT request required."}, status=400)

    post = Post.objects.get(pk=post_id)
    user = request.user
    try:
        Like.objects.get(owner=user, post=post).delete()
        return JsonResponse({"message": "Unliked successfully", "is_liked": False, "like_count": post.number_likes()},
                            safe=False)

    except Like.DoesNotExist:
        Like.objects.create(owner=user, post=post)
        return JsonResponse({"message": "Liked successfully", "is_liked": True, "like_count": post.number_likes()},
                            safe=False)


@login_required(login_url="/login")
@csrf_exempt
def follow(request, user_id):
    """
        return: JSON format bool is_following and int followers count
    """
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    try:
        user_target = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return JsonResponse({"error": "User Not found."}, status=400)
    Follow.objects.all()
    try:
        # Unfollow
        Follow.objects.get(following=user_target, follower=request.user).delete()
        return JsonResponse({"message": "Unfollowed successfully", "is_followed": False,
                             "followers_count": user_target.followers_count()}, safe=False)
    except Follow.DoesNotExist:
        # follow
        Follow.objects.create(follower=user_target, following=request.user)
        return JsonResponse(
            {"message": "followed successfully", "is_followed": True, "followers_count": user_target.followers_count()},
            safe=False)


@csrf_exempt
def follow_users(request, user_id, type):
    """
    type: can be either followees or followers
    This will return either a user's followees or followers
    """
    if request.method != "GET":
        return JsonResponse({"error": "GET request required."}, status=400)
    user = User.objects.get_object_or_404(pk=user_id)
    if type.lower == "followees":
        followees = user.followees.all()
        return JsonResponse({"followees": [followee.serialize() for followee in followees]}, status=200)

    elif type.lower == "followers":
        followers = user.followers.all()
        return JsonResponse({"followers": [follower.serialize() for follower in followers]}, status=200)

    return JsonResponse({"message": "Something wrong in the backend server happened!"}, status=400)


def getArticles(request):
    articles = Article.objects.all()
    return JsonResponse([article.serialize() for article in articles], safe = False)