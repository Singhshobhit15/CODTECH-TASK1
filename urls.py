from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.home, name='home'),
    # path('c_Post', views.c_Post, name='c_post'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('send_friend_request/<int:user_id>/', views.send_friend_request, name='send_friend_request'),
    path('create_post/', views.create_post, name='create_post'),
    path('favicon.ico', RedirectView.as_view(url='/static/images/favicon.ico')),
]

