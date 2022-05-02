from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="recipes-home"),
    path('receitas/<int:id>/', views.receitas, name="recipes-recipe"),
]
