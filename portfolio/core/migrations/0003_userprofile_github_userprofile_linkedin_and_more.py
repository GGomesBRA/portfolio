# Generated by Django 5.0 on 2023-12-31 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_userprofile_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='github',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='linkedin',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='twiiter',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
