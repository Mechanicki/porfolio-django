# Generated by Django 3.2.4 on 2021-08-03 09:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('PostApp', '0013_auto_20210802_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='post_comments',
            name='pub_hour',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 3, 9, 33, 33, 516856, tzinfo=utc), null=True),
        ),
    ]