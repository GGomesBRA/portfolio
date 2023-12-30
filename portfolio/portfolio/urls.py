from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from . import views

urlpatterns = [
    path("", include("core.urls")),
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls", namespace="blog")),
    path("projects/", include("projects.urls", namespace="projects")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
