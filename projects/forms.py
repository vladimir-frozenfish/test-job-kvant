from django.forms import ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple

from .models import Project, User


class ProjectForm(ModelForm):

    class Meta:
        """форма для добавления или редактирования проекта"""
        model = Project
        fields = ('name', 'priority', 'status', 'performer')

    performer = ModelMultipleChoiceField(queryset=User.objects.all(), widget=CheckboxSelectMultiple, required=False, label='Исполнители')

