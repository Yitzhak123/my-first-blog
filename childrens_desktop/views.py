from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import DesktopUserManager
from .forms import DesktopUserManagerForm
from .models import DesktopUserManagerLoginDetails
from .forms import DesktopUserManagerLoginDetailsForm

@login_required
def load_user_page(request, desktop_user_manager=None):
    desktop_user_manager = DesktopUserManager.objects.get(username=request.user.username)
    return render(request, 'childrens_desktop/load_user_page.html',
                  {'desktop_user_manager': desktop_user_manager})

def add_new_user(request):
    if(request.method == "POST"):
        form = DesktopUserManagerForm(request.POST)
        if (form.is_valid()):
            desktop_user_manager = form.save(commit=False)
            desktop_user_manager.add_user()
            return redirect('login')
    else:
        form = DesktopUserManagerForm()
    return render(request, 'childrens_desktop/add_new_user.html', {'form': form})


