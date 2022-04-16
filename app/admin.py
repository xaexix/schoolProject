from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import (
    admin,
)
from django import (
    forms,
)
from app.models import (
    Theme,
    Exercise,
)


class ExerciseAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Exercise
        fields = '__all__'


class ExerciseAdmin(admin.ModelAdmin):
    form = ExerciseAdminForm
    list_display = ('__str__', 'short_description')


class ThemeAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'description')


admin.site.register(Theme, ThemeAdmin)
admin.site.register(Exercise, ExerciseAdmin)
