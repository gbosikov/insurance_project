# Generated by Django 4.2.4 on 2023-10-09 19:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Diction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom_name', models.CharField(default=None, max_length=150, null=True, verbose_name='custom name')),
                ('name_e', models.CharField(max_length=30, verbose_name='english name')),
                ('name_g', models.CharField(max_length=30, verbose_name='georgian name')),
                ('name_r', models.CharField(max_length=30, verbose_name='russian name')),
                ('custom_order', models.IntegerField(default=None, null=True, verbose_name='custom order')),
                ('color', models.IntegerField(default=None, null=True, verbose_name='color')),
                ('visible', models.BooleanField(default=True, verbose_name='visible')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='create date')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user who add row')),
            ],
            options={
                'verbose_name_plural': 'Diction',
                'db_table': 'diction',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Risks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom_name', models.CharField(default=None, max_length=150, null=True, verbose_name='custom name')),
                ('name_e', models.CharField(max_length=150, verbose_name='english name')),
                ('name_g', models.CharField(max_length=150, verbose_name='georgian name')),
                ('name_r', models.CharField(max_length=150, verbose_name='russian name')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('diction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='environment.diction', verbose_name='diction id')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user who add row')),
            ],
            options={
                'verbose_name_plural': 'Risks',
                'db_table': 'risks',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Objects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom_name', models.CharField(default=None, max_length=150, null=True, verbose_name='custom name')),
                ('name_e', models.CharField(max_length=30, verbose_name='english name')),
                ('name_g', models.CharField(max_length=30, verbose_name='georgian name')),
                ('name_r', models.CharField(max_length=30, verbose_name='russian name')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('diction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='environment.diction', verbose_name='diction id')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user who add row')),
            ],
            options={
                'verbose_name_plural': 'Objects',
                'db_table': 'objects',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='InsTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom_name', models.CharField(default=None, max_length=150, null=True, verbose_name='custom name')),
                ('name_e', models.CharField(max_length=150, verbose_name='english name')),
                ('name_g', models.CharField(max_length=150, verbose_name='georgian name')),
                ('name_r', models.CharField(max_length=150, verbose_name='russian name')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('diction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='environment.diction', verbose_name='diction id')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user who add row')),
            ],
            options={
                'verbose_name_plural': 'InsTypes',
                'db_table': 'ins_types',
                'ordering': ('id',),
            },
        ),
    ]