from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import DeskTopUserManager
from .forms import DeskTopUserManagerForm
from .models import DeskTopUserManagerLoginDetails
from .forms import DeskTopUserManagerLoginDetailsForm

# users_list_contains_name should be empty or contains one object
def is_name_password_valid(name, password, user):
    #if (user == None) or (user == null)
    if (not user):
        return False

    if(user.password == password):
        return True

    return False

@login_required
def login_page(request):
    if (request.method == "POST"):
        email = request.POST.get("email")
        password = request.POST.get("password")
        desktop_user_manager = DeskTopUserManager.objects.filter(email=email).first()

        if( is_name_password_valid(email, password, desktop_user_manager) ):
            return load_user_page(request, desktop_user_manager)

    form = DeskTopUserManagerLoginDetailsForm()
    return render(request, 'childrens_desktop/login_page.html', {'form': form})

def load_user_page(request, desktop_user_manager=None):
    return render(request, 'childrens_desktop/load_user_page.html',
                  {'desktop_user_manager': desktop_user_manager})

def add_new_user(request):
    if(request.method == "POST"):
        form = DeskTopUserManagerForm(request.POST)
        if (form.is_valid()):
            desktop_user_manager = form.save(commit=False)
            desktop_user_manager.add_user()
            return redirect('login_page')
    else:
        form = BookForm()
    return render(request, 'book_store/book_edit.html', {'form': form})


