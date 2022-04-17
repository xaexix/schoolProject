from django.urls import path

from app.views import (
    ExerciseDetailView,
    ThemeDetailView,
    ThemeListView,
    answer_check,
)

urlpatterns = [
    path('', ThemeListView.as_view(), name='theme_list'),
    path('answer-check/', answer_check, name='answer_check'),
    path('theme-detail/<int:pk>', ThemeDetailView.as_view(), name='theme_detail'),
    path('exercise-detail/<int:pk>', ExerciseDetailView.as_view(), name='exercise_detail'),
]
