from django.shortcuts import render

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
    context = {"projects": projectsList}

    return render(request, "projects/projects.html", context)

def project(request, pk):
    projectObject = None

    for i in projectsList:
        if i['id'] == str(pk):
            projectObject = i

    return render(request, "projects/project.html", {"project": projectObject})