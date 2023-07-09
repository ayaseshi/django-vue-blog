from django.urls import path, include

from . import views

urlpatterns = [
    path('tags/', views.get_tags),
]