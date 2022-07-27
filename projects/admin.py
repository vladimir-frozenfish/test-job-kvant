from django.contrib import admin

from .models import Project # ProjectPerformer


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'priority', 'status', 'creation_time', 'get_performer')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

'''
class ProjectPerformerAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'performer')
'''

admin.site.register(Project, ProjectAdmin)
# admin.site.register(ProjectPerformer, ProjectPerformerAdmin)
