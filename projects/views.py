from django.shortcuts import render
from projects.models import Project

# Create your views here.
def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    technologies = project.technologies.all()
    context = {
        'project': project,
        'technologies': technologies
    }
    return render(request, 'project_detail.html', context)