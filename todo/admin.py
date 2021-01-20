from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    #create a listview for the model in the admin page
    list_display = ('title', 'description', 'completed')

# Register your models here.
admin.site.register(Todo, TodoAdmin)