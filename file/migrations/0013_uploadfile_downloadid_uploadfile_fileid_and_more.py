# Generated by Django 4.1.4 on 2023-11-04 16:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('file', '0012_alter_uploadfile_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfile',
            name='downloadid',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='uploadfile',
            name='fileid',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='uploadfile',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to=settings.AUTH_USER_MODEL),
        ),
    ]
