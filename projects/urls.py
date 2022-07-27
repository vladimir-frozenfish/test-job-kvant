from django.urls import path

from .views import create, index, project


app_name = 'projects'

urlpatterns = [
    path('', index, name='index'),
    path('project/<slug:slug>/', project, name='project'),
    path('create/', create, name='create'),
]
