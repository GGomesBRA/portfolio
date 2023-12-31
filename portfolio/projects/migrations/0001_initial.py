# Generated by Django 5.0 on 2023-12-31 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='projects/images/')),
                ('url', models.URLField(blank=True, null=True)),
                ('technologies', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(max_length=100)),
                ('challenges', models.TextField(blank=True)),
                ('solutions', models.TextField(blank=True)),
                ('role', models.CharField(max_length=100)),
                ('repository_link', models.URLField(blank=True, null=True)),
                ('experiment', models.BooleanField(default=False)),
            ],
        ),
    ]
