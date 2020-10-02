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