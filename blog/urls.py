from django.urls import path
from django.contrib.auth import views as auth_views

from blog.views import about, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from users.views import register, profile

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
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
