from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('success')
        else:
            messages.error(request, 'Invalid credentials')
    else:
        form = AuthenticationForm()

    return render(request, 'authentication/base.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def success_view(request):
    return render(request, 'authentication/success.html', {'username': request.user.username})
