# Generated by Django 5.0.4 on 2024-05-12 07:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_rename_studentprofile_studenstprofile'),
        ('system_admin', '0005_remove_systemadminprofile_first_name_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StudenstProfile',
            new_name='StudentProfile',
        ),
    ]