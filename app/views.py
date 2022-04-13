from django.views.generic import ListView, DetailView

from app.models import (
    Theme,
    Exercise,
)


class ThemeListView(ListView):
    model = Theme


class ThemeDetailView(DetailView):
    model = Theme

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        exercises = Exercise.objects.filter(theme=kwargs.get('object'))
        context['exercises'] = exercises
        return context


class ExerciseDetailView(DetailView):
    model = Exercise
