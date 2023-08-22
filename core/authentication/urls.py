from django.urls import path
from authentication import views


urlpatterns = [
    path('authentication/', views.login_view, name='login')
]
