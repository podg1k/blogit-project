# Generated by Django 3.0.2 on 2020-10-03 18:55

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0003_auto_20200919_2008'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Without title', max_length=250)),
                ('text', models.TextField(default='')),
                ('text_slug', models.CharField(blank=True, default='', max_length=200)),
                ('image', models.ImageField(upload_to='blog_image/%Y/%m/%d', verbose_name='Blog Image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('likes', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=list, help_text='Collects profile ids as Integer', size=None)),
                ('is_published', models.BooleanField(blank=True, default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='profiles.Profile')),
            ],
        ),
    ]
