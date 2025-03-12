# Generated by Django 5.1 on 2024-11-08 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0008_alter_task_hours"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="name",
            field=models.CharField(max_length=100, unique=True, verbose_name="nombre"),
        ),
        migrations.AlterField(
            model_name="task",
            name="title",
            field=models.CharField(max_length=200, verbose_name="titulo"),
        ),
    ]
