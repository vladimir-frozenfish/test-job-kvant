from django.db import models
from django.contrib.auth import get_user_model

from .validators import priority


User = get_user_model()


class ProjectStatus:
    CREATED = 'created'
    LAUNCHED = 'launched'
    STOPPED = 'stopped'


class Project(models.Model):
    project_status = (
        (ProjectStatus.CREATED, ProjectStatus.CREATED),
        (ProjectStatus.LAUNCHED, ProjectStatus.LAUNCHED),
        (ProjectStatus.STOPPED, ProjectStatus.STOPPED),
    )

    name = models.CharField(max_length=100, verbose_name='Имя проекта')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL_project')
    priority = models.PositiveIntegerField(validators=[priority,], verbose_name='Приоритет')     # от 0 до 100
    status = models.CharField(max_length=20, choices=project_status, default='created')
    creation_time = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    # performer = models.ManyToManyField(User, through='ProjectPerformer')
    performer = models.ManyToManyField(User, symmetrical=False, blank=True, null=True, related_name='projects', verbose_name = 'Исполнители проекта')

    def get_performer(self):
        return ', '.join(self.performer.all().values_list('username', flat=True))

    get_performer.short_description = 'Исполнители проекта'

    class Meta:
        verbose_name_plural = 'Проекты'
        verbose_name = 'Проект'
        ordering = ['creation_time']

    def __str__(self):
        return self.name

'''
class ProjectPerformer(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    performer = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Исполнители в проекте'
        verbose_name = 'Исполнитель в проекте'
        ordering = ['project']

        constraints = [
            models.UniqueConstraint(
                fields=['project', 'performer'],
                name='unique_project_performer'
            )
        ]

    def __str__(self):
        return f'{self.project} {self.performer}'
'''