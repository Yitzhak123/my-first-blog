import  json
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import DesktopUserManager
from .forms import DesktopUserManagerForm
from .models import DesktopUser
from .forms import DesktopUserForm

@login_required
def load_user_manager_page(request):
    desktop_user_manager = DesktopUserManager.objects.get(username=request.user.username)
    jsonDec = json.JSONDecoder()
    users = jsonDec.decode(desktop_user_manager.desktop_users_group)
    return render(request, 'childrens_desktop/load_user_manager_page.html',
                  {'desktop_user_manager': desktop_user_manager, 'users': users})

def add_new_user_manager(request):
    if(request.method == "POST"):
        form = DesktopUserManagerForm(request.POST)
        if (form.is_valid()):
            desktop_user_manager = form.save(commit=False)
            desktop_user_manager.add_user_manager()
            return redirect('login')
    else:
        form = DesktopUserManagerForm()
    return render(request, 'childrens_desktop/add_new_user_manager.html', {'form': form})

@login_required
def add_new_user(request):
    manager = DesktopUserManager.objects.get(username=request.user.username)
    if (request.method == "POST"):
        form = DesktopUserForm(request.POST)
        if (form.is_valid()):
            desktop_user = form.save(commit=False)
            desktop_user.add_user()
            manager.add_user_to_group(desktop_user.username)
            return redirect('load_user_manager_page')
    else:
        form = DesktopUserForm()
    return render(request, 'childrens_desktop/add_new_user.html', {'form': form})

def user_detail(request, pk):
    user = get_object_or_404(DesktopUser, pk=pk)
    return render(request, 'childrens_desktop/user_detail.html', {'user': user})

# def users_list(request):
#     manager = DesktopUserManager.objects.get(username=request.user.username)
#     jsonDec = json.JSONDecoder()
#     users_group_list = jsonDec.decode(manager.desktop_users_group)
#
# 	return render(request, 'book_store/book_list.html', {'books' : books})

