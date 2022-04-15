from django.contrib import (
    admin,
)
#from django.contrib.gis import forms

from app.models import (
    Theme,
    Exercise,
)
#from ckeditor.widgets import CKEditorWidget


#class ExerciseAdminForm(forms.ModelForm):
#    description = forms.CharField(widget=CKEditorWidget())
#
#    class Meta:
#        model = Exercise
#        fields = '__all__'


#class ExerciseAdmin(admin.ModelAdmin):
#    form = ExerciseAdminForm


admin.site.register(Theme)
admin.site.register(Exercise)