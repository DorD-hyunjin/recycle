from django.urls import path

from . import views

urlpatterns = [
    path('first', views.get_points, name='get_points'),
    path('second', views.post_user_info, name='post_user_info'),
]