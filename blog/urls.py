from django.urls import path
from .views import *
name = 'blog'

urlpatterns = [
    path('',Post_list.as_view(),name='post_list'),
    path('post/<int:pk>',Post_detail.as_view(),name='post_detail')
]
