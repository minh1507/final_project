# Generated by Django 5.0.7 on 2024-07-24 13:14

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ethnic',
            fields=[
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('deletedAt', models.DateTimeField(blank=True, default=None, null=True)),
                ('isFreeze', models.BooleanField(default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Password',
            fields=[
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('deletedAt', models.DateTimeField(blank=True, default=None, null=True)),
                ('isFreeze', models.BooleanField(default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('hash', models.CharField(max_length=60)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('deletedAt', models.DateTimeField(blank=True, default=None, null=True)),
                ('isFreeze', models.BooleanField(default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=10)),
                ('lastname', models.CharField(max_length=10)),
                ('middlename', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('age', models.PositiveIntegerField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('deletedAt', models.DateTimeField(blank=True, default=None, null=True)),
                ('isFreeze', models.BooleanField(default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('isActivate', models.BooleanField(default=False)),
                ('username', models.CharField(max_length=10, unique=True)),
                ('ethnic', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='App.ethnic')),
                ('password', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='App.password')),
                ('profile', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='App.profile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
