from django.shortcuts import render, get_object_or_404

from .models import Project


def index(request):
    """главная страница - выводит все проекты"""
    projects = Project.objects.all()

    template = 'projects/index.html'

    context = {'projects': projects}

    return render(request, template, context)


def project(request, slug):
    """выводит информацию о конкретном проекте"""
    project = get_object_or_404(Project, slug=slug)
    performers = project.performer.all()

    template = 'projects/project.html'

    context = {
        'project': project,
        'performers': performers
    }

    return render(request, template, context)

