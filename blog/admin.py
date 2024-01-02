from django.contrib import admin
from django.urls import reverse
from .models import *

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}
    list_display = ["title", "postLink"]
    
admin.site.register(Post,PostAdmin)  # ActiveUserCountPerDay,
