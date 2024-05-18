# Generated by Django 5.0.4 on 2024-05-07 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty_member', '0008_alter_facultymemberprofile_faculty_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challengearea',
            name='difficulty',
            field=models.CharField(choices=[('A', 'Advanced'), ('I', 'Intermediate'), ('B', 'Beginner')], max_length=10),
        ),
        migrations.AlterField(
            model_name='challengeevent',
            name='difficulty',
            field=models.CharField(choices=[('A', 'Advanced'), ('I', 'Intermediate'), ('B', 'Beginner')], max_length=10),
        ),
    ]