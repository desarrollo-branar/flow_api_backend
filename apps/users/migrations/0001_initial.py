# Generated by Django 5.1 on 2025-02-07 19:37

import django.contrib.auth.validators
import django.db.models.deletion
import django.db.models.functions.datetime
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified', verbose_name='modified')),
                ('deleted', models.DateTimeField(blank=True, default=None, null=True, verbose_name='deleted')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
                ('email', models.EmailField(error_messages={'unique': 'A user with that email already exists.'}, max_length=254, unique=True, verbose_name='email address')),
                ('is_verified', models.BooleanField(default=False, help_text='Set to true when the user have verified its email address. ', verbose_name='verified')),
                ('last_login', models.DateTimeField(default=django.db.models.functions.datetime.Now(), verbose_name='Último inicio de sesión')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='HumanResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified', verbose_name='modified')),
                ('deleted', models.DateTimeField(blank=True, default=None, null=True, verbose_name='deleted')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
                ('biography', models.TextField(blank=True)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='users/pictures')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'human_resources',
            },
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['-created'], name='users_created_9da240_idx'),
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['active'], name='users_active_eed388_idx'),
        ),
        migrations.AddIndex(
            model_name='humanresource',
            index=models.Index(fields=['-created'], name='human_resou_created_028276_idx'),
        ),
        migrations.AddIndex(
            model_name='humanresource',
            index=models.Index(fields=['active'], name='human_resou_active_0b9090_idx'),
        ),
    ]
