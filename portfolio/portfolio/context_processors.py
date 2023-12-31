from django.contrib.auth.models import User


def global_context(request):
    superuser = User.objects.filter(is_superuser=True).first()
    if superuser and hasattr(superuser, "profile"):
        profile = superuser.profile
    else:
        profile = None

    context = {
        "global_superuser": superuser,
        "global_profile": profile,
    }

    return context
