from django.urls import path, include

from . import views

urlpatterns = [
    path('tags/', views.get_tags),
    path('get-recipes/', views.get_recipes),
    path('get_recipes_by_page/', views.get_recipes_by_page),
]