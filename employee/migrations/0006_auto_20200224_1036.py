# Generated by Django 2.2 on 2020-02-24 05:06

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20200224_1017'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employee', '0005_auto_20200224_1030'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='supervisors',
            unique_together={('project', 'user')},
        ),
    ]
