# Generated by Django 4.1.4 on 2023-11-02 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0010_alter_uploadfile_thumb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadfile',
            name='thumb',
        ),
    ]
