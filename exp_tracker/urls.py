from django.urls import path, include
from . import views

urlpattern = [
    path('', views.home, name='home')
    path('accounts/register/', views.register, name='register'),
    path('account/', include('django.contrib.auth.urls')),
]