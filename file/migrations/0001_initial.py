# Generated by Django 4.1 on 2022-09-27 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Uploadfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='New Document', max_length=100)),
                ('file', models.FileField(upload_to='')),
                ('thumb', models.FileField(upload_to='')),
            ],
        ),
    ]
