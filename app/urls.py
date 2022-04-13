from django.urls import path

from app.views import (
    ThemeListView,
    ThemeDetailView,
    ExerciseDetailView,
)

urlpatterns = [
    path('', ThemeListView.as_view(), name='theme-list'),
    path('theme-detail/<int:pk>', ThemeDetailView.as_view(), name='theme_detail'),
    path('exercise-detail/<int:pk>', ExerciseDetailView.as_view(), name='exercise_detail'),
]
