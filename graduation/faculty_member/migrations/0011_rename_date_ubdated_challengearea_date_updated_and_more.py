# Generated by Django 5.0.4 on 2024-05-16 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faculty_member', '0010_remove_facultymemberprofile_first_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='challengearea',
            old_name='date_ubdated',
            new_name='date_updated',
        ),
        migrations.RenameField(
            model_name='challengeevent',
            old_name='date_ubdated',
            new_name='date_updated',
        ),
        migrations.RenameField(
            model_name='optionsarea',
            old_name='date_ubdated',
            new_name='date_updated',
        ),
        migrations.RenameField(
            model_name='optionsevent',
            old_name='date_ubdated',
            new_name='date_updated',
        ),
        migrations.RenameField(
            model_name='paragrapharea',
            old_name='date_ubdated',
            new_name='date_updated',
        ),
        migrations.RenameField(
            model_name='paragraphevent',
            old_name='date_ubdated',
            new_name='date_updated',
        ),
        migrations.RenameField(
            model_name='questionarea',
            old_name='date_ubdated',
            new_name='date_updated',
        ),
        migrations.RenameField(
            model_name='questionevent',
            old_name='date_ubdated',
            new_name='date_updated',
        ),
        migrations.RenameField(
            model_name='topicarea',
            old_name='date_ubdated',
            new_name='date_updated',
        ),
        migrations.RenameField(
            model_name='topicevent',
            old_name='date_ubdated',
            new_name='date_updated',
        ),
    ]
