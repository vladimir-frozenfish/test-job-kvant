from django.forms import ModelForm

from .models import Project


class ProjectForm(ModelForm):

    class Meta:
        """форма для добавления или редактирования проекта"""
        model = Project
        fields = ('name', 'slug', 'priority', 'status', 'performer')

