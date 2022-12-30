from django.contrib import admin

# Register your models here.
from theme.models import Theme, ThemeType

admin.site.register(Theme)
admin.site.register(ThemeType)