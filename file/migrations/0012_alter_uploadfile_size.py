# Generated by Django 4.1.4 on 2023-11-02 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0011_remove_uploadfile_thumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='size',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
    ]
