from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Physician, Specialty
from .forms import PhysicianForm

# Create your views here.


@login_required(login_url="login")
def index(request):
    search = request.GET.get('search')
    if search is not None:
        physicians = Physician.objects.filter(Q(first_name__icontains=search) |
                                              Q(last_name__icontains=search) |
                                              Q(us_city__icontains=search) |
                                              Q(us_state__icontains=search)).order_by("last_name")
    else:
        physicians = Physician.objects.all().order_by("last_name")
    specialties = Specialty.objects.all().order_by("name")
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


@login_required(login_url="login")
def logout_user(request):
    specialties = Specialty.objects.all().order_by("name")
    context = {}
    context["specialties"] = specialties
    logout(request)
    return redirect("/", context)


def register_user(request):
    form = UserCreationForm()
    specialties = Specialty.objects.all().order_by("name")
    context = {}
    context["specialties"] = specialties
    context["form"] = form
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            messages.success(request, "Woo! You're registered! 🎉")
            return redirect("/", context)
        else:
            messages.error(request, "Uh-oh! There was an error with registration! Try again?")
            return render(request, 'base/register.html', context)
    return render(request, 'base/register.html', context)


@login_required(login_url="login")
@permission_required("base.can_add_physician")
def add_physician(request):
    form = PhysicianForm()
    specialties = Specialty.objects.all().order_by("name")
    context = {}
    context["specialties"] = specialties
    context["form"] = form
    if request.method == "POST":
        form = PhysicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/", context)
        else:
            messages.error(request, "Uh-oh! There was an error adding this physician! Try again?")
            return render(request, 'base/add_physician.html', context)
    return render(request, 'base/add_physician.html', context)


@login_required(login_url="login")
@permission_required("base.can_change_physician")
def edit_physician(request, pk):
    physician_record = Physician.objects.get(id=pk)
    form = PhysicianForm(instance=physician_record)
    specialties = Specialty.objects.all().order_by("name")
    context = {}
    context["physician"] = physician_record
    context["specialties"] = specialties
    context["form"] = form
    if request.method == "POST":
        form = PhysicianForm(request.POST, instance=physician_record)
        if form.is_valid():
            form.save()
            messages.success(request, "This physician has been updated!")
            return redirect("/", context)
        else:
            messages.error(request, "Uh-oh! There was an error updating this physician! Try again?")
            return render(request, 'base/edit_physician.html', context)
    return render(request, 'base/edit_physician.html', context)


@login_required(login_url="login")
@permission_required("base.can_delete_physician")
def delete_physician(request, pk):
    physician_record = Physician.objects.get(id=pk)
    specialties = Specialty.objects.all().order_by("name")
    context = {}
    context["physician"] = physician_record
    context["specialties"] = specialties
    if request.method == "POST":
        physician_record.delete()
        messages.success(request, "This physician has been deleted!")
        return redirect("/", context)
    return render(request, 'base/delete_physician.html', context)


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
    search = request.GET.get('search')
    if search is not None:
        physician_by_specialty = Physician.objects.filter(specialty=pk).filter(Q(first_name__icontains=search) |
                                                                          Q(last_name__icontains=search) |
                                                                          Q(us_city__icontains=search) |
                                                                          Q(us_state__icontains=search)).order_by("last_name")
    else:
        physician_by_specialty = Physician.objects.filter(specialty=pk).order_by("last_name")
    specialties = Specialty.objects.all().order_by("name")
    specialty = Specialty.objects.get(id=pk)
    context = {}
    context["physicians"] = physician_by_specialty
    context["specialties"] = specialties
    context["specialty"] = specialty
    return render(request, 'base/specialty.html', context)
