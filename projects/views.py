from django.shortcuts import render

from .models import Project
from .forms import ProjectForm

projectsList = [
    {
        "id": "1",
        "title": "Ecommerce Website",
        "description": "Fully functional ecommerce website",
        "topRated": True
    },
    {
        "id": "2",
        "title": "Portfolio Website",
        "description": "A personal website to write articles and display work",
        "topRated": False
    },
    {
        "id": "3",
        "title": "Social Network Website",
        "description": "An open source project built by the community",
        "topRated": True
    }
]

def projects(request):
    projects = Project.objects.all()
    context = {"projects": projects}

    # context = {"projects": projectsList}

    return render(request, "projects/projects.html", context)

def project(request, pk):
    # projectObject = None

    # for i in projectsList:
    #     if i['id'] == str(pk):
    #         projectObject = i

    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    reviews = projectObj.review_set.all()

    context = {"project": projectObj, "tags": tags, "reviews": reviews}

    return render(request, "projects/project.html", context)

def createProject(request):
    form = ProjectForm()
    context = {"form": form}

    return render(request, "projects/project-form.html", context)