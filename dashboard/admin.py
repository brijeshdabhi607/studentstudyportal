from django.contrib import admin
from .models import Notes, Homework,Todo

# Register your models here.

admin.site.register(Notes)
@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ['id','user','subject','title','description','due','is_complete']

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['id','user','title','is_finished']
