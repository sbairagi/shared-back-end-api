# Generated by Django 4.2.3 on 2023-08-19 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YouubeVideos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videoid', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('desc', models.TextField(default='')),
            ],
        ),
    ]
