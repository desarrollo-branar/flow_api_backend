# Generated by Django 5.1 on 2024-09-03 00:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified', verbose_name='modified')),
                ('name', models.CharField(max_length=120, unique=True, verbose_name='nombre')),
                ('description', models.TextField(blank=True, max_length=255, null=True, verbose_name='descripcion')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaskStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified', verbose_name='modified')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='titulo')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='descripcion')),
                ('hours', models.TimeField(verbose_name='tiempo')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tasks.department')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='tasks.taskstatus')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
