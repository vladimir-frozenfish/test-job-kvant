from django.urls import path

from .views import create, choose, destroy, edit, index, project


app_name = 'projects'

urlpatterns = [
    path('', index, name='index'),
    path('project/<int:project_id>/', project, name='project'),
    path('create/', create, name='create'),
    path('project/<int:project_id>/destroy/', destroy, name='destroy'),
    path('project/<int:project_id>/edit/', edit, name='edit'),
    path('choose/', choose, name='choose'),
]
