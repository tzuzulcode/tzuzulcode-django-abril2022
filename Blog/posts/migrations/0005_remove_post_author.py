# Generated by Django 4.0.4 on 2022-05-17 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
