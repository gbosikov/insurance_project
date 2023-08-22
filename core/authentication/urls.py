from django.urls import path
from authentication import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('authentication/', views.login_view, name='login'),
]
