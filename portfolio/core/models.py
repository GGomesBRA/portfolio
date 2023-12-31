from django.db import models
from django.contrib.auth.models import User


class ProgrammingLanguage(models.Model):
    LANGUAGES = [
        ("Python", "Python"),
        ("JavaScript", "JavaScript"),
        ("Java", "Java"),
        # Add other languages
    ]

    name = models.CharField(max_length=100, choices=LANGUAGES)

    def __str__(self):
        return self.name


class Framework(models.Model):
    FRAMEWORKS = [
        ("Django", "Django"),
        ("Flask", "Flask"),
        ("React", "React"),
        # Add other frameworks
    ]

    name = models.CharField(max_length=100, choices=FRAMEWORKS)
    language = models.ForeignKey(ProgrammingLanguage, on_delete=models.CASCADE, related_name="frameworks")

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    profile_picture = models.ImageField(upload_to="profile_pictures/", blank=True, null=True)
    role = models.CharField(default="Full Stack Developer / Python", max_length=100)
    github = models.CharField(default="", blank=True, null=True, max_length=100)
    linkedin = models.CharField(default="", blank=True, null=True, max_length=100)
    twiiter = models.CharField(default="", blank=True, null=True, max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
