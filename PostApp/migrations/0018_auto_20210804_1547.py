# Generated by Django 3.2.4 on 2021-08-04 13:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('PostApp', '0017_auto_20210803_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post_comments',
            name='pub_hour',
        ),
        migrations.AddField(
            model_name='post_comments',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
