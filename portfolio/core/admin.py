from django.contrib import admin
from .models import ProgrammingLanguage, Framework, UserProfile

admin.site.register(ProgrammingLanguage)
admin.site.register(Framework)
admin.site.register(UserProfile)
