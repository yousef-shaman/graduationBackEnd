# Generated by Django 5.0.4 on 2024-04-26 10:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('faculty_member', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1, null=True)),
                ('level', models.PositiveIntegerField(default=1)),
                ('gpa', models.FloatField(blank=True, max_length=3)),
                ('earned_points', models.PositiveIntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'student_profile',
            },
        ),
        migrations.CreateModel(
            name='StudentProfermenceEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.PositiveIntegerField()),
                ('challenge_area_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='faculty_member.challengeevent')),
                ('student_profile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.studentprofile')),
            ],
            options={
                'db_table': 'student_profermence_event',
            },
        ),
        migrations.CreateModel(
            name='StudentProfermenceArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.PositiveIntegerField()),
                ('challenge_area_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='faculty_member.challengearea')),
                ('student_profile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.studentprofile')),
            ],
            options={
                'db_table': 'student_profermence_area',
            },
        ),
    ]