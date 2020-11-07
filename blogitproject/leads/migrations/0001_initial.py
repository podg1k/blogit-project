# Generated by Django 3.0.2 on 2020-11-04 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=60)),
                ('subject', models.CharField(blank=True, default='', max_length=60)),
                ('email', models.EmailField(default='', max_length=250)),
                ('message', models.TextField(blank=True, default='')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('is_answered', models.BooleanField(default=False)),
            ],
        ),
    ]