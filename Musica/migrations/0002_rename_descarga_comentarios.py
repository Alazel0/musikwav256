# Generated by Django 4.1.2 on 2022-10-30 22:05

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Musica', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Descarga',
            new_name='Comentarios',
        ),
    ]
