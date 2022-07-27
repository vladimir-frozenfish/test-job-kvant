from django.urls import path

from .views import index, project


app_name = 'projects'

urlpatterns = [
    path('', index, name='index'),
    path('project/<slug:slug>/', project, name='project'),
]
