from django.shortcuts import render, get_object_or_404, redirect

from .models import Project
from .forms import ProjectForm


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


def create(request):
    template = 'projects/create.html'

    # print(request.POST)
    # print(request.POST['slug'])

    form = ProjectForm(request.POST or None)
    if form.is_valid():
        saving = form.save(commit=False)
        saving.save()
        return redirect('projects:project', request.POST['slug'])

    context = {'form': form}
    return render(request, template, context)
