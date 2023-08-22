from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib.auth import login
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            authenticated_user = authenticate(username=request.POST['card-user'], password=request.POST['card-password'])
            if authenticated_user is not None:
                login(request, authenticated_user)
                return HttpResponseRedirect(reverse('authentication/login.html'))  # Replace 'success_page' with the actual URL name
        else:
            print(form)
            return render(request, 'authentication/login.html', {'login_form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'authentication/base.html', {'login_form': form})



