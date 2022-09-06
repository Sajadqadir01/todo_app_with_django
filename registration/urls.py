from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns=[
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('accounts/profile/', views.profile),
    path('sign_up', views.RegisterPage.as_view(), name='register')
]