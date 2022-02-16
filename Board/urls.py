from django.urls import path, include
from . import views

urlpatterns=[
    path('',views.getSongList,name='Songs'),
    path('song_detail/<int:pk>/', views.getSongDetail, name='song_detail')
]