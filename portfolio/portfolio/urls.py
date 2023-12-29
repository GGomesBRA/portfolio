from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path("blog/", include("blog.urls", namespace='blog')),
    path("projects/", include("projects.urls", namespace='projects')),
]
