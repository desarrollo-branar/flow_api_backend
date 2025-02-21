# Generated by Django 5.1 on 2025-02-21 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("petitions", "0002_alter_petition_status_approval"),
    ]

    operations = [
        migrations.AddField(
            model_name="petition",
            name="end_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="petition",
            name="hours",
            field=models.DurationField(
                blank=True, null=True, verbose_name="tiempo invertido"
            ),
        ),
        migrations.AddField(
            model_name="petition",
            name="start_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
