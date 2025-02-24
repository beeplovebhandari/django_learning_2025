# Generated by Django 5.1.5 on 2025-02-24 11:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classroom_students', to='crud.classroom')),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.FileField(blank=True, null=True, upload_to='profile_pictures')),
                ('address', models.CharField(max_length=20)),
                ('contact', models.CharField(max_length=14)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='crud.student')),
            ],
        ),
    ]
