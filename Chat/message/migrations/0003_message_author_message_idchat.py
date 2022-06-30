# Generated by Django 4.0.5 on 2022-06-30 20:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contacts', '0001_initial'),
        ('message', '0002_alter_message_sent'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='author',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='idChat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contacts.contacts'),
            preserve_default=False,
        ),
    ]
