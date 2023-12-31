# projects/views.py

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Project
from django.core.serializers.json import DjangoJSONEncoder
import json


# This is one possible way to serialize a django model. Manually, field by field.
# Another possible way is using django_rest_framework, that I will do for some other case, just to show
def serialize_project(project):
    return {
        "id": project.id,
        "title": project.title,
        "description": project.description,
        "image_url": project.image.url if project.image else "",
        "url": project.url,
        "technologies": project.technologies,
        "start_date": project.start_date,
        "end_date": project.end_date if project.end_date else "Ongoing",
        "status": project.status,
        "challenges": project.challenges,
        "solutions": project.solutions,
        "role": project.role,
        "repository_link": project.repository_link,
        "experiment": project.experiment,
    }


def index(request):
    projects = Project.objects.all()
    projects_serialized = [serialize_project(project) for project in projects]

    context = {
        "projects": projects,
        "projects_json": json.dumps(projects_serialized, cls=DjangoJSONEncoder),
    }
    return render(request, "projects/index.html", context)


def experiments(request):
    template = loader.get_template("projects/experiments.html")
    context = {}
    return HttpResponse(template.render(context, request))


def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    return render(request, "projects/project_detail.html", {"project": project})


def experiment_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    return render(request, "projects/experiment_detail.html", {"project": project})
