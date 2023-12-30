from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User


def home(request):
    template = loader.get_template("core/home.html")
    context = {}
    return HttpResponse(template.render(context, request))


def about(request):
    superuser = User.objects.filter(is_superuser=True).first()
    if superuser and hasattr(superuser, "profile"):
        profile = superuser.profile
    else:
        profile = None

    context = {
        "superuser": superuser,
        "profile": profile,
    }
    return render(request, "core/about.html", context)
