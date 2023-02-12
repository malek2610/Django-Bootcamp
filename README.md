# Python Django 2021 Bootcamp Course Sessions

## Course Content

- Session #1: Views, URLs & Templates
- Session #2: Admin Panel, Models & Database Queries
- Session #3: Models Forms & CRUD
- Session #4: Static Files & Theme Installation

![Django Framework Architecture](./assets/django_architecture.png "Django Framework Architecture")

### Views, URLs & Templates

1. Start new project

   ```shell
   django-admin startproject devsearchlive .
   ```

   The previous command will generate automatically all files needed for your project as listed bellow.

   ```shell
    ├── devsearchlive
    │   ├── asgi.py
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── manage.py
    ├── README.md
    └── requirements.txt
   ```

1. Run the server

   Once the project created, you can start running the server anytime you would like by running the following command:

   ```shell
   python manage.py runserver
   ```

   !["Django Server is Running Successfully!"](./assets/runserver.png "Django Server is Running Successfully!")

1. Create new application

   The following command will create a new `projects` application within the main `devsearchlive` directory

   ```shell
   python manage.py startapp projects
   ```

   The new generated files therefore are:

   ```shell
    projects
    ├── admin.py
    ├── apps.py
    ├── __init__.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py
   ```

1. Register the application (add it to the installed applications)

   Go to the `settings.py` file within the `devsearchlive` directory and add the name of the created application as shown bellow

   ```python
    # Application definition

    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",

        "projects.apps.ProjectsConfig",
    ]
   ```

1. Add new `projects/` url

   Once the application created, we can add now a new url to access that application. We need therefore, to crate a new project function (later we will be using views instead) and create new path to that function.

   We need to modify the `urls.py` file within the `devsearchlive` directory as following:

   ```python
   from django.http import HttpResponse

   def projects(request):
       return HttpResponse("This is the projects page!")

   urlpatterns = [
       path("admin/", admin.site.urls),
       path("projects/", projects),
   ]
   ```

   !["Basic Projects Page"](./assets/projects_page.png "Basic Projects Page")

1. Render dynamic pages

   It's also possible to render dynamic pages by using `<int:pk>` configuration in the url paths.

   Bellow an example using a simple function within the `url.py` file.

   ```python
   from django.http import HttpResponse

   def project(request, pk):
       return HttpResponse(f"This is the project No. {str(pk)} page!")

   urlpatterns = [
       path("admin/", admin.site.urls),
       path("projects/", projects),
       path("project/<str:pk>/", project),
   ]
   ```

   !["Dynamic Project Page"](./assets/dynamic_project_page.png "Dynamic Project Page")

1. Add a `urls.py` for each application

   The correct way of adding paths and views is to use a `urls.py` and `views.py` of each application.

   - To do so, let move the `projects` and `project` functions to the `views.py` file inside the `projects` application
   - We create than a `urls.py`

     ```python
        from django.urls import path

        from . import views

        urlpatterns = [
            path("", views.projects),
            path("project/<str:pk>/", views.project),
        ]
     ```

   - Include the `projects` application `urls.py` into the main `devsearchlive` directory `urls.py` file

     ```python
     from django.contrib import admin
     from django.urls import path, include

     urlpatterns = [
         path("admin/", admin.site.urls),
         path("", include("projects.urls"))
     ]
     ```

1. Templates and Template Inheritance

   One possible configuration is inside the root directory, we add `templates` directory

   ```shell
       .
       ├── assets
       ├── devsearchlive
       │   └── __pycache__
       ├── projects
       │   ├── migrations
       │   │   └── __pycache__
       │   └── __pycache__
       └── templates
   ```

   Once the templates are used, we will be no longer using the `HttpResponse` in views but the `render`

   ```python
    def projects(request):
        return render(request, "projects.html")
   ```

   However, before using the templates we need to tell Django where they are located, so we have to update the `settings.py` file

   ```python
    import os

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [
                os.path.join(BASE_DIR, "templates")
            ],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ],
            },
        },
    ]
   ```

   Another way to use templates is for each application, we add a specific templates directory. This is the Django recommended method

   ```shell
    .
    ├── assets
    ├── devsearchlive
    │   └── __pycache__
    ├── projects
    │   ├── migrations
    │   │   └── __pycache__
    │   ├── __pycache__
    │   └── templates
    │       └── projects
    └── templates
   ```

   In this case the view function will be modified by specifying the name of the application inside the render method

   ```python
    def projects(request):
        return render(request, "projects/projects.html")
   ```

## Admin Panel, Models & Database Queries

The aim here is to build the DB, manage interactions and design queries.

1. Use the default SQLite database, before creating models or using the Admin panel we need to migrate all changes

   ```shell
   python manage.py makemigrations
   python manage.py migrate
   ```

1. Create superuser account for the administration of the application

   ```shell
   python manage.py createsuperuser
   ```

   We can now access the admin panel using the chosen username and password

   !["Django Admin Panel"](./assets/django_admin.png "Django Admin Panel")

   Now if you access successfully to the Django Admin interface you'll see the following dashboard

   !["Django Admin Dashboard"](./assets/django_admin_dashboard.png "Django Admin Dashboard")

1. Create our own Models by adding our DB tables to the `models.py` within the application directory

   ```python
    from django.db import models
    import uuid

    class Project(models.Model):
        # owner = WILL BE COMPLETED LATER
        title = models.CharField(max_length=200)
        description = models.TextField(null=True, blank=True)
        # feature_image = WILL BE COMPLETED LATER
        demo_link = models.CharField(max_length=1000, null=True, blank=True)
        source_link = models.CharField(max_length=1000, null=True, blank=True)
        vote_total = models.IntegerField(default=0)
        vote_ratio = models.IntegerField(default=0)
        created = models.DateTimeField(auto_now_add=True)
        id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

        def __str__(self):
            return self.title
   ```

1. Make new migration to update the DB with the new model just created

   ```shell
   python manage.py makemigrations
   python manage.py migrate
   ```

1. Register the model within the admin panel to be visible in the admin interface, therefore, we need to update the `admin.py` file of the application as following

   ```python
   from django.contrib import admin

   # Register your models here.
   from .models import Project

   admin.site.register(Project)
   ```

   Now we can see our Model inside the Admin panel

   !["Django Admin Model"](./assets/django_admin_model.png "Django Admin Model")

1. Now models can be used within the `view.py` file

## Models Forms & CRUD

## Static Files & Theme Installation

## Requirements

```
- Django==4.1.6
```
