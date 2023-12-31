from django.urls import path

from . import views

# Here, we are using namespaces. In the project URL conf, we use namespace inside the include
# So we need to define here that this is the app_name in whyich it is going to search.
app_name = "projects"

urlpatterns = [
    path("", views.index, name="index"),
    path("detail/<int:project_id>/", views.project_detail, name="project_detail"),
    path("experiments/", views.experiments, name="experiments"),
    path("epexriments/detail/<int:experiment_id>/", views.experiment_detail, name="experiment_detail"),
]
