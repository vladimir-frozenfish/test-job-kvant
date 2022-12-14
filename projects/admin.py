from django.contrib import admin

from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'priority', 'status', 'creation_time', 'get_performer')
    search_fields = ('name',)


admin.site.register(Project, ProjectAdmin)
