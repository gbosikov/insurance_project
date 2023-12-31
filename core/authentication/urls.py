from django.urls import path
from authentication import views
from django.contrib.auth import views as auth_views

from authentication.views import page_not_found

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('forgot-password/', views.forgot_password_view, name='forgot-password'),
]


handler404 = page_not_found
