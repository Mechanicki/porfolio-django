# Generated by Django 3.2.4 on 2021-07-31 06:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('PostApp', '0007_post_comments_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_comments',
            name='pub_hour',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 31, 6, 44, 12, 508290, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='post_comments',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 31, 6, 44, 12, 508290, tzinfo=utc), null=True),
        ),
    ]