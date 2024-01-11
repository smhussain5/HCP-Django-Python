from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Physician, Specialty

# Create your views here.


@login_required(login_url="login")
def index(request):
    specialties = Specialty.objects.all().order_by("name")
    physicians = Physician.objects.all().order_by("last_name")
    context = {}
    context["specialties"] = specialties
    context["physicians"] = physicians
    return render(request, 'base/index.html', context)


def login_user(request):
    specialties = Specialty.objects.all().order_by("name")
    context = {}
    context["specialties"] = specialties
    if request.method == "POST":
        username = request.POST['un_input']
        password = request.POST['pw_input']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Woo! You're logged in! 🎉")
            return redirect("/", context)
        else:
            messages.error(request, "Uh-oh! There was an error logging you in! Try again?")
            return render(request, 'base/login.html', context)
    else:
        return render(request, 'base/login.html', context)


def logout_user(request):
    specialties = Specialty.objects.all().order_by("name")
    context = {}
    context["specialties"] = specialties
    logout(request)
    return redirect("/", context)


def register_user(request):
    specialties = Specialty.objects.all().order_by("name")
    context = {}
    context["specialties"] = specialties
    return render(request, 'base/register.html', context)


@login_required(login_url="login")
def by_physician(request, pk):
    specialties = Specialty.objects.all().order_by("name")
    physician_record = Physician.objects.get(id=pk)
    context = {}
    context["physician"] = physician_record
    context["specialties"] = specialties
    return render(request, 'base/physician.html', context)


@login_required(login_url="login")
def by_specialty(request, pk):
    specialties = Specialty.objects.all().order_by("name")
    specialty = Specialty.objects.get(id=pk)
    physician_by_specialty = Physician.objects.filter(specialty=pk)
    context = {}
    context["physicians"] = physician_by_specialty
    context["specialties"] = specialties
    context["specialty"] = specialty
    return render(request, 'base/specialty.html', context)