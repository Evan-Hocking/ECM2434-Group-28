from django.contrib import admin
from Food_Scanner.models import Demo, Score
# Register your models here.

@admin.register(Demo)
class DemoAdmin(admin.ModelAdmin):
    pass

@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    pass