from django.contrib import admin

# Register your models here.
from .models import Technology, Project

admin.site.register(Technology)
admin.site.register(Project)