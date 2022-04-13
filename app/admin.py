from django.contrib import (
    admin,
)
from app.models import (
    Exercise,
    Theme,
)


admin.site.register(Theme)
admin.site.register(Exercise)