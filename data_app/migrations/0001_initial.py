# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-08 22:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LgStoreTestResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.TextField()),
                ('locale_code', models.TextField()),
                ('image_file', models.FileField(upload_to='data/lgstoretestresult/')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('file', models.FileField(upload_to='data/lgstoretestresult/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='lgstoretestresult',
            name='raw_file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_app.Post'),
        ),
    ]
