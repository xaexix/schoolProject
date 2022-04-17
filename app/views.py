from django.http import JsonResponse
from django.views import View
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


class AnswerCheckView(View):
    def post(self, request, *args, **kwargs):
        successful = False
        pk = kwargs.get('pk', None)
        answer = request.POST.get('answer', None)
        exercise = self.model.objects.get(pk=pk)
        correct_answer = exercise.correct_answer
        if answer == correct_answer:
            successful = True
        return JsonResponse({"successful": successful})
