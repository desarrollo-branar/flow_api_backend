# Generated by Django 5.1 on 2025-02-25 12:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0001_initial'),
        ('petitions', '0004_alter_petition_department_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='commission',
            name='commissions_id_b0137d_idx',
        ),
        migrations.RemoveIndex(
            model_name='document',
            name='documents_id_2c4ffe_idx',
        ),
        migrations.AddIndex(
            model_name='commission',
            index=models.Index(fields=['id', 'active', 'deleted'], name='commissions_id_093c7c_idx'),
        ),
        migrations.AddIndex(
            model_name='document',
            index=models.Index(fields=['id', 'active', 'deleted'], name='documents_id_1c58a1_idx'),
        ),
    ]
