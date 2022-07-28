from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Max

from .models import Project, ProjectStatus
from .forms import ProjectForm


def index(request):
    """главная страница - выводит все проекты"""
    projects = Project.objects.all()

    template = 'projects/index.html'

    context = {'projects': projects}

    return render(request, template, context)


def project(request, project_id):
    """выводит информацию о конкретном проекте"""
    project = get_object_or_404(Project, id=project_id)
    performers = project.performer.all()

    template = 'projects/project.html'

    context = {
        'project': project,
        'performers': performers
    }

    return render(request, template, context)


def create(request):
    """создание нового проекта"""
    template = 'projects/create.html'

    form = ProjectForm(request.POST or None)
    if form.is_valid():
        obj = form.save()
        return redirect('projects:project', project_id=obj.id)

    context = {'form': form}
    return render(request, template, context)


def edit(request, project_id):
    """редактирование проекта"""
    template = 'projects/create.html'
    project = get_object_or_404(Project, id=project_id)

    form = ProjectForm(request.POST or None, instance=project)
    if form.is_valid():
        form.save()
        return redirect('projects:project', project_id=project.id)

    context = {'form': form,
               'is_edit': True}
    return render(request, template, context)


def destroy(request, project_id):
    """удаление проекта"""
    project = get_object_or_404(Project, id=project_id)
    project.delete()

    return redirect('projects:index')


def choose(request):
    """определяет и возвращает наиболее приоритетный проект
     со статусами «создан» и «остановлен», созданный раньше остальных"""
    priority_project = Project.objects.exclude(status=ProjectStatus.LAUNCHED).latest('priority')
    return redirect('projects:project', priority_project.id)
