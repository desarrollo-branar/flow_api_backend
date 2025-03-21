# Generated by Django 5.1 on 2025-02-25 12:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petitions', '0003_petition_end_date_petition_hours_petition_start_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='petition',
            name='department',
            field=models.ForeignKey(limit_choices_to={'active': True, 'deleted__isnull': True}, on_delete=django.db.models.deletion.PROTECT, related_name='departments', to='petitions.department'),
        ),
        migrations.AddIndex(
            model_name='company',
            index=models.Index(fields=['active', 'deleted'], name='petitions_c_active_132e42_idx'),
        ),
        migrations.AddIndex(
            model_name='department',
            index=models.Index(fields=['active', 'deleted'], name='departments_active_4e9b59_idx'),
        ),
        migrations.AddIndex(
            model_name='petition',
            index=models.Index(fields=['active', 'deleted'], name='petitions_active_0d7d1f_idx'),
        ),
        migrations.AddIndex(
            model_name='petitionsattachment',
            index=models.Index(fields=['active', 'deleted'], name='petition_at_active_f1bdf8_idx'),
        ),
    ]
