from django.urls import path
from django.contrib.auth import views as auth_views

from blog.views import home, about
from users.views import register, profile

urlpatterns = [
    path('', home, name='blog-home'),
    path('about/', about, name='blog-about'),
    path('login/',
         auth_views.LoginView.as_view(template_name='users/login.html'),
         name='login',
         ),
    path('logout/',
         auth_views.LogoutView.as_view(template_name='users/logout.html'),
         name='logout',
         ),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
]
