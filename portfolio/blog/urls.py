from django.urls import path
from . import views



urlpatterns = [
    path('all_posts/', views.all_posts, name='all-posts'),
    path('post_details/<int:pk>/', views.post_details, name='post-details'),
]