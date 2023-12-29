from django.urls import path

from . import views

# Here, we are using namespaces. In the project URL conf, we use namespace inside the include
# So we need to define here that this is the app_name in whyich it is going to search.
app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
]