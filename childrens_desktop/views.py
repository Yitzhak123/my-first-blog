import  json
from django.apps import apps
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

@login_required
def load_user_manager_page(request):
    manager = DesktopUserManager.objects.get(username=request.user.username)
    users = DesktopUser.objects.filter(group_id=manager.pk)
    return render(request, 'childrens_desktop/load_user_manager_page.html',
                  {'manager': manager, 'users': users, 'movies': manager.movies.all(),
                   'games': manager.games.all()})

def add_new_user_manager(request):
    if(request.method == "POST"):
        form = DesktopUserManagerForm(request.POST)
        if (form.is_valid()):
            desktop_user_manager = form.save(commit=False)
            desktop_user_manager.add_user_manager()
            return redirect('login')
    else:
        form = DesktopUserManagerForm()
    return render(request, 'childrens_desktop/add_new_user_manager.html',
                  {'form': form})


@login_required
def user_detail(request, pk):
    user = get_object_or_404(DesktopUser, pk=pk)
    return render(request, 'childrens_desktop/user_detail.html', {'user': user})


@login_required
def add_new_user(request):
    manager = DesktopUserManager.objects.get(username=request.user.username)
    if (request.method == "POST"):
        form = DesktopUserForm(request.POST)
        if (form.is_valid()):
            desktop_user = form.save(commit=False)
            desktop_user.add_user(manager.pk)
            return redirect('load_user_manager_page')
    else:
        form = DesktopUserForm()
    return render(request, 'childrens_desktop/user_edit.html',
                  {'form': form, 'form_headline': "Add new user"})


@login_required
def user_edit(request, pk):
    user = get_object_or_404(DesktopUser, pk=pk)
    if request.method == "POST":
        form = DesktopUserForm(request.POST, instance=user)
        if form.is_valid():
            post = form.save(commit=True)
            return redirect('load_user_manager_page')
    else:
        form = DesktopUserForm(instance=user)
    return render(request, 'childrens_desktop/user_edit.html',
                  {'form': form, 'form_headline': "Edit user details"})


@login_required
def remove_user(request, pk):
    user = get_object_or_404(DesktopUser, pk=pk)
    user.delete()
    return redirect('load_user_manager_page')


@login_required
def add_new_app(request, app_type):
    manager = DesktopUserManager.objects.get(username=request.user.username)
    if(request.method == "POST"):
        # The variable app_type also indicate the appropriate model's name
        form = get_form_by_model_name(app_type, request.POST)
        if(form.is_valid()):
            app = form.save(commit=True)
            app.save()
            manager.add_app(app_type, app)
            return redirect('load_user_manager_page')
    else:
        # The variable app_type also indicate the appropriate model's name
        form = get_form_by_model_name(app_type)
    return render(request, 'childrens_desktop/add_new_app.html',
                  {'form': form, 'app_type': app_type})


# This function is for internal use
# The function gets two variables model_name - indicate the model name,
# and data - in this variable will be other information that we want to pass
# to the form
def get_form_by_model_name(model_name, data=None):
    if model_name == "movie":
        return MovieForm(data)
    if model_name == "game":
        return GameForm(data)


@login_required
def app_detail(request, app_type, pk):
    app_model = apps.get_model('childrens_desktop', app_type)
    app = get_object_or_404(app_model, pk=pk)
    return render(request, 'childrens_desktop/'+app_type+'_detail.html', {app_type: app})


@login_required
def remove_app(request, app_type, pk):
    manager = DesktopUserManager.objects.get(username=request.user.username)
    app_model = apps.get_model('childrens_desktop', app_type)
    app = get_object_or_404(app_model, pk=pk)
    app.delete()
    return redirect('load_user_manager_page')