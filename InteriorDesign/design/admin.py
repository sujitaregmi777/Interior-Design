from django.contrib import admin
from .models import Work

# Register your models here.
@admin.register(Work)
class WORKADMIN(admin.ModelAdmin):
    list_display = ('name', 'image', 'cost', 'story')
    search_fields = ('name', 'story')
