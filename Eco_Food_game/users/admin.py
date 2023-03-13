from django.contrib import admin
from .models import Profile, History


# Register extend database
admin.site.register(Profile)
admin.site.register(History)
