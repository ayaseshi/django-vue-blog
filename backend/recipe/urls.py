from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('tags', views.TagViewSet)
router.register('recipe', views.RecipeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('get_recipes_by_page/', views.RecipePaginationView.as_view()),
]