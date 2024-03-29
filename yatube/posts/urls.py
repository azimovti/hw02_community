from . import views
from django.urls import path

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='main_post'),
    path('group/<slug:slug>/', views.group_posts, name='group_posts'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('posts/<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('posts/create/',views.post_create, name='post_create')


]
