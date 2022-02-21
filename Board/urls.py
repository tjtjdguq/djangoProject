from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('',views.getSongList,name='Songs'),
    path('song_detail/<int:rank>/', views.getSongDetail, name='song_detail'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name="Board/registration/login.html"), name="login"),
    path('accounts/logout',auth_views.LogoutView.as_view(),name='logout'),
    path('accounts/signup',views.signup,name='signup'),
    path('<int:rank>/lyric_insert',views.insertLyric,name='insert_lyric'),
]